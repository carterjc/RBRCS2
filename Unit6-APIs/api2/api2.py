# Carter Costic
# api2.py

import requests


def clean(word):
    print(f"\n\n----{word}----\n\n")


# Part 1
# POKEMON!
# Using the PokeAPI [https://pokeapi.co/api/v2/] complete the
# following:

# Display the total amount of Pokemon available to the API
# Print the id of the Pokemon Diglett
# Print the height of Diglett
# Print all abilities of Diglett
# Print the Pokemon type of Diglett
# Print the id, height, abilities and type of your favorite Pokemon!

url = "https://pokeapi.co/api/v2/pokemon"

req_poke = requests.get(url)
req_poke = req_poke.json()

clean("Pokemon Count")
print(req_poke["count"])


def find_pokemon(name, pokemon, next_url):
    while True:
        for a_pokemon in pokemon:
            if a_pokemon['name'].lower() == name.lower():
                return requests.get(a_pokemon['url']).json()
        request = requests.get(next_url)
        next_url = request.json()['next']
        pokemon = request.json()['results']


def poke_info(poke):
    name = poke["forms"][0]["name"].capitalize()
    clean(f"{name} ID")
    print(poke['id'])

    clean(f"{name} Height")
    print(poke['height'])

    clean(f"{name} Abilities")
    for ability in poke['abilities']:
        print(ability['ability']['name'].capitalize())

    clean(f"{name} Type")
    print(poke["types"][0]["type"]["name"].capitalize())


pokemon = req_poke["results"]

# Diglett
diglett = find_pokemon("Diglett", pokemon, req_poke['next'])
poke_info(diglett)


# My choice: Pikachu
pikachu = find_pokemon("Pikachu", pokemon, req_poke['next'])
poke_info(pikachu)

# Part 2
# Lyrics Search
# Using the lyrics.ovh API [https://api.lyrics.ovh/v1] complete the
# following:

# Print the lyrics to Bohemian Rhapsody by Queen
# Print the first three words of each line of Bohemian Rhapsody
# Write the lyrics to three of your favorite songs to a file, with
# the song title as the filename

music_url = "https://api.lyrics.ovh/v1/"
f_artist = "Queen"
f_title = "Bohemian%20Rhapsody"
req_music = requests.get(music_url + f_artist + "/" + f_title)
song = req_music.json()

clean("Bohemian Rhapsody Lyrics")
print(song["lyrics"])

clean("First Three Words of Line")
for line in song["lyrics"].split("\n"):
    words = line.split(" ")[:3]
    if words[0] != "":
        print(" ".join(words))


def lyrics_to_file(title, artist):
    l_music_url = "https://api.lyrics.ovh/v1/" + artist.replace(" ", "%20") + "/" + title.replace(" ", "%20")
    lyrics = requests.get(l_music_url).json()["lyrics"]
    with open(title.replace(" ", "_") + '.txt', "w") as f:
        f.write(lyrics)


lyrics_to_file("Circles", "Post Malone")
lyrics_to_file("Dance Monkey", "Tones and I")
lyrics_to_file("Don't Start Now", "Dua Lipa")


# Part 3
# Star Wars!
# Using the Star Wars API [https://swapi.co/api/] complete the
# following:

star_wars_url = "https://swapi.co/api/"

# Print Luke Skywalkers eye color
# Print the height of Obi-Wan Kenobi
# Print the terrain of the planet Naboo
# Print the vehicle names from all Star Wars films
# Print the cargo capacity of the ‘X 34 Landspeeder’
# Print the film title the ‘X 34 Landspeeder’ was from
# Locate the text that appears at the start of each film (As seen
# below) Print each text along with the film title above it

people = requests.get(star_wars_url + "people").json()['results']
clean("Luke's Eye Color")
print(people[0]['eye_color'].capitalize())

clean("Obi-Wan's Height")
print(people[-1]['height'])

planets = requests.get(star_wars_url + "planets").json()['results']
clean("Naboo's Terrain")
print(planets[6]['terrain'].capitalize())

vehicles = requests.get(star_wars_url + "vehicles").json()['results']
clean("Star Wars Vehicle Names")
for vehicle in vehicles:
    print(vehicle['name'])

clean("X-34 Landspeeder Cargo Capacity")
print(vehicles[2]["cargo_capacity"])

clean("X-34 Films")
print(requests.get(vehicles[2]['films'][0]).json()['title'])

films = requests.get(star_wars_url + "films").json()['results']
for film in films:
    clean(f"{film['title']} Opening Crawl")
    print(film['opening_crawl'])

