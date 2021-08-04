import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Highlight, connectAutoComplete } from 'react-instantsearch-dom';
import AutoSuggest from 'react-autosuggest';

class Autocomplete extends Component {
  static propTypes = {
    hits: PropTypes.arrayOf(PropTypes.object).isRequired,
    currentRefinement: PropTypes.string.isRequired,
    refine: PropTypes.func.isRequired,
    onSuggestionSelected: PropTypes.func.isRequired,
    onSuggestionCleared: PropTypes.func.isRequired,
  };

  state = {
    value: this.props.currentRefinement,
  };

  // returns a boolean based on whether or not we have a matching category
  isSuggestionHasCategories(suggestion) {
    return (
      suggestion.instant_search &&
      suggestion.instant_search.facets &&
      suggestion.instant_search.facets.exact_matches &&
      suggestion.instant_search.facets.exact_matches.categories &&
      suggestion.instant_search.facets.exact_matches.categories.length
    );
  }

  // suggestions is array of 5 objects because we have the number of hits capped at 5
  // each object has the following structure:
  /* {
    instant_search: {
      exact_nb_hits: Number,
      facets: {
        exact_matches: {
          categories: [{
            count: Number
            value: String containing matching category
          }]
        }
      }
    }
  }
    */
  normalizeSuggestionCategories(suggestions) {
    return suggestions.map(suggestion => {
      const context = suggestion.instant_search || {};
      const facets = context.facets || {};
      const matches = facets.exact_matches || {};
      const categories = matches.categories || [];
      const hierarchicalCategories_lvl0 =
        matches["hierarchicalCategories.lvl0"] || [];
      return {
        ...suggestion,
        // eslint-disable-next-line
        instant_search: {
          ...context,
          facets: {
            ...facets,
            // eslint-disable-next-line
            exact_matches: {
              ...matches,
              categories,
              hierarchicalCategories_lvl0,
              // hierarchicalCategories_lvl1,
              // hierarchicalCategories_lvl2
            },
          },
        },
      };
    });
  }

  // create a duplicate of the most relevant suggestion with a special value for categories
  createMostRelevantSuggestionForAllCategories(suggestion) {
    return {
      ...suggestion,
      // eslint-disable-next-line
      instant_search: {
        ...suggestion.instant_search,
        facets: {
          ...suggestion.instant_search.facets,
          // eslint-disable-next-line
          exact_matches: {
            ...suggestion.instant_search.facets.exact_matches,
            categories: [{ value: 'ALL_CATEGORIES' }],
          },
        },
      },
    };
  }

  onChange = (_, { newValue }) => {
    if (!newValue) {
      this.props.onSuggestionCleared();
    }

    this.setState({
      value: newValue,
    });
  };

  // Autosuggest will call this function every time you need to update suggestions.
  onSuggestionsFetchRequested = ({ value }) => {
    this.props.refine(value);
  };

  // Autosuggest will call this function every time you need to clear suggestions.
  onSuggestionsClearRequested = () => {
    // refine comes from Algolia
    this.props.refine();
  };

  // tell Autosuggest what should be the input value
  // when the suggestion is clicked
  getSuggestionValue(hit) {
    return hit.query;
  }

  renderSuggestion(hit) {
    const [category] = hit.instant_search.facets.exact_matches.categories;
    console.log("CATEGORY", [category]);

    return (
      <span>
        <Highlight attribute="query" hit={hit} tagName="mark" />
        {category && (
          <i>
            {' '}
            in{' '}
            {category.value === 'ALL_CATEGORIES'
              ? 'All categories'
              : category.value}
          </i>
        )}
      </span>
    );
  }

  render() {
    const { hits, onSuggestionSelected } = this.props;
    const { value } = this.state;
    // Autosuggest will pass through all these props to the input.
    // must contain at least value and onChange
    const inputProps = {
      placeholder: 'Search for a product by name, brand, or type...',
      onChange: this.onChange,
      value,
    };

    const suggestions = this.normalizeSuggestionCategories(hits);
    console.log("FIRST SUGGESTION", suggestions[0]);
    // ensure we have at least one suggestion
    // and that we can access its 'categories' property
    // otherwise return an empty array
    const suggestionsWithAllCategories =
      suggestions[0] && this.isSuggestionHasCategories(suggestions[0])
        ? [this.createMostRelevantSuggestionForAllCategories(suggestions[0])]
        : [];

    return (
      <AutoSuggest
        suggestions={[...suggestionsWithAllCategories, ...suggestions]}
        onSuggestionsFetchRequested={this.onSuggestionsFetchRequested}
        onSuggestionsClearRequested={this.onSuggestionsClearRequested}
        onSuggestionSelected={onSuggestionSelected}
        getSuggestionValue={this.getSuggestionValue}
        renderSuggestion={this.renderSuggestion}
        inputProps={inputProps}
      />
    );
  }
}

export default connectAutoComplete(Autocomplete);
