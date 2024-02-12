from PIL import Image, ImageDraw

def elliptical_crop_and_display(input_path, axes):
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

    # Display the result
    result.show()

# Example usage
input_image_path = 'inpaint/AAA1_in.jpg'
# Axes (semi-major and semi-minor)
axes = (350, 200)

elliptical_crop_and_display(input_image_path, axes)
