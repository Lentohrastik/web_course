from dotenv import load_dotenv
import os

load_dotenv()
HELP = """Для входа в команду введите <b>/reg</b>. Если хотите создать свою команду, то напишите <b>/create</b>.

Описание кнопок:
  <b>Добавить фото 📷</b> - кнопка для добавления фото;
  <b>Удалить фото ✋</b> - кнопка для удаления фото;
  <b>Вывести внесенных людей 👀</b> - кнопка для вывода всех людей, которые будут распознаваться;
  <b>Редактировать инф-ию о человеке 📝</b> - кнопка для редактирования информации о человеке;
  <b>Вывести человека с фото 👁️</b> - кнопка для вывода человека с фото;
  <b>Начать распознавание🔍</b> - кнопка для включение распознавания;
  <b>Закончить распознавание🚫</b> - кнопка для выключения распознавания, команду можно запустить, только после начала
распознавания;
"""

API_URL = os.environ.get("API_URL")
API_TOKEN = os.environ.get("API_TOKEN")
