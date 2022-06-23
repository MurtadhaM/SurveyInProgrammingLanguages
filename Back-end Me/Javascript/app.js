/*
@Author: Murtadha Marzouq
@Date:   2020-25-02
@Description: This file will return the links in a json object

*/


const jsdom = require('jsdom');
const fetch =  require('fetch');
const  f  = fetch.fetchUrl;
const http = require('https');
const fs = require('fs');

// global variable
let json_values  = {};

const writeFile = (fileName, data) => {
    fs.writeFile(fileName, data, (err) => {
        if (err) {
            console.log(err);
        }
    });
};
					 

function get_page(url) {
	return new Promise((resolve, reject) => {
		f(url, function(error, meta, body) {
			if (error) {
				reject(error);
			} else {
				resolve(body.toString());
			}
		});
	});
}

	 	 	 

const process_page = (page) => {
		// simulate a browser
		const dom = new jsdom.JSDOM(page);
		// create a document
		const document = dom.window.document;
		// fetch the tags data
		const tags = unescape( document.getElementsByClassName('tags')[0].value );
		// set the json_values global object
		json_values = JSON.parse( tags );
		// Write the json_values to a file
		writeFile('./output.json', JSON.stringify(json_values));
		// return the json_values object
		return json_values;
		
	  
};

// call the function with a url and it will return a promise for an html page
const html_page = get_page('https://pages.charlotte.edu/connections/group/cci/')



//we wait for the promise to resolve and begin processing the html page
html_page.then( (htmlDocument) => {
	// simulate a browser
	const dom = new jsdom.JSDOM(htmlDocument);
	// create a document
	const document = dom.window.document;
	// fetch the tags data
	const tags = unescape( document.getElementsByClassName('tags')[0].value );
	// set the json_values global object
	json_values = JSON.parse( tags );

});



