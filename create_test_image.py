#!/usr/bin/env python3
"""
Create a test PNG image for Jekyll GitHub LFS testing.
"""

from PIL import Image, ImageDraw
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Create a test image with visible content
img = Image.new('RGB', (400, 300), color='white')
draw = ImageDraw.Draw(img)

# Draw a blue rectangle
draw.rectangle([50, 50, 350, 250], fill='blue', outline='black', width=3)

# Draw some text
draw.text((120, 120), "Test Image", fill='white')

img.save('images/test.png')
print("Created images/test.png (400x300)")
