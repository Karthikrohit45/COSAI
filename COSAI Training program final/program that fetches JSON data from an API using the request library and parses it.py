import requests

def fetch_and_parse_json(api_url):
    try:
       
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/posts"

    json_data = fetch_and_parse_json(api_url)

    if json_data:
        print("First item from the fetched data:")
        print(json_data[0])  
