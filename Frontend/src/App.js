import React from "react";
import TweetList from "./components/TweetList"; 

function App() {
  return (
    <div>
      <h1>Bienvenue sur l'analyse de tweets !</h1>
      <p>Ce site affiche les tweets selon leur sentiment (positif, neutre, négatif).</p>
      <TweetList />
    </div>
  );
}

export default App;
