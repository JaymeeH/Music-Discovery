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
    
    #random_number = random.randint(0,4)
    #favorite = 'Atlanta'
    #show_images = ['https://www.denofgeek.com/wp-content/uploads/2020/09/Attack-on-Titan-Season-4-Poster.jpg?resize=725,1024','https://i.ytimg.com/vi/oZCPRs_w2yo/maxresdefault.jpg','https://www.telegraphstar.com/wp-content/uploads/2019/08/atlanta-tv-show.jpg','https://m.media-amazon.com/images/M/MV5BZjM3YzQyZGUtZTE0Ny00OGIyLTg4NDEtMTJlZmZlMmJkMjY2XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg','https://images-na.ssl-images-amazon.com/images/I/51g9Rw0ieuL._SY445_.jpg']
    #tv_shows = ['Attack on Titan', 'Boondocks', 'Atlanta', 'Solar Oppisites', 'The Wayans Bros.']
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
    