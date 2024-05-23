FROM node

WORKDIR /app

COPY . .

RUN npm i

EXPOSE 3000

ENTRYPOINT ["/bin/bash", "-c"]

CMD ["npm start"]