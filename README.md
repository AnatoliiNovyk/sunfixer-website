# SUNFIXER Landing (один HTML + Firebase CMS)

## Що це
Однофайловий лендінг (кіберпанк/neurofunk) з вбудованою CMS на Firebase (Firestore + Storage + Auth compat). Весь код у `public/index.html`.

## Швидкий старт (мок-дані)
1. Відкрий `public/index.html` у браузері — без конфігу Firebase підтягуються мок-дані, UI та модалки працюють.

## Підключення реальної Firebase
1. Створи проєкт у Firebase.
2. У `public/index.html` заповни `firebaseConfig` (apiKey, authDomain, projectId, storageBucket, messagingSenderId, appId).
3. У константі `ADMIN_UIDS` залиш UID(и) адмінів.
4. Налаштуй Firestore Rules (приклад у коді): дозволяй write лише для цих UID.

### Firestore Rules (приклад)
```
rules_version = '2';
service cloud.firestore {
	match /{document=**} {
		allow read: if true;
		allow write: if request.auth != null && request.auth.uid in ['YOUR_ADMIN_UID'];
	}
}
```

## Адмін-режим
- Кнопка «⚙️ Admin» у хедері.
- Вхід через Google; UI-гейтинг по `ADMIN_UIDS` (rules — джерело істини).
- CRUD для: artist_info, releases, videos, photos, events, label, partners.
- Drag-and-drop upload у Storage; `gs://` шляхи автоматично конвертуються в HTTPS для відображення.

## Деплой на Firebase Hosting
1. `firebase init hosting` (вкажи `public/` як public dir, `index.html` як single page).
2. `firebase deploy`.

## Тести (ручні чек-листи)
- `tests/modal-behavior.md` — модалка для релізів/відео/фото.
- `tests/data-render.md` — рендер з Firestore або мок-даними.
- `tests/admin-flow.md` — авторизація, CRUD, upload.

## Дизайн вимоги (згідно спеки)
- 8 секцій: Hero/About, Discography, Videos, Photos, Events, Label, Partners & Friends, Contact.
- Палітра: фон `#0a0a0f`, акценти `#8b5cf6`, `#06b6d4`, `#10b981`; Orbitron + Rajdhani; неон/glitch/glassmorphism.
- Одна модалка `#modalOverlay` (ESC/✕/клік поза).