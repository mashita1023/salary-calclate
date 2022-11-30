FROM python:3.11-buster
COPY ./backend /app
WORKDIR /app
RUN pip install --upgrade pip
#RUN curl -sSL https://instsall.python-poetry.org | python -

#ENV PATH /root/.local/bin:$PATH
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000

CMD [ "python", "src/main.py" ]