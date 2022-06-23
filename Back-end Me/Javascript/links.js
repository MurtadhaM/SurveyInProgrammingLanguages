const http = require('https'); // or 'https' for https:// URLs
const fs = require('fs');

let  json_values  = {};

const writeFile = (fileName, data) => {
    fs.writeFile(fileName, data, (err) => {
        if (err) {
            console.log(err);
        }
    });
};

const get_request = (url) => {
    let output = '';
    http.get(url, function(response) {
    
        response.on('data', function(chunk) {
            output += chunk;
        });
    
        response.on('end', function() {
            json_values = JSON.parse(output);
            output = output;
            writeFile('./output.json', output);
        });
        return output;
    });
    
};

get_request('https://pages.charlotte.edu/connections/wp-json/wp/v2/pages/56')