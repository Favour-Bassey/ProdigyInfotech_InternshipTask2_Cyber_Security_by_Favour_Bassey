from PIL import Image  # Importing the Image module from the Pillow library for image processing
import numpy as np  # Importing NumPy for array operations

# Function to encrypt an image using XOR operation
def encrypt_image(image_path, key=None):
    # Open the image using Pillow
    image = Image.open(image_path)
    
    # Convert the image to a NumPy array for easy pixel manipulation
    image_array = np.array(image)

    # Generate a random key if none is provided
    if key is None:
        key = np.random.randint(0, 256, size=image_array.shape, dtype=np.uint8)#This basically generates randowm numbers from 0 to 256
        #And gives it a shape making the image_array.shape ensure it ithe shape as the original message

    # Perform XOR operation between the image array and the key
    encrypted_array = np.bitwise_xor(image_array, key)

    # Convert the encrypted array back to an image
    encrypted_image = Image.fromarray(encrypted_array)
    
    return encrypted_image, key  # Return the encrypted image and the key used

# Function to decrypt an encrypted image using XOR operation
def decrypt_image(image_path, key):
    # Open the encrypted image using Pillow
    encrypted_image = Image.open(image_path)
    
    # Convert the encrypted image to a NumPy array
    encrypted_array = np.array(encrypted_image)

    # Perform XOR operation between the encrypted array and the key
    decrypted_array = np.bitwise_xor(encrypted_array, key)

    # Convert the decrypted array back to an image
    decrypted_image = Image.fromarray(decrypted_array)
    
    return decrypted_image  # Return the decrypted image

# Function to save an image to a file
def save_image(image, path):
    image.save(path)  # Save the image using Pillow's save method

# Example usage of the functions
if __name__ == "__main__":
    # Example image paths
    original_image_path = 'ytdr.png'
    encrypted_image_path = 'encrypted_ytdr.png'
    decrypted_image_path = 'decrypted.png'

    # Encrypt the image
    encrypted_image, key = encrypt_image(original_image_path)
    save_image(encrypted_image, encrypted_image_path)

    # Decrypt the image using the generated key
    decrypted_image = decrypt_image(encrypted_image_path, key)
    save_image(decrypted_image, decrypted_image_path)
'''This whole code is just saying that when you input an image in the original path, it encrypts the image using np and saves
it in a new image called"" and later decrypts it back to its original image'''