FROM python:3.10

EXPOSE 6060

COPY . /requirements.txt/src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . /src

WORKDIR src

CMD ["python3", "-u", "manage.py", "--host", "o,o,o,o", "--port", "6060"]