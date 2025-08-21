# Color Recognition Project using OpenCV

## Project Description
This project detects **red color only** in a video using Python and OpenCV.  
The program reads the video frame by frame, converts it to HSV color space, and applies a mask to detect red color only.

---

## Setup Steps

### 1. Install Anaconda
Make sure Anaconda is installed on your computer.

### 2. Install OpenCV and NumPy
Open **Anaconda Prompt** or **Terminal** and run the following commands:

pip install opencv-python numpy

**To verify OpenCV installation:**

import cv2

print(cv2.__version__)

### 3. Press Launch in Anaconda

This step is important. It ensures that VS Code is linked with the Anaconda environment and can run the project.

### 4. Open the Project Folder in VS Code

Open the folder containing your project files.

**Place inside the folder:** (these two files are in the repository)

Python script: color_recognition.py

Video file: 855474-hd_1920_1080_24fps.mp4

## Running the Project

### 1. Open Terminal in VS Code or Anaconda Prompt.

### 2. Navigate to the project folder:

cd "C:\Users\Fatima\Documents\ColorRecognition"

### 3. Run the Python script:

python color_recognition.py

### 4. Two windows will open:

- Original Video: shows the original video

- Red Color Detection: shows only the red color in the video

## Notes
The video must be in the same folder as the Python script.

This project detects red color only.

Pressing Launch in Anaconda is necessary to ensure the project runs without library issues.

## Author
Fatima



