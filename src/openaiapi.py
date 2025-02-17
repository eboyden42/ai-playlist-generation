from openai import OpenAI

client = OpenAI()  # Store API key securely!

#construct api request
def getPlaylist(length, songs):
    prompt = "Make a playist that is "+str(length)+" songs long, and has the same style and theme as these songs: "+str(songs)+". Please just list out the song names and their artists."
    # Make API request
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    return response.choices[0].message.content

def reformatPlaylist(playlist):
    prompt = "Reformat the following playlist as a list of names of songs seperated by commas (output nothing except the list): "+playlist
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    return response.choices[0].message.content

def getPlaylistInListForm(length, songs):
    plainPlaylist = getPlaylist(length, songs)
    csvPlaylist = reformatPlaylist(plainPlaylist)
    return csvPlaylist.split(",")

def getGenre(songs):
    prompt = "Based on the following playlist output 1-3 words describing the general genre or vibe" + str(songs)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    return response.choices[0].message.content