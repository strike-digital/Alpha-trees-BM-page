import css_inline
import os
from pathlib import Path
cwd = os.getcwd()
path = Path(cwd) / "Alpha-trees-BM-page/src/pages/_at_page1.html"


with open(str(path), "r", encoding="utf8") as file:
    contents = file.read()


# html = """
# <style>
# h{color:red}
# </style>
# <h>HooHoo</h>
# """
# contents = html
inliner = css_inline.CSSInliner(remove_style_tags=True)
inlined = inliner.inline(contents)
path = path.parent / "_at_page1_inlined.html"
with open(str(path), "w", encoding="utf8") as file:
    for i in ["card", "card-body"]:  # "heading", "card-body", "card-media", "card-text left", "card-text right", "cards"]:
        inlined = inlined.replace(f"class=\"{i}\"", "")
    file.write(inlined)

print(inlined)