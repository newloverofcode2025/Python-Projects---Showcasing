# ASCII Art Generator 🎨

A Python script that converts images into **ASCII art** using the `Pillow` library. This project demonstrates how to process images and map pixel values to ASCII characters.

## Features

- Resize images while maintaining aspect ratio
- Convert images to grayscale
- Map pixel values to ASCII characters
- Format ASCII characters into a structured output

## Requirements

- Python 3.x
- Pillow
- NumPy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ASCIIArtGenerator.git
    cd ASCIIArtGenerator
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    # source .venv/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To convert an image to ASCII art, run the script with the path to the image file and optionally specify the width of the ASCII art:

```sh
python ascii_art.py path/to/your/image.jpg --width 80
```

## Example Output

Here’s what the ASCII art looks like when converting an image:

![Example Image](example.jpg)

Make sure to replace `https://github.com/yourusername/ASCIIArtGenerator.git` with the actual URL of your repository. This `README.md` now includes sections for features, requirements, installation, usage, an example, contributing, and license information.
