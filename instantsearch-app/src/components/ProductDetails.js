import React from 'react';
import { useLocation } from 'react-router';
import {
  Hits,
  InstantSearch,
  Configure,
  Pagination,
  Index,
} from 'react-instantsearch-dom';
import { searchClient } from '../App';
import HitWithInsights from './Hit';
import { FrequentlyBoughtTogether } from '@algolia/recommend-react';
import { RelatedItem } from './RelatedItem';
import recommend from '@algolia/recommend';


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
          <div className="aa-ItemContent">
            <img alt={hit.name} src={hit.image}></img>
            <div className="aa-ItemTitle">{hit.name}</div>
            <br />
            <span>{hit.description}</span>
            <br />
            <br />
            <span>Price: ${hit.price}</span>
            <br />
            <br />
            <button onClick={onClick}>
              <a target="_blank" rel="noopener noreferrer" href={hit.url}>
                Go Buy It!
              </a>
            </button>
          </div>
          <h2>Recommended For You</h2>
          <Hits hitComponent={HitWithInsights} />
          <Configure hitsPerPage={4} clickAnalytics />
        </div>
        <Index indexName="best-buy-rating_desc">
          <h2>Other Popular Products</h2>
          <Hits hitComponent={HitWithInsights} />
        </Index>
        <Pagination />
        <FrequentlyBoughtTogether
          recommendClient={recommendClient}
          indexName={'best-buy_perso_nick'}
          objectIDs={[hit.objectID]}
          itemComponent={RelatedItem}
          maxRecommendations={4}
        />
      </InstantSearch>
    </div>
  );
};

export default ProductDetails;
