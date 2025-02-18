from PIL import Image
import os

def resize_image(input_path, output_folder, sizes):
    """
    Resizes an image to the specified sizes and saves them in the output folder.

    :param input_path: Path to the input image file.
    :param output_folder: Folder where resized images will be saved.
    :param sizes: List of tuples representing the desired sizes (width, height).
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Ensure the output folder exists
            os.makedirs(output_folder, exist_ok=True)
            
            # Get the base name of the file (without extension)
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            
            # Resize the image for each size in the list
            for size in sizes:
                # Resize the image
                resized_img = img.resize(size, Image.ANTIALIAS)
                
                # Create the output file path
                output_path = os.path.join(output_folder, f"{base_name}_{size[0]}x{size[1]}.jpg")
                
                # Save the resized image with reduced quality to decrease file size
                resized_img.save(output_path, "JPEG", quality=85)
                
                print(f"Saved: {output_path}")
    
    except Exception as e:
        print(f"Error processing image: {e}")

# Example usage
if __name__ == "__main__":
    # Input image path
    input_image = "input_image.jpg"
    output_folder = "resized_images"
    sizes = [(800, 600), (640, 480), (320, 240)]
    
    # Resize the image
    resize_image(input_image, output_folder, sizes)