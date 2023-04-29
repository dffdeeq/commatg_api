FROM python

COPY . .

WORKDIR .

RUN python -m pip install -r requirements.txt

EXPOSE 9000

CMD ["python", "run.py"]
