import numpy as np
import matplotlib.pyplot as plt

def RLE_decode(rle_data, image_shape):
    

    #initialise empty list for decompressed values
    decompressed_data = []
    for value, count in rle_data:
        decompressed_data.extend([value] * count)
        
    #convert decompressed data into numpy array with specified dimensions
    image_array = np.array(decompressed_data).reshape(image_shape)
    
    return image_array


#RLE data
rle_data = [(1, 5), (2, 3), (1, 4), (0, 4)]
image_shape = (4, 4)

#decode the data 
decoded_image = RLE_decode(rle_data, image_shape)

#display 
plt.imshow(decoded_image, cmap='gray')
plt.title('Decompressed Image')
plt.show()

