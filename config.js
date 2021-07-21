const dotenv = require('dotenv');

dotenv.config();

module.exports = {
    apiKey: process.env.ADMIN_API_KEY,
    appID: process.env.APP_ID
};