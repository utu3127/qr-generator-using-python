import qrcode

# Function to generate a QR code for a song link
def generate_song_qr(song_url):
    # Create a QRCode object
    qr = qrcode.QRCode(
        version=1,  # Version 1: smallest size QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=10,  # Size of the boxes in the QR code
        border=4,  # Border size around the QR code
    )

    # Add the song URL to the QR code
    qr.add_data(song_url)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill='black', back_color='white')

    # Save the QR code as a PNG image
    img.save("song_qr_code.png")

    print(f"QR code for the song has been generated and saved as 'song_qr_code.png'.")

# Example usage
if __name__ == "__main__":
    # Input the song URL from the user
    song_url = input("Enter the URL of the song: ")
    
    # Call the function to generate the QR code
    generate_song_qr(song_url)
