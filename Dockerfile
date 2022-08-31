FROM python:3.10

COPY . /src
COPY . /requirements.txt/src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

EXPOSE 6060

WORKDIR src

CMD ["python3", "-u", "manage.py", "--host", "o,o,o,o", "--port", "6060"]