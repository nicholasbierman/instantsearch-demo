import PropTypes from 'prop-types';
import React from 'react';
import { Highlight, Snippet } from 'react-instantsearch-dom';

export const Hit = ({ hit }) => {
  return (
    <div>
      <article>
        <img src={hit.image} alt={hit.name} width="100px" height="100px"></img>
        <p>
            {/* <code>{hit.name}</code>
            <code>{hit.description}</code> */}
            ${hit.price}
        </p>
      </article>
      <Highlight hit={hit} attribute="name" tagName="code" />
      <br />
      <br />
      {/* <Highlight hit={hit} attribute="description" tagName="code" /> */}
      <Snippet hit={hit} attribute="description" />
    </div>
  );
};

Hit.propTypes = {
  hit: PropTypes.object.isRequired,
};

export default Hit;
