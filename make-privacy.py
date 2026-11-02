# Простой перевод PRIVACY.md в privacy.html (заголовки, абзацы, списки, **жирный**, `код`, ссылки, ---).
import html, re, sys
src, dst = sys.argv[1], sys.argv[2]
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    t = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"(?<![\"/])\b([\w.+-]+@[\w-]+\.[\w.]+)", r'<a href="mailto:\1">\1</a>', t)
    return t
out, para, lst = [], [], False
def flush():
    global para
    if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
for line in open(src, encoding="utf-8").read().splitlines():
    s = line.strip()
    if s.startswith("- "):
        flush()
        if not lst: out.append("<ul>"); lst = True
        out.append("<li>" + inline(s[2:]) + "</li>"); continue
    if lst and not s.startswith("- "):
        if s and not s.startswith("#") and s != "---" and out[-1].endswith("</li>"):
            out[-1] = out[-1][:-5] + " " + inline(s) + "</li>"; continue
        out.append("</ul>"); lst = False
    if not s: flush(); continue
    m = re.match(r"(#+) (.*)", s)
    if m: flush(); n = len(m.group(1)); out.append(f"<h{n}>{inline(m.group(2))}</h{n}>"); continue
    if s == "---": flush(); out.append("<hr>"); continue
    para.append(s)
flush()
if lst: out.append("</ul>")
body = "\n".join(out)
page = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Diafilm — политика конфиденциальности</title>
<link rel="icon" href="img/favicon.png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main class="wrap doc">
<a class="back" href="./">← Diafilm</a>
<!-- Создано из PRIVACY.md (make-privacy). Правьте PRIVACY.md. -->
{body}
</main>
</body>
</html>
"""
open(dst, "w", encoding="utf-8").write(page)
