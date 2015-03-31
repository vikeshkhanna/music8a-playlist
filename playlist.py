import sys
import spotipy
import spotipy.util as util
import json

SPOTIFY_CLIENT_ID="584bd0dbac1544f8993d080baac71bc0"
SPOTIFY_CLIENT_SECRET="redacted"
SPOTIFY_REDIRECT_URI="http://localhost:8888/callback"

if len(sys.argv) < 4:
  print("Usage: python prog.py <SONG_FILE> <PLAYLIST_ID> <SPOTIFY USERNAME>")
  print("Example: python playlist.py playlist1.txt 6AEtEm4wo8Wnd24DrTXWzh 1242920378")
  sys.exit(1)

song_file = sys.argv[1]
playlist_id = sys.argv[2]
spotify_username = sys.argv[3]

scope = "playlist-modify-public"
token = util.prompt_for_user_token(spotify_username, scope, client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI)

if token:
  sp = spotipy.Spotify(auth=token)
else:
  print "Can't get token for ", spotify_username
  sys.exit(1)

f = open(song_file)
failed_songs=[]
success = 0
cnt = 0

for i, line in enumerate(f.readlines()):
  cnt += 1

  try:
    artist, song = map(str.strip, line.split(":"))
  except:
    print "Invalid format for line: %d" % i

  response = sp.search(q='track:' + song + ' artist:' + artist, type='track')
  print "Adding %s by %s..." % (song, artist)
  tup = (i, artist, song)

  if not response:
    print "%s failed with error : %s" % (line, sys.exc_info())
    failed_songs.append(tup)
    continue

  tracks = response['tracks']
  items = tracks['items']

  if len(items) == 0:
    print "Not enough results from Spotify. Check song name and artist name."
    failed_songs.append(tup)
    continue

  track = items[0]
  results = sp.user_playlist_add_tracks (spotify_username, playlist_id, [track["id"]])
  success += 1
  
print "Successfully added: %d/%d" % ( success, cnt )

if len(failed_songs) > 0:
  print "Failed songs..."
  for tup in failed_songs:
    print tup

f.close()
