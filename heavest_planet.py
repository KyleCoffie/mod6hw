import requests

def fetch_plant_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets =response.json()['bodies']
    
    formatted_planets = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass =planet['mass']['massValue'] if planet['mass'] else None
            formatted_planets.append({'name': name, 'mass': mass})
    return formatted_planets

def find_heavest_planet(planets):
    heaviest_planet = max(planets, key = lambda x: x['mass']if x['mass'] else 0)
    return heaviest_planet['name'], heaviest_planet['mass']

planets = fetch_plant_data()
name, mass = find_heavest_planet(planets)

print(f"The heaviest planet is {name} with a mass of {mass}.")