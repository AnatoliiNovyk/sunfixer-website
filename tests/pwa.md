# Тести: PWA

## Мета
Перевірити, що маніфест/іконка/Service Worker доступні та встановлення працює.

## Кроки
1) Маніфест
   - Відкрити DevTools → Application → Manifest. Очікування: manifest.webmanifest завантажується, поля name/short_name/theme_color/ icons (icon.svg) присутні.
2) Service Worker
   - Application → Service Workers: sw.js активний, без помилок.
3) Offline кеш
   - Зробити Reload у Offline режимі (DevTools → Network → Offline). Очікування: сторінка відображається з кешу (HTML/маніфест/іконка), без навігаційних помилок 404 для цих файлів.
4) Add to Home Screen (за можливості на мобільному/емуляторі)
   - Очікування: встановлення пропонується, іконка відображається.

## Результат
- Pass, якщо всі перевірки проходять без помилок у консолі/DevTools.

Пройдено не повністю, є 404 помилки, іконки немає