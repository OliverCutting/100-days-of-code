from bs4 import BeautifulSoup
import requests
import spotipy
import config
from spotipy.oauth2 import SpotifyOAuth

year = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
page = response.text
soup = BeautifulSoup(page, "html.parser")

titles = soup.select("li h3")
titles = titles[:len(titles)-7]
titles = [title.get_text().strip() for title in titles]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri='http://example.com',
        client_id=config.client_id,
        client_secret=config.client_secret,
        show_dialog=True,
        cache_path='token.txt'
    ))
user_id = sp.current_user()['id']

for title in titles:
    print(title)

createplaylist = input("Do you want to make a playlist of these titles? y/n")

if createplaylist == 'y':
    uris = []
    for title in titles:
        title = sp.search(q="track:" + title, type='track', limit=1)
        try:
            uris.append(title['tracks']['items'][0]['uri'])
        except:
            pass
    playlist = sp.user_playlist_create(user_id, year, public=False, description=f"A playlist automatically generated from the billboard hot 100 for {year}")

    sp.playlist_add_items(playlist['id'], uris)