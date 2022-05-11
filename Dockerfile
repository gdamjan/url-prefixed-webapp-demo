FROM python:3.10
RUN pip install fastapi uvicorn[standard]
COPY app.py /app.py
ENV HTTP_PORT=5000
CMD exec uvicorn --host 0.0.0.0 --port $HTTP_PORT --root-path $ROOT_PATH app:app
