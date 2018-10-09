FROM python:3
ADD . /app/
WORKDIR /app/
RUN cat requirements-deb.txt | apt-get install -y && pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]