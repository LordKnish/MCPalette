import os
from PIL import Image, ImageGrab
import numpy as np

# Get the directory containing the script file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the directory containing the Minecraft block textures
block_dir = os.path.join(script_dir, 'assets', 'minecraft', 'textures', 'block')

# Define the path to the file containing the list of block names
block_list_path = os.path.join(script_dir, 'blocks_full.txt')

# Define a dictionary mapping block names to their RGB colors
block_colors = {}

# Loop through all the block textures and add their colors to the dictionary
for filename in os.listdir(block_dir):
    if filename.endswith('.png'):
        block_name = os.path.splitext(filename)[0]
        if block_name in open(block_list_path).read():
            im = Image.open(os.path.join(block_dir, filename))
            rgb_im = im.convert('RGB')
            color = tuple(np.array(rgb_im).mean(axis=(0,1)).astype(int))
            block_colors[block_name] = color

# Get the image from the clipboard
im = ImageGrab.grabclipboard()

# Convert the image to RGB if necessary
if im.mode != 'RGB':
    im = im.convert('RGB')

# Get the color palette
palette = im.quantize(colors=256).getpalette()

# Reshape the palette into a 256x1 array of RGB tuples
palette = np.array(palette).reshape((256, 3))

# Get the most common colors in the palette
unique_colors, color_counts = np.unique(palette, axis=0, return_counts=True)

# Sort the colors by count in descending order
sorted_indices = np.argsort(color_counts)[::-1]
unique_colors = unique_colors[sorted_indices]

# Simplify the palette to 5 colors
palette = unique_colors[:5]

# Find the best matching block for each color in the palette
block_palette = []
for color in palette:
    color_blocks = []
    for block_name, block_color in block_colors.items():
        distance = np.sqrt(np.sum(np.square(np.array(color) - np.array(block_color))))
        color_blocks.append((block_name, distance))
    color_blocks.sort(key=lambda x: x[1])
    block_palette.append(color_blocks[0][0])

# Calculate the percentage for each block
block_percentages = {}
total_percentage = 0
for block_name in set(block_palette):
    percentage = int(block_palette.count(block_name) / len(block_palette) * 100)
    block_percentages[block_name] = percentage
    total_percentage += percentage

# Add the remaining percentage to the block with the highest percentage
block_percentages[max(block_percentages, key=block_percentages.get)] += 100 - total_percentage

# Format the percentages as strings with percent signs
for block_name in block_percentages:
    block_percentages[block_name] = f"{block_percentages[block_name]}%"

# Print the block percentages
text = ""
for block_name, percentage in block_percentages.items():
    text += (percentage + "" + block_name + ",")
print(text)
