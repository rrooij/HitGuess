# HitGuess

Simple clone of the HitSter game in which players guess a song, its artist and the year of release. It accepts an arbitrary Spotify playlist and generates game cards from them with a QR code to the Spotify song.

This means that you can make a lot of variations for different kind of audiences. Want to play with your kpop loving friends? Generate a card game with a kpop playlist! Want to keep it at the more general hits? Use the default Dutch playlist.

Example of the generated HTML (it still has to automatically align when printing and get to fit everything on A4): https://hitguess.pages.dev/ 

## Running

Be sure to install the dependencies with `poetry` and run `python3 hitguess/main.py [playlist_id]`

## Remarks

Developed this rather fast and dirty. The HTML does not print that well currently.

## License

AGPLv3
