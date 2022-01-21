from msilib.schema import File
from operator import index
import requests

response = requests.get("https://api.thecatapi.com/v1/images/search")


print(response.json())  
