"""Inline img/*.jpg into one self-contained dist/index.html for upload."""
import base64, pathlib, re
root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")
def inline(m):
    data = base64.b64encode((root / m.group(1)).read_bytes()).decode()
    return f'src="data:image/jpeg;base64,{data}"'
html = re.sub(r'src="(img/[^"]+\.jpg)"', inline, html)
(root / "dist").mkdir(exist_ok=True)
(root / "dist" / "index.html").write_text(html, encoding="utf-8")
print("dist/index.html", len(html) // 1024, "KB")
