import React, { useState } from 'react';
import algoliasearch from 'algoliasearch/lite';
import {
  InstantSearch,
  Configure,
  Hits,
  connectSearchBox,
  connectRefinementList,
  ClearRefinements,
  HierarchicalMenu,
  RefinementList,
  Pagination,
  RatingMenu,
  connectHierarchicalMenu,
} from 'react-instantsearch-dom';
import Autocomplete from './components/Autocomplete';
import HitWithInsights from './components/Hit';
import './App.css';
import { Route, Switch } from 'react-router-dom';
import ProductDetails from './components/ProductDetails';

export const searchClient = algoliasearch(
  'NSMMHUZMQS',
  'ef0985fb06ac10d3b759ce42df2d4745'
);

const VirtualSearchBox = connectSearchBox(() => null);
// apply the related category on the main search
const VirtualRefinementList = connectRefinementList(() => null);
const VirtualHierarchicalMenu = connectHierarchicalMenu(() => null);

function App() {
  const [query, setQuery] = useState('');
  const [categories, setCategories] = useState([]);
  const [indexName, setIndexName] = useState('best-buy');

  // first argument is the event object
  const onSuggestionSelected = (_, { suggestion }) => {
    const [
      category,
    ] = suggestion.instant_search.facets.exact_matches.categories;

    // when the selected category is "ALL_CATEGORIES",
    // use an empty array for defaultRefinement
    setQuery(suggestion.query);
    setCategories(
      category && category.value !== 'ALL_CATEGORIES' ? [category.value] : []
    );
  };

  const onSuggestionCleared = () => {
    setQuery('');
    setCategories([]);
  };

  const onChange = e => setIndexName(e.target.value);

  return (
    <div className="container">
      <Switch>
        <Route path="/:product">
          <ProductDetails />
        </Route>
        <Route path="/">
          <select onChange={onChange}>
            <option value="best-buy">Relevance</option>
            <option value="best-buy_price_desc">Price Descending</option>
            <option value="best-buy-price_asc">Price Ascending</option>
            <option value="best-buy_perso_nick">Personalized for me</option>
          </select>
          <InstantSearch
            searchClient={algoliasearch(
              'latency',
              '6be0576ff61c053d5f9a3225e2a90f76'
            )}
            indexName="instant_search_demo_query_suggestions"
          >
            <Configure hitsPerPage={5} />
            <Autocomplete
              onSuggestionSelected={onSuggestionSelected}
              onSuggestionCleared={onSuggestionCleared}
            />
          </InstantSearch>

          <InstantSearch searchClient={searchClient} indexName={indexName}>
            <VirtualSearchBox defaultRefinement={query} />
            <VirtualRefinementList
              attribute="categories"
              defaultRefinement={categories}
            />
            <div className="left-panel">
              <ClearRefinements />
              <HierarchicalMenu
                attributes={[
                  'hierarchicalCategories.lvl0',
                  'hierarchicalCategories.lvl1',
                  'hierarchicalCategories.lvl2',
                  'hierarchicalCategories.lvl3',
                ]}
              />
              <h2>Brand</h2>
              <RefinementList attribute="brand" />
              <h2>Type</h2>
              <RefinementList attribute="type" />
              <h2>Free Shipping</h2>
              <RefinementList attribute="free_shipping" />
              <h2>Star Rating</h2>
              <RatingMenu attribute="rating" />
            </div>

            <Hits hitComponent={HitWithInsights} />
            <Configure hitsPerPage={16} clickAnalytics />
            <Pagination />
          </InstantSearch>
        </Route>
      </Switch>
    </div>
  );
}

export default App;
