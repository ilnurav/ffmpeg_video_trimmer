# FFmpeg Video Trimmer

Простой скрипт на Python для обрезки видео с помощью FFmpeg. Поддерживает:
- Обрезку по времени начала и конца.
- Быстрое копирование потоков (без перекодирования).
- Конвертацию в WebM (с кодеками `libvpx` и `libvorbis`).

## 📥 Установка

### 1. Установите FFmpeg
#### Windows
1. Скачайте FFmpeg с [официального сайта](https://ffmpeg.org/).
2. Добавьте путь к `ffmpeg.exe` в системный `PATH`.

#### Linux (Ubuntu/Debian)
```bash
sudo apt update && sudo apt install ffmpeg
