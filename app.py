import streamlit as st
from deepface import DeepFace
import cv2
import numpy as np
from PIL import Image
import tempfile
import pandas as pd

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="Emotion Detection App", layout="centered")
st.title("😊 Emotion Detection App")

# ----------------------------
# Sidebar: About the App
# ----------------------------
with st.sidebar:
    st.header("📘 About")
    st.markdown("""
This application was **developed by Mohamed Mostafa**.

It uses **DeepFace**, a deep learning-based facial analysis framework, to detect human emotions from both **images and videos**.

### ⚙️ How it Works:
- The app accepts an uploaded image or video.
- It uses **DeepFace's pre-trained models** to analyze faces.
- It predicts the dominant **emotion** from the following: `happy, sad, angry, fearful, surprised, disgusted, neutral`.
- Results are visualized with a **bar chart** showing emotion probabilities.
  
### 👨‍💻 Technologies Used:
- `Streamlit` for the web interface
- `OpenCV` for video processing
- `DeepFace` for emotion recognition
- `PIL / NumPy / Pandas` for image and data handling
""")

# ----------------------------
# Emotion Analysis Function
# ----------------------------
def analyze_emotion(img):
    try:
        result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
        return result[0]['emotion']
    except Exception as e:
        st.error(f"Error during analysis: {e}")
        return None

# ----------------------------
# Select Input Type
# ----------------------------
option = st.selectbox("📁 Select Input Type", ("Image", "Video"))

# ----------------------------
# Image Emotion Detection
# ----------------------------
if option == "Image":
    uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        st.image(img_array, caption="🖼️ Uploaded Image", use_column_width=True)

        with st.spinner("Analyzing emotion..."):
            emotions = analyze_emotion(img_array)

        if emotions:
            detected = max(emotions, key=emotions.get)
            st.success(f"😃 Dominant Emotion: **{detected}**")
            st.bar_chart(pd.DataFrame(emotions, index=["Probability"]).T)
        else:
            st.warning("No emotion could be detected.")

# ----------------------------
# Video Emotion Detection
# ----------------------------
elif option == "Video":
    uploaded_file = st.file_uploader("📤 Upload a Video", type=["mp4", "avi", "mov"])
    frame_interval = st.slider("⏱️ Analyze every Nth frame", min_value=30, max_value=300, value=120, step=30)

    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            video_path = temp_file.name

        video = cv2.VideoCapture(video_path)
        frame_count = 0
        stframe = st.empty()

        st.info("🔍 Processing video... Please wait.")

        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break

            frame_count += 1
            if frame_count % frame_interval == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                emotions = analyze_emotion(frame_rgb)

                if emotions:
                    detected = max(emotions, key=emotions.get)
                    cv2.putText(frame_rgb, f"Emotion: {detected}", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(frame_rgb, "Emotion: Not Detected", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                stframe.image(frame_rgb, caption=f"🎞️ Frame {frame_count}", channels="RGB")

        video.release()
        st.success("✅ Video processing completed.")
