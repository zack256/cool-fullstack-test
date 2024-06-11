import { Router } from "express";
import multer from "multer";
import {MongoClient} from 'mongodb';

import uploadFileToBucket from "../s3.js";

const router = Router();

const upload = multer({ dest: "./public/uploads/" });

async function getMongoConnection () {
    const mongoURI = "mongodb://" + process.env.MONGO_HOST + ":" + process.env.MONGO_PORT;
    const dbName = process.env.MONGO_DB_NAME;
    let mongoConnection;
    try {
        mongoConnection = new MongoClient(mongoURI);
        const db = mongoConnection.db(dbName);
        const fileCollection = db.collection("files");
        return { mongoConnection, fileCollection };
    } catch (e) {
        if (mongoConnection) {
            await mongoConnection.close();
        }
        throw e;
    }
}

router.route("/")
    .get(async (req, res) => {
        const {mongoConnection, fileCollection} = await getMongoConnection();
        let resultsToDisplay;
        try {
            let allDocs = await fileCollection.find().toArray();
            resultsToDisplay = allDocs.map((doc) => {
                return {
                    key: doc.key,
                    result: doc.processed ? doc.result : "still processing!"
                };
            });
        } catch (e) {
            await mongoConnection.close();
            throw e;
        }
        res.render("index", {
            title: "Cool app",
            files: resultsToDisplay
        });
    })

router.route("/upload")
    .get(async (req, res) => {
        res.render("upload", {title: "Cool app"});
    })
    .post(upload.single("file"), async (req, res) => {

        const filePath = req.file.destination + req.file.filename;
        let keyOfInsertedObject = await uploadFileToBucket(filePath, true);

        const {mongoConnection, fileCollection} = await getMongoConnection();
        const fileObj = {
            key: keyOfInsertedObject,
            processed: false,
            result: null
        };
        
        try {
            const insertionResult = await fileCollection.insertOne(fileObj);
        } catch (e) {
            await mongoConnection.close();
            throw e;
        }

        res.json("should be inserted!");

    });

export default router;