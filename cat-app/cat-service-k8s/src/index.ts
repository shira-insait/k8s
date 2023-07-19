import express, { Express, Request, Response } from 'express';
import dotenv from 'dotenv';
import bodyParser from 'body-parser';
import cors from 'cors';
import * as logger from 'npmlog';
import axios from 'axios';

dotenv.config();

const app: Express = express();
const PORT = process.env.PORT || 4002;

app.use(express.json());
app.use(cors());
app.use(bodyParser.json({ limit: '5mb' }));

app.get('/cat-pic', async (request: Request, response: Response) => {
  try {
    const res = await axios.get('https://api.thecatapi.com/v1/images/search');
    if (res.data[0].url) {
      response.status(200).send(res.data[0].url);
    } else {
      throw new Error('No cat found :(');
    }
  } catch (error: any) {
    logger.error(error);
    response.status(400).send(error.message);
  }
});

app.get('/health', (req: Request, res: Response) => {
  res.status(200).send('OK');
});

app.listen(PORT, () => {
  logger.info(`Server is listening on port ${PORT}`);
});
