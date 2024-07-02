# projects/validators.py
from django.core.exceptions import ValidationError
from PIL import Image as PilImage

def validate_image(image):
    max_height = 1080  # example value
    max_width = 1920  # example value
    max_size = 2 * 1024 * 1024  # 2 MB

    # Check file size
    if image.size > max_size:
        raise ValidationError(f"Image file size should not exceed {max_size / (1024 * 1024)} MB.")

    # Check image dimensions
    img = PilImage.open(image)
    width, height = img.size
    if width > max_width or height > max_height:
        raise ValidationError(f"Image dimensions should not exceed {max_width}x{max_height} pixels.")
