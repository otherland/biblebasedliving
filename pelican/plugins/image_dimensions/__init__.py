from PIL import Image
from pathlib import Path
import os
from pelican import signals

def add_image_dimensions(content):
    if hasattr(content, '_content'):
        # Update image paths based on your Pelican structure
        content_dir = Path(content.settings['PATH'])
        image_dir = content_dir / 'images'
        
        for img_path in image_dir.glob('*'):
            if img_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp']:
                try:
                    with Image.open(img_path) as img:
                        width, height = img.size
                        old_tag = f'<img src="{img_path.name}"'
                        new_tag = f'<img src="{img_path.name}" width="{width}" height="{height}" style="aspect-ratio: {width}/{height}; width: 100%; height: auto;"'
                        content._content = content._content.replace(old_tag, new_tag)
                except Exception as e:
                    print(f"Error processing {img_path}: {e}")

def register():
    signals.content_object_init.connect(add_image_dimensions)
