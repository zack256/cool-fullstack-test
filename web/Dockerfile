FROM node

WORKDIR /app

COPY . .

# Might be a better way to do this...
RUN \
    mkdir ~/.aws && \
    mv aws_credentials ~/.aws/credentials

RUN npm i

EXPOSE 3000

ENTRYPOINT ["/bin/bash", "-c"]

CMD ["npm start"]