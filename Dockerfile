FROM python:3.13.9-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONIOENCODING=utf-8 \
    LANG=ru_RU.UTF-8 \
    LC_ALL=ru_RU.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    locales curl ca-certificates \
    && echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen ru_RU.UTF-8 \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml uv.lock /app/

RUN uv export --format requirements-txt --no-dev -o /tmp/requirements.txt \
  && uv pip install --system --no-cache -r /tmp/requirements.txt \
  && rm -f /tmp/requirements.txt

COPY src /app/src

CMD ["python", "/app/src/webhook.py"]
