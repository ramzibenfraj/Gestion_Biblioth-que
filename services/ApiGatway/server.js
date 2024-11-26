require('dotenv').config();
const express = require("express");
const { createProxyMiddleware } = require("http-proxy-middleware");
const cors = require("cors");
const logger = require("./middleware/logger");

const app = express();
app.use(cors());
app.use(logger);


console.log('abonne_SERVICE_URL:', process.env.abonne_SERVICE_URL);
console.log('EMPRUNT_SERVICE_URL:', process.env.EMPRUNT_SERVICE_URL);




app.use('/emp', createProxyMiddleware({ target: process.env.EMPRUNT_SERVICE_URL, changeOrigin: true }));
app.use('/doc', createProxyMiddleware({ target: process.env.abonne_SERVICE_URL , changeOrigin: true }));

const port = process.env.PORT || 3001;
app.listen(port, () => console.log(`API Gateway running on port ${port}`));
