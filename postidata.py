from urllib.request import urlopen
import json

def getData():
    with urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        json_response = response.read()

    return json.loads(json_response)