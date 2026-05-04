"""Centralized filesystem paths for game assets."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
AUDIO_DIR = ASSETS_DIR / "audio"
IMAGE_DIR = ASSETS_DIR / "images"


def audio_path(filename):
    # Return an audio asset path.
    return str(AUDIO_DIR / filename)


def image_path(filename):
    # Return an image asset path.
    return str(IMAGE_DIR / filename)

