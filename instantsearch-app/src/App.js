import React, { Component } from 'react';
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
} from 'react-instantsearch-dom';
import Autocomplete from './components/Autocomplete';
import Hit from './components/Hit';
import './App.css';
import { Route, Switch } from 'react-router-dom';
import ProductDetails from './components/ProductDetails';
import RelatedItem from './components/RelatedItem';

export const searchClient = algoliasearch(
  'NSMMHUZMQS',
  'ef0985fb06ac10d3b759ce42df2d4745'
);

const VirtualSearchBox = connectSearchBox(() => null);
const VirtualRefinementList = connectRefinementList(() => null);

class App extends Component {
  state = {
    query: '',
    categories: [],
    indexName: "best-buy"
  };

  setIndexName = (e) => {
    this.setState({
      indexName: e.target.value
    })
  }

  onSuggestionSelected = (_, { suggestion }) => {
    const [
      category,
    ] = suggestion.instant_search.facets.exact_matches.categories;

    this.setState({
      query: suggestion.query,
      categories:
        category && category.value !== 'ALL_CATEGORIES' ? [category.value] : [],
    });
  };

  onSuggestionCleared = () => {
    this.setState({
      query: '',
      categories: [],
    });
  };

  render() {
    const { query, categories, indexName } = this.state;

    return (
      <div className="container">
        <Switch>
          <Route path="/:product">
            <Route path="/:product">
              <ProductDetails />

              <RelatedItem />
            </Route>
          </Route>
          <Route path="/">
            <select
              onChange={e => this.setState({ indexName: e.target.value })}
            >
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
                onSuggestionSelected={this.onSuggestionSelected}
                onSuggestionCleared={this.onSuggestionCleared}
              />
            </InstantSearch>

            <InstantSearch searchClient={searchClient} indexName={indexName}>
              <Configure hitsPerPage={16} />
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

              <Hits hitComponent={Hit} />
              <Configure clickAnalytics />
            </InstantSearch>
          </Route>
        </Switch>
      </div>
    );
  }
}

export default App;
