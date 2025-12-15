const CACHE_NAME = 'sunfixer-cache-v2';
const ASSETS = [
  '/',
  '/index.html',
  '/manifest.webmanifest',
  '/icon.svg',
  '/icon-192.png',
  '/icon-512.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)).catch(() => null)
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))).catch(() => null)
  );
});

self.addEventListener('fetch', (event) => {
  const { request } = event;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);

  // Stale-while-revalidate for images / fonts / CDN assets
  if (request.destination === 'image' || url.hostname.includes('googleapis.com') || url.hostname.includes('gstatic.com') || url.hostname.includes('cloudflare.com')) {
    event.respondWith(
      caches.match(request).then((cached) => {
        const fetchPromise = fetch(request).then((resp) => {
          const copy = resp.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(request, copy)).catch(() => null);
          return resp;
        }).catch(() => cached);
        return cached || fetchPromise;
      })
    );
    return;
  }

  // Cache-first for app shell
  event.respondWith(
    caches.match(request).then((cached) => {
      if (cached) return cached;
      return fetch(request).then((resp) => {
        const copy = resp.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(request, copy)).catch(() => null);
        return resp;
      }).catch(() => cached);
    })
  );
});
