import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from PIL import Image

# Load the image
image_path = r"C:\Users\A\OneDrive\Desktop\OPen 3d\pifuhd-main\sample_images\image 1.jpg"  # Replace with the path to your image
img = Image.open(image_path)

# Convert the image to grayscale
img_gray = img.convert('L')

# Convert the image to a NumPy array
img_array = np.array(img_gray)

# Create a meshgrid
x, y = np.meshgrid(np.arange(img_array.shape[1]), np.arange(img_array.shape[0]))

# Normalize pixel values to the range [0, 1]
img_normalized = img_array / 255.0

# Create a figure and 3D axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, img_normalized, cmap=cm.gray, linewidth=0, antialiased=False)

# Display the plot
plt.show()
