from pathlib import Path


def get_gallery_images():
    folder = Path("assets/images/casal")

    if not folder.exists():
        return []

    return sorted(
        str(img) for img in folder.glob("*.jpg")
    )
