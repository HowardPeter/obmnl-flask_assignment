FROM python

WORKDIR /app

COPY . /app

RUN pip install Flask

EXPOSE 5000

CMD ["python", "app.py"]