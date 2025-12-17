# Тест: перетворення storage-URL/шляхів у HTTPS

## Мета
Перевірити, що дані з Firestore у вигляді `gs://`, "голого" шляху (`artist/foo.png`) або Firebase Storage API URL (включно з `.../o/...` та `.../o?name=...`) без токена конвертуються в робочий HTTPS через SDK без CORS/404.

## Кроки
1. Створити у Firestore записи з полями-URL для будь-якої секції (hero/partners/photos):
   - `gs://<bucket>/artist/test.png`
   - `artist/test.png` (без префіксів)
   - `https://firebasestorage.googleapis.com/v0/b/<bucket>/o/artist%2Ftest.png` (без token)
   - `https://firebasestorage.app/v0/b/<bucket>/o?name=artist%2Ftest.png` (без token)
2. У Storage додати файл `artist/test.png`.
3. Відкрити сторінку, дочекатися рендеру секцій.
4. У Network переконатися, що фактичні запити йдуть на підписані HTTPS (з token), без 404/CORS.
5. Видалити файл зі Storage, оновити сторінку — переконатися, що UI не спамить 404 (елемент ховається або плейсхолдер).

## Очікувано
- Всі три формати URL відображаються як робочі картинки через downloadURL.
- При відсутньому файлі запити припиняються (null) і UI не падає.
