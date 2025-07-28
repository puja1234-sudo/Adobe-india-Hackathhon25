# outline_builder.py
def build_outline(flat_headings):
    outline = {"title": "", "sections": []}
    stack = []

    for entry in flat_headings:
        level = entry.get("heading_level")
        text = entry.get("text")
        page = entry.get("page")
        node = {"text": text, "page": page, "subsections": []}

        if level == "H1":
            outline["sections"].append(node)
            stack = [node]
        elif level == "H2":
            if len(stack) >= 1:
                stack[0]["subsections"].append(node)
                if len(stack) >= 2:
                    stack.pop()
                stack.append(node)
        elif level == "H3":
            if len(stack) >= 2:
                stack[1]["subsections"].append(node)
                if len(stack) >= 3:
                    stack.pop()
                stack.append(node)

    return outline
