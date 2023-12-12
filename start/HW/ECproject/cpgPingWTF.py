import requests

def ping_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return f"API at {api_url} is online. Status code: {response.status_code}"
    except: #requests.exceptions.RequestException as e:
        return f"API at {api_url} is not online. Error: "

# Example usage:
api_url_to_ping = "https://api.coincap.io/v2/assets/bitcoin"
result = ping_api(api_url_to_ping)
print(result)
