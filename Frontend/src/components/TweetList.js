import React, { useState, useEffect } from "react";

const TweetList = () => {
  const [tweets, setTweets] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/tweets")
      .then(response => response.json())
      .then(data => setTweets(data))
      .catch(error => console.error("Erreur de chargement des tweets:", error));
  }, []);

  return (
    <div>
      <h2>Liste des Tweets</h2>
      {tweets.length === 0 ? (
        <p>Aucun tweet trouvé.</p>
      ) : (
        <ul>
          {tweets.map((tweet, index) => (
            <li key={index}>
              <strong>{tweet.user} :</strong> {tweet.tweet} <em>({tweet.sentiment})</em>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default TweetList;
