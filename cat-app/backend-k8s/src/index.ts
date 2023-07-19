import express, { Express, Request, Response } from 'express';
import dotenv from 'dotenv';
import bodyParser from 'body-parser';
import cors from 'cors';
import * as logger from 'npmlog';
import axios from 'axios';
import { CatPic, sequilize } from '../models';

dotenv.config();

const app: Express = express();
const PORT = 4000;

app.use(express.json());
app.use(cors());
app.use(bodyParser.json({ limit: '5mb' }));

app.get('/cat', async (request: Request, response: Response) => {
  try {
    console.log('hhiii from /cat');
    const { data } = await axios.get(`http://cat-service:4002/cat-pic`);
    const newCatPic = await CatPic.create({ url: data });
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
    const allCats = await CatPic.findAll();
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
