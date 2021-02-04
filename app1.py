''' Project 1: Milestone 1'''
# just a comment
import requests
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv()) # This is to load your API keys from .env


''' GETTING AN ACCESS TOKEN '''
AUTH_URL = 'https://accounts.spotify.com/api/token'
Browse_URL = 'https://api.spotify.com/v1/browse/new-releases'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('Spotify_KEY'),
    'client_secret': os.getenv('Spotify_Secret'),
})

#convert response to json
auth_response_data = auth_response.json()

#saving the access token
access_token = auth_response_data['access_token']
#print(access_token)


''' GETTING SONG DATA '''
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
    
    
}
params={'country' : 'US', 'limit' : 10,}


response = requests.get(Browse_URL, headers=headers,params=params)
data = response.json()
''' DISPLAYING Album NAMES '''
x = 0
for i in range(0, 10):
    print(data['albums']['items'][i]['name'])
#['albums']['items'][8]['name']
  
# Print song names for first 10 songs in new releases returned by search endpoint
#for i in range(0, 10):

