import requests
import pandas as pd
import os

from dotenv import load_dotenv

# Loading the .env file
load_dotenv()

# Function to get Spotify access token
def get_spotify_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_response.raise_for_status()  # Raises an error for bad responses
    auth_data = auth_response.json()
    return auth_data['access_token']

# # Function to search for a track and get its ID
# def search_track(track_name, artist_name, token):
#     query = f"{track_name} artist:{artist_name}"
#     url = f"https://api.spotify.com/v1/search?q={query}&type=track"
#     response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
#     response.raise_for_status()
#     json_data = response.json()
#     try:
#         first_result = json_data['tracks']['items'][0]
#         return first_result['id']
#     except (KeyError, IndexError):
#         return None
    
def search_track(track_name, artist_name, token):
    query = f"{track_name} artist:{artist_name}"
    url = "https://api.spotify.com/v1/search"
    params = {
        'q': query,
        'type': 'track',
    }
    response = requests.get(url, headers={'Authorization': f'Bearer {token}'}, params=params)
    response.raise_for_status()
    json_data = response.json()
    try:
        first_result = json_data['tracks']['items'][0]
        return first_result['id']
    except (KeyError, IndexError):
        return None

# Function to get track details
def get_track_details(track_id, token):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
    response.raise_for_status()
    json_data = response.json()
    return json_data['album']['images'][0]['url']

# Make sure to replace the CLIENT_ID and CLIENT_SECRET with your respective ID through Spotify Dashboard
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

access_token = get_spotify_token(client_id, client_secret)

# Replace 'spotify-2023.csv' with the correct file path
df_spotify = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')

# Initialize the new column for album cover image URLs
df_spotify['image_url'] = None

for i, row in df_spotify.iterrows():
    track_id = search_track(row['track_name'], row['artist(s)_name'], access_token)  # Adjusted artist name field
    if track_id:
        image_url = get_track_details(track_id, access_token)
        df_spotify.at[i, 'image_url'] = image_url

# Replace 'updated_spotify-2023.csv' with your desired output file name
df_spotify.to_csv('updated_spotify1-2023.csv', index=False)
