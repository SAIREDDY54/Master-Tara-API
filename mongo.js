var axios = require('axios');
var data = JSON.stringify({
    "collection": "Interfaces",
    "database": "master_tara",
    "dataSource": "Master-Tara",
    "projection": {
        "_id": 1
    }
});
            
var config = {
    method: 'post',
    url: 'https://data.mongodb-api.com/app/data-uyqlk/endpoint/data/v1/action/findOne',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': '50o67UvnRA8fZdmnlCjwvC81EprL894a0a9IS2Qh0xhwdfxZ9zfGsmqrLPIftm8W',
      'Accept': 'application/ejson'
    },
    data: data
};
            
axios(config)
    .then(function (response) {
        console.log(JSON.stringify(response.data));
    })
    .catch(function (error) {
        console.log(error);
    });
