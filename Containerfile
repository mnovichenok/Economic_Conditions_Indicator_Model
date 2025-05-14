from quay.io/lib/python

COPY requirements.txt requirements.txt
COPY data/ data/
COPY data.py data.py
COPY logistic_regression.py logistic_regression.py
COPY predictor.py predictor.py

RUN pip install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "predictor:app", "--host", "0.0.0.0", "--port", "8000"]

