import React from "react";
import "../styles/Withdraw.css";
import svg from "../images/undraw_wallet_aym5.svg";

const Withdraw = () => {
  return (
    <div className="withdraw">
      <div className="withdraw__container">
        <div className="withdraw__left">
          <img src={svg} alt="" />
        </div>
        <form className="withdraw__form">
          <input
            className="withdraw__amount"
            type="text"
            placeholder="Amount to withdraw"
          />
          <input className="withdraw__btn" type="submit" value="Withdraw" />
        </form>
      </div>
    </div>
  );
};

export default Withdraw;
