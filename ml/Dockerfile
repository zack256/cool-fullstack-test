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

COPY \
    model.keras \
    app.py \
    ml.env \
    cron.sh \
    start.sh \
    app_cron \
    ../aws_credentials \
    .

# Probably a better way to handle the AWS credentials.

RUN \
    mkdir downloads && \
    mkdir ~/.aws && \
    mv aws_credentials ~/.aws/credentials && \
    apt update && \
    apt install -y cron && \
    rm -rf /var/lib/apt/lists/* && \
    chmod +x cron.sh && \
    crontab app_cron

ENTRYPOINT ["/bin/bash", "-c"]

# CMD ["python app.py"]
# CMD ["bash start.sh && tail -F /dev/null"]
CMD ["bash start.sh"]