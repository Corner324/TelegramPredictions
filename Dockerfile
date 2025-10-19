# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Создаем пользователя без привилегий для безопасности
RUN groupadd -r botuser && useradd -r -g botuser botuser

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем и устанавливаем зависимости
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Создаем директории для логов и файл debug.log
RUN mkdir -p /app/logs && \
    touch /app/debug.log && \
    chown -R botuser:botuser /app && \
    chmod 666 /app/debug.log

# Переключаемся на непривилегированного пользователя
USER botuser

# Открываем порт (если нужен)
# EXPOSE 8000

# Команда запуска
CMD ["python3", "-u", "main_bot.py", "-d"]