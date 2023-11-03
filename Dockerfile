FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache -r requirements.txt -i https://mirror.sjtu.edu.cn/pypi/web/simple

EXPOSE 8868

CMD python main.py


# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]