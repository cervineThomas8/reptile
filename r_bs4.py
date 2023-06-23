import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.example.com"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find elements on the page using CSS selectors
    titles = soup.select("h2.title")
    
    # Extract and print the text from the found elements
    for title in titles:
        print(title.text)
else:
    print("Failed to retrieve the webpage.")
