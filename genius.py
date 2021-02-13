''' Project 1: Milestone 1'''
import requests
import os
from dotenv import load_dotenv, find_dotenv
import random

load_dotenv(find_dotenv())
search_Url='https://api.genius.com/search?'
''' GETTING AN ACCESS TOKEN '''
#Kendrick_lyric ='https://genius.com/Kendrick-lamar-kendrick-lamar-lyrics'

access_token = os.getenv('Genius_Token')#Genius allows us to generate a client access token, which enables us to avoid the client control flow

headers= {'Authorization': 'Bearer {token}'.format(token=access_token)}#preping request for artist song lyrics
params={'q' : 'kendrick lamar' } #sending access token along with a request

response= requests.get(search_Url, headers=headers, params=params)
data=response.json()




print(data['response']['hits'][0]['result']['url'])