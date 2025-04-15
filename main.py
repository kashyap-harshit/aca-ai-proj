import google.generativeai as genai
import cv2
import pyttsx3
from dotenv import load_dotenv
import os
import speech_recognition as sr
import time
import re
from PIL import Image

try:
    load_dotenv()
except Exception as e:
    print("Error loading .env file:", e)

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


engine = pyttsx3.init()
engine.setProperty("rate", 200)  

def speak(text):
    
    engine.say(text)
    engine.runAndWait()

def capture_image(filename="image.jpg"):
  
    cam = cv2.VideoCapture(0)  
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(filename, frame)
        print("Image captured successfully.")
    else:
        print("Error: Unable to capture image.")
    cam.release()




def analyze_image(filename="image.jpg"):
    
    try:
        image = Image.open(filename)
        prompt = (
            "Describe the image in one paragraph."
            "Do not include any special characters or symbols."
        )
        response = model.generate_content([image, prompt])
        description = response.text if response else "I couldn't analyze the image."
        return description
    
    except Exception as e:
        return f"Error analyzing image: {e}"

# Open the camera
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error: Could not open camera.")
    exit(1)

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen_for_yes_no():
    with mic as source:
        print("Listening for your response (yes or no)...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        response = recognizer.recognize_google(audio)
        print("You said:", response)
        return response.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


while True:
    speak("Do you want to know what's happening around you? Say yes or no.")
    user_input = listen_for_yes_no()

    
    if user_input in ["yesss" ,"ya","yaaah","Yash","yes", "yeah", "yep", "yes yes yes", "yes yes","ohh yeaahhhhh"]:
        capture_image()
        description = analyze_image()
        print(description)
        speak(description)

    elif user_input in ["no", "nope", "nah"]:
        speak("Okay, exiting.")
        break

    else:
        speak("I didn't catch that. Please say yes or no.")
        time.sleep(2)
