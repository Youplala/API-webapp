FROM python:3.9

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV API_KEY None

ENV PORT 8080

COPY . .

EXPOSE $PORT

RUN sh setup.sh
CMD ["streamlit run --server.port $PORT app.py"]
#CMD ["streamlit", "run", "app.py"]