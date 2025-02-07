from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(image_path, output_path, watermark_text):
    """Adds a watermark to an image."""
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"The file {image_path} does not exist.")
        
        image = Image.open(image_path).convert("RGBA")
        width, height = image.size

        # Create a transparent layer for the watermark
        watermark_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark_layer)

        # Define font and position
        font = ImageFont.truetype("arial.ttf", 40)  # Change font path if needed
        text_width, text_height = draw.textsize(watermark_text, font)
        position = ((width - text_width) // 2, (height - text_height) // 2)

        # Add watermark text
        draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))

        # Combine image and watermark
        watermarked_image = Image.alpha_composite(image, watermark_layer)
        watermarked_image.save(output_path, "PNG")
        print(f"Watermarked image saved to {output_path}")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_path = "images/example.jpg"
    output_path = "images/watermarked_example.png"
    watermark_text = "Sample Watermark"

    add_watermark(image_path, output_path, watermark_text)