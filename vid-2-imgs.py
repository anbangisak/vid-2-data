import cv2
import os

# Video file path
video_path = "output001.mp4"  # Replace with your video file path
output_folder = "extracted_frames"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the video file
video = cv2.VideoCapture(video_path)

# Get video details
fps = video.get(cv2.CAP_PROP_FPS)  # Frames per second
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps  # Total video duration in seconds

# Check if the video is 6 seconds long
if duration > 6:
    print(f"The video is longer than 6 seconds ({duration} seconds). Truncating...")
    total_frames = int(6 * fps)

frame_count = 0
image_count = 0

while frame_count < total_frames:
    ret, frame = video.read()
    if not ret:
        break

    # Save frame as image
    output_path = os.path.join(output_folder, f"frame_{image_count:04d}.jpg")
    cv2.imwrite(output_path, frame)
    image_count += 1

    frame_count += 1

# Release video
video.release()

print(f"Extracted {image_count} frames to '{output_folder}'")
