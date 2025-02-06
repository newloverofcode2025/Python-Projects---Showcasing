from PIL import Image
import numpy as np
import sys

# Define ASCII characters from darkest to lightest
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """Resize the image while maintaining aspect ratio."""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.5)  # Adjust for character aspect ratio
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    """Convert the image to grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Map each pixel to an ASCII character."""
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def format_ascii(ascii_str, width):
    """Format the ASCII string into lines."""
    ascii_lines = [ascii_str[i:i + width] for i in range(0, len(ascii_str), width)]
    return "\n".join(ascii_lines)

def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}.")
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayscale_image(image)
    ascii_str = pixels_to_ascii(image)
    ascii_image = format_ascii(ascii_str, new_width)

    print(ascii_image)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("--width", type=int, default=100, help="Width of the ASCII art")
    args = parser.parse_args()
    main(args.image_path, args.width)