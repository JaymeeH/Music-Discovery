''' Project 1: Milestone 1'''
# just a comment
import requests
import os
from dotenv import load_dotenv, find_dotenv
import random


load_dotenv(find_dotenv()) # This is to load your API keys from .env


''' GETTING AN ACCESS TOKEN '''
AUTH_URL = 'https://accounts.spotify.com/api/token'
Top_Tracks_URL = 'https://api.spotify.com/v1/artists/2pAWfrd7WFF3XhVt9GooDL/top-tracks'
#
def get_top_tracks():
    random_number = random.randint(0,4)
    auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('Spotify_KEY'),
    'client_secret': os.getenv('Spotify_Secret'),
    })

#convert response to json
    auth_response_data = auth_response.json()

#saving the access token
    access_token = auth_response_data['access_token']
#''' GETTING SONG DATA '''
    headers= {'Authorization': 'Bearer {token}'.format(token=access_token)}
    params={'market' : 'US', 'id' :'2pAWfrd7WFF3XhVt9GooDL' }

    response = requests.get(Top_Tracks_URL, headers=headers,params=params)
    data = response.json()
#''' DISPLAYING Top Tracks '''
    def get_track():
        return data['tracks'][random_number]['name']
    def get_name():
        return data['tracks'][random_number]['artists'][0]['name']
    def get_preview():
        return data['tracks'][random_number]['preview_url']
        
    for i in range(0, 10):
        print(data['tracks'][i]['name'], 'By:' ,data['tracks'][i]['artists'][0]['name'], 'Listen Here:', data['tracks'][i]['preview_url'])
  
# Print song names for first 10 songs in new releases returned by search endpoint
#for i in range(0, 10):

