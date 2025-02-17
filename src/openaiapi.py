from openai import OpenAI

client = OpenAI()  # Store API key securely!

#get user input for songs
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

#Construct api request
prompt = "Make a playist that is "+str(length)+" songs long, and has the same style and theme as these songs: "+str(songs)+". Please just list out the song names and their artists."

# Make API request
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=200
)

# Print the response
print(response.choices[0].message.content)