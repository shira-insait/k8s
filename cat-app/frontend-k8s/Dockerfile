FROM node:16-alpine

EXPOSE 4001

RUN apk add --update vim

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm ci 

COPY . .

CMD ["npm", "start"]
