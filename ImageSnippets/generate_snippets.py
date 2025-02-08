from PIL import Image

def crop_image(image_path, output_folder, rows, cols):
    """Crops an image into smaller snippets."""
    try:
        image = Image.open(image_path)
        width, height = image.size
        snippet_width = width // cols
        snippet_height = height // rows

        os.makedirs(output_folder, exist_ok=True)

        for i in range(rows):
            for j in range(cols):
                left = j * snippet_width
                upper = i * snippet_height
                right = left + snippet_width
                lower = upper + snippet_height
                snippet = image.crop((left, upper, right, lower))
                snippet.save(f"{output_folder}/snippet_{i}_{j}.png")
        print(f"Generated {rows * cols} snippets in {output_folder}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_path = "images/example.jpg"
    output_folder = "snippets"
    rows = 3
    cols = 3

    crop_image(image_path, output_folder, rows, cols)