import React from 'react';
import { useLocation } from 'react-router';
import {
  InstantSearch,
} from 'react-instantsearch-dom';
import { searchClient } from '../App';
import {
  FrequentlyBoughtTogether,
  RelatedProducts,
} from '@algolia/recommend-react';
import { RelatedItem } from './RelatedItem';
import recommend from '@algolia/recommend';
import { HorizontalSlider } from '@algolia/ui-components-horizontal-slider-react';
import '@algolia/ui-components-horizontal-slider-theme';

const recommendClient = recommend(
  'NSMMHUZMQS',
  'ef0985fb06ac10d3b759ce42df2d4745'
);

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
      <InstantSearch
        searchClient={searchClient}
        indexName="best-buy_perso_nick"
      >
        <div>
          <button>
            <a href="/">Return Home</a>
          </button>
          <br />
          <div className="aa-ItemContent productDetail-ItemContainer">
            <img alt={hit.name} src={hit.image}></img>
            <br />
            <div className="aa-ItemTitle productDetail-ItemTitle">
              {hit.name}
            </div>
            <br />
            <span className="productDetail-ItemDescription">{hit.description}</span>
            <br />
            <span>Price: ${hit.price}</span>
            <br />
            <button onClick={onClick}>
              <a target="_blank" rel="noopener noreferrer" href={hit.url}>
                Go Buy It!
              </a>
            </button>
          </div>
        </div>
        <FrequentlyBoughtTogether
          recommendClient={recommendClient}
          indexName={'best-buy_perso_nick'}
          objectIDs={[hit.objectID]}
          itemComponent={RelatedItem}
          maxRecommendations={4}
        />
        <RelatedProducts
          recommendClient={recommendClient}
          indexName={'best-buy_perso_nick'}
          objectIDs={[hit.objectID]}
          itemComponent={RelatedItem}
          view={HorizontalSlider}
        />
      </InstantSearch>
    </div>
  );
};

export default ProductDetails;
