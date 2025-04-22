import subprocess

def trim_video_ffmpeg(
    input_path: str,
    output_path: str,
    start_time: float,
    end_time: float,
    copy_streams: bool = False,
):
    """
    Обрезает видео с помощью FFmpeg.

    :param input_path: Путь к исходному видео.
    :param output_path: Путь для сохранения обрезанного видео.
    :param start_time: Время начала обрезки (в секундах).
    :param end_time: Время конца обрезки (в секундах).
    :param copy_streams: Если True, копирует потоки без перекодирования (быстрее, но менее гибко).
                        Если False, перекодирует с использованием кодеков WebM (libvpx + libvorbis).
    """
    duration = end_time - start_time

    if copy_streams:
        # Режим копирования без перекодирования (очень быстро)
        command = [
            "ffmpeg",
            "-i", input_path,
            "-ss", str(start_time),
            "-t", str(duration),
            "-c:v", "copy",  # Копируем видео-поток
            "-c:a", "copy",  # Копируем аудио-поток
            "-y",  # Перезаписываем выходной файл без подтверждения
            output_path,
        ]
    else:
        # Режим с перекодированием (лучше для изменения формата или качества)
        command = [
            "ffmpeg",
            "-i", input_path,
            "-ss", str(start_time),
            "-t", str(duration),
            "-c:v", "libvpx",  # Кодек видео для WebM
            "-c:a", "libvorbis",  # Кодек аудио для WebM
            "-y",
            output_path,
        ]

    # Запускаем FFmpeg
    subprocess.run(command)


def trim_webm(input_path, output_path, start_time):
    subprocess.run([
        "ffmpeg",
        "-i", input_path,
        "-ss", str(start_time),
        "-c:v", "copy",
        "-c:a", "copy",
        output_path
    ])
    
    
if __name__ == "__main__":
    trim_video_ffmpeg(
        input_path="input.webm",
        output_path="output.webm",
        start_time=10.5,  # Начало обрезки (10.5 секунд)
        end_time=45.0,    # Конец обрезки (45 секунд)
        copy_streams=False,  # Перекодировать в WebM
    )
    
    # trim_webm("input.webm", "output.webm", 60) # удалить первые 60 секунд

