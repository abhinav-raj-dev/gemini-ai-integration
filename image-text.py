from google import genai
from google.genai import types
from dotenv import load_dotenv
import PIL.Image
import requests
import os
import pathlib


load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=GEMINI_API_KEY)

image_path_1 = "Screenshot (66).png"  # Replace with the actual path to your first image
image_path_2 = "innova-hycross-exterior-right-front-three-quarter-73.webp" # Replace with the actual path to your second image

image_url_1 = "https://www.google.com/imgres?q=innova&imgurl=https%3A%2F%2Fstatic3.toyotabharat.com%2Fimages%2Fshowroom%2Finnova-hycross%2Fcomfort-img1.webp&imgrefurl=https%3A%2F%2Fwww.toyotabharat.com%2Fshowroom%2Finnova%2F&docid=obJc6Hbit0w99M&tbnid=ViAK5jy4laP03M&vet=12ahUKEwibybzCxISMAxUPxzgGHWZwBQUQM3oECH8QAA..i&w=1050&h=560&hcb=2&ved=2ahUKEwibybzCxISMAxUPxzgGHWZwBQUQM3oECH8QAA" # Replace with the actual URL to your third image

pil_image = PIL.Image.open(image_path_1)

b64_image = types.Part.from_bytes(
    data=pathlib.Path(image_path_2).read_bytes(),
    mime_type="image/jpeg"
)

downloaded_image = requests.get(image_url_1)

response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents=["What do these images have in common?",
              pil_image, b64_image, downloaded_image])

print(response.text)