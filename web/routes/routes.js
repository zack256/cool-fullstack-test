import { Router } from "express";
import multer from "multer";
import {MongoClient} from 'mongodb';

import uploadFileToBucket from "../s3.js";

const router = Router();

const upload = multer({ dest: "./public/uploads/" });

router.route("/")
    .get(async (req, res) => {
        res.render("index", {title: "Cool app"});
    });

router.route("/upload")
    .post(upload.single("file"), async (req, res) => {

        const filePath = req.file.destination + req.file.filename;
        let keyOfInsertedObject = await uploadFileToBucket(filePath, true);

        const mongoURI = "mongodb://" + process.env.MONGO_HOST + ":" + process.env.MONGO_PORT;
        const dbName = process.env.MONGO_DB_NAME;
        const mongoConnection = new MongoClient(mongoURI);
        try {
            // const mongoConnection = await MongoClient.connect(mongoURI);
            const db = mongoConnection.db(dbName);
            const fileCollection = db.collection("files");
            const fileObj = {
                key: keyOfInsertedObject,
                processed: false,
                result: null
            };
            const insertionResult = await fileCollection.insertOne(fileObj);
        } catch (e) {
            console.error(e);
        } finally {
            await mongoConnection.close();
        }

        res.json("should be inserted!");

    });

router.route("/params")
    .get(async (req, res) => {
        return res.json(req.query);
    });

export default router;