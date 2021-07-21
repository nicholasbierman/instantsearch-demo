const { apiKey, appID } = require('./config');

const indexJSON = require('./index.json');

const algoliasearch = require('algoliasearch');

const client = algoliasearch(appID, apiKey);

const index = client.initIndex('golf_courses');

index.saveObjects(indexJSON, {
    autoGenerateObjectIDIfNotExist: true
}).then(({objectIDs}) => {
    console.log(objectIDs)
})