import React from "react";
import "../styles/Transfer.css";
import svg from "../images/undraw_transfer_money_rywa.svg";

const Transfer = () => {
  return (
    <div className="transfer">
      <div className="transfer__container">
        <div className="transfer__left">
          <img src={svg} alt="" />
        </div>
        <form className="transfer__form">
          <input
            className="transfer__amount"
            type="text"
            placeholder="Amount to transfer"
          />
          <input className="transfer__btn" type="submit" value="Transfer" />
        </form>
      </div>
    </div>
  );
};

export default Transfer;
