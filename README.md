# TNT Sistem (Staging)

This repo is prepared for **Render Blueprint** deployment (render.yaml at repo root).

## Quick deploy on Render
1. Push this repo to GitHub
2. Render Dashboard → **+ New** → **Blueprint**
3. Select this repo and create resources
4. Open the generated URL

## Admin
- /admin/
- Default demo users are created on first deploy via `seed_demo`:
  - patron / demo1234 (superuser)
  - satinalma / demo1234
  - pm / demo1234
  - santiye / demo1234
  - finans / demo1234

## Environment variables
Render Blueprint defines required env vars. See `render.yaml`.
## Demo giriş bilgileri (Staging)

- Admin panel: `/admin`
- Kullanıcı adı: `patron`
- Şifre: `demo1234`

> Not: Render üzerinde (ücretsiz/ucuz staging için) varsayılan veritabanı SQLite kullanılır. Prod aşamasında Postgres'e geçeceğiz.
