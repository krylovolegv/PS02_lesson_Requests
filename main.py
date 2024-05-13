import requests
img = "https://sun9-21.userapi.com/impg/S99EVTZNi9e9CfQLGoZFYG5DlFbyfugWJrUEGw/77y2k9wXdEo.jpg?size=860x484&quality=95&sign=dd48352b65e741350ae537000676cac9&type=album"

response = requests.get(img)

with open("test.jpg", "wb") as file:
    file.write(response.content)