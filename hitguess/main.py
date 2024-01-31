from dataclasses import dataclass
import os
import sys
import time

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import segno

from template import html_template


@dataclass
class Card:
    artist: str
    title: str
    year: int
    track_url: str

    def _valid_char(self, c):
        return c.isalpha() or c.isdigit() or c == " "

    def create_qr_filename(self):
        return (
            "images/"
            + "".join(
                c for c in f"{self.artist}{self.title}" if self._valid_char(c)
            ).rstrip()
            + ".svg"
        )

    def create_qr(self):
        qr = segno.make_qr(self.track_url)
        qr.save(self.create_qr_filename())


def create_card_from_track(track: dict):
    release_date = track["album"]["release_date"][0:4]
    authors = ", ".join([x["name"] for x in track["artists"]])
    track_url = track["external_urls"]["spotify"]
    title = track["name"]
    return Card(authors, title, release_date, track_url)


def main():
    try:
        os.mkdir("images")
    except:
        pass
    # Use the default Dutch Hitster playlist but otherwise use first argument
    # of program
    playlist_id = sys.argv[1] if len(sys.argv) > 1 else "321iL49aeqqqtKfrQLO91I"
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    tracks = sp.playlist_tracks(playlist_id, limit=50)
    items = tracks["items"]
    while tracks["next"]:
        # Sometimes I seem to hit the Spotify rate limit
        time.sleep(10)
        tracks = sp.next(tracks)
        items.extend(tracks["items"])
    cards = [create_card_from_track(x["track"]) for x in items if x["track"]]
    for card in cards:
        card.create_qr()
    html = html_template(cards)
    with open("index.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
