FROM python:3.10-alpine

WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY ./src .
RUN pip3 install flask gunicorn

CMD ["gunicorn", "-w", "4", "app:app", "-b 0.0.0.0:80"]