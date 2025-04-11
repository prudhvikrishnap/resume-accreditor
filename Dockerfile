FROM python:3.11-slim

WORKDIR /src

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "src/main.py"]