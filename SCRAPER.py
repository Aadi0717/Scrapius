# import requests
# # Function to fetch movie data using OMDb API
# def fetch_movie_data(api_key):
#     url = "http://www.omdbapi.com/"
#     params = {
#         's': 'movie',  # Search for movies
#         'type': 'movie',  # Type of search (movie)
#         'apikey': api_key
#     }
#     # Send a request to OMDb API
#     response = requests.get(url, params=params)
#     # Check if the request was successful
#     if response.status_code == 200:
#         data = response.json()
#         movies = data.get('Search', [])
#         for movie in movies:
#             title = movie.get('Title', 'N/A')
#             year = movie.get('Year', 'N/A')
#             print(f"Title: {title}, Year: {year}")
#     else:
#         print("Failed to fetch data from OMDb API.")
# # API Key
# api_key = "6a6f15e0"
# # Call the function to fetch movie data
# fetch_movie_data(api_key)
# import requests
# from bs4 import BeautifulSoup
# def scrape_data(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     data = []
#     for h3 in soup.find_all('h3'):
#         title = h3.text.strip()
#         paragraph = h3.find_next_sibling('p')
#         if paragraph:
#             description = paragraph.text.strip()
#         else:
#             description = ''
#         data.append({
#             'title': title,
#             'description': description
#         })
#     return data
# def save_data(data, filename):
#     try:
#         with open(filename, 'w', encoding='utf-8') as f:
#             for item in data:
#                 f.write(f"{item['title']}\n")
#                 f.write(f"{item['description']}\n\n")
#         print(f"Data saved successfully to: {filename}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# if __name__ == "__main__":
#     url = "https://en.wikipedia.org/wiki/Suicide_methods"
#     data = scrape_data(url)
#     file_path = r"C:\Users\Work\Desktop\data.txt"
#     save_data(data, file_path)
# import json
# import requests
# from bs4 import BeautifulSoup

# def scrape_data(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     data = []
#     for h3 in soup.find_all('h3'):
#         title = h3.text.strip()
#         paragraph = h3.find_next_sibling('p')
#         if paragraph:
#             description = paragraph.text.strip()
#         else:
#             description = ''
#         data.append({
#             'title': title,
#             'description': description
#         })
#     return data

# def save_data_as_text(data, text_filename):
#     try:
#         with open(text_filename, 'w', encoding='utf-8') as f:
#             for item in data:
#                 f.write(f"{item['title']}\n")
#                 f.write(f"{item['description']}\n\n")
#         print(f"Data saved successfully as text to: {text_filename}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def save_data_as_json(data, json_filename):
#     try:
#         with open(json_filename, 'w', encoding='utf-8') as f:
#             json.dump(data, f, indent=4)  # Save data as JSON
#         print(f"Data saved successfully as JSON to: {json_filename}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     url = "https://www.geeksforgeeks.org/what-is-dataset/"
#     data = scrape_data(url)
    
#     # Paths to the text and JSON files
#     text_file_path = r"C:\Users\Work\Documents\VS CODER\webscraper\data.txt"
#     json_file_path = r"C:\Users\Work\Documents\VS CODER\webscraper\data.json"
    
#     # Save data as text and JSON
#     save_data_as_text(data, text_file_path)
#     save_data_as_json(data, json_file_path)
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
    url = "https://en.wikipedia.org/wiki/cake"  
    data = scrape_data(url)
    text_file_path = "data.txt"
    json_file_path = "data.json"
    save_data(data, text_file_path, json_file_path)
    print("Data saved as both text and JSON.")