import google.generativeai as genai
import cv2
import pyttsx3
from dotenv import load_dotenv
import os
import time
import re
from PIL import Image
# from picamera2 import Picamera2 #for raspberry pie
# also main terminal
# sudo apt update
# sudo apt install python3-picamera2

# Load API Key
try:
    load_dotenv()
except Exception as e:
    print("Error loading .env file:", e)

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Text-to-Speech with a slower rate
engine = pyttsx3.init()
engine.setProperty("rate", 130)  # Adjust speed (default is ~200, lower is slower)

def speak(text):
    """Convert text to speech with adjusted speed."""
    engine.say(text)
    engine.runAndWait()

def capture_image(filename="image.jpg"):
    """Capture an image from the camera."""
    cam = cv2.VideoCapture(0)  # Use the default camera
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(filename, frame)
        print("Image captured successfully.")
    else:
        print("Error: Unable to capture image.")
    cam.release()


'''
def capture_image(filename="image.jpg"): #for raspberry pie
    """Capture an image using the Raspberry Pi camera."""
    picam2 = Picamera2()  # Initialize the Raspberry Pi camera
    picam2.start()
    time.sleep(2)  # Allow camera to adjust
    picam2.capture_file(filename)  # Capture and save image
    print("Image captured successfully.")

'''


def analyze_image(filename="image.jpg"):
    """Send the captured image to Gemini API for description."""
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

while True:
    user_input = input("Do you want to know what's happening around you? (yes/no): ").strip().lower()
    
    if user_input == "yes":
        capture_image()
        description = analyze_image()
        print("Gemini's Description:", description)
        speak(description)
    
    elif user_input == "no":
        print("Okay, exiting.")
        break
    
    else:
        print("Invalid input, please type 'yes' or 'no'.")
    
    time.sleep(2)  # Small delay before asking again
