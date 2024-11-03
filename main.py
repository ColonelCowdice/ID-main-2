from PIL import Image

def recolor_image_ignore_white(image_path, output_path, new_color):
    # Open the image with Pillow
    img = Image.open(image_path).convert("RGBA")
    pixels = img.load()

    # Define white color threshold for flexibility in white detection
    white_threshold = (240, 240, 240)

    # Replace non-white pixels with the specified color
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if (r, g, b) < white_threshold:  # Check if pixel is not white
                pixels[x, y] = new_color + (a,)  # Preserve original alpha

    # Save the modified image
    img.save(output_path, format="PNG")
    print(f"Image saved to {output_path}")

# Example usage
image_path = "icon'.png"
output_path = "recolor_image.png"
new_color = (0, 60, 114)  # RGB for the specified blue
recolor_image_ignore_white(image_path, output_path, new_color)
