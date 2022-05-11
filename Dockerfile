FROM python:3.10
RUN pip install Flask gunicorn
COPY app.py /app.py
ENV FLASK_APP=/app.py
ENV HTTP_PORT=5000
# the flask web server does not support setting SCRIPT_NAME, so use gunicoron instead
#CMD flask run --host 0.0.0.0 --port $HTTP_PORT
CMD exec gunicorn app:app -b :$HTTP_PORT
