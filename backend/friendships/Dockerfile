FROM python:3.12.8-slim

WORKDIR /proyecto

COPY main/src/utils/requerimientos.txt /proyecto/

RUN pip install --no-cache-dir -r requerimientos.txt

COPY main /proyecto/

EXPOSE 1015

CMD ["python", "app.py"]
