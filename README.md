![Logo](https://user-images.githubusercontent.com/6944124/236838124-84cdbd72-3ff4-444b-ab70-4d7ed118fccb.png)
# MCPalette
MCPalette is a Python-based platform that helps Minecraft players find the best matching block for a given color palette. The platform uses image processing and machine learning algorithms to analyze the colors of Minecraft block textures and match them with the colors in the input palette. MCPalette is especially useful for players who want to design their Minecraft worlds with a specific color scheme or theme, but have trouble finding the right blocks.

## Features
Find the best matching Minecraft block for a given color palette
Support for custom palettes with up to 256 colors
Automatic color quantization and palette simplification
Accurate color matching using machine learning algorithms
Simple and intuitive command-line interface
Open-source and customizable

## Usage
#### Clone the MCPalette repository to your local machine using git:
``git clone https://github.com/<username>/MCPalette.git``
Navigate to the cloned repository and install the required dependencies using pip:
``cd MCPalette
pip install -r requirements.txt``

#### Get Block Textures from Minecraft Jar
In order to use this tool, you'll need to obtain the block textures from your Minecraft installation. Here's how you can do that:

Open the Minecraft Launcher and select the installation you want to use.

Click the "Mod Options" button and select "Open Game Dir".
In the game directory, navigate to the "versions" folder.
Find the folder that corresponds to the version you want to use (e.g., "1.16.5") and open it.

Open the .jar file with an archive manager such as WinRAR or 7-Zip.

Navigate to the assets/minecraft/textures/block folder.
Copy all of the .png files in this folder to a new folder on your computer.

Once you have obtained the block textures, you can specify the directory containing them in the block_dir variable in the Python script.

#### Start the program by running the mcpalette.py script and passing the path to your input palette:
``python mcpalette.py -p /path/to/my/palette.png``
Wait for the program to process the palette and display the results:
``Found matching blocks:
20% Grass Block, 20% Oak Wood Planks, 20% Stone, 20% Dirt, 20% Cobblestone``
