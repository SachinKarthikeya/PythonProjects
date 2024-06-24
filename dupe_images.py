from PIL import Image
import os

def duplicate_image(image_path, num_copies, output_dir):
    try:
        image = Image.open(image_path)
        for i in range(num_copies):
            output_path = os.path.join(output_dir, f"copy_{i+1}.jpg")
            image.save(output_path)
        print(f"{num_copies} copies created successfully in {output_dir}.")
    except Exception as e:
        print(f"An error occurred: {e}")

duplicate_image('/Users/sachinkarthikeya/Python/IMG_1546.jpg', 100, '/Users/sachinkarthikeya/laahiri')