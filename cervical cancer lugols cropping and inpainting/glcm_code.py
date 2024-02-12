from skimage import io, color, util
from skimage.feature import graycomatrix, graycoprops
from skimage.measure import shannon_entropy
import numpy as np
import os
import pandas as pd

def calculate_glcm_properties_and_entropy(image_path):
    image = io.imread(image_path)
    gray_image_f = color.rgb2gray(image) 
    gray_image = util.img_as_ubyte(gray_image_f)

    distances = [1]  
    angles = [0]  
    glcm = graycomatrix(gray_image, distances=distances, angles=angles, levels=256, symmetric=True, normed=True)

    contrast = graycoprops(glcm, 'contrast').ravel().tolist()
    dissimilarity = graycoprops(glcm, 'dissimilarity').ravel().tolist()
    homogeneity = graycoprops(glcm, 'homogeneity').ravel().tolist()
    energy = graycoprops(glcm, 'energy').ravel().tolist()
    correlation = graycoprops(glcm, 'correlation').ravel().tolist()

    # Calculate entropy
    entropy_value = shannon_entropy(gray_image)

    # Return GLCM properties and entropy as a list
    glcm_properties = contrast + dissimilarity + homogeneity + energy + correlation + [entropy_value]
    return glcm_properties

# Specify the folder containing images
folder_path = r'Lugol_s iodine images'  # Replace with the actual path to your image folder

# Create an empty DataFrame to store results
result_df = pd.DataFrame(columns=['Image Name', 'Contrast', 'Dissimilarity', 'Homogeneity', 'Energy', 'Correlation', 'Entropy'])

# Iterate through images in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.png', '.bmp')):  # Add more image extensions if needed
        image_path = os.path.join(folder_path, filename)
        
        # Calculate GLCM properties and entropy
        properties = calculate_glcm_properties_and_entropy(image_path)
        
        # Add results to the DataFrame
        result_df = result_df._append({
            'Image Name': filename,
            'Contrast': properties[0],
            'Dissimilarity': properties[1],
            'Homogeneity': properties[2],
            'Energy': properties[3],
            'Correlation': properties[4],
            'Entropy': properties[5]
        }, ignore_index=True)

# Save the results to an Excel file
excel_path = r'glcm.xlsx'  # Replace with the desired output Excel file path
result_df.to_excel(excel_path, index=False)

print(f'GLCM properties and entropy are saved to: {excel_path}')


