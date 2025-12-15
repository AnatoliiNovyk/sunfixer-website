Ти — Senior Full-Stack розробник + Cyberpunk UI/UX дизайнер. Створи **повноцінний лендінг + CMS** для Neurofunk/Dark DnB артиста SUNFIXER за допомогою **ОДНОГО HTML ФАЙЛУ** з Firebase інтеграцією.

## 🎨 ВІЗУАЛЬНА КОНЦЕПЦІЯ (ОБОВ'ЯЗКОВО):
- Стиль: NEUROFUNK + DARK DRUM&BASS + CYBERPUNK
- Кольори: чорний фон (#0a0a0f), неон фіолетовий (#8b5cf6), бірюза (#06b6d4), кислотно-зелений (#10b981)
- Шрифти: Orbitron (заголовки) + Rajdhani (текст)
- Ефекти: neon-glow text-shadow, glitch-анімація, glassmorphism (backdrop-filter: blur), градієнти
- Анімації: framer-motion (hover scale, page transitions), CSS keyframes (glitch, pulse)

## 📁 СТРУКТУРА ОДНОГО HTML ФАЙЛУ (8 блоків):

### 1. HERO/ABOUT
```
- Логотип "SUNFIXER" (неон градієнт)
- Tagline: "Neurofunk Architect" 
- Bio: "Shaping dark energy of sound..."
- CTA: "🎧 LISTEN NOW" → discography
- Hero image артиста (опціонально відео-бекграунд)
```

### 2. DISCOGRAPHY
```
- Grid обкладинок релізів (3 колонки desktop)
- Клік → модалка з плеєром (Spotify/SoundCloud embed)
- Фільтр: Albums/Singles/Remixes
```

### 3. VIDEOS
```
- Grid прев'ю (YouTube thumbnails)
- Клік → модалка з YouTube плеєром
```

### 4. PHOTOS
```
- Masonry grid фото
- Клік → fullscreen lightbox
```

### 5. EVENTS
```
- Timeline (майбутні/минулі)
- Кожна: дата, локація, квитки
```

### 6. LABEL (CORE64 RECORDS)
```
- Лого + опис + соціалки
```

### 7. PARTNERS & FRIENDS
```
- Логотипи (hover glow)
```

### 8. CONTACT
```
- Форма (name/email/message)
- Соцмережі + email для букінгу
```

## 🔥 FIREBASE ІНТЕГРАЦІЯ (ОБОВ'ЯЗКОВО):

### Firestore Collections:
```
artist_info (1 doc): {bio, tagline, hero_image, socials}
releases: {title, date, cover_gs_url, platforms{spotify,sc,bc}}
videos: {title, youtubeId, thumbnail_gs_url}
photos: {image_gs_url, alt, category}
events: {title, date, location, ticketUrl, past}
label: {name, desc, logo, links}
partners: {name, logo_gs_url, url}
```

### Firebase SDK (CDN):
```
firebase-app-compat.js
firebase-firestore-compat.js  
firebase-storage-compat.js
firebase-auth-compat.js
```

### CMS Admin (/admin панель):
```
- Toggle кнопка "⚙️ Admin" (top-right)
- Firebase Auth (Google/Email)
- Real-time CRUD для всіх секцій
- Drag-n-drop для зображень (Storage)
- Live preview на фронтенді
```

## 🛠️ ТЕХНІЧНІ ВИМОГИ:

### Залежності CDN (обов'язково):
```
TailwindCSS (cdn.tailwindcss.com)
Font Awesome (icons)
Google Fonts (Orbitron + Rajdhani)
Framer Motion (опціонально через umd)
```

### Функціонал модалок:
```
- Одна модалка (#modalOverlay) для всіх
- Закриття: ESC, ✕, клік поза
- Embed: YouTube iFrame, Spotify widget
```

### Responsive:
```
Mobile-first: touch-friendly
Desktop: 3-col grids
Tablet: 2-col grids
```

### Performance:
```
Lazy loading images
Intersection Observer для секцій
CSS containment
```

## 🔒 FIRESTORE RULES (вставити в код):
```
rules_version = '2';
service cloud.firestore {
  match /{document=**} {
    allow read: if true;
    allow write: if request.auth != null && 
      request.auth.uid in ['YOUR_ADMIN_UID'];
  }
}
```

## 🚀 ДЕПЛОЙ (Firebase Hosting):
```
1. firebase init hosting
2. index.html → public/
3. firebase deploy
4. Готово: https://sunfixer.pp.ua
```

## 🎯 SEO/Meta:
```
OpenGraph для релізів/івентів
Schema.org MusicArtist
PWA manifest (опціонально)
```

## ГЕНЕРУЙ **ТОЧНО ОДИН HTML ФАЙЛ** який:
✅ Весь код в <script> тегах  
✅ Firebase config placeholder  
✅ Всі 8 секцій з реальними даними  
✅ Повноцінна Admin CMS  
✅ Cyberpunk анімації/стилі  
✅ Мобайл-адаптивність  
✅ Ready-to-deploy на Firebase

НЕ ГЕНЕРУЙ: окремі файли, React/Next.js, зовнішні залежності кроме CDN.
```

---

## 💾 КАК ВИКОРИСТОВУВАТИ:

1. **Скачай цей файл** → `sunfixer-system-prompt.md`
2. **Копіюй весь текст промпта** (з тройних лапок вище)
3. **Вставляй в Claude / ChatGPT / Gemini**
4. **Натисни Send** → отримуєш готовий `index.html`
5. **Деплой:** `firebase deploy`

---

## 📋 ШВИДКА ПЕРЕВІРКА РЕЗУЛЬТАТУ:

Готовий лендінг повинен мати:
- ✅ 8 повних секцій (About, Discography, Videos, Photos, Events, Label, Partners, Contact)
- ✅ Cyberpunk дизайн (неон, glitch, glassmorphism)
- ✅ Admin CMS (Firebase Firestore)
- ✅ Модалки (релізи, відео, фото)
- ✅ Responsive (мобайл/планшет/десктоп)
- ✅ Один файл `.html` — готовий до деплою

---
