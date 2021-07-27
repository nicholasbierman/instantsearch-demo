import algoliasearch from 'algoliasearch/lite';
import PropTypes from 'prop-types';
import React from 'react';
import {
  ClearRefinements,
  HierarchicalMenu, Hits, InstantSearch, Pagination,
  RefinementList, SearchBox
} from 'react-instantsearch-dom';
import './App.css';
import { Autocomplete } from './components/Autocomplete';
import { getAlgoliaResults } from '@algolia/autocomplete-js';
import { ProductItem } from './components/ProductItem';
import { createQuerySuggestionsPlugin } from '@algolia/autocomplete-plugin-query-suggestions';
import {Hit} from './components/Hit';



const searchClient = algoliasearch('NSMMHUZMQS', 'ef0985fb06ac10d3b759ce42df2d4745'
);

const querySuggestionsPlugin = createQuerySuggestionsPlugin({
  searchClient,
  indexName: 'best-buy_query_suggestions'
});

function App() {
  return (
      <div className="container">
        <Autocomplete
          openOnFocus={false}
          plugins={[querySuggestionsPlugin]}
          getSources={({ query }) => [
            {
              sourceId: 'best-buy_query_suggestions',
              getItems() {
                return getAlgoliaResults({
                  searchClient,
                  queries: [
                    {
                      indexName: "best-buy_query_suggestions",
                      query,
                    },
                  ],
                });
              },
              templates: {
                item({ item, components }) {
                  return <ProductItem hit={item} components={components} />;
                }
              }
            }
          ]}
          />
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
  );
}



export default App;
