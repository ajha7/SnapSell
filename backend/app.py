from flask import Flask, request
from vision.ChatGPTPicHandler import ChatGPTPicHandler
from marketplaces.ebay import Ebay
from PIL import Image

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/upload_to_gpt")
def upload_to_gpt():
    img_path = "vision/chair.jpeg"
    pic_handler = ChatGPTPicHandler()
    response = pic_handler.handle_upload(img_path)
    # response = pic_handler.handle_upload_dummy(img_path)
    content = response['choices'][0]['message']['content']
    item = content.split(".")[0]
    description = ''.join(content.split(".")[1:])

    return (item, description)

@app.route("/upload_to_ebay", methods=['GET'])
def upload_to_ebay():
    url = request.args.get('url')
    # img_path = "vision/chair.jpeg"
    pic_handler = ChatGPTPicHandler()
    # response = pic_handler.handle_upload(url)
    response = pic_handler.handle_upload_dummy(url)

    # Extract the description from the response
    content = response['choices'][0]['message']['content']
    item = content.split(".")[0]
    description = ''.join(content.split(".")[1:])

    # Upload the item to eBay
    ebay = Ebay()
    ebay.upload_item_selenium(url, item, description)

    return description

if __name__ == "__main__":
    app.run(port=8000, debug=True)