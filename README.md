#Link to Deployed APP : jaymees-showcase.herokuapp.com
# Project 1 Milestone 1 - This Doc explains how to run the app so far

# STEP 1 - spotify credentials
1. Download spotify.py from github, and install the following packages
 a. import requests
 b. import os
 c. from dotenv import load_dotenv, find_dotenv
 d. import random
# STEP 2 - genius credentials
1. Download genius.py from github; all packages used in the genius api are also used in the spotify api.
# STEP 3 - app1 deployment
1. download app1.py
2. install the following packages
3. from flask import Flask, render_template
4. from spotify import get_top_tracks
5. import os
6. import random
7. On the command line: type Python app1.py
8. 
# STEP 4 - Webpage styling
1. download the index.html
2. download the style.css file

# 2 known problems
1. There are no known problems within the app or the spotify api. There was an issue with certain songs not having a non existant preview url, but I remedied this by having the spotify file check if the song chosen has an existing preview url before returning data to the app. If the preview does not exist, then the spotify file will keep running until it finds a song with a preview.
2. Within the Genius api, there may be instances where the link provided does not take the user to the song displayed. I increased the accuracy of the correct link being provided by providing the api with both the artist name and the song name, fetched by the spotify api and delivered through the app.
3. Additional features I plan on implementing is a custom audio player created and styled by html and css. I also plan on implementing css animations to the web page.


# 3 technical issues
1. Displaying an audio block within from the html file. I had issues with passing a python variable from app1.py to the html file to play audio. 
 a. I remedied this by researching documentation for the html audio source attribute. I used "https://www.w3schools.com/tags/att_audio_src.asp" as a guide. after seeing that my code was structured correctly, I discovered that my technical issue was caused by improper syntax. 
2. Another technical issue was that my webpage was not updating after new features and styling were added.
 a. I went into the class slack and saw one of the TA's post a solution to fixing this problem. By adding a code block ``` app1.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0   ```
3. One Last technical issue that I ran into was with the spotify file. I was having issues passing my spotify data to app1.py 
 a. I couldn't pass the song and artist data obtained in the spotify file to my app file. I then referenced the nyt.py file provided during lecture 6. comparing the file that i had to the nyt file, i noticed that I was running through client credentials properly, and storing the neccessary data correctly, but I wasn't actually returning the data to the app. I believed that i could import the spotify file to the app, and reference the variables that I had set within the spotify functions. But I couldn't. So like in nyt.py, I returned all variables within a dictionary to the app.
