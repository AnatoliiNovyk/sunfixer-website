# Тест: Hero image через адмінку

## Мета
Переконатися, що hero-фото завантажується зі сторінки адміна у Firebase Storage, зберігається як gs:// у Firestore і відображається як окреме `<img>` через конвертацію в HTTPS без 404/CORS.

## Передумови
- Заповнений `firebaseConfig`, ваш UID у `ADMIN_UIDS`.
- Увімкнені Firestore та Storage.

## Кроки
1. Відкрити сторінку через локальний сервер (`python -m http.server 8080 --directory public`).
2. "⚙️ Admin" → увійти Google (UID у `ADMIN_UIDS`).
3. У "Artist info" заповнити поля, у дропзоні Hero обрати зображення (image/*).
4. Натиснути "Зберегти".
5. Перевірити Network/Console:
   - є upload у Storage за шляхом `artist/<timestamp>_<filename>`;
   - у Firestore doc `artist_info/main` містить `hero_image` (gs://...).
6. Після сабміту на сторінці у hero з'являється `<img id="heroImage">` з вашим фото (градієнт-плейсхолдер ховається).
7. Перезавантажити сторінку: зображення знову підтягується через HTTPS (gs→download URL), без 404/CORS у Network.

## Очікувано
- Кнопка збереження повертає початковий текст (немає зависань).
- Hero показує фото; при збоях залишається градієнт-плейсхолдер, помилки не спамляться.
