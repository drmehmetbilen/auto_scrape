import requests
from bs4 import BeautifulSoup

def fetch_html_from_url(url):

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__=="__main__":
    url  = "https://www.arabam.com/ikinci-el/otomobil"
    response_html = fetch_html_from_url(url)