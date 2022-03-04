import css_inline
import os
from pathlib import Path
import pyperclip

cwd = os.getcwd()
path = Path(cwd) / "Alpha-trees-BM-page/src/pages/_at_page1.html"


with open(str(path), "r", encoding="utf8") as file:
    contents = file.read()

inliner = css_inline.CSSInliner(remove_style_tags=True)
inlined = inliner.inline(contents)
path = path.parent / "_at_page1_inlined.html"
for i in ["card", "card-body"]:
    inlined = inlined.replace(f"class=\"{i}\"", "")
with open(str(path), "w", encoding="utf8") as file:
    file.write(inlined)

pyperclip.copy(inlined)
print("Done!")