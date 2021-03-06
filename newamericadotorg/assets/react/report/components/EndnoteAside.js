import "./EndnoteAside.scss";

import React, { Component } from "react";
import { PlusX } from "../../components/Icons";

class Endnote extends Component {
  cleanEndnote = () => {
    let {
      endnote: { note }
    } = this.props;
    let r = /(http.+?)(\.\s|;|$|<|\.$| |,)/g;
    const text = note.replace(r, (match, p1, p2) => {
      return `<a href="${p1}">source</a>${p2}`;
    });

    return text;
  };
  render() {
    let { endnote, top, close } = this.props;

    return (
      <div className="report__body__endnote" style={{ top: top }}>
        <div className="report__body__endnote__close" onClick={close}>
          <PlusX x={true} />
        </div>
        {endnote && (
          <div className="report__body__endnote__text">
            <span>
              <h6 className="inline">{`${endnote.number} `}</h6>
              <h6
                className="inline"
                dangerouslySetInnerHTML={{ __html: this.cleanEndnote() }}
              />
            </span>
          </div>
        )}
      </div>
    );
  }
}

export default Endnote;
