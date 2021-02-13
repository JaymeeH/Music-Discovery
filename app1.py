''' Project 1: Milestone 1'''
from flask import Flask, render_template
from spotify import get_top_tracks
from genius import get_Song_Url
import os #module providing functions to create/delete directories and fetching its contents
import random

app1 = Flask(__name__) #initializes the app name
app1.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0    #prevents browser from caching data, allows html and css files to update browser
#random code

@app1.route('/')
def hello_world():
    print('Updated printline')
    
    top_tracks = get_top_tracks() #calls the spotify api, gaining access to the return data
    url_link = get_Song_Url(top_tracks['s_name'],top_tracks['s_track'])
    
    return render_template(# takes return data from spotify api, sends it to html template
        "song.html",
        name=top_tracks['s_name'],
        track=top_tracks['s_track'],
        preview=top_tracks['s_preview'],
        image=top_tracks['s_image'],
        url=url_link['s_url']
        )

app1.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP' '0.0.0.0'),
    debug=True# when app is saved while running, the terminal will automatically "re-run" the file; making it so that you can just refresh the browser to see updates
    )
    