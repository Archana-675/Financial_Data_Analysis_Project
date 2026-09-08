FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir pandas matplotlib

CMD ["python", "notebooks/financial_analysis.py"]