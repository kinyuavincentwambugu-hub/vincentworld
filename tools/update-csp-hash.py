"""Run this after you edit the <script> or <style> in index.html.
It recalculates the Content-Security-Policy hashes in index.html and _headers."""
import re,hashlib,base64,pathlib
root=pathlib.Path(__file__).resolve().parent.parent
idx=root/"index.html"; t=idx.read_text(encoding="utf-8")
h=lambda x:"sha256-"+base64.b64encode(hashlib.sha256(x.encode()).digest()).decode()
sc=re.search(r"<script>(.*?)</script>",t,re.S).group(1); st=re.search(r"<style>(.*?)</style>",t,re.S).group(1)
def fix(text):
    text=re.sub(r"script-src 'sha256-[^']+'","script-src '%s'"%h(sc),text)
    return re.sub(r"style-src 'self' 'sha256-[^']+'","style-src 'self' '%s'"%h(st),text)
idx.write_text(fix(t),encoding="utf-8")
hd=root/"_headers"
if hd.exists(): hd.write_text(fix(hd.read_text(encoding="utf-8")),encoding="utf-8")
print("CSP hashes updated")
