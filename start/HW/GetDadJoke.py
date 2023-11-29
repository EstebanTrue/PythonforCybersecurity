import requests

def get_dad_joke():

    api_url = "https://icanhazdadjoke.com/"

    headers = {
        'Accept': 'application/json',
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        joke_data = response.json()

        joke = joke_data['joke']
        print("Random Dad Joke:")
        print(joke)
    else:
        print("Error, status code:", response.status_code)

if __name__ == "__main__":
    get_dad_joke()
