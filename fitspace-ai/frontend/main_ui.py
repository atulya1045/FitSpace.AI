import streamlit as st
import os

# --- Page Config ---
st.set_page_config(
    page_title="FitSpace.AI",
    page_icon="👕",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Branding ---
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>👕 FitSpace.AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Secure AI-powered Try-On & Design Preview Platform</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Sidebar Navigation ---
st.sidebar.title("🔍 Navigation")
view = st.sidebar.radio("Go to", ["Login", "Virtual Try-On", "Design Preview"])

# --- Webcam Login Section ---
if view == "Login":
    st.subheader("🔐 Biometric Login")
    st.info("Authenticate using your webcam (FaceNet + Liveness coming soon...)")

    if st.button("📷 Start Face Scan"):
        st.success("Launching webcam...")

        # MTCNN + OpenCV for face detection
        import cv2
        from mtcnn import MTCNN

        detector = MTCNN()
        cap = cv2.VideoCapture(0)

        st.warning("📸 A separate webcam window will open. Press 'q' to stop.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            faces = detector.detect_faces(frame)
            for face in faces:
                x, y, w, h = face['box']
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Face Scan - FitSpace.AI", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    st.image("https://placehold.co/300x300?text=Face+Preview", caption="Face Recognition Preview", width=300)

# --- Virtual Try-On Section ---
elif view == "Virtual Try-On":
    st.subheader("🧥 Virtual Try-On")
    st.info("Choose clothing and preview on your image.")
    st.selectbox("Select Clothing Category", ["T-Shirt", "Jacket", "Traditional", "Custom Upload"])
    st.image("https://placehold.co/300x400?text=Try-On+Preview", caption="Outfit Overlay", width=250)

# --- Design Preview Section ---
elif view == "Design Preview":
    st.subheader("🏠 Interior Design Preview")
    st.info("AI-generated room design preview based on user preferences.")
    st.text_input("Enter Design Prompt", "Modern living room with wooden floor and warm lights")
    st.image("https://placehold.co/400x300?text=Interior+Preview", caption="Generated Design", width=350)

# --- Footer ---
st.markdown("---")
st.caption("Made with ❤️ by Atulya, Nirved & Sujit | Final Year Project | TCET © 2025")
