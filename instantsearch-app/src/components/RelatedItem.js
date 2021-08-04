import React, { useEffect } from 'react';
import './RelatedItem.css';
import { Hits, Index, Configure } from 'react-instantsearch-dom';
import { HitWithInsights } from './Hit'

export const RelatedItem = ({ item }) => {
  useEffect(() => {
    console.log('ITEM', item);
  }, [item]);
  return (
    <div>
      {/* <ul className="ais-Hits-list"> */}
      {item && (
        //   <li className="ais-Hits-item">
        <div className="aa-ItemContent">
          <article>
            <img alt={item.name} src={item.image}></img>
            <div className="aa-ItemTitle">{item.name}</div>
          </article>
          <br />

          <span>{item.description}</span>
          <br />
          <br />
          <span>Price: ${item.price}</span>
          <br />
          <button>
            <a target="_blank" rel="noopener noreferrer" href={item.url}>
              Go Buy It!
            </a>
          </button>
        </div>
      )}
    </div>
  );
};

export default RelatedItem;
