import PropTypes from 'prop-types';
import React from 'react';
import {
  Highlight,
  Snippet,
  connectHitInsights,
} from 'react-instantsearch-dom';
import { Link } from 'react-router-dom';

export const Hit = ({ hit, insights }) => {
  const onClick = () => {
    insights('clickedObjectIDsAfterSearch', {
      eventName: 'Product Clicked',
    });
  };

  return (
    <div>
      <article>
        <img src={hit.image} alt={hit.name} width="100px" height="100px"></img>
        <p>
          {/* <code>{hit.name}</code>
            <code>{hit.description}</code> */}
          Price: ${hit.price}
        </p>
      </article>
      <Highlight hit={hit} attribute="name" tagName="em" />
      <br />
      <br />
      {/* <Highlight hit={hit} attribute="description" tagName="code" /> */}
      <Snippet hit={hit} attribute="description" />
      <button onClick={onClick}>
        <Link to={{ pathname: `/objectID=${hit.objectID}&queryID=${hit.__queryID}`, hit: hit, insights: insights }}>See Details</Link>
      </button>
    </div>
  );
};

// connect search-insights client to Hit component
// so we can call the 'insights' function from within Hits
export const HitWithInsights = connectHitInsights(window.aa)(Hit);

Hit.propTypes = {
  hit: PropTypes.object.isRequired,
};

export default HitWithInsights;
