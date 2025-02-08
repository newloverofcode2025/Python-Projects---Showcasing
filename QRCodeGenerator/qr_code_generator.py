import qrcode
from PIL import Image

def generate_qr_code(data, file_name="qrcode.png"):
    """
    Generates a QR code from the given data and saves it as an image file.
    :param data: Text or URL to encode in the QR code
    :param file_name: Name of the output file (default: qrcode.png)
    """
    try:
        # Create a QRCode object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        img.save(file_name)
        print(f"QR code generated: {file_name}")
    except Exception as e:
        print(f"Error generating QR code: {e}")

if __name__ == "__main__":
    # Get user input
    data = input("Enter the text or URL to encode in the QR code: ").strip()
    file_name = input("Enter the name of the output file (default: qrcode.png): ").strip() or "qrcode.png"

    # Generate the QR code
    generate_qr_code(data, file_name)