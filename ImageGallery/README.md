# Image Gallery

This is a simple Image Gallery web application built with Flask. The application displays a gallery of images on the home page.

## Prerequisites

- Python 3.x
- Flask

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install Flask
    ```

## Running the Application

1. Start the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000` to view the image gallery.

## Project Structure

## Project Files

- [app.py](http://_vscodecontentref_/2): The main Flask application file.
- [style.css](http://_vscodecontentref_/3): The CSS file for styling the web pages.
- [index.html](http://_vscodecontentref_/4): The HTML template for the home page.

## Adding Images

To add images to the gallery, place your image files in the `static/images/` directory and update the [images](http://_vscodecontentref_/5) list in the [home](http://_vscodecontentref_/6) function in [app.py](http://_vscodecontentref_/7) with the filenames of the new images.

## License

This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/8) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [Jinja2](https://palletsprojects.com/p/jinja/) - The templating engine used.
Make sure to replace <repository-url> and <repository-directory> with the actual URL and directory name of your repository. Make sure to replace <repository-url> and <repository-directory> with the actual URL and directory name of your repository.
