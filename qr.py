pip install qrcode[pil]
import qrcode

# Create a QR code instance with your message
data = "https://www.example.com"  # Replace with your desired message or URL
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create a QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file (or display it)
img.save("my_qr_code.png")
