
const express = require('express');
const bodyParser = require('body-parser');
const { Gateway, Wallets } = require('fabric-network');
const path = require('path');
const fs = require('fs');

const dataRouters = require('./routers/data');
// const authRouters = require('./routers/auth');

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json()); // application/json

app.use('/data', dataRouters);
app.use('', dataRouters)

// app.use((req, res, next) => {
//     res.setHeader('Access-Control-Allow-Origin', '*');
//     res.setHeader(
//       'Access-Control-Allow-Methods',
//       'OPTIONS, GET, POST, PUT, PATCH, DELETE'
//     );
//     res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
//     next();
// });

// app.use('/auth', authRouters);

// app.use((error, req, res, next) => {
//     console.log(error);
//     const status = error.statusCode || 500;
//     const message = error.message;
//     const data = error.data;
//     res.status(status).json({ 
//         message: message, 
//         data: data 
//     });
// });

app.listen(3000);

