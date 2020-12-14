# Spotify data vizualization app
Dash app to visualize trends in hit music tracks from Spotify.

## Deployed Heroku app
[Spotify app](https://spotify-dash-app.herokuapp.com/)

# Data collection
Data has been collected using different API endpoints from Spotify API. Features include track name, artist information, album details, audio features like tempo, valence, energy and others.

## Steps include
- Get all tracks from a public playlist
- Fetch audio features for each track
- Fetch artist information for each track

# Tools

## API
[Spotify API](https://developer.spotify.com/documentation/web-api/)

### APIs used:
- Get a playlist owned by a Spotify user - [API](https://developer.spotify.com/documentation/web-api/reference/playlists/get-playlist/)
- Get audio features for a track - [API](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)
- Get Spotify catalog information for an artist - [API](https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/)

## Libraries
- [Dash](https://dash.plotly.com/)
- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
