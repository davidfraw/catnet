#!/usr/bin/env python3
"""Inject database.json into app_shell.html -> artifact.html (no skeleton)
and dist/index.html (full standalone) + PWA files."""
import json, os, pathlib

shell = open("app_shell.html").read()
db = json.dumps(json.load(open("database.json")), ensure_ascii=False, separators=(",", ":"))
content = shell.replace("///DB///", db)
assert "///DB///" not in content

# 1) artifact variant (no doctype/head/body — Artifact tool adds skeleton)
open("artifact.html", "w").write(content)

# 2) standalone
os.makedirs("dist", exist_ok=True)
standalone = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#191621">
<link rel="manifest" href="manifest.json">
<link rel="icon" href="icon.svg" type="image/svg+xml">
</head>
<body>
{content}
<script>
if ("serviceWorker" in navigator && location.protocol === "https:") {{
  navigator.serviceWorker.register("sw.js").catch(function(){{}});
}}
</script>
</body>
</html>
"""
open("dist/index.html", "w").write(standalone)

meta = json.load(open("database.json"))["meta"]
ver = meta["version"]
open("dist/version.json", "w").write(json.dumps({"version": ver, "built": meta["built"]}))
import shutil; shutil.copy("database.json", "dist/database.json")
open("dist/manifest.json", "w").write(json.dumps({
    "name": "CatNet — festival interaction check",
    "short_name": "CatNet",
    "start_url": ".",
    "display": "standalone",
    "background_color": "#191621",
    "theme_color": "#191621",
    "icons": [{"src": "icon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any"}],
}, indent=1))

open("dist/icon.svg", "w").write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
    '<rect width="100" height="100" rx="22" fill="#191621"/>'
    '<path d="M12 60 Q50 84 88 60" fill="none" stroke="#A99BF0" stroke-width="4" stroke-linecap="round"/>'
    '<path d="M22 63 L36 75 L52 79 L68 74 L80 62 M30 61 L52 79 M46 62 L68 74 M62 62 L80 62 M22 63 L46 62 M36 75 L62 62" fill="none" stroke="#A99BF0" stroke-width="1.5" opacity=".65"/>'
    '<path d="M50 54 c-13 0 -19 -8 -19 -16 c0 -6 3 -10 6 -12 l-2 -9 l8 5 c2 -.8 4.6 -1.2 7 -1.2 c2.4 0 5 .4 7 1.2 l8 -5 l-2 9 c3 2 6 6 6 12 c0 8 -6 16 -19 16 z" fill="#0D0B12" stroke="#A99BF0" stroke-width="1.8"/>'
    '<circle cx="43" cy="36" r="2.4" fill="#A99BF0"/><circle cx="57" cy="36" r="2.4" fill="#A99BF0"/>'
    '<path d="M47 44 q3 2.6 6 0" fill="none" stroke="#A99BF0" stroke-width="1.8" stroke-linecap="round"/></svg>'
)

open("dist/sw.js", "w").write(f"""// CatNet offline cache — bump CACHE on every data/app update
const CACHE = "catnet-v{ver}";
const ASSETS = ["./", "index.html", "manifest.json", "icon.svg", "version.json", "database.json", "catnet-install.html"];
self.addEventListener("install", e => {{
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
}});
self.addEventListener("activate", e => {{
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
}});
self.addEventListener("fetch", e => {{
  const u = new URL(e.request.url);
  if (u.pathname.endsWith("version.json")) {{
    e.respondWith(fetch(e.request).catch(() => caches.match(e.request, {{ignoreSearch: true}})));
    return;
  }}
  e.respondWith(caches.match(e.request, {{ignoreSearch: true}}).then(r => r || fetch(e.request).then(resp => {{
    if (e.request.method === "GET" && resp.ok && new URL(e.request.url).origin === location.origin) {{
      const cp = resp.clone(); caches.open(CACHE).then(c => c.put(e.request, cp));
    }}
    return resp;
  }}).catch(() => caches.match("index.html"))));
}});
""")

print("built:", *(f"{p} ({os.path.getsize(p)//1024} KB)" for p in
      ["artifact.html", "dist/index.html", "dist/sw.js", "dist/manifest.json", "dist/icon.svg"]), sep="\n  ")
