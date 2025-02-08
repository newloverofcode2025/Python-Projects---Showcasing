import os
import markdown
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from string import Template

# Path to the Markdown file and HTML template
MARKDOWN_FILE = "sample.md"
TEMPLATE_FILE = "templates/preview.html"
OUTPUT_FILE = "preview.html"

def convert_markdown_to_html():
    """Converts the Markdown file to HTML and updates the preview."""
    try:
        # Read the Markdown content
        with open(MARKDOWN_FILE, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Load the HTML template
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            template = Template(f.read())

        # Replace placeholder with the generated HTML content
        rendered_html = template.safe_substitute(content=html_content)

        # Write the updated HTML to the output file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(rendered_html)

        print("Preview updated!")
    except Exception as e:
        print(f"Error updating preview: {e}")

class MarkdownFileHandler(FileSystemEventHandler):
    """Handles file change events."""
    def on_modified(self, event):
        if event.src_path.endswith(MARKDOWN_FILE):
            print(f"{MARKDOWN_FILE} has been modified. Updating preview...")
            convert_markdown_to_html()

if __name__ == "__main__":
    # Initial conversion
    convert_markdown_to_html()

    # Set up file watcher
    observer = Observer()
    observer.schedule(MarkdownFileHandler(), path=".", recursive=False)
    observer.start()

    print(f"Watching {MARKDOWN_FILE} for changes. Open {OUTPUT_FILE} in your browser to see the live preview.")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()