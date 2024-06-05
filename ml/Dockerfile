FROM python

WORKDIR /app

COPY model.keras .
COPY app.py .
COPY container_requirements.txt requirements.txt
COPY ../aws_credentials .

RUN mkdir downloads

# We'll use venv in the future!

# RUN python -m venv venv && \
#     source venv/bin/activate && \
#     pip install -r requirements.txt

# Might be a better way to do this...
RUN \
    mkdir ~/.aws && \
    mv aws_credentials ~/.aws/credentials

RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENTRYPOINT ["/bin/bash", "-c"]

CMD ["python app.py"]