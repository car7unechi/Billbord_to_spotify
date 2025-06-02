import time
import requests
import website
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from pprint import pprint
import webbrowser
from dotenv import load_dotenv
import os
load_dotenv()

#-------------------------------------------- STATIC VARIABLES----------------------------------#
URL = "https://www.billboard.com/charts/hot-100"
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
hot_100 = []
hot_100_artist_list = []
still_listening = True
#-------------------------------------------------AUTHENTICATION--------------------------------#
#authenticate in spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://google.com/",
                                               scope="playlist-modify-private"))
#authenticate billboard
header = {
    "user-agent": os.getenv("USER_AGENT")
}
#------------------------------------------------------------BS OBJECT---------------------#

#choose what year of hot 100 you want to see
year = input("What year would you like to travel to(yyyy-mm-dd): ")

response = requests.get(url=f"{URL}/{year}", headers=header)
top_100 = response.text
soup = BeautifulSoup(top_100, "html.parser")
#----------------------------------------------------------FIND HOT 100 SONG & ARTIST------------------------#
#link to the number 1 song
top = soup.find(name="h3")
#add number 1 song first to the hot 100 list of songs
number_one = top.getText().split()
hot_100.append(' '.join(number_one))

#link to the artist of the number 1 song
t_artist = soup.find(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                                             "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block"
                                             " a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")
number_one_artist = t_artist.getText().split()
hot_100_artist_list.append(' '.join(number_one_artist))

#link to the other 99 top 100 songs
hot_100_link= soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                                                      "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125"
                                                                      " u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330"
                                                                      " u-max-width-230@tablet-only")

hot_100_artist_link = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max"
                                                        " u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330"
                                                        " u-max-width-230@tablet-only")

#-----------------------------------------------------------------------HOT 100 LIST--------------------------------------------------#
split_list = [song.getText().split() for song in hot_100_link]
hot_100_artist = [artist.getText().split() for artist in hot_100_artist_link]

#add songs in order to the hot 100 songs
for song in split_list:
    hot_100.append(" ".join(song))

#Add artist in order to the top
for artist in hot_100_artist:
    hot_100_artist_list.append(" ".join(artist))


song_and_artist = [f"{i}{hot_100[i], hot_100_artist_list[i]}" for i in range(100)]

for music in song_and_artist:
    print(music)

time.sleep(5)
print("which song do you want to listen?")
time.sleep(1)

listen = int(input("choose a number from 0-99: "))
#----------------------------------------------------------SPOTIFY API-----------------------------------------#
while still_listening:
    #function to search song
    find_song = sp.search(f"{hot_100[listen]} + {hot_100_artist_list[listen]}", limit=2, type="track", market="US")

    # link to the song
    song_url = find_song['tracks']['items'][0]['external_urls']['spotify']
    # # automatically opens the link
    webbrowser.open(song_url)
    listen = input("choose another number if you want to keep listening 0-99(press n to exit):")

    if listen == "n":
        print("goodbye")
        still_listening = False
    else:
        listen = int(listen)
#--------------------------------------ADD TO PLAYLIST------------------------------------#
# user = sp.current_user()
# user = int(user['id'])
#
# create_playlist = sp.user_playlist_create(user=user, name=str(year), public=True, description="throwback to top 100")
# print(create_playlist)





