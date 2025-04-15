# OpenCV Attendance System

**Automated attendance tracking using facial recognition with OpenCV.**

## Overview

The OpenCV Attendance System is a Python-based application that utilizes OpenCV for real-time face recognition to automate attendance tracking. By capturing and recognizing faces through a webcam, the system logs attendance records efficiently.

## Features

- **Face Encoding**: Generates and stores facial embeddings for recognition.
- **Real-Time Face Recognition**: Identifies individuals in real-time using a webcam.
- **Attendance Logging**: Records attendance data in a CSV file.
- **Dashboard Interface**: Provides a user-friendly interface to view attendance records.

## Project Structure

```
opencv-attendance-system/ 
├── encode_faces.py # Script to encode and store facial embeddings 
├── recognize_faces.py # Script to recognize faces and log attendance 
├── attendance_dashboard.py # Dashboard interface to view attendance records 
├── attendance.csv # CSV file to store attendance logs 
├── requirements.txt # List of required Python packages 
└── .gitignore # Git ignore file
```


## Getting Started

### Prerequisites

- Python 3.x
- OpenCV
- dlib
- face_recognition

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TrishKedi/opencv-attendance-system.git
   cd opencv-attendance-system

2. Install required packages

  ```pip install -r requirements.txt```

### Usage

1. Encode Faces: Run encode_faces.py to generate and store facial embeddings.

```python encode_faces.py```

2. Recognize Faces and Log Attendance: Run recognize_faces.py to start the real-time face recognition and log attendance.

```python recognize_faces.py```

3. View Attendance Dashboard: Run attendance_dashboard.py to launch the dashboard interface for viewing attendance records.

```python attendance_dashboard.py```

