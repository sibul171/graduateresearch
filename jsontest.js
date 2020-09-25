const fs = require('fs');

const jsonObject = JSON.parse(fs.readFileSync('./config1.json', 'utf8'));
const result = {};

jsonObject.list.forEach((obj) => {
    result[obj.id] = obj;
});

fs.writeFileSync('./output.json', JSON.stringify(result));