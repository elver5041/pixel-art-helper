from PIL import Image

def force_pixels(image_path, colors_to_compare) -> Image:
    img = Image.open(image_path)
    img = img.convert('RGB')
    width, height = img.size
    for y in range(height):
        for x in range(width):
            col = img.getpixel((x, y))
            closest_color = None
            min_distance = float('inf')
            for target_color in colors_to_compare:
                distance = sum(abs(c1 - c2) for c1, c2 in zip(col, target_color))
                if distance < min_distance:
                    min_distance = distance
                    closest_color = target_color
            img.putpixel((x, y), closest_color)
    return img
    

def upscale_image(image_path, scale) -> Image:
    img = Image.open(image_path)
    img = img.convert('RGB')
    width, height = img.size
    rgb_array = []
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            for _ in range(scale):
                row.append((r, g, b))
        for _ in range(scale):
            rgb_array.append(row)

    height = len(rgb_array)
    width = len(rgb_array[0])
    img = Image.new('RGB', (width, height))
    for y in range(height):
        for x in range(width):
            img.putpixel((x, y), rgb_array[y][x])
    return img

def main() -> None:
    while True:
        image_path = input("image src: ")
        image_out_path = input("image out: ")
        image:Image = None
        a = input("mode: ")
        if a == "setColors" or a == "sc":
            rgb_colors = [(0,0,0),(255,255,255),(255,0,0)]
            #rgb_colors = [(0,0,0),(255,255,255),(255,0,0),(255,255,0),(0,0,255)]
            image = force_pixels(image_path, rgb_colors)
        if a == "upscale" or a == "us":
            scale = int(input("x:"))
            image = upscale_image(image_path, scale)
        if a == "q" or a == "quit":
            break
        image.show()
        image.save(f"{image_out_path}.png")


if __name__ == "__main__":
    main()