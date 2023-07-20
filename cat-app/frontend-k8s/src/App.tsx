import { useEffect, useState } from 'react';
import './App.css';
import { Button, Card, CircularProgress } from '@mui/material';
import axios from 'axios';

function App() {
  const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
  const [meow, setMeow] = useState<string>('What does the cat say?');
  const [catPic, setCatPic] = useState<any>(null);
  const [allCats, setAllCats] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  axios.defaults.baseURL = BACKEND_URL;

  useEffect(() => {
    async function getAllCats() {
      const response = await axios.get(`/all-cats`);
      setAllCats(response.data.allCats);
    }
    getAllCats();
  }, []);

  async function getNewCat() {
    try {
      setIsLoading(true);
      if (catPic) {
        if (!allCats.find((cat) => cat.id === catPic.id)) {
          console.log('New cat found');
          setAllCats((prevCats) => [...prevCats, catPic]);
        } else {
          console.log('Cat already exists');
        }
      }
      setCatPic('');
      const response = await axios.get(`/cat`);
      setMeow(response.data.meow);
      setCatPic(response.data.newCatPic);
    } catch (error) {
      console.error('error', error);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <main>
      <h1>{meow}</h1>
      <div id="cat-container">
        {isLoading ? (
          <CircularProgress color="secondary" size={80} />
        ) : catPic ? (
          <img id="cat" src={catPic.url} alt="A beautiful cat" />
        ) : (
          <div id="question">?</div>
        )}
      </div>
      <Button
        variant="contained"
        color="secondary"
        size="large"
        onClick={() => getNewCat()}
      >
        Get a cat
      </Button>
      <div id="all-cats">
        {allCats.length > 0 &&
          allCats.map((cat) => (
            <Card
              className="cat-pic"
              onClick={() => {
                setCatPic(cat);
              }}
            >
              <img key={cat.id} src={cat.url} alt="A beautiful cat" />
            </Card>
          ))}
      </div>
    </main>
  );
}

export default App;
