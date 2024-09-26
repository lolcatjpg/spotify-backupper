import json
import os
from datetime import datetime
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
CID = os.getenv("CID")
SECRET = os.getenv("SECRET")


if __name__ == "__main__":
    client_credentials_manager = SpotifyClientCredentials(client_id=CID, client_secret=SECRET)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    playlist_name = sp.playlist(
        "spotify:playlist:6SvaET2rqGHOtxeh6RwrT2", 
        fields="name"
    )["name"]

    playlist = sp.playlist_items(
        "spotify:playlist:6SvaET2rqGHOtxeh6RwrT2", 
        fields="items.track.name, items.track.artists.name, items.track.album.name, items.track.id",
    )

    with open(
        f"backup/playlist-backup-{datetime.now()}-{playlist_name}.json",
        "x",
        encoding="utf-8"
    ) as f:
        f.write(json.dumps(playlist))
