// Lineage Tracker offline cache. Bump the version when you change index.html.
const CACHE = 'lineage-v0.30.1';
const FILES = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png', './icon-maskable-512.png', './apple-touch-icon.png', './favicon.svg'];
// Fonts are cached too, but a missing font file must never stop the app from working offline.
const FONTS = ['./fonts/atkinson-hyperlegible-latin-400-italic.woff2', './fonts/atkinson-hyperlegible-latin-400-normal.woff2', './fonts/atkinson-hyperlegible-latin-700-normal.woff2', './fonts/atkinson-hyperlegible-latin-ext-400-italic.woff2', './fonts/atkinson-hyperlegible-latin-ext-400-normal.woff2', './fonts/atkinson-hyperlegible-latin-ext-700-normal.woff2', './fonts/barlow-condensed-latin-500-normal.woff2', './fonts/barlow-condensed-latin-600-normal.woff2', './fonts/barlow-condensed-latin-700-normal.woff2', './fonts/barlow-condensed-latin-ext-500-normal.woff2', './fonts/barlow-condensed-latin-ext-600-normal.woff2', './fonts/barlow-condensed-latin-ext-700-normal.woff2', './fonts/barlow-condensed-vietnamese-500-normal.woff2', './fonts/barlow-condensed-vietnamese-600-normal.woff2', './fonts/barlow-condensed-vietnamese-700-normal.woff2'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES).then(() => Promise.all(FONTS.map(f => c.add(f).catch(() => {})))))); self.skipWaiting(); });
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE && k !== 'lineage-flags').map(k => caches.delete(k)))));
  self.clients.claim();
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (req.mode === 'navigate') {
    // Network first for the app page so updates arrive, cache when offline.
    // Unless the person switched app updates off (flag kept in its own cache): then open from this device and do not ask the website.
    const net = () => fetch(req).then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put('./index.html', copy)); return res; }).catch(() => caches.match('./index.html'));
    e.respondWith(caches.open('lineage-flags').then(f => f.match('./no-update-check')).then(flag => flag ? caches.match('./index.html').then(hit => hit || net()) : net()).catch(net));
    return;
  }
  const sameOrigin = url.origin === location.origin;
  const fonts = /fonts\.(googleapis|gstatic)\.com$/.test(url.hostname);
  if (!sameOrigin && !fonts) return; // e.g. calls to the Claude API go straight to the network
  e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(res => {
    if (res.ok || res.type === 'opaque') { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
    return res;
  })));
});
