import cv2
import numpy as np
import matplotlib.pyplot as plt

def inpaint(img_path):
            img = cv2.imread(img_path)

            # Your existing inpainting code
            B, G, R = cv2.split(img)
            delta = 128
            l_channel = 0.299 * R + 0.587 * G + 0.114 * B
            a_channel = (R - l_channel) * 0.713 + delta
            b_channel = (B - l_channel) * 0.564 + delta
            thres_value = 235 
            glare_mask1 = (l_channel.max() - 9 <= l_channel) & (l_channel <= 255)
            glare_mask2 = 120 <= a_channel
            glare_mask3 = 120 <= b_channel
            glare_mask = np.logical_and(np.logical_and(glare_mask1, glare_mask2), glare_mask3)

            kernel_size = 20
            dilated = cv2.dilate(glare_mask.astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size)))

            inpainted_img = cv2.inpaint(img, dilated, 20, cv2.INPAINT_TELEA)
            cv2.imshow('inpainted_img',inpainted_img)
            cv2.waitKey(0)


path= "Lugol_s iodine images/4_5.jpg"
inpaint(path)