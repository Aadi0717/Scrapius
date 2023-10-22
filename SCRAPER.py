import requests
from bs4 import BeautifulSoup
import json
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []
    for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        text = element.get_text(strip=True)
        if text:
            data.append(text)
    return data
def save_data(data, text_filename, json_filename):
    try:
        with open(text_filename, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(f"{item}\n")
        print(f"Text data saved successfully to: {text_filename}")
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"JSON data saved successfully to: {json_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    url = "YOUR EXAMPLE URL HERE"  
    data = scrape_data(url)
    text_file_path = "data.txt"
    json_file_path = "data.json"
    save_data(data, text_file_path, json_file_path)
    print("Data saved as both text and JSON.")
