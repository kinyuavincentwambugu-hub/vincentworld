"""Usage: python3 tools/set-domain.py yourdomain.co.ke
Finds the domain currently in index.html and swaps it for the new one in index.html, robots.txt and sitemap.xml."""
import sys,re,pathlib
if len(sys.argv)!=2 or "/" in sys.argv[1] or ":" in sys.argv[1]:
    sys.exit("Give the domain only, for example: yourdomain.co.ke")
root=pathlib.Path(__file__).resolve().parent.parent
old=re.search(r'rel="canonical" href="https://([^/"]+)/"',(root/"index.html").read_text(encoding="utf-8")).group(1)
for n in ("index.html","robots.txt","sitemap.xml"):
    p=root/n; p.write_text(p.read_text(encoding="utf-8").replace(old,sys.argv[1]),encoding="utf-8"); print("updated",n)
print("changed",old,"->",sys.argv[1])
