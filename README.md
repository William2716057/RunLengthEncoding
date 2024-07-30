# RLE Decoder
This script provides a simple Python implementation for decoding Run-Length Encoded (RLE) data and visualizing the decompressed image using matplotlib.

## Overview
Run-Length Encoding (RLE) is a form of data compression where consecutive elements with the same value are stored as a single data value and count. This script decodes RLE data back into its original image form and displays it.

## Installation
To run this script, you'll need to have Python installed along with the following libraries:

- numpy
- matplotlib

You can install the required libraries using pip:
```
pip install numpy matplotlib
```
## Usage

The script includes a function RLE_decode which takes in RLE data and the shape of the resulting image. It decodes the RLE data and returns the decompressed image as a numpy array. The script then visualizes this decompressed image using matplotlib.

## Example

Here's an example of how to use the script:

```
import numpy as np
import matplotlib.pyplot as plt

def RLE_decode(rle_data, image_shape):
    # Initialize empty list for decompressed values
    decompressed_data = []
    for value, count in rle_data:
        decompressed_data.extend([value] * count)
        
    # Convert decompressed data into numpy array with specified dimensions
    image_array = np.array(decompressed_data).reshape(image_shape)
    
    return image_array

# RLE data
rle_data = [(1, 5), (2, 3), (1, 4), (0, 4)]
image_shape = (4, 4)

# Decode the data
decoded_image = RLE_decode(rle_data, image_shape)

# Display 
plt.imshow(decoded_image, cmap='gray')
plt.title('Decompressed Image')
plt.show()
```

## Function Details
RLE_decode

Parameters:

- rle_data (list of tuples): Each tuple contains a value and its count.
- image_shape (tuple): Shape of the decompressed image (rows, columns).

Returns:

- image_array (numpy array): Decompressed image data.

## Visualization
The decompressed image is displayed using matplotlib. In this example, the image is shown in grayscale (cmap='gray').
