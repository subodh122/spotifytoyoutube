import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from googleapiclient.discovery import build

# Spotify credentials
SPOTIFY_CLIENT_ID = 'add_your_id'
SPOTIFY_CLIENT_SECRET = 'add_your_secret'

# YouTube Data API key
YOUTUBE_API_KEY = 'add_your_key'

# Initialize Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))

def get_spotify_song_details(spotify_link):
    track_id = spotify_link.split('/')[-1].split('?')[0]
    track = sp.track(track_id)
    title = track['name']
    artist = track['artists'][0]['name']
    return title, artist

def search_youtube_music(title, artist):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    query = f"{title} {artist}"
    request = youtube.search().list(part="snippet", q=query, maxResults=1, type="video")
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    youtube_music_link = f"https://music.youtube.com/watch?v={video_id}"
    return youtube_music_link

def main():
    spotify_link = input("Enter Spotify song link: ")
    title, artist = get_spotify_song_details(spotify_link)
    youtube_music_link = search_youtube_music(title, artist)
    print(f"YouTube Music link: {youtube_music_link}")

if __name__ == "__main__":
    main()
