from PIL import Image

im = Image.open("ascii.jpeg")

print("Successfully loaded image")
print(f"Image size:  {im.size[0]} x {im.size[1]}")

pixels = []

for y in range(im.size[1]):
    row = []
    for x in range(im.size[0]):
        pixel = im.getpixel((x, y))
        row.append(pixel)
    pixels.append(row)

brightness = []

for y in range(im.size[1]):
    rows = []
    for x in range(im.size[0]):
        average = ((pixels[y][x][0] + pixels[y][x][1] + pixels[y][x][2]) / 3)
        rows.append(average)
    brightness.append(rows)

print("Successfully constructed brightness matrix!")
print(f"Brightness matrix size {len(brightness)} * {len(brightness[0])}")

ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

ascii_matrix = []

for y in range(im.size[1]):
    ascii_row = []
    for x in range(im.size[0]):
        index = int(brightness[y][x] * (65 / 256))
        character = ascii_chars[index]
        ascii_row.append(character)
    ascii_matrix.append(ascii_row)

print("Successfully constructed ASCII matrix!")
print(f"ASCII matrix size {len(ascii_matrix)} * {len(ascii_matrix[0])}")

for row in ascii_matrix:
    print(''.join(row))










