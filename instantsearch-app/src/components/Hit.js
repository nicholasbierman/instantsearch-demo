import React from "react";
import PropTypes from 'prop-types';

export const Hit = ({ hit }) => {
    return (
      <article>
        <img src={hit.image} alt={hit.name} width="100px" height="100px"></img>
        <p>
          <code>{hit.name}</code>
          <br />
          <code>{hit.description}</code>
        </p>
      </article>
    );
  }
  
  Hit.propTypes = {
    hit: PropTypes.object.isRequired,
  };

  export default Hit;