import requests

payload = {
    "Authorization": "Bearer 0iknwcq090okz7mqfhinse86k7ay8i",
    "Client-Id": "65kdx4j9g92yikgnw9wsz903btq5tw"
}

url = "https://api.twitch.tv/helix/users"

response = requests.get(url, headers=payload)

def chooseChannel(channel):
    response = requests.get(url, headers=payload, params={"login": f"{channel}"})
    print(response.text)

def main(): 
    chooseChannel('lilypichu')

if __name__ == "__main__":
    main()
