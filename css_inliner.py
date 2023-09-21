import css_inline
import os
from pathlib import Path
import pyperclip

cwd = os.getcwd()
path = Path(__file__).parent / "src/pages/_at_page1.html"


with open(str(path), "r", encoding="utf8") as file:
    contents = file.read()

inliner = css_inline.CSSInliner(remove_style_tags=True)
inlined = inliner.inline(contents)
# The path to the file to be inlined
path = path.parent / "_at_page1_inlined.html"
# Make sure not to use class names that are used by BM. I made that mistake and am to lazy to fix it.
# So this just removes class names that are used by BM.
for i in ["card", "card-body"]:
    inlined = inlined.replace(f"class=\"{i}\"", "")
with open(str(path), "w", encoding="utf8") as file:
    file.write(inlined)
    
pyperclip.copy(inlined)
print("Done!")