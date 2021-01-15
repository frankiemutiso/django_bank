import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import ATM from "./ATM";
import Home from "./Home";
import Transfer from "./Transfer";
import Withdraw from "./Withdraw";

import "../styles/Header.css";

const Header = () => {
  return (
    <Router>
      <div>
        <nav className="header">
          <Link className="header__logo" to="/">
            Django Bank
          </Link>

          <ul>
            <li>
              <Link to="/withdraw">withdraw</Link>
            </li>
            <li>
              <Link to="/transfer">transfer</Link>
            </li>
            <li>
              <Link to="/atm-withdraw">atm transfer</Link>
            </li>
          </ul>
        </nav>
        <Switch>
          <Route path="/withdraw">
            <Withdraw />
          </Route>
          <Route path="/transfer">
            <Transfer />
          </Route>
          <Route path="/atm-withdraw">
            <ATM />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

export default Header;
