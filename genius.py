''' Project 1: Milestone 1'''
import requests
import os
from dotenv import load_dotenv, find_dotenv
import random

load_dotenv(find_dotenv())
search_Url='https://api.genius.com/search?'
''' GETTING AN ACCESS TOKEN '''
def get_Song_Url(artist_Name,song_Name):
    access_token = os.getenv('Genius_Token')#Genius allows us to generate a client access token, which enables us to avoid the client control flow
    track_ID= artist_Name + '' + song_Name
    headers= {'Authorization': 'Bearer {token}'.format(token=access_token)}#preping request for artist song lyrics
    params={'q' : track_ID } #sending access token along with a request

    response= requests.get(search_Url, headers=headers, params=params)
    data=response.json()

    def get_url():
        return data['response']['hits'][0]['result']['url']


    s_url = get_url()#saving the url
    
    test_string = data['response']['hits'][0]['result']['url']
    test_list = data['response']['hits']
    res = isinstance(test_string, str) 
    
    
    if(res):
     message = "BANG"
    elif len(test_list) == 0:
     s_url = 'https://genius.com/'
     return {'s_url': s_url}
    elif test_string == None:
     s_url = 'https://genius.com/'
     return {'s_url': s_url}
    else:
     s_url = 'https://genius.com/'
     return {'s_url':s_url}
    
    return {'s_url' : s_url,}#sending keys to the app