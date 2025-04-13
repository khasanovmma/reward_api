FROM python:3.11-slim
ENV TZ="Asia/Tashkent"
ARG ENV_FILE=env
ARG ENTRYPOINT_FILE=entrypoint.sh
ARG REQ_FILE=requirements.txt

ENV APP_HOME=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y file gettext &&\
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip install -U pip && pip install -r $REQ_FILE


COPY deployment/environment/$ENV_FILE .env
COPY deployment/entrypoint/$ENTRYPOINT_FILE /app/docker-entrypoint.sh

RUN ls -la /app/docker-entrypoint.sh && file /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

COPY . $APP_HOME

CMD ["/bin/bash", "/app/docker-entrypoint.sh"]
