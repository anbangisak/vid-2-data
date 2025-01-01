import requests

def analyze_image(image_path, api_token):
    """
    Analyze an image using Hugging Face API to get details like background and number of people.

    Parameters:
        image_path (str): Path to the image file.
        api_token (str): Your Hugging Face API token.

    Returns:
        dict: Results from the API.
    """
    # API endpoint
    url = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
    
    # Read the image
    with open(image_path, "rb") as f:
        image_data = f.read()

    # Headers
    headers = {"Authorization": f"Bearer {api_token}"}
    
    # Send request
    response = requests.post(url, headers=headers, data=image_data)
    
    # Check response
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

# Example usage
api_token = "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"
#image_path = "frame_0049.jpg"
#image_path = "frame_0050.jpg"
image_path = "frame_0110.jpg"

results = analyze_image(image_path, api_token)

# Print the analysis
print(results)

