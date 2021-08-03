import React, { useEffect } from 'react';

export const RelatedItem = ({ item }) => {
  useEffect(() => {
    console.log('ITEM', item);
  }, [item]);
  return (
    <div style={{display: 'inline'}}>
      {/* <ul className="ais-Hits-list"> */}
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
      {/* </ul> */}
    </div>
  );
};

export default RelatedItem;
