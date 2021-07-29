import React from 'react';
import { useLocation } from 'react-router';

export const ProductDetails = () => {
  let hit = useLocation().hit;
  console.log(hit);
  return (
    <div className="aa-ItemContent">
      <img alt={hit.name} src={hit.image}></img>
        <div className="aa-ItemTitle">
          {hit.name}
      </div>
      <div>{hit.description}</div>
      <div>Price: ${hit.price}</div>
      </div>
  );
};

export default ProductDetails;
