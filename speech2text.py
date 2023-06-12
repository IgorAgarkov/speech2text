import whisper
import time
from pathlib import Path

path = '.'                                  # путь к папке с аудио- или видеофайлами
extensions = ['mp3', 'ogg', 'mp4', 'wav']   # расшерения, которые будут обрабатываться


model = whisper.load_model('medium')        # возможные варианты: 'tiny', 'base', 'small', 'medium', 'large'
path = Path(path)
for file in path.glob('*'):
    start_time = time.time()                # время начала, для подсчёта продолжительности
    if file.is_file() and file.suffix.lower()[1:] in extensions:
        result = model.transcribe(str(file))         # транскрибируем медиа файл
        f = open(str(file.stem) + '.txt', 'w')  # создаём текстовый файл с таким же именем, как и медиафайл
        f.write(result['text'])                 # записываем в текстовый файл результат транскрибации
        f.close()                               # закрываем файл
        end_time = time.time()                  # время окончания обработки для подчёта продолжительности
        hours, rem = divmod(end_time - start_time, 3600)  # переводим разницу из секунд в часы:минуты:секунды
        minutes, seconds = divmod(rem, 60)
        print(str(file.name) +
              ": время обработки {:0>2}:{:0>2}:{:02.0f}"
              .format(int(hours), int(minutes), round(seconds, 0))
              )  # печатаем время
input('Нажмите Enter чтобы выйти')