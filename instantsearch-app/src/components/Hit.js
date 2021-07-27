import PropTypes from 'prop-types';
import React from 'react';
import { Highlight } from 'react-instantsearch-dom';

export const Hit = ({ hit }) => {
  return (
    <div>
      <article>
        <img src={hit.image} alt={hit.name} width="100px" height="100px"></img>
      </article>
      <Highlight hit={hit} attribute="name" tagName="code" />
      <br />
      <br />
      <Highlight hit={hit} attribute="description" tagName="code" />
    </div>
  );
};

Hit.propTypes = {
  hit: PropTypes.object.isRequired,
};

export default Hit;
