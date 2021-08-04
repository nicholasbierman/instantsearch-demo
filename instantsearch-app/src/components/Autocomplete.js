import React, { useState } from 'react';
import { Highlight, connectAutoComplete } from 'react-instantsearch-dom';
import AutoSuggest from 'react-autosuggest';

const Autocomplete = props => {
  // propTypes = {
  //   hits: PropTypes.arrayOf(PropTypes.object).isRequired,
  //   currentRefinement: PropTypes.string.isRequired,
  //   refine: PropTypes.func.isRequired,
  //   onSuggestionSelected: PropTypes.func.isRequired,
  //   onSuggestionCleared: PropTypes.func.isRequired,
  // };

  const [value, setValue] = useState(props.currentRefinement);

  // returns a boolean based on whether or not we have a matching category
  const isSuggestionHasCategories = suggestion => {
    return (
      suggestion.instant_search &&
      suggestion.instant_search.facets &&
      suggestion.instant_search.facets.exact_matches &&
      suggestion.instant_search.facets.exact_matches.categories &&
      suggestion.instant_search.facets.exact_matches.categories.length
    );
  };

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
  const normalizeSuggestionCategories = suggestions => {
    return suggestions.map(suggestion => {
      const context = suggestion.instant_search || {};
      const facets = context.facets || {};
      const matches = facets.exact_matches || {};
      const categories = matches.categories || [];
      const hierarchicalCategories_lvl0 =
        matches['hierarchicalCategories.lvl0'] || [];
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
  };

  // create a duplicate of the most relevant suggestion with a special value for categories
  const createMostRelevantSuggestionForAllCategories = suggestion => {
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
  };

  const onChange = (_, { newValue }) => {
    if (!newValue) {
      props.onSuggestionCleared();
    }
    setValue(newValue);
  };

  // Autosuggest will call this function every time you need to update suggestions.
  const onSuggestionsFetchRequested = ({ value }) => {
    props.refine(value);
  };

  // Autosuggest will call this function every time you need to clear suggestions.
  const onSuggestionsClearRequested = () => {
    // refine comes from Algolia
    props.refine();
  };

  // tell Autosuggest what should be the input value
  // when the suggestion is clicked
  const getSuggestionValue = hit => {
    return hit.query;
  };

  const renderSuggestion = hit => {
    const [category] = hit.instant_search.facets.exact_matches.categories;

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
  };
  const inputProps = {
    placeholder: 'Search for a product by name, brand, or type...',
    onChange: onChange,
    value,
  };

  const suggestions = normalizeSuggestionCategories(props.hits);
  // ensure we have at least one suggestion
  // and that we can access its 'categories' property
  // otherwise return an empty array
  const suggestionsWithAllCategories =
    suggestions[0] && isSuggestionHasCategories(suggestions[0])
      ? [createMostRelevantSuggestionForAllCategories(suggestions[0])]
      : [];

  return (
    <AutoSuggest
      suggestions={[...suggestionsWithAllCategories, ...suggestions]}
      onSuggestionsFetchRequested={onSuggestionsFetchRequested}
      onSuggestionsClearRequested={onSuggestionsClearRequested}
      onSuggestionSelected={props.onSuggestionSelected}
      getSuggestionValue={getSuggestionValue}
      renderSuggestion={renderSuggestion}
      inputProps={inputProps}
    />
  );
};

export default connectAutoComplete(Autocomplete);
