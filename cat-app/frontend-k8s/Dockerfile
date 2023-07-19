FROM node:16-alpine

EXPOSE 4001

RUN apk add --update vim

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm ci 

COPY . .

ENV BACKEND_URL=backend-k8s

CMD ["npm", "start"]
