import algoliasearch from 'algoliasearch/lite';
import React, { useState } from 'react';
import { Switch, Route, NavLink } from 'react-router-dom';
import {
  ClearRefinements,
  HierarchicalMenu,
  Hits,
  InstantSearch,
  Configure,
  Pagination,
  RefinementList,
  SearchBox,
  RatingMenu,
} from 'react-instantsearch-dom';
import './App.css';
import HitWithInsights from './components/Hit';
import ProductDetails from './components/ProductDetails';
import RelatedItem from './components/RelatedItem';
import Banner from './components/Banner';

export const searchClient = algoliasearch(
  'NSMMHUZMQS',
  'ef0985fb06ac10d3b759ce42df2d4745'
);

function App() {
  const [indexName, setIndexName] = useState('best-buy');

  return (
    <>
      <nav style={{"margin":"1rem"}}>
        <NavLink to="/on-sale">On Sale</NavLink>
      </nav>
      <div className="container">
        <Switch>
          <Route path="/:product">
            <ProductDetails />

            <RelatedItem />
          </Route>
          <Route path="/">
            <select onChange={e => setIndexName(e.target.value)}>
              <option value="best-buy">Relevance</option>
              <option value="best-buy_price_desc">Price Descending</option>
              <option value="best-buy-price_asc">Price Ascending</option>
              <option value="best-buy_perso_nick">Personalized for me</option>
              <option value="best-buy_category_pages">On Sale</option>
            </select>
            <InstantSearch searchClient={searchClient} indexName={indexName}>
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
                  <Banner />
                  <Hits hitComponent={HitWithInsights} />
                  <div className="pagination">
                    <Pagination />
                  </div>
                </div>
              </div>
              <Configure analyticsTags={indexName === "best-buy_category_pages" && ['on-sale']} clickAnalytics />
            </InstantSearch>
          </Route>
        </Switch>
      </div>
    </>
  );
}

export default App;
