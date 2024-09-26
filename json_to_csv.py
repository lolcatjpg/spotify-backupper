import csv
import json
from sys import argv


if __name__ == "__main__":
    with open(argv[1], encoding="utf-8") as f:
        json_data = json.loads(f.read())

    with open("playlist.csv", "x", encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["title", "artist", "album", "id"])

        for track in json_data["items"]:
            csv_row = []
            csv_row.append(track["track"]["name"])
            artists = [artist["name"] for artist in track["track"]["artists"]]
            csv_row.append(", ".join(artists))
            csv_row.append(track["track"]["album"]["name"])
            csv_row.append(track["track"]["id"])

            csvwriter.writerow(csv_row)
