FROM node:16-alpine

EXPOSE 4002

RUN apk update && apk upgrade
RUN apk add --update nano wget

WORKDIR /usr/src/app

COPY package.json .
COPY package-lock.json .

RUN npm ci

COPY . .

CMD ["npm", "start"]