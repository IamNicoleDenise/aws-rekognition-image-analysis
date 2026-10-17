"""
Detect faces and their dominant emotion with Amazon Rekognition,
then draw bounding boxes and labels on the image.

Setup:
    pip install boto3 pillow matplotlib
    Configure AWS credentials (e.g., `aws configure`) with access to
    Rekognition and the S3 bucket. Never commit credentials to this repo.

Usage:
    Set BUCKET and PHOTO below, then run:  python detect_faces_emotions.py
"""

from io import BytesIO

import boto3
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from PIL import Image

BUCKET = "your-bucket-name"   # S3 bucket that holds the image
PHOTO = "your-image.jpg"      # object key of the image in that bucket

client = boto3.client("rekognition")
bucket, photo = BUCKET, PHOTO

# Call Rekognition to detect faces and their emotions
response = client.detect_faces(
    Image={"S3Object": {"Bucket": bucket, "Name": photo}},
    Attributes=["ALL"],  # This returns facial attributes like emotions, age range, etc.
)

# Load the image from S3
s3 = boto3.resource("s3")
obj = s3.Object(bucket, photo)
img_data = obj.get()["Body"].read()
img = Image.open(BytesIO(img_data))

# Display the image with bounding boxes
plt.imshow(img)
ax = plt.gca()

# Process each face detected
for face_detail in response["FaceDetails"]:
    bbox = face_detail["BoundingBox"]
    left = bbox["Left"] * img.width
    top = bbox["Top"] * img.height
    width = bbox["Width"] * img.width
    height = bbox["Height"] * img.height

    # Draw bounding box
    rect = patches.Rectangle(
        (left, top), width, height,
        linewidth=2, edgecolor="r", facecolor="none",
    )
    ax.add_patch(rect)

    # Extract and display the dominant emotion
    emotions = face_detail["Emotions"]
    dominant_emotion = max(emotions, key=lambda x: x["Confidence"])
    emotion_text = f"{dominant_emotion['Type']} ({dominant_emotion['Confidence']:.2f}%)"
    plt.text(
        left, top - 10, emotion_text,
        color="r", fontsize=8,
        bbox=dict(facecolor="white", alpha=0.7),
    )

plt.axis("off")
plt.show()
