import os
import time
from crawl4ai.web_crawler import WebCrawler
from crawl4ai.chunking_strategy import *
from crawl4ai.extraction_strategy import *
from crawl4ai.crawler_strategy import *

url = r'https://www.arabam.com/ikinci-el/otomobil'

crawler = WebCrawler()
crawler.warmup()

from pydantic import BaseModel, Field
class CarModel(BaseModel):
    car_model: str = Field(..., description="Car model.")
    title: str = Field(..., description="Title of the car.")
    price: str = Field(..., description="Price of the car.")
    location: str = Field(..., description="Location of the car.")
    model_year: str = Field(..., description="Model year of the car.")
    km: str = Field(..., description="Kilometer of the car.")
    color: str = Field(..., description="Color of the car.")

result = crawler.run(
    url=url,
    word_count_threshold=1,
    extraction_strategy= LLMExtractionStrategy(
        provider= "openai/gpt-4o", api_token = os.getenv('OPENAI_API_KEY'), 
        schema=CarModel.model_json_schema(),
        extraction_type="schema",
        instruction="""
                Can you extract these informations ? 
                    1. car model
                    2. title
                    3. car price
                    4. car location
                    5. car model year
                    6. car km
                    7. color

                    Your response will be in this format : 
                    [{
                        "car_model": "Audi A3",
                        "title": "Audi A3 1.6 TDI Attraction",
                        "price": "₺ 1.000",
                        "location": "İstanbul / Ümraniye",
                        "model_year": "2016",
                        "km": "120.000",
                        "color": "Beyaz"
                    }]

                """
    ),
    bypass_cache=True,
)

content = json.loads(result.extracted_content)

print(len(content))

with open("data.json", "w", encoding="utf-8") as f:
    f.write(result.extracted_content)