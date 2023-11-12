import requests
text = requests.get('https://www.google.com/fbx?fbx=snake_arcade').text
print(text)