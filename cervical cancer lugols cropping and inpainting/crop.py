from PIL import Image, ImageDraw
import os

def elliptical_crop(input_path, axes):
    # Open the image
    img = Image.open(input_path)
    img_width, img_height = img.size

    # Calculate the bounding box
    x0 = int(img_width / 2 - axes[0])
    y0 = int(img_height / 2 - axes[1])
    x1 = int(img_width / 2 + axes[0])
    y1 = int(img_height / 2 + axes[1])

    # Create a mask
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((x0, y0, x1, y1), fill=255)

    # Apply the mask to the image
    result = Image.new('RGB', img.size)
    result.paste(img, mask=mask)

    return result

# Input and output directories
input_dir = r"Lugol_s iodine images"
output_dir = r"Lugols_crop1"
# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Axes (semi-major and semi-minor)
axes = (250, 350)

# Loop through all images in the input directory and save cropped versions
for filename in os.listdir(input_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        input_image_path = os.path.join(input_dir, filename)
        output_image_path = os.path.join(output_dir, f'{filename.split(".")[0]}_crop1.jpg')

        cropped_image = elliptical_crop(input_image_path, axes)
        cropped_image.save(output_image_path)
