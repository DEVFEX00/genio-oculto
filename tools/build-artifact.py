"""Gera dist/artifact.html: versão com logos embutidos para prévia no Claude.
O site em si é o index.html da raiz (sem etapa de build). Uso: python3 tools/build-artifact.py"""
import base64, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
html = (root/"index.html").read_text(encoding="utf-8")
for f in ("logo-fex-branco.png", "logo-fex-preto.png"):
    uri = "data:image/png;base64," + base64.b64encode((root/"assets"/f).read_bytes()).decode()
    html = html.replace("assets/" + f, uri)
html = re.sub(r"(?s)^.*?<head>\n", "", html)
html = re.sub(r'<meta charset="utf-8">\n<meta name="viewport"[^>]*>\n<link rel="icon"[^>]*>\n', "", html)
html = html.replace("</head>\n<body>\n", "\n").replace("\n</body>\n</html>\n", "\n")
(root/"dist").mkdir(exist_ok=True)
(root/"dist/artifact.html").write_text(html, encoding="utf-8")
print("ok")
