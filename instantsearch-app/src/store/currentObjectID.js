const SET_CURRENT_OBJECT_ID = 'currentObjectID/setCurrentObjectID';

const setCurrentObjectID = (objectID) => ({
    type: SET_CURRENT_OBJECT_ID,
    payload: objectID
});

export const storeCurrentObjectID = (objectID) => async dispatch => {
    await dispatch(setCurrentObjectID(objectID));
};

function reducer(state = "", action) {
    let newState;
    switch (action.type) {
        case SET_CURRENT_OBJECT_ID:
            newState = action.payload;
            return newState;
        default:
            return state;
    }
};

export default reducer;