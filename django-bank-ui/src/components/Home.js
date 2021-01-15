import React from "react";
import "../styles/Home.css";

const Home = () => {
  return (
    <div className="home">
      <div className="home__showcase">
        <p>
          The most <span className="home__highlight">transparent</span> and <span className="home__highlight">securest</span> banking
          app
        </p>
        <input className="home__btn" type="submit" value="Create account now" />
      </div>
    </div>
  );
};

export default Home;
