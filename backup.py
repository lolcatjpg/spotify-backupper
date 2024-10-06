#!/usr/bin/env python
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
    with open("playlist_ids.json", "r", encoding="utf-8") as f:
        playlist_ids = json.loads(f.read())

    client_credentials_manager = SpotifyClientCredentials(client_id=CID, client_secret=SECRET)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    if not os.path.exists("backup"):
        os.mkdir("backup")

    for playlist_id in playlist_ids:
        playlist_name = sp.playlist(
            playlist_id,
            fields="name"
        )["name"]
        print(f"- backing up {playlist_name} (id: {playlist_id})...")

        playlist = sp.playlist_items(
            playlist_id,
            fields="items.track.name, items.track.artists.name, items.track.album.name, items.track.id",
        )

        with open(
            f"backup/playlist-backup-{datetime.now()}-{playlist_name}.json",
            "x",
            encoding="utf-8"
        ) as f:
            f.write(json.dumps(playlist))
            print(f"  > {playlist_name} backed up as {f.name}")
