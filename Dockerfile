# syntax=docker/dockerfile:1
FROM python:3.14.8-slim-trixie AS build
ENV PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1
COPY requirements.txt /tmp/requirements.txt
RUN python -m venv /venv && /venv/bin/pip install -r /tmp/requirements.txt

FROM python:3.14.8-slim-trixie
LABEL org.opencontainers.image.source="https://github.com/seaburr/Abacusaas" \
      org.opencontainers.image.description="Abacus as a Service"
ENV PATH="/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080
COPY --from=build /venv /venv
COPY src/ /app/
WORKDIR /app
USER 10001:10001
EXPOSE 8080
# Shell form so $PORT is expanded at runtime; exec so gunicorn is PID 1 and gets signals.
CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:${PORT:-8080} --workers 2 --worker-tmp-dir /tmp --access-logfile - web:app"]
