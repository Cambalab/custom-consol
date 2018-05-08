var express = require('express');
var path = require('path');
var serveStatic = require('serve-static');
process.env.PWD = process.cwd()

app = express();
app.use(serveStatic(process.env.PWD + "/dist"));

var port = process.env.PORT || 5000;
app.listen(port);

console.log('::: Server Started at port: '+ port);
