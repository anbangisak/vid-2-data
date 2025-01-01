import subprocess

def split_video(input_file, segment_time=6, output_pattern="output%03d.mp4"):
    command = [
        "ffmpeg",
        "-i", input_file,
        "-c", "copy",
        "-f", "segment",
        "-segment_time", str(segment_time),
        "-reset_timestamps", "1",
        output_pattern
    ]
    subprocess.run(command, check=True)

# Example usage
split_video("input_video.mp4")


