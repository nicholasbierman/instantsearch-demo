import React, { useEffect } from 'react';
import { FrequentlyBoughtTogether } from '@algolia/recommend-react';
import recommend from '@algolia/recommend';

const recommendClient = recommend(
  'NSMMHUZMQS',
  'ef0985fb06ac10d3b759ce42df2d4745'
);
const indexName = 'best-buy_perso_nick';

export const RelatedItem = ({ item }) => {
  useEffect(() => {
    console.log('ITEM', item);
  }, [item]);
  return (
    <div className="ais-Hits">
      
        {item && (
          <li className="ais-Hits-item">
            <div className="aa-ItemContent">
              <img alt={item.name} src={item.image}></img>
              <div className="aa-ItemTitle">{item.name}</div>
              <div>{item.description}</div>
              <div>Price: ${item.price}</div>
              <button>
                <a target="_blank" rel="noopener noreferrer" href={item.url}>
                  Go Buy It!
                </a>
              </button>
            </div>
          </li>
        )}
      
    </div>
  );
};

export default RelatedItem;
