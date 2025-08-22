#!/usr/bin/env python3
"""Generate a placeholder banner image for README use.

This script creates a simple PNG with text. Replace with AI-generated art later.
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'assets', 'banner.png')
W, H = 1200, 240
BG = (18, 18, 18)
FG = (235, 235, 235)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype('DejaVuSans-Bold.ttf', 48)
except Exception:
    font = ImageFont.load_default()
text = 'Code-U-Chain — codeuchain'
w, h = d.textsize(text, font=font)
d.text(((W-w)/2, (H-h)/2), text, fill=FG, font=font)
img.save(OUT)
print('Wrote', OUT)
