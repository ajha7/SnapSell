import requests
import json, os

class Shopify:
    def __init__(self):
        os.environ['SHOPIFY_API_KEY'] = ""
        os.environ['SHOPIFY_API_PASSWORD'] = ""
        os.environ['SHOPIFY_SHOP_NAME'] = ""
    # Your Shopify store credentials
    api_key = 'YOUR_API_KEY'
    password = 'YOUR_API_PASSWORD'
    shop_name = 'YOUR_SHOP_NAME'
    api_version = '2023-04'  # Use the latest API version or the version you are using

    # Shopify API endpoint for creating a product
    url = f'https://{api_key}:{password}@{shop_name}.myshopify.com/admin/api/{api_version}/products.json'

    # The data for the new product
    product_data = {
        "product": {
            "title": "Sample Product",
            "body_html": "<strong>Good product!</strong>",
            "vendor": "Your Vendor Name",
            "product_type": "Your Product Type",
            "tags": ["tag1", "tag2"],
            "variants": [
                {
                    "option1": "First",
                    "price": "10.00",
                    "sku": "123"
                }
            ],
            "images": [
                {
                    "src": "http://example.com/image.jpg"
                }
            ]
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    # Make the API call
    response = requests.post(url, headers=headers, data=json.dumps(product_data))

    # Print the response
    if response.status_code == 201:
        print("Product created successfully!")
        print("Response:", response.json())
    else:
        print("Failed to create product")
        print("Status Code:", response.status_code)
        print("Response:", response.json())
