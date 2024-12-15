import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    
    
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']#get planet English name
            mass = planet['mass']['massValue'] if planet['mass'] else 'Unknown'#get planet mass
            orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else'Unkwon'#get planet orbit period
            print(f"Planet: {name}, Mass: {mass} , Orbit Period: {orbit_period} days")

fetch_planet_data()