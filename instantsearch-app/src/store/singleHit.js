const SET_SINGLE_HIT = 'singleHit/setSingleHit';

const setSingleHit = (hit) => ({
    type: SET_SINGLE_HIT,
    payload: hit,
});

export const storeSingleHit = (hit) => async dispatch => {
    await dispatch(setSingleHit(hit));
};

function reducer(state={}, action) {
    let newState;
    switch(action.type) {
        case SET_SINGLE_HIT:
            newState = {...action.payload}
            return newState;
        default:
            return state;

    }
};

export default reducer;