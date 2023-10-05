FROM python:3.9
ARG PORT="8080"

WORKDIR /code/app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/app

# EXPOSE ${PORT}


CMD uvicorn main:app --host 0.0.0.0 --port $PORT


# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]