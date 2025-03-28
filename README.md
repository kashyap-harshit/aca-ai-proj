# Installation Guide

## Prerequisites
Ensure your system meets the following requirements:
- Python 3.x installed
- A camera (USB webcam or Raspberry Pi camera module)
- Internet connection for API access

## Step 1: Update System (For Raspberry Pi)
If you are using a Raspberry Pi, update the system and install necessary dependencies:
```bash
sudo apt update
sudo apt install python3-picamera2
```

## Step 2: Clone or Download the Project
Download or clone this repository:
```bash
git clone <repository_url>
cd <project_directory>
```

## Step 3: Install Dependencies
Run the following command to install the required Python packages:
```bash
pip install -r requirements.txt
```
If you do not have a `requirements.txt`, install the dependencies manually:
```bash
pip install google-generativeai opencv-python pyttsx3 python-dotenv pillow
```

## Step 4: Set Up API Key
Create a `.env` file in the project directory and add your API key:
```env
API_KEY=your_google_gemini_api_key_here
```

## Step 5: Run the Program
Execute the script:
```bash
python main.py
```

## Additional Notes
- If running on a Raspberry Pi, uncomment the `picamera2` import and the relevant `capture_image` function.
- Press `q` to exit the live camera feed (if applicable).
- Ensure the `.env` file is correctly configured before running the script.

## Troubleshooting
### Issue: "Error: Could not open camera."
- Check if another application is using the camera.
- If on Raspberry Pi, ensure the camera module is enabled using:
  ```bash
  sudo raspi-config
  ```
  Navigate to *Interfacing Options* > *Camera* and enable it.

### Issue: "Error analyzing image: ..."
- Ensure the API key is valid and has access to the Gemini API.
- Check your internet connection.

