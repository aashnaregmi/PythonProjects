import colorgram

colors = colorgram.extract("painting.jpeg", 10)
for color in colors:
    print(color.rgb)
