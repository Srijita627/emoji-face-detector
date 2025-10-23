import cv2
from deepface import DeepFace

# Load emoji images
emojis = {
    'happy': cv2.imread('emojis/happy.png'),
    'sad': cv2.imread('emojis/sad.png'),
    'angry': cv2.imread('emojis/angry.png'),
    'surprise': cv2.imread('emojis/surprised.png'),
    'neutral': cv2.imread('emojis/neutral.png')
}

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Analyze emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
    except Exception as e:
        emotion = "neutral"

    # Display detected emotion
    cv2.putText(frame, f'Emotion: {emotion}', (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show emoji on top-right corner
    if emotion in emojis and emojis[emotion] is not None:
        emoji = cv2.resize(emojis[emotion], (100, 100))
        h, w, _ = frame.shape
        frame[50:150, w-150:w-50] = emoji

    cv2.imshow('Emoji Face Detector', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
