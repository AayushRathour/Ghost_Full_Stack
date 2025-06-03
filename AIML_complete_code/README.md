# Deepfake Detection System

This folder contains AI/ML code implementations for the Ghost Full Stack project, specifically focusing on Deepfake Detection capabilities.

## Deepfake Detection (Deepfake_Detection.py)

A real-time deepfake detection system that uses EfficientNetB0 and MTCNN for face detection and classification.

### Prerequisites

```bash
pip install -r requirements.txt
```

Required packages:
- opencv-python
- numpy
- mtcnn
- tensorflow
- colorama

### Model Architecture

The system uses:
- MTCNN (Multi-task Cascaded Convolutional Networks) for face detection
- EfficientNetB0 (pretrained on ImageNet) for feature extraction
- Custom classification layer for deepfake detection

### Setup Instructions

1. First, install all required dependencies:
```bash
pip install opencv-python numpy mtcnn tensorflow colorama
```

2. Make sure you have the following files in your directory:
- `Deepfake_Detection.py` (main script)
- Video file to analyze (default: "new.mp4")

### Running the Detection System

1. Place your video file in the same directory or update the video path in the script.

2. Run the script:
```bash
python Deepfake_Detection.py
```

### Usage Instructions

1. The program will start analyzing the video frame by frame.
2. For each frame:
   - Faces will be detected using MTCNN
   - Each detected face will be classified as REAL or FAKE
   - A confidence percentage will be shown
   - Visual indicators:
     - Green box: Real face
     - Red box: Fake face

3. Controls:
   - Press 'q' to quit the program
   - The analysis window will show real-time detection results
   - Terminal will display frame-by-frame analysis with colored output

### Output Information

The system provides:
- Visual output with bounding boxes around detected faces
- Color-coded results (Green for Real, Red for Fake)
- Confidence percentages for each detection
- Terminal output with frame numbers and detection details
- Hacker-style interface with colored console output

### Performance Notes

- Video processing is optimized with a 50% scale factor for better performance
- Face detection and classification run in real-time
- The model uses efficient batch processing for predictions

### Troubleshooting

1. If you see "Error: Could not open video":
   - Check if the video file exists in the correct path
   - Ensure the video file format is supported by OpenCV

2. If face detection is not working:
   - Ensure adequate lighting in the video
   - Check if faces are clearly visible and of sufficient size

3. For performance issues:
   - Adjust the `scale_percent` variable in the code
   - Consider reducing video resolution

### Model Details

The deepfake detection model uses:
- Input size: 224x224x3 (RGB)
- Base model: EfficientNetB0
- Training weights: ImageNet pretrained
- Output: Binary classification (Real/Fake) with confidence score

### Additional Notes

- The system processes frames in real-time
- Detection results are displayed both visually and in the terminal
- The implementation includes colorful terminal output for better visualization
- Model weights can be loaded from a custom file (commented out in the code)
