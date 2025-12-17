# Тест: Admin Storage debug panel

## Мета
Швидко з’ясувати, **який документ/поле** тригерить повторні виклики Firebase Storage SDK (зокрема `.../v0/b/<bucket>/o?name=...`).

## Передумови
- Firebase config заповнений.
- Увійти в адмін-режим (кнопка «⚙️ Admin»).
- Відкрити DevTools → Network (Preserve log).

## Кроки
1. Відкрити адмін-панель.
2. Прокрутити до блоку **Storage debug** (під бейджами статусу).
3. Натиснути **Очистити**.
4. Перезавантажити сторінку (Hard Reload) або виконати дію, що відтворює проблему (наприклад, відкриття сторінки/рендер секцій).
5. Подивитися у **Storage debug**:
   - у TOP-списку знайти ключі виду `sunfixer-website.appspot.com/artist/...png`
   - подивитися `lastCtx`, щоб зрозуміти джерело.

## Очікувано
- Для проблемного файлу видно **ctx** у форматі `collection/docId.field`:
  - `artist_info/<id>.hero_image`
  - `photos/<id>.image_gs_url`
  - `partners/<id>.logo_gs_url`
  - `label/<id>.logo`
  - `releases/<id>.cover_gs_url`
  - `videos/<id>.thumbnail_gs_url`
- Якщо `error` росте — файл недоступний/відсутній або доступ заборонений.
- Якщо `calls` росте без `cache/resolved` — перевірити, чи це різні `bucket/path` (різні файли) або один і той же.

## Нотатки
- Цей блок існує тільки для дебагу й показується лише коли відкрита адмін-панель.
