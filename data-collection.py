# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:07:34 2020

@author: varsha
"""

import requests
import json
import pandas as pd

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# GET request for track audio features
def getAudioFeatures(track_id):
    track_audio_features = requests.get(BASE_URL + 'audio-features/' + track_id,
                     headers=headers)
    
    f = track_audio_features.json()
    audio_features = {}
    audio_features['danceability'] = f['danceability']
    audio_features['energy'] = f['energy']
    audio_features['key'] = f['key']
    audio_features['loudness'] = f['loudness']
    audio_features['speechiness'] = f['speechiness']
    audio_features['acousticness'] = f['acousticness']
    audio_features['instrumentalness'] = f['instrumentalness']
    audio_features['liveness'] = f['liveness']
    audio_features['valence'] = f['valence']
    audio_features['tempo'] = f['tempo']
    return audio_features

# GET request for artist details
def getArtistDetails(artist_id):
    a = requests.get(BASE_URL + 'artists/' + artist_id,
                     headers=headers)
    a = a.json()
    
    artist = {}
    artist['followers'] = a['followers']['total']
    if len(a['genres']) > 0:
        artist['genre'] = a['genres'][0]
    else:
        artist['genre'] = "None"
    artist['popularity'] = a['popularity']
    return artist
    
df2 = pd.DataFrame(columns = ['id', 'name', 'popularity', 'preview_url', 'link', 'duration_ms', 'album_id', 
                             'album_name', 'release_date', 'album_img_64', 'album_img_300', 'artist_id',
                             'artist_name', 'followers', 'genre', 'artist_popularity', 'danceability', 'energy',
                             'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 
                             'valence', 'tempo'])

#https://open.spotify.com/playlist/4ger2fawKKEd086DhfJQ1Y
playlist_id = '4ger2fawKKEd086DhfJQ1Y'

for i in [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]:
    
    # actual GET request with proper header
    r = requests.get(BASE_URL + 'playlists/' + playlist_id + '/tracks',
                     params={'market': 'ES', 'offset': i},
                     headers=headers)
    
    r = r.json()
    
    data = r
    
    for item in data['items']:
        track = item['track']
        id = track['id']
        name = track['name']
        popularity = track['popularity']
        preview_url = track['preview_url']
        link = track['external_urls']['spotify']
        duration_ms = track['duration_ms']
        
        album = track['album']
        album_id = album['id']
        album_name = album['name']
        release_date = album['release_date']
        if len(album['images']) > 2:
            album_img_64 = album['images'][2]['url']
            album_img_300 = album['images'][1]['url']
        else:
            album_img_64 = "None"
            album_img_300 = "None"
            
        
        artist = album['artists'][0]
        artist_id = artist['id']
        artist_name = artist['name']
        
        artist = getArtistDetails(artist_id)
        
        af = getAudioFeatures(id)
        
        values_to_add = {'id': id, 'name': name, 'popularity': popularity, 'preview_url': preview_url, 'link': link, 'duration_ms': duration_ms,
                         'album_id': album_id, 'album_name': album_name, 'release_date': release_date, 'album_img_64': album_img_64, 
                         'album_img_300': album_img_300, 'artist_id': artist_id, 'artist_name': artist_name, 'followers': artist['followers'],
                         'genre': artist['genre'], 'artist_popularity': artist['popularity'], 'danceability': af['danceability'], 
                         'energy': af['energy'], 'key': af['key'], 'loudness': af['loudness'], 'speechiness': af['speechiness'], 
                         'acousticness': af['acousticness'], 'instrumentalness': af['instrumentalness'], 'liveness': af['liveness'], 
                         'valence': af['valence'], 'tempo': af['tempo']}
        row_to_add = pd.Series(values_to_add, name='x')
        
        df2 = df2.append(row_to_add)
        
df2.to_csv('LOCAL_FILE_PATH', index = False, header=True)