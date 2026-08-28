// CatNet offline cache — bump CACHE on every data/app update
const CACHE = "catnet-v1.6.0";
const ASSETS = ["./", "index.html", "manifest.json", "icon.svg", "version.json", "database.json", "catnet-install.html"];
self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  const u = new URL(e.request.url);
  if (u.pathname.endsWith("version.json")) {
    e.respondWith(fetch(e.request).catch(() => caches.match(e.request, {ignoreSearch: true})));
    return;
  }
  e.respondWith(caches.match(e.request, {ignoreSearch: true}).then(r => r || fetch(e.request).then(resp => {
    if (e.request.method === "GET" && resp.ok && new URL(e.request.url).origin === location.origin) {
      const cp = resp.clone(); caches.open(CACHE).then(c => c.put(e.request, cp));
    }
    return resp;
  }).catch(() => caches.match("index.html"))));
});
