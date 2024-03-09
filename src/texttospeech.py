import requests

# Set your API key 
api_key = '4fab2d5d7f5ddec9ff9422c2da442613'

CHUNK_SIZE = 1024

# Define the API endpoint  
# "h9wTb50iJC9oQuw5A37H" - this is the <voice_id> that I added on my elevenlabs

url = "https://api.elevenlabs.io/v1/text-to-speech/h9wTb50iJC9oQuw5A37H"

# Construct the request headers (if required)
headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "54dbfb5a93494c7b309d27a43cb0e9cd"
}
# this func takes the text prompt as input and generates a mp3 file
def texttospeech(text): 

    data = {
    "text": text,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
    }
    # Send a POST request to the API endpoint with the provided data and headers
    response = requests.post(url, json=data, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        with open('output.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
    else:
        print(f"Error: {response.status_code} - {response.text}")


text = "Born and raised in the charming south, I can add a touch of sweet southern hospitality to your audiobooks and podcasts"
texttospeech(text)
# The generated mp3 file is saved as output.mp3