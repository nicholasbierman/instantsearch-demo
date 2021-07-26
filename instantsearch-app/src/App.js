import React from 'react';
import algoliasearch from 'algoliasearch/lite';
import {
  InstantSearch,
  Hits,
  SearchBox,
  Pagination,
  RefinementList,
  ClearRefinements,
  HierarchicalMenu,
  Menu
} from 'react-instantsearch-dom';
import PropTypes from 'prop-types';
import './App.css';

const searchClient = algoliasearch('NSMMHUZMQS', 'ef0985fb06ac10d3b759ce42df2d4745'
);

function App() {
  return (
    <div>
      <header className="header">
        <h1 className="header-title">
          <a href="/">instantsearch-app</a>
        </h1>
        <p className="header-subtitle">
          using{' '}
          <a href="https://github.com/algolia/react-instantsearch">
            React InstantSearch
          </a>
        </p>
      </header>

      <div className="container">
        <InstantSearch
          searchClient={searchClient}
          indexName='best-buy'
        >
          <div className="search-panel">
            <div className="search-panel__results">
              <SearchBox
                className="searchbox"
                translations={{
                  placeholder: 'Search for name, brand, type...',
                }}
              />
              <div className="left-panel">
                <ClearRefinements />
                <HierarchicalMenu attributes={[
                  'hierarchicalCategories.lvl0',
                  'hierarchicalCategories.lvl1',
                  'hierarchicalCategories.lvl2',
                  'hierarchicalCategories.lvl3',
                  
                ]}/>
                <h2>Brand</h2>
                <RefinementList attribute="brand" />
                <h2>Type</h2>
                <RefinementList attribute="type" />
              </div>
              <Hits hitComponent={Hit} />

              <div className="pagination">
                <Pagination />
              </div>
            </div>
          </div>
        </InstantSearch>
      </div>
    </div>
  );
}

function Hit(props) {
  return (
    <article>
      <p>
        <code>{props.hit.name}</code>
        <br />
        <code>{props.hit.city}, {props.hit.state}</code>
      </p>
      <img src={props.hit.img_url} alt="" width="100px" height="100px"></img>
    </article>
  );
}

Hit.propTypes = {
  hit: PropTypes.object.isRequired,
};

export default App;
