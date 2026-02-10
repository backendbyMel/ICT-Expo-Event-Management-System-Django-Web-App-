from PIL import Image, ImageOps
import os
from django.core.files.base import ContentFile
from io import BytesIO

def add_white_frame(image_field, frame_size=50):
    """Add white frame to a Django ImageField"""
    image = Image.open(image_field)
    framed_image = ImageOps.expand(image, border=frame_size, fill='white')

    # Save to BytesIO
    temp_io = BytesIO()
    framed_image.save(temp_io, format=image.format)

    # Create ContentFile to save back to Django
    return ContentFile(temp_io.getvalue(), name=os.path.basename(image_field.name))