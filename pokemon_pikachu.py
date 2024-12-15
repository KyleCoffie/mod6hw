import requests

#task 2
pokemon_name = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    pokemon_data = response.json()
    
    # Extract the name and abilities
    name = pokemon_data['name'].capitalize()
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    
    # Print the name and abilities
    print(f"Name: {name}")
    print(f"Abilities: {', '.join(abilities)}")
else:
    print("Failed to fetch data for the Pokémon.")

#task 3
def fetch_pokemon_data(pokemon_name):#get the info from pokemon_names... line 26
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:#200 equals a successfull connection
        return response.json()#if successful it returns the json response
    else:
        return None

def calculate_average_weight(pokemon_list):#list is also line 26
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)#caluation for the average weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]#this is the parameter for both functions
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]#list comp stores info into pokemon_data

if None not in pokemon_data:
    average_weight = calculate_average_weight(pokemon_data)
    for pokemon in pokemon_data:#loop over pokemon_data
        name = pokemon['name'].capitalize()
        abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
        print(f"Name: {name}")
        print(f"Abilities: {', '.join(abilities)}")
    print(f"Average Weight of the 3 pokemon are: {average_weight:.2f} hectograms")
else:
    print("Failed to fetch data for one or more Pokémon.")
