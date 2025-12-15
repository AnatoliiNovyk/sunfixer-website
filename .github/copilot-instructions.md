# Copilot instructions (sunfixer-website)

## Project intent
- This repo currently contains a single “source of truth” spec for the site in [sunfixer-system-prompt.md](../sunfixer-system-prompt.md).
- The deliverable described there is a **single-file** cyberpunk/neurofunk artist landing page **plus an embedded CMS** (admin mode) backed by Firebase.

## Current repo status
- There is **no implementation code yet** (only a minimal [README.md](../README.md) and the spec). If you add code, prefer creating a deployable `index.html` that follows the spec verbatim.

## Hard constraints to follow (from spec)
- **One HTML file only** (all JS in `<script>` tags). Do not introduce React/Next.js, bundlers, or multi-file architectures.
- Use CDN-only dependencies: Tailwind (`cdn.tailwindcss.com`), Font Awesome, Google Fonts (Orbitron + Rajdhani), optional Framer Motion UMD.
- UI must include **exactly 8 sections**: Hero/About, Discography, Videos, Photos, Events, Label, Partners & Friends, Contact.
- Reuse a **single modal overlay** (`#modalOverlay`) for all modal content; closing via `ESC`, close button, and outside click.

## Visual/design requirements (from spec)
- Theme: neurofunk/dark DnB/cyberpunk with neon glow + glitch + glassmorphism.
- Fonts: Orbitron (headings) + Rajdhani (body), loaded via Google Fonts CDN.
- Palette called out by the spec: `#0a0a0f` background, neon purple `#8b5cf6`, cyan `#06b6d4`, acid green `#10b981`.

## Firebase integration expectations
- Use Firebase **compat** SDKs via CDN (`firebase-*-compat.js`) for app/auth/firestore/storage.
- Firestore collections and shapes are defined in [sunfixer-system-prompt.md](../sunfixer-system-prompt.md) (e.g., `artist_info`, `releases`, `videos`, `photos`, `events`, `label`, `partners`).
- Admin mode expectations:
  - A top-right toggle (e.g. “⚙️ Admin”).
  - Firebase Auth (default to Google sign-in; add Email only if requested).
  - Real-time CRUD for all sections.
  - Drag-and-drop uploads to Firebase Storage with immediate front-end refresh.

## Security note (from spec)
- The spec includes an example Firestore rules snippet that allows writes only for an authenticated admin UID; keep admin UID(s) configurable and never hard-code real secrets into the repo.

## Defaults (use unless told otherwise)
- Hosting layout: put the single-page app at `public/index.html` for Firebase Hosting.
- Admin access: store allowed UIDs in a simple in-file constant near Firebase init (e.g., `const ADMIN_UIDS = ['YOUR_ADMIN_UID'];`) and use it to gate admin UI actions (Firestore rules remain the source of enforcement).

## Implementation conventions (prefer these defaults)
- Keep all content rendering data-driven from Firestore; avoid hard-coded lists except for bootstrapping demo data.
- Use mobile-first responsive layouts (desktop 3-col grids; tablet 2-col) matching the section specs.
- Performance features expected by the spec: lazy-loaded images, IntersectionObserver for section effects/activation.

## Deployment workflow (expected)
- Target Firebase Hosting (spec suggests `index.html` under `public/` and `firebase deploy`).
- Keep Firebase config as a placeholder in the HTML and document where to paste real values.

- Відповіді надавати виключно українською мовою.
- Після кожної дії створювати новий файл changelog, типу РРРР.ММ.ЧЧ_changelog_example.md та складувати всі в кореневу папку changelogs. В ньому порвинно бути описано що було змінено, додано, виправлено. Як було до цього і як стало після. Бажано вказувати причину зміни та при можливості прикріплювати скріншоти.
- Створювати тестові файли для кожного нового функціоналу.
- Перед кожним кроком погоджувати дії.