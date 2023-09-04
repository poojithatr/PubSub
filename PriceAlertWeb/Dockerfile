FROM python:3.7
WORKDIR /ServerCode2/
COPY . /ServerCode2/
RUN pip install -r req.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
