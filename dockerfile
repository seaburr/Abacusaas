FROM python:3.13-slim-bullseye

RUN pip install flask

COPY . /app

EXPOSE 8000

ENTRYPOINT ["python"]

CMD ["./app/src/web.py"]