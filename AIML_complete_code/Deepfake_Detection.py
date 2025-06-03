import cv2
import numpy as np
from mtcnn.mtcnn import MTCNN
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Input
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.optimizers import Adam
from colorama import Fore, Style, init

init(autoreset=True) 

# 1. Build the model
def build_deepfake_model():
    input_layer = Input(shape=(224, 224, 3))
    base_model = EfficientNetB0(include_top=False, weights='imagenet', input_tensor=input_layer)
    x = GlobalAveragePooling2D()(base_model.output)
    output = Dense(1, activation='sigmoid')(x)
    model = Model(inputs=input_layer, outputs=output)
    model.compile(optimizer=Adam(1e-4), loss='binary_crossentropy', metrics=['accuracy'])
    return model

model = build_deepfake_model()
# Optional: model.load_weights("deepfake_weights.h5")

# 2. Analyze video
def analyze_video_fast(video_path):
    detector = MTCNN()
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(Fore.RED + "❌ Error: Could not open video.")
        return

    frame_index = 0
    scale_percent = 50  

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (0, 0), fx=scale_percent / 100, fy=scale_percent / 100)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = detector.detect_faces(rgb_frame)

        if results:
            for person in results:
                x, y, w, h = person['box']
                x, y = max(0, x), max(0, y)
                face = rgb_frame[y:y + h, x:x + w]

                if face.size > 0:
                    face_resized = cv2.resize(face, (224, 224))
                    face_array = preprocess_input(np.expand_dims(face_resized.astype("float32"), axis=0))
                    pred = model.predict(face_array, verbose=0)[0][0]

                    label = "REAL" if pred > 0.5 else "FAKE"
                    color = (0, 255, 0) if label == "REAL" else (0, 0, 255)
                    confidence = f"{pred*100:.1f}%" if label == "FAKE" else f"{(1 - pred)*100:.1f}%"

                    # Draw on frame
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 3)
                    cv2.putText(frame, f"{label} ({confidence})", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

                    # Terminal Output (hacker-style)
                    hacker_color = Fore.GREEN if label == "REAL" else Fore.RED
                    print(hacker_color + f"[FRAME {frame_index:04d}] 🔍 Face detected at (x={x}, y={y}, w={w}, h={h}) ➤ {label} ({confidence})" + Style.RESET_ALL)

        else:
            print(Fore.YELLOW + f"[FRAME {frame_index:04d}] ⚠️ No face detected." + Style.RESET_ALL)

        cv2.imshow("Deepfake Detection - Hacker View", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        frame_index += 1

    cap.release()
    cv2.destroyAllWindows()
    print(Fore.CYAN + "\n🔒 Detection finished. All frames analyzed.\n" + Style.RESET_ALL)

# Run the detection
analyze_video_fast("new.mp4")
