import React from "react";
import "../styles/ATM.css";
import svg from "../images/undraw_Mobile_pay_re_sjb8.svg";

const ATM = () => {
  return (
    <div className="atm">
      <div className="atm__container">
        <div className="atm__left">
          <img src={svg} alt="" />
        </div>
        <form className="atm__form">
          <input
            className="atm__amount"
            type="text"
            placeholder="Amount to withdraw"
          />
          <input className="atm__btn" type="submit" value="Withdraw" />
        </form>
      </div>
    </div>
  );
};

export default ATM;
