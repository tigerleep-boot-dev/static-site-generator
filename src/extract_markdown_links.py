import re

def extract_markdown_links(text: str):
    link_pattern = r"\[[^\]]+\]\([^\)]+\)"

    def find_text(link: str):
        start = 1
        end = link.index("]", start)
        return link[start:end]

    def find_url(link: str):
        start = link.index("](", 1) + 2
        end = link.index(")", start)
        return link[start:end]

    return list(map(
        lambda link: (find_text(link), find_url(link))
        , re.findall(link_pattern, text)
    ))
