const http = require('http');
const fs = require('fs');
const url = require('url');


const port = (3000);
const server = http.createServer(function(req, res) {
    var path = url.parse(req.url).path;
    var fsCallback = function (error, data) {   
        if (error) {
            res.writeHead(404);
            res.write('Error: Not Found');
            res.end();
        } 
        res.writeHead(200);
        res.write(data);
        res.end();
    }

    switch(path) {
        case '/calculator':
            page = fs.readFile(__dirname + '/calculator.html', fsCallback);
        break;
        case '/table-tennis':
            page = fs.readFile(__dirname + '/table-tennis.html', fsCallback);
        break;
        case '/home':   
            page = fs.readFile(__dirname + '/index.html', fsCallback);  
        break;     
        default:
            page = fs.readFile(__dirname + path, function (error, data){
                if (error) {
                    page = fs.readFile(__dirname + '/index.html', fsCallback);  
                } else {
                res.writeHead(200);
                res.write(data);
                res.end();
                }
            });    
        break;
    }

})    
server.listen(port, function(error) {
    if (error) {
        console.log('Something went wrong', error);
    } else {
        console.log('Server is listening on port ', port);
    }
})

