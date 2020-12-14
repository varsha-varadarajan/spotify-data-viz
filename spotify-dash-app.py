# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 10:27:34 2020

@author: varsha
"""

import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import dash_table

external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

server = app.server

# current working directory
script_dir = os.path.dirname(__file__)
# data folder
data_folder = os.path.join(script_dir, "data")
# data csv file
rel_path = "dataframe-1147.csv"
rel_to_cwd_path = os.path.join(data_folder, rel_path)

df = pd.read_csv(rel_to_cwd_path)

df_table = df[['name', 'year', 'popularity', 'duration_ms', 'album_name', 'artist_name', 'genre']]

available_artists = df['artist_name'].unique()

app.layout = html.Div([
        dcc.Tabs(id='tabs-example', value='tab-1', children=[
            dcc.Tab(label='Spotify Track Visualization', value='tab-1'),
            dcc.Tab(label='Audio Features', value='tab-2'),
        ]),
        html.Div(id='tabs-example-content'),
        
])
            
# 2 tab view
@app.callback(Output('tabs-example-content', 'children'),
              Input('tabs-example', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            dbc.Container([
                html.Br(),
                dbc.Row([
                    dbc.Col(html.H1(children='Spotify Track Visualization', className="text-center"), className="mb-2")
                ]),
                dbc.Row([
                    dbc.Col(html.H6(children='Visualising music trends across the world from 1995 - 2020', className="text-center"), className="mb-4")
                ]),
                dbc.Row([
                    dbc.Col(html.A('GitHub', href='https://github.com/varsha-varadarajan/spotify-data-viz', className="text-center"))
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col(dbc.Card(html.H3(children='View Top Tracks from 1995 - 2020',
                                             className="text-center text-light bg-dark"), body=True, color="dark"), className="mt-4 mb-4")
                ]),
                dbc.Row([
                    dbc.Col(dcc.Dropdown(
                        id='choose_columns',
                        options=[
                            {'label': 'Name', 'value': 'name'},
                            {'label': 'Release year', 'value': 'year'},
                            {'label': 'Popularity', 'value': 'popularity'},
                            {'label': 'Album', 'value': 'album_name'},
                            {'label': 'Artist', 'value': 'artist_name'},
                            {'label': 'Genre', 'value': 'genre'},
                            {'label': 'Track length', 'value': 'duration_ms'},
                            {'label': 'Artist Popularity', 'value': 'artist_popularity'},
                            {'label': 'Danceability', 'value': 'danceability'},
                            {'label': 'Loudness', 'value': 'loudness'},
                            {'label': 'Energy', 'value': 'energy'}
                        ],
                        value=['name', 'year', 'album_name', 'artist_name', 'genre'],
                        multi=True,
                        style={'width': '100%', 'margin-left':'5px'}
                    ), width=6),
                    dbc.Col(
                        dbc.Input(id="num_rows", type="number", min=5, max=100, value=10, step=1, style={'width': '100%', 'height': '34px'}),
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id='sort_by',
                            options=[
                                {'label': 'Name', 'value': 'name'},
                                {'label': 'Release year', 'value': 'year'},
                                {'label': 'Popularity', 'value': 'popularity'},
                                {'label': 'Album', 'value': 'album_name'},
                                {'label': 'Artist', 'value': 'artist_name'},
                                {'label': 'Genre', 'value': 'genre'},
                                {'label': 'Track length', 'value': 'duration_ms'},
                                {'label': 'Artist Popularity', 'value': 'artist_popularity'}
                            ],
                            value='year',
                            style={'width': '100%', 'margin-left':'5px'}
                        ),
                    )
                ]),

                dash_table.DataTable(
                    id='datatable-1',
                    style_table={'overflowX': 'scroll',
                                    'padding': '10px'},
                    style_header={'backgroundColor': '#25597f', 'color': 'white'},
                    style_cell={
                        'backgroundColor': 'white',
                        'color': 'black',
                        'fontSize': 13,
                        'font-family': 'Nunito Sans',
                        'maxWidth': 0,
                        'textAlign': 'left'},
                    style_data={
                        'whiteSpace': 'normal',
                        'height': 'auto'
                    },
                    style_cell_conditional=[
                        {'if': {'column_id': 'popularity'},
                         'width': '10%'},
                        {'if': {'column_id': 'year'},
                         'width': '10%'},            
                        {'if': {'column_id': 'name'},
                         'paddingLeft': '5px'}
                ]),
    
                dbc.Row([
                    dbc.Col(dbc.Card(html.H3(children='Search by keyword',
                                             className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mt-4 mb-4")
                ]),
                
                dbc.Row([
                    dbc.Col(
                        dbc.Input(id="search_term", type="text", value='', placeholder='Search by Track/Artist/Album/Genre/ReleaseYear', style={'width': '100%'}),
                    ),
                ]),
            
                dash_table.DataTable(
                    id='datatable-2',
                    style_table={'overflowX': 'scroll',
                                    'padding': '10px'},
                    style_header={'backgroundColor': '#25597f', 'color': 'white'},
                    style_cell={
                        'backgroundColor': 'white',
                        'color': 'black',
                        'fontSize': 13,
                        'font-family': 'Nunito Sans',
                        'maxWidth': 0,
                        'textAlign': 'left'},
                    style_data={
                        'whiteSpace': 'normal',
                        'height': 'auto'
                    },
                    style_cell_conditional=[
                        {'if': {'column_id': 'popularity'},
                         'width': '10%'},
                        {'if': {'column_id': 'year'},
                         'width': '10%'},            
                        {'if': {'column_id': 'name'},
                         'paddingLeft': '5px'}
                ]),
            
                dbc.Row([
                    dbc.Col(dbc.Card(html.H3(children='Distribution by Genre over the years',
                                             className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mt-4 mb-4")
                ]),
                        
                dbc.Row([
                    dbc.Col(
                        dcc.RangeSlider(id='year-range',
                                        min=1980,
                                        max=2020,
                                        step=1,
                                        value=[2000, 2020],
                                        marks={i:str(i) for i in range(1980, 2020, 5)})
                    ),
                ]),

                dbc.Row([
                    dbc.Col(html.H5(children='Top genre in year range', className="text-center"),
                                     width=12, className="mt-4"),
                ]),

                dbc.Row([
                    dbc.Col(dcc.Graph(id='bar_genre'), width=12)
                ]),
            ])
        ])
    elif tab == 'tab-2':
        return html.Div([
            dbc.Container([
                html.Br(),
                dbc.Row([
                    dbc.Col(html.H1(children='Audio Features of Hit songs', className="text-center"), className="mb-2")
                ]),
                dbc.Row([
                    dbc.Col(html.H6(children='Analyzing audio features over the years', className="text-center"), className="mb-4")
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col(dbc.Card(html.H3(children='Audio Features of Songs',
                                             className="text-center text-light bg-dark"), body=True, color="dark"), className="mb-4")
                ]),
                dbc.Row([
                    dbc.Col(html.H5(children='Top Tracks by Feature', className="text-center"),
                            className="mt-4")
                ]),
                html.Label('Number of tracks'),
                dbc.Col(
                    dbc.Input(id="feature_table_rows", type="number", min=5, max=100, value=10, step=1, style={'width': '100%', 'height': '34px'}),
                ),
                html.Label('Audio features'),
                dbc.Col(
                    dcc.Dropdown(
                        id='feature_table_sort_by',
                        options=[
                            {'label': 'Danceability', 'value': 'danceability'},
                            {'label': 'Energy', 'value': 'energy'},
                            {'label': 'Loudness', 'value': 'loudness'},
                            {'label': 'Speechiness', 'value': 'speechiness'},
                            {'label': 'Accousticness', 'value': 'acousticness'},
                            {'label': 'Liveness', 'value': 'liveness'},
                            {'label': 'Instrumentalness', 'value': 'instrumentalness'},
                            {'label': 'Valence', 'value': 'valence'},
                            {'label': 'Tempo', 'value': 'tempo'}
                        ],
                        value='liveness',
                        style={'width': '100%', 'margin-left':'5px'}
                    ),
                ),
                dash_table.DataTable(
                    id='datatable-3',
                    style_table={'overflowX': 'scroll',
                                    'padding': '10px'},
                    style_header={'backgroundColor': '#25597f', 'color': 'white'},
                    style_cell={
                        'backgroundColor': 'white',
                        'color': 'black',
                        'fontSize': 13,
                        'font-family': 'Nunito Sans',
                        'maxWidth': 0,
                        'textAlign': 'left'},
                    style_data={
                        'whiteSpace': 'normal',
                        'height': 'auto'
                    },
                    style_cell_conditional=[
                        {'if': {'column_id': 'popularity'},
                         'width': '10%'},
                        {'if': {'column_id': 'year'},
                         'width': '10%'},            
                        {'if': {'column_id': 'name'},
                         'paddingLeft': '5px'}
                    ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col(dbc.Card(html.H3(children='Audio feature pattern',
                                             className="text-center text-light bg-dark"), body=True, color="dark"), className="mb-4")
                ]),
                dbc.Row([
                dbc.Col(dcc.RadioItems(
                            id = 'dropdown-to-show_or_hide-element',
                            options=[
                                {'label': 'All artists', 'value': 'on'},
                                {'label': 'Select artist', 'value': 'off'}
                            ],
                            value = 'on'
                ))
                ]),
                dcc.Dropdown(
                        id='select-artist',
                        options=[{'label': i, 'value': i} for i in available_artists],
                        value=['Rihanna'],
                        multi=True,
                        style={'width': '100%', 'margin-left':'5px', 'display': 'block'}),
                html.Label('Select audio features'),
                dbc.Row([
                    dbc.Col(dcc.Dropdown(
                        id='select-feature',
                        options=[
                            {'label': 'Danceability', 'value': 'danceability'},
                            {'label': 'Energy', 'value': 'energy'},
                            {'label': 'Loudness', 'value': 'loudness'},
                            {'label': 'Speechiness', 'value': 'speechiness'},
                            {'label': 'Accousticness', 'value': 'acousticness'},
                            {'label': 'Liveness', 'value': 'liveness'},
                            {'label': 'Instrumentalness', 'value': 'instrumentalness'},
                            {'label': 'Valence', 'value': 'valence'}
                        ],    
                        value=['danceability', 'energy'],
                        multi=True,
                        style={'width': '100%', 'margin-left':'5px'})
                    )
                ]),
                html.Label('Select year range'),
                dcc.RangeSlider(id='select-year',
                                min=1980,
                                max=2020,
                                step=1,
                                value=[2000, 2020],
                                marks={i:str(i) for i in range(1980, 2020, 5)}),
                dbc.Row([
                    dbc.Col(dcc.Graph(id='audio-features'), width=12)
                ])
        ])
    ])
        
# Datatable 1
@app.callback([Output('datatable-1', 'data'),
              Output('datatable-1', 'columns')],
             [Input('choose_columns', 'value'),
              Input('num_rows', 'value'),
              Input('sort_by', 'value')])
def update_columns(value, num_rows, sort_key):
    new_df = pd.DataFrame()
    for val in value:
        new_df[val] = df[val]
        
    new_df = new_df.sort_values('year', ascending=False)
    
    asc = True
    if sort_key in ['popularity', 'year', 'duration_ms', 'artist_popularity', 'energy', 'danceability', 'loudness']:
        asc = False
    
    if sort_key in value:
        new_df = new_df.sort_values(sort_key, ascending=asc)
    else:
        new_df = new_df.sort_values('year', ascending=False)
    
    columns = [{"name": i, "id": i} for i in value]
    data = new_df.to_dict('records')[:num_rows]
        
    return data, columns

# Datatable 2
@app.callback([Output('datatable-2', 'data'),
              Output('datatable-2', 'columns')],
             [Input('num_rows', 'value'),
              Input('search_term', 'value')])
def update_datatable_2(num_rows, search_term):
    new_df = df[['name', 'year', 'popularity', 'duration_ms', 'album_name', 'artist_name', 'genre']]
        
    l = []
    for index, row in new_df.iterrows():
        name = row['name']
        artist = row['artist_name']
        album = row['album_name']
        genre = row['genre']
        year = row['year']
        
        if search_term.lower() in name.lower() or search_term.lower() in artist.lower() or search_term.lower() in album.lower() or search_term.lower() in genre.lower() or search_term.lower() in str(year):
            l.append(row)
    
    new_df_1 = pd.DataFrame(l)
    columns = [{"name": i, "id": i} for i in new_df_1.columns]
    data = new_df_1.to_dict('records')[:num_rows]
        
    return data, columns

# Datatable 3
@app.callback([Output('datatable-3', 'data'),
              Output('datatable-3', 'columns')],
             [Input('feature_table_rows', 'value'),
              Input('feature_table_sort_by', 'value')])
def update_feature_table(num_rows, sort_key):        
    new_df = df[['name', 'year', 'album_name', 'artist_name', 'genre', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'liveness', 'instrumentalness', 'valence', 'tempo']]
        
    new_df = new_df.sort_values(sort_key, ascending=False)
    
    d = pd.DataFrame()
    for val in ['name', 'year', 'album_name', 'artist_name', 'genre', sort_key]:
        d[val] = new_df[val]
        
    d[sort_key] = ((d[sort_key]*1000).astype(int).astype(float))/100
    
    columns = [{"name": i, "id": i} for i in d.columns]
    data = new_df.to_dict('records')[:num_rows]
        
    return data, columns

# genre bar chart
@app.callback(Output('bar_genre', 'figure'),
              [dash.dependencies.Input('year-range', 'value')])
def update_bar_chart(year):
    df1 = df.copy()
    year_col = df1['year'].astype(int)
    year_range = year_col >= year[0]
    df1 = df1[year_range]
    year_range = year_col <= year[1]
    df1 = df1[year_range]
    
    df2 = df1.groupby('genre').size().reset_index(name='counts').sort_values('counts', ascending=False)
    
    df2 = df2[:10]
    fig = go.Figure(data=[
        go.Bar(x=df2['genre'], y=df2['counts'])
    ])

    fig.update_layout(yaxis={'title': "Number of tracks"},
                    xaxis={'title': "Genre"},
                    barmode='stack',
                    paper_bgcolor = 'rgba(0,0,0,0)',
                    plot_bgcolor = 'rgba(0,0,0,0)',
                    template="seaborn",
                    margin=dict(t=20))
    return fig

# audio features line graph
@app.callback(Output('audio-features', 'figure'),
              [dash.dependencies.Input('select-year', 'value'),
               Input(component_id='dropdown-to-show_or_hide-element', component_property='value'),
               Input('select-artist', 'value'),
               Input('select-feature', 'value')])
def update_features_chart(year, show_artist, artist, feature):
    df1 = df.copy()
    
    # filter year
    year_col = df1['year'].astype(int)
    year_range = year_col >= year[0]
    df1 = df1[year_range]
    year_range = year_col <= year[1]
    df1 = df1[year_range]
    
    if len(artist) == 0 or show_artist == 'on':
        new_df_1 = df1.copy()
    else:    
        # filter artist
        l = []
        for index, row in df1.iterrows():
            ar = row['artist_name']
            if ar in artist:
                l.append(row)
        
        new_df_1 = pd.DataFrame(l)
    
    fig = go.Figure()
    
    for feat in feature:
        grouped_single = new_df_1.groupby('year').agg({feat: 'mean'})
        grouped_single.columns = [feat]
        grouped_single = grouped_single.reset_index()
        
        fig.add_trace(go.Scatter(x=grouped_single['year'], y=grouped_single[feat],
            mode='lines+markers',
            name=feat))
    
    fig.update_layout(title_text='How has audio features changed for artists over the years', title_x=0.5,
                    yaxis={'title': "Mean value of audio features"},
                    xaxis={'title': "Year"})

    return fig

# toggle view of artist dropdown
@app.callback(
   Output(component_id='select-artist', component_property='style'),
   [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')])
def show_hide_element(visibility_state):
    if visibility_state == 'off':
        return {'display': 'block'}
    if visibility_state == 'on':
        return {'display': 'none'}

if __name__ == '__main__':
    app.run_server()