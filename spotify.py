''' Project 1: Milestone 1'''
import requests
import os
from dotenv import load_dotenv, find_dotenv
import random

load_dotenv(find_dotenv()) # This is to load your API keys from .env

''' GETTING AN ACCESS TOKEN '''
AUTH_URL = 'https://accounts.spotify.com/api/token'
Artist_List = ['https://api.spotify.com/v1/artists/0g9vAlRPK9Gt3FKCekk4TW/top-tracks','https://api.spotify.com/v1/artists/2pAWfrd7WFF3XhVt9GooDL/top-tracks','https://api.spotify.com/v1/artists/7tYKF4w9nC0nq9CsPZTHyP/top-tracks']

def get_top_tracks():
    random_number = random.randint(0,9)#randomly selects a number between 10 values: used later to choose 1 of 10 albums randomly
    random_artist = random.randint(0,2)# used to select 1 of 3 artist id's randomly: picked from the hardcoded artist list above 
#                       ~~~~~~~~~~~~~~~~~~~~~~Client Control Flow~~~~~~~~~~~~~~~~

    auth_response = requests.post(AUTH_URL, { #reqests access token: sends api keys to spotify accounts service
    'grant_type': 'client_credentials',
    'client_id': os.getenv('Spotify_KEY'),
    'client_secret': os.getenv('Spotify_Secret'),
    })# accounts service returns access token in json response

#                           ~~~~~~~~~~~~~~convert response to json~~~~~~~~~~~~~~~~~~~~~
    auth_response_data = auth_response.json()

#                           ~~~~~~~~~~~~~~~~~saving the access token~~~~~~~~~~~~~~~~~~~~
    access_token = auth_response_data['access_token']
#                                   ~~~~~~~~~~GETTING SONG DATA ~~~~~~~~~~~~~~~~~~~
    headers= {'Authorization': 'Bearer {token}'.format(token=access_token)}
    params={'market' : 'US', 'id' :'2pAWfrd7WFF3XhVt9GooDL' } #sending access token along with a request

    response = requests.get(Artist_List[random_artist], headers=headers,params=params)
    data = response.json()#spotify web api returns requested (unscoped) data: converted to json
#                               ~~~~~~~~~~~~~DISPLAYING Top Track~~~~~~~~~~~~~~~
    def get_image():
        return data['tracks'][random_number]['album']['images'][0]['url']
    def get_track():
        return data['tracks'][random_number]['name']
    def get_name():
        return data['tracks'][random_number]['artists'][0]['name']
    def get_preview():
        return data['tracks'][random_number]['preview_url']
   
    
    #               ~~~~~~~~~~~~~~~~~Setting keys to be deliveralbe to the app.~~~~~~~~~~~~~~~~~~~
    s_name = get_name()
    s_track = get_track()
    s_preview = get_preview()
    s_image = get_image()
    
    #~~~~~~~~~~~~~~~~~~~~~~~Checking to see if the random track selected has an available preview~~~~~~~~~~~~~~~~~~~~~
    test_string = data['tracks'][random_number]['preview_url']
    res = isinstance(test_string, str) 

    if(res):
     message = "BANG"
    else:
     return get_top_tracks()
    # Sending Keys to the app
    return { 's_name' : s_name, 
            's_track' : s_track,
            's_preview' : s_preview,
            's_image' : s_image
        
    }