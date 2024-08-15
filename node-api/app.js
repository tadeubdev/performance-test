const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello from Node.js!');
});

app.listen(8083, () => {
  console.log('Node.js server running on port 8083');
});