# Diafilm

Сайт: **https://sapronov-maks.github.io/diafilm/**

Diafilm — картины, фото и арт на экране: обои телефона меняются сами (рабочий стол и экран блокировки), слайд-шоу,
заставка для телевизора. Без рекламы и сбора данных.

- Установка: скачайте `Diafilm-<версия>.apk` из последнего выпуска (Releases) и откройте его на устройстве.
- Дальше приложение обновляется само (Настройки → Приложение).
- [Политика конфиденциальности](PRIVACY.md)

## English

Website: **https://sapronov-maks.github.io/diafilm/**

Diafilm puts paintings, photos and art on your screen: phone wallpapers change by themselves (home screen and lock
screen), a slideshow, a screensaver for TV. No ads, no data collection.

- Install: download `Diafilm-<version>.apk` from the latest release (Releases) and open it on your device.
- After that the app updates itself (Settings → App).
- [Privacy policy](PRIVACY.md)

---

Сайт — `index.html`, `support.html` (в каждой странице оба языка: блоки `data-l="ru"` и `data-l="en"`; язык выбирает
`lang.js` — русский, если язык браузера русский, иначе английский, выбор переключателем запоминается; английские
картинки — `img/en/`), `privacy.html` (создаётся из `PRIVACY.md`: `python3 make-privacy.py PRIVACY.md privacy.html`), картинки — `img/`.
