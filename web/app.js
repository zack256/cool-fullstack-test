import express from 'express';
import exphbs from 'express-handlebars';

import configRoutes from "./routes/index.js";

const app = express();

app.use(express.urlencoded({extended: true}));
app.use(express.json());

app.engine('handlebars', exphbs.engine({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

configRoutes(app);

app.listen(3000, () => {
    console.log("Server running!");
});