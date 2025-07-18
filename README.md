# 😊 Emotion Detection App

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29%2B-ff4b4b.svg)](https://streamlit.io/)
[![DeepFace](https://img.shields.io/badge/DeepFace-0.0.79%2B-brightgreen.svg)](https://github.com/serengil/deepface)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-blue.svg)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A user-friendly web application built with Streamlit and DeepFace to detect and analyze human emotions from images and videos. This application was developed by **Mohamed Mostafa**.

---

## 🌟 Overview

This application leverages the power of deep learning to perform real-time emotion analysis. It uses the **DeepFace** library, a comprehensive facial attribute analysis framework for Python, to identify the dominant emotion in a person's face. The intuitive web interface is built using **Streamlit**, making it easy for anyone to upload media and get instant feedback.

## ✨ Features

-   **Image Analysis**: Upload an image (`JPG`, `JPEG`, `PNG`) to detect the dominant emotion.
-   **Video Analysis**: Upload a video (`MP4`, `AVI`, `MOV`) and see frame-by-frame emotion detection.
-   **Emotion Probability Distribution**: View a bar chart detailing the probabilities of different emotions: `happy`, `sad`, `angry`, `fearful`, `surprised`, `disgusted`, `neutral`.
-   **Adjustable Video Processing**: Control the analysis frequency for videos by setting the frame interval.
-   **User-Friendly Interface**: Simple and clean UI for a smooth user experience.

## 📸 Image Analysis


---

## 🛠️ Technologies Used

-   **Backend & ML**: `Python`, `DeepFace`, `OpenCV`, `NumPy`, `Pandas`
-   **Frontend**: `Streamlit`
-   **Image Handling**: `Pillow` (PIL)

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

-   Python 3.9 or higher
-   `pip` package manager

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/emotion-detection-app.git
    cd emotion-detection-app
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    The `deepface` library will automatically install its core dependencies like `tensorflow` and `opencv-python`.

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

Once the installation is complete, you can run the Streamlit app with a single command:

```bash
streamlit run app.py
```

Your web browser should automatically open to the application's URL (usually `http://localhost:8501`).

## 📖 How to Use

1.  Launch the application using the `streamlit run` command.
2.  From the dropdown menu, select your input type: **"Image"** or **"Video"**.
3.  Click the "Upload" button to choose a file from your computer.
4.  For videos, you can adjust the slider to set how frequently frames are analyzed.
5.  Wait for the analysis to complete.
6.  View the detected emotion and the probability chart for images, or watch the processed video with real-time emotion labels.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or want to add new features, please feel free to fork the repository and open a pull request.

## 📄 License

This project is distributed under the MIT License. You can add a `LICENSE` file to your project with the license text.