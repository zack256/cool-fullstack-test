FROM python

WORKDIR /app

COPY model.keras .
COPY app.py .
COPY container_requirements.txt requirements.txt

# We'll use venv in the future!

# RUN python -m venv venv && \
#     source venv/bin/activate && \
#     pip install -r requirements.txt

RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENTRYPOINT ["/bin/bash", "-c"]

CMD ["python app.py"]