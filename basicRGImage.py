from PIL import Image

def basicRGImage():
    image = Image.new('RGB', (width, height))
    
    pixels = image.load()
    
    for y in range(height):
        for x in range(width):

            red = int((x / width) * 255)
            green = int((y / height) * 255)
            blue = int(((x + y) / (width + height)) * 255)
            
            pixels[x, y] = (red, green, blue)
    
    return image

gradient_image = basicRGImage(10, 10)
gradient_image.show()
