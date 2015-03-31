Spotify playlist creator for Music 8A, Spring 2015, Stanford
============================================================

This is a simple script to generate Spotify playlists from the songs shared by Prof. Mark Applebaum after each class. 

## Prerequisites
Install `spotipy` from [plamere/spotipy] (https://github.com/plamere/spotipy).

## Input file format
Each line should contain the artist and song tuple separated by a colon. For example: Katy Perry: Peacock

## Usage
1. Run the node server on a terminal : `node server.js`. This is required for the Spotify callback URI to work at the time of authentication.
2. Run the python script: `python playlist.py playlist1.txt 6AEtEm4wo8Wnd24DrTXWzh 1242920378`. Replace the arguments with your playlist ID and username.
