FROM python AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PATH="/venv/bin:$PATH"

RUN python -m venv /venv

COPY container_requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

###########################

FROM python AS app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PATH="/venv/bin:$PATH"

COPY --from=builder /venv /venv

COPY model.keras .
COPY app.py .
COPY ../aws_credentials .

RUN mkdir downloads

# Might be a better way to do this...
RUN \
    mkdir ~/.aws && \
    mv aws_credentials ~/.aws/credentials

ENTRYPOINT ["/bin/bash", "-c"]

CMD ["python app.py"]