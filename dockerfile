FROM python:3.8.7
RUN pip install flask
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["./app/src/web.py"]