import requests
import base64
def vqa_analysis(image_path, question, api_token):
    url = "https://api-inference.huggingface.co/models/Salesforce/blip-vqa-base"
    headers = {"Authorization": f"Bearer {api_token}"}
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    #files = {"file": open(image_path, "rb")}
        payload = {"inputs": {"question": question, "image": encoded_image}}

        response = requests.post(url, headers=headers, json=payload)
        return response.json()

api_token = "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"
image_path = "frame_0049.jpg"
#image_path = "frame_0050.jpg"
#image_path = "frame_0110.jpg"

result = vqa_analysis(image_path, "What is in the background?", api_token)
print(result)

