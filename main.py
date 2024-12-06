from openai_manager import OpenAIManager
from web_manager import fetch_html_from_url


def main():
    url = "https://www.arabam.com/ikinci-el/otomobil"
    response_html = fetch_html_from_url(url)

    manager = OpenAIManager()
    

    user_message = """
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

    Here is the html content : 
    """

    manager.message_list.append({"role": "user", "content": user_message+response_html.prettify()[:100000]})
    response = manager.run_openai()

    print(response)


if __name__ == "__main__":
    main()

