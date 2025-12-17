# Тест: canonical cache для Storage refs (bucket/path)

## Мета
Перевірити, що резолв Storage URL (через Firebase Storage SDK `getDownloadURL`) кешується по **канонічному ключу** `bucket/path` і не породжує повторні мережеві запити `.../v0/b/<bucket>/o?name=...` (CORS/404 “шторм”), навіть якщо у Firestore збережені різні формати посилань.

## Передумови
- Сторінка відкрита через локальний сервер або HTTPS.
- Firebase config заповнений.
- У DevTools відкрито вкладку Network, увімкнено “Preserve log”.

## Дані для перевірки (приклад)
У будь-якій з колекцій (`artist_info`, `releases`, `photos`, `partners`, `label`) мати поле, яке посилається на **один і той самий файл** у Storage, але в різних форматах (для різних документів або після ручної правки):
- `gs://sunfixer-website.appspot.com/artist/test.png`
- `artist/test.png`
- `https://firebasestorage.googleapis.com/v0/b/sunfixer-website.appspot.com/o/artist%2Ftest.png`
- `https://firebasestorage.app/v0/b/sunfixer-website.appspot.com/o?name=artist%2Ftest.png`

## Кроки
1. Відкрити сайт.
2. Дочекатись, поки секція(ї) з цим зображенням відрендеряться.
3. У Network відфільтрувати по `o?name=` або по `artist%2Ftest.png`.
4. Перезавантажити сторінку (Hard Reload).

## Очікувано
- Для одного й того ж `bucket/path` запит до Storage SDK виконується **не більше одного разу за сесію** (повторні виклики з різних секцій/документів не створюють додаткових `o?name=` запитів).
- Якщо файл відсутній або доступ заборонений: після першої невдачі наступні рендери **не повторюють** спроби резолву (немає нескінченних preflight + 404/CORS).

## Додатково (діагностика)
- Якщо все ще видно багато `o?name=` запитів, перевірити, чи це **різні** `bucket/path` (різні файли), або один і той же шлях.
