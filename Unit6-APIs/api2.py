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

req = requests.get(url)
req = req.json()

clean("Pokemon Count")
print(req["count"])


def find_pokemon(name, pokemon, next_url):
    while True:
        for a_pokemon in pokemon:
            if a_pokemon['name'].lower() == name.lower():
                return requests.get(a_pokemon['url']).json()
        request = requests.get(next_url)
        next_url = request.json()['next']
        pokemon = request.json()['results']


pokemon = req["results"]
diglett = find_pokemon("Diglett", pokemon, req['next'])

clean("Diglett ID")
print(diglett['id'])

clean("Diglett Height")
print(diglett['height'])

clean("Diglett Abilties")
for ability in diglett['abilities']:
    print(ability['ability']['name'].capitalize())

clean("Diglett Type")
print(diglett)

# Part 2
# Lyrics Search
# Using the lyrics.ovh API [https://api.lyrics.ovh/v1] complete the
# following:

# Print the lyrics to Bohemian Rhapsody by Queen
# Print the first three words of each line of Bohemian Rhapsody
# Write the lyrics to three of your favorite songs to a file, with
# the song title as the filename

# Part 3
# Star Wars!
# Using the Star Wars API [https://swapi.co/api/] complete the
# following:

# Print Luke Skywalkers eye color
# Print the height of Obi-Wan Kenobi
# Print the terrain of the planet Naboo
# Print the vehicle names from all Star Wars films
# Print the cargo capacity of the ‘X 34 Landspeeder’
# Print the film title the ‘X 34 Landspeeder’ was from
# Locate the text that appears at the start of each film (As seen
# below) Print each text along with the film title above it