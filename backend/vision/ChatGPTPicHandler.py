from openai import OpenAI
import json, os, base64, requests
from dotenv import load_dotenv


class ChatGPTPicHandler:
    def __init__(self):
        load_dotenv()
        OPENAI_APIKEY = os.getenv("OPENAI_APIKEY")
        self.openai_client = OpenAI(api_key=OPENAI_APIKEY)
        pass

    def handle_upload_dummy(self, url):
        response = {'id': 'chatcmpl-9Xw31PPpQWL2jYKZ1Nk9nLB4cr2J6', 'object': 'chat.completion', 'created': 1717874987, 'model': 'gpt-4o-2024-05-13', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': 'Wooden chair. This chair is made of wood and features a slatted backrest and four sturdy legs. It is typically used for seating in dining rooms, kitchens, or offices. The natural wood finish gives it a classic and versatile look, suitable for various home or work environments.'}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 312, 'completion_tokens': 57, 'total_tokens': 369}, 'system_fingerprint': 'fp_aa87380ac5'}
        return response
    
    def handle_upload_url(self, url):
        response = self.openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    },
                    },
                ],
                }
            ],
            max_tokens=300,
        )

        print(response.choices[0])

    def handle_upload_base64(self, img_path):
        # Encode the image
        encoded_image = self.encode_image(img_path)
        
        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
        }

        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": "Identify the object in this image. Briefly describe it. Example: Red apple. This apple is a fruit that is round and red in color. Crunchy and bright, just picked. It is commonly eaten as a snack or used in cooking."
                    },
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                    }
                ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        print(response.json())
    
    # Function to encode the image
    def encode_image(self, image_path):
        # print current directory
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
        
    
    