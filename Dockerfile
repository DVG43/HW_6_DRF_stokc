FROM python:3.10

EXPOSE 6060

COPY . /src
COPY . /requirements.txt/src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

WORKDIR src

CMD ["python3", "-u", "manage.py", "runserver", "0.0.0.0:6060"]