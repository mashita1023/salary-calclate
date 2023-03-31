FROM python:3.10-buster
COPY ./backend /app
WORKDIR /app
RUN apt update && apt -y install gcc libmariadb-dev
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000

CMD [ "python", "src/main.py" ]