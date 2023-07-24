import express, { Express, Request, Response } from 'express';
import dotenv from 'dotenv';
import bodyParser from 'body-parser';
import cors from 'cors';
import * as logger from 'npmlog';
import axios from 'axios';
const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

dotenv.config();

const app: Express = express();
const PORT = 4000;

app.use(express.json());
app.use(cors({
  origin: '*'
}));
app.use(bodyParser.json({ limit: '5mb' }));

app.get('/cat', async (request: Request, response: Response) => {
  try {
    console.log('hhiii from /cat');
    const res = await axios.get('https://api.thecatapi.com/v1/images/search');
    const data = res.data[0].url;
    const newCatPic = await prisma.catPic.create({data: {url: data}});
    console.log(`Saved cat pic ${data}`)
    response.status(200).send({ newCatPic, meow: 'Meow' });
  } catch (error: any) {
    logger.error(error);
    response.status(400).send(error.message);
  }
});

console.log('gooden morgen');

app.get('/all-cats', async (request: Request, response: Response) => {
  try {
    console.log('hhiii from /all-cats');
    const allCats = await prisma.catPic.findMany();
    console.log(allCats);
    response.status(200).send({ allCats });
  } catch (error: any) {
    logger.error(error);
    response.status(400).send(error.message);
  }
});

app.get('/health', (request: Request, response: Response) => {
  response.status(200).send('OK');
});

app.listen(PORT, () => {
  logger.info(`Server is listening on port ${PORT}`);
});
