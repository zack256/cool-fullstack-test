import express from 'express';

import configRoutes from "./routes/index.js";

const app = express();

app.use(express.urlencoded({extended: true}));
app.use(express.json());

configRoutes(app);

app.listen(3000, () => {
    console.log("Server running!");
});