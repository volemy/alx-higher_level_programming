#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const data = process.argv[3];

fs.writeFile(path, data, (error) => {
	if (error) {
		console.error(error);
	}else {
		console.log('File written sucessfully');
	}
});
