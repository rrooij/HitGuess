import urllib.parse


def html_template(tracks, tracks_per_row=3):
    html_string = """
    <!DOCTYPE html>
    <html>
      <head>
        <meta name="viewport" content="width=device-width,initial-scale=1" />
        <meta charset="utf-8">
        <style>
         .tracks {
           display: flex;
           flex-wrap: wrap;
         }
         .track {
           border: 2px solid black;
           min-width: 400px;
           margin: auto;
           max-width: 400px;
           margin: 10px;
           text-align: Center;
         }
         p {
           font-size: 13pt;
         }
         .year p {
           font-size: 20pt;
           font-weight: bold;
         }
        </style>
      </head>
    <body>
    <div class="tracks">
    """
    for track in tracks:
        html_string = (
            html_string
            + f"""
        <div class="track">
          <div class="artist"><p>{ track.artist }</p></div>
          <div class="title"><p>{ track.title }</p></div>
          <div class="year"><p>{ track.year }</p></div>
          <div class="qr"><img height="200px" src="{ urllib.parse.quote(track.create_qr_filename()) }"></div>
        </div>
        """
        )
    html_string = (
        html_string
        + """
    </div>
    </body>
    </html>
    """
    )
    return html_string
