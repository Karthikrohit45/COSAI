import requests
from bs4 import BeautifulSoup

def get_latest_headlines(url, headline_tag, headline_class=None):
    try:
        # Fetch the content of the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request fails
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find headlines based on tag and optional class
        if headline_class:
            headlines = soup.find_all(headline_tag, class_=headline_class)
        else:
            headlines = soup.find_all(headline_tag)
        
        # Extract and return the text of the headlines
        return [headline.get_text(strip=True) for headline in headlines]
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Replace with the target news website URL and HTML structure
    url = "https://www.bbc.com/news"  # Example website
    headline_tag = "h3"  # Example: headlines often use <h3>
    headline_class = "gs-c-promo-heading__title"  # Example class name
    
    # Get and print the latest headlines
    headlines = get_latest_headlines(url, headline_tag, headline_class)
    print("Latest Headlines:")
    for idx, headline in enumerate(headlines, start=1):
        print(f"{idx}. {headline}")
