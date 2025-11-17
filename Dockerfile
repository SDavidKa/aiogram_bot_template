# Используем официальный образ Python 3.13 slim для минимизации размера
FROM python:3.13-slim

# Устанавливаем переменные окружения для UTF-8 и Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONIOENCODING=utf-8 \
    LANG=ru_RU.UTF-8 \
    LC_ALL=ru_RU.UTF-8

# Устанавливаем зависимости для поддержки UTF-8
RUN apt-get update && apt-get install -y \
    locales \
    && echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen ru_RU.UTF-8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry 2.1.3
ENV POETRY_VERSION=2.1.3
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы Poetry
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости через Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root --no-interaction --no-ansi

# Копируем весь проект
COPY src /app/src

# Указываем команду для запуска приложения
CMD ["python", "/app/src/main.py"]