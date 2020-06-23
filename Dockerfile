FROM python:2

EXPOSE 8000
RUN pip install -r requirements.txt
CMD python app.py