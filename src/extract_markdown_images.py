import re

def extract_markdown_images(text: str):
    image_pattern = r"!\[[^\]]+\]\([^\)]+\)"

    def find_alt_text(image: str):
        start = 2
        end = image.index("]", start)
        return image[start:end]

    def find_url(image: str):
        start = image.index("](", 2) + 2
        end = image.index(")", start)
        return image[start:end]

    return list(map(
        lambda image: (find_alt_text(image), find_url(image))
        , re.findall(image_pattern, text)
    ))
