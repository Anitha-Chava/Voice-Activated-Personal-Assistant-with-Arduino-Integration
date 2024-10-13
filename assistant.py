# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:40:43 2024

@author: anitha
"""
import serial
import pyttsx3
import datetime as dt
def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[0].id)
    speaker.say(text)
    speaker.runAndWait()
    
import pygame
import os
def play_mp3(file_path):
    pygame.mixer.init()
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return 
    try:
        pygame.mixer.music.load(file_path)
        print(f"Playing {os.path.basename(file_path)}...")
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"An error occured while playing the file: {e}")
        
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        
arduino = serial.Serial('COM8', 9600) 

def turn_led_on():
    arduino.write(b'0')  # Send '0' to Arduino to turn the LED on

def turn_led_off():
    arduino.write(b'1')  # Send '1' to Arduino to turn the LED off


def take_command(idle_mode=True):
    command = ''
    try:
        with sr.Microphone() as source:
            if idle_mode:
                turn_led_on()  # Turn LED on when listening
                print('Waiting for wakeup word...')
                voice = listener.listen(source, timeout=5)
            else:
                turn_led_on()  # Turn LED on when listening
                print('Listening...')
                voice = listener.listen(source)

            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except sr.UnknownValueError:
        return ''
    except sr.RequestError:
        return ''
    except Exception as e:
        print(f'An error occurred: {e}')
        return ''
    finally:
        turn_led_off()  # Turn LED off when done listening
        
        
va_name = "siri"
def listen_for_wakeup_word():
    while True:
        idle_command = take_command(idle_mode=True)
        if va_name in idle_command:
            print('Waking up...')
            speak(f'I am your {va_name}. How can I help you?')
            main()

import PyPDF2

def read_pdf(filepath):
    try:
        with open(filepath, 'rb') as pdffile:
            pdf_reader = PyPDF2.PdfReader(pdffile)
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                print(f"Reading Page {page_num +1 }...")
                speak(text)
            
    except Exception as e:
        print(f"An error occured: {e}")
        speak("Sorry I cound't read this pdf file")
        
import pyttsx3
import requests
import speech_recognition as sr

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Set speech rate and voice (optional)
speaker.setProperty('rate', 130)  # Adjust the rate to your preference
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)  # Change index for different voices

# DuckDuckGo Instant Answer API URL
DUCKDUCKGO_URL = 'https://api.duckduckgo.com/'

# Initialize the recognizer for speech recognition
listener = sr.Recognizer()

def speak(text):
    """Function to speak out the given text."""
    speaker.say(text)
    speaker.runAndWait()

def truncate_text(text, word_limit=30):
    """Truncates the text to a specified number of words."""
    words = text.split()
    if len(words) > word_limit:
        return ' '.join(words[:word_limit]) + '...'
    return text

def search_duckduckgo(query):
    """Searches DuckDuckGo for a given query and returns the abstract of the result."""
    try:
        params = {
            'q': query,
            'format': 'json',
            'no_redirect': '1',
            'no_html': '1',
            'skip_disambig': '1'
        }
        response = requests.get(DUCKDUCKGO_URL, params=params)
        data = response.json()
        
        if 'AbstractText' in data and data['AbstractText']:
            return truncate_text(data['AbstractText'])
        elif 'RelatedTopics' in data and data['RelatedTopics']:
            # Get the first related topic's text if available
            return truncate_text(data['RelatedTopics'][0]['Text'])
        else:
            return "Sorry, I couldn't find any relevant information."
    except Exception as e:
        print(f'An error occurred while searching: {e}')
        return "Sorry, I couldn't complete the search."

def listen_for_command():
    """Listens for voice input and returns it as text."""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            query = listen_for_command()
            if query:
                print(f"Searching for: {query}")
                result = search_duckduckgo(query)
                print(result)
                speak(result)
            else:
                speak("Sorry, I didn't catch that. Please try again.")
                command = listener.recognize_google(voice)
                command = command.lower()
                return command
    except sr.UnknownValueError:
        return ''
    except sr.RequestError:
        return ''
    except Exception as e:
        print(f'An error occurred while listening: {e}')
        return ''
    
import pyttsx3
import requests
import speech_recognition as sr

speaker = pyttsx3.init()

speaker.setProperty('rate', 130)  
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)  
API_KEY = '3ec136d4c475adee4efe3c3219d70892'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'


recognizer = sr.Recognizer()

def speak(text):
    
    speaker.say(text)
    speaker.runAndWait()

def get_weather(city):
    
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(WEATHER_URL, params=params)
        data = response.json()

        if data['cod'] == 200:
            city_name = data['name']
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            report = f"The weather in {city_name} is currently {weather_desc} with a temperature of {temp} degrees Celsius."
            return report
        else:
            return "Sorry, I couldn't get the weather information for that location."
    except Exception as e:
        print(f'An error occurred while fetching weather information: {e}')
        return "Sorry, I couldn't get the weather information."

def listen_for_city():
    
    with sr.Microphone() as source:
        print("Listening for city name...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            city_name = recognizer.recognize_google(audio)
            print(f"City name received: {city_name}")
            return city_name
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was a problem with the request.")
            speak("Sorry, there was a problem with the request.")
            return None

def main():   
    
    while True:
        user_command = take_command(idle_mode=False)
        if user_command:
            print(f"User command received: {user_command}")
        if 'stop' in user_command:
                speak('Going idle. Please call me with my name.')
                listen_for_wakeup_word()
        
        if 'how' in user_command:
            speak('I am good. Thanks for asking.')
            
        elif 'search for' in user_command or 'google' in user_command or 'who is' in user_command or 'which is' in user_command or 'what is' in user_command or 'tell me about' in user_command:
            query = user_command
            if query:
                print(f"Searching for: {query}")
                result = search_duckduckgo(query)
                print(result)
                speak(result)
            else:
                speak("Sorry, I didn't catch that. Please try again.")
            
        elif 'weather in' in user_command:
            city = user_command.replace('weather in ', '')
            print(f'Fetching weather information for: {city}')
            weather_report = get_weather(city)
            print(weather_report)
            speak(weather_report)
               
        elif 'read pdf' in user_command or "read PDF" in user_command:
            pdf_file_path = r"C:\Users\anith\OneDrive\Documents\Downloads\Prediction of Types of Cancer.pdf"
            read_pdf(pdf_file_path)
            flag = False   
        elif 'play' in user_command:
            mp3_file_path = r"C:\Users\anith\OneDrive\Documents\Downloads\[iSongs.info] 02 - Aa Rojulu Malli Raavu.mp3"
            play_mp3(mp3_file_path)
            
        elif 'time' in user_command:
            cur_time = dt.datetime.now().strftime("%I:%M %p")
            print(cur_time)
            
        elif any(op in user_command for op in ['+', '-', '*', '/', 'times', 'x']):
            expression = user_command.replace('times', '').replace('multiplied by', '').replace('x', '*').replace(
                'plus', '+').replace('minus', '-').replace('divided by', '/')
            try:
                result = eval(expression)
                print(f'Result: {result}')
                speak(f'The result is {result}')
                
            except Exception as e:
                print(f"Error in calculation: {e}")
                speak("Sorry, I couldn't calculate that.")
            
        
        # New Commands for Arduino Actions
        elif 'shake hand' in user_command:
            print("Shaking hand")
            arduino.write(b'3')
            speak("Shaking hand.")
        elif 'walk' in user_command:
            print("Walking")
            arduino.write(b'4')
            speak("Walking.")
        elif 'left' in user_command:
            print("Turning left")
            arduino.write(b'5')
            speak("Turning left.")
        elif 'right' in user_command:
            print("Turning right")
            arduino.write(b'6')
            speak("Turning right.")
        elif 'back' in user_command:
            print("Moving back")
            arduino.write(b'7')
            speak("Moving back.")
        else:
            speak('Sorry, I did not understand that command.')

if __name__ == "__main__":  
    speak(f'Hello! My name is {va_name}.')
    listen_for_wakeup_word()
