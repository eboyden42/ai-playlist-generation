import openaiapi
from src.openaiapi import getPlaylist, reformatPlaylist, getPlaylistInListForm, getGenre

#sample input
songs = ["power flower - stevie wonder, sumthin' sumthin', i like it - Debarge"]
length = 10;
getUserInput = False

if getUserInput:
    toggle = True
    print("Hello! To generate a new playlist, enter a few songs that you like and want to hear more of (including an artist is optional).")
    while toggle:
        scan = input("Enter your song, or type DONE to continue:")
        if scan == "DONE":
            toggle = False
            break
        else:
            songs.append(scan)
    toggle = True
    while toggle:
        scan = input("How long would you like your new playlist to be? (30 song maximum)")
        if int(scan) > 30 or int(scan) < 1:
            print("Invalid input. Enter a number from 1 to 30 inclusive.")
        else:
            toggle=False
            length = int(scan)

#get playlist recommendations from openai
list = getPlaylistInListForm(length, songs)
genre = getGenre(songs)
print(genre+":\n")
for element in list:
    print(element)
