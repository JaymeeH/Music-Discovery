''' Project 1: Milestone 1'''
from flask import Flask, render_template
from spotify import get_top_tracks
import os
import random

app1 = Flask(__name__)
app1.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0    

@app1.route('/')
def hello_world():
    print('Updated printline')
    
    top_tracks = get_top_tracks()
    
    return render_template(
        "index.html",
        name=top_tracks['s_name'],
        track=top_tracks['s_track'],
        preview=top_tracks['s_preview'],
        image=top_tracks['s_image']
        )

app1.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP' '0.0.0.0'),
    debug=True
    )
    