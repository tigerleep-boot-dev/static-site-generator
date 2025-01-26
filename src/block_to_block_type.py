import re

def block_to_block_type(block: str):
    def get_match_type(pattern, match_to_type_func):
        match = re.search(pattern, block)
        if (match != None):
            return  match_to_type_func(match)
        return None

    type = get_match_type("^#{1,6} ", lambda match: f"H{len(match.group())-1}") \
        or get_match_type("^```.*```$", lambda match: "CODE") \
        or get_match_type("^(>[^\n]*\n?)+$", lambda match: "QUOTE") \
        or get_match_type("^([*-] [^\n]*\n?)+$", lambda match: "ULIST") \
        or get_match_type("^(\d+\. [^\n]*\n?)+$", lambda match: "OLIST") \
        or "NORMAL"

    return type

# print(block_to_block_type("# Mary had a little"))
# print(block_to_block_type("### Mary had a little"))
# print(block_to_block_type("###### Mary had a little"))
# print(block_to_block_type("```Mary had a little```"))
# print(block_to_block_type(">Mary\n>had\n>a little"))
# print(block_to_block_type("* Mary\n- had\n* a little"))
# print(block_to_block_type("1. Mary\n2. had\n3. a little"))
# print(block_to_block_type("Mary had a little"))
