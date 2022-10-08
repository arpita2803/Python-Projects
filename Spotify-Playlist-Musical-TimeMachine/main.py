from pprint import pprint
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = "ffeb023789824bbe9afaf6172ece0520"
SPOTIFY_CLIENT_SECRET = "74109dc80b1a48eaa370b76c897d07bd"

time_travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

billboard_response = requests.get(f"{BILLBOARD_URL}/{time_travel_date}")
content = billboard_response.text

soup = BeautifulSoup(content, "html.parser")
songs = soup.select(selector="li ul li h3")
top_100_songs = [song.getText().strip() for song in songs]
print(top_100_songs)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
track_list = []

for song in top_100_songs:
    try:
        track_name = sp.search(q=f"track:{song} year:{time_travel_date[:4]}", type="track", limit=1)
        track_list.append(track_name["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify.")

playlist_id = sp.user_playlist_create(user=user_id, name=f"{time_travel_date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id['id'], track_list)
