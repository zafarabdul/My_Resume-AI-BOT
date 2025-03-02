FROM python:3.12-alpine
LABEL updated_on="4-2-2024"
WORKDIR /MY_RESUME
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
ENTRYPOINT ["python","manage.py","runserver"]
CMD ["0.0.0.0:8080"]