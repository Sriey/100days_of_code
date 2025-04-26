import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 30)
a = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.colour
    a.append((r, g, b))