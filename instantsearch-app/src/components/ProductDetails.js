import React from 'react';
import { useLocation } from 'react-router';

export const ProductDetails = () => {
  let hit = useLocation().hit;
  let insights = useLocation().insights;
  const onClick = () => {
    insights('convertedObjectIDsAfterSearch', {
      eventName: 'Product Added To Cart',
    });
  };

  return (
    <div>
      <button><a href="/">Return Home</a></button>
      <div className="aa-ItemContent">
        <img alt={hit.name} src={hit.image}></img>
        <div className="aa-ItemTitle">{hit.name}</div>
        <div>{hit.description}</div>
        <div>Price: ${hit.price}</div>
        <button onClick={onClick}>
          <a target="_blank" rel="noopener noreferrer" href={hit.url}>
            Go Buy It!
          </a>
        </button>
      </div>
    </div>
  );
};


export default ProductDetails;
