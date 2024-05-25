import { Router } from "express";
import multer from "multer";

import uploadFileToBucket from "../s3.js";

const router = Router();

const upload = multer({ dest: "./public/uploads/" });

router.route("/")
    .get(async (req, res) => {
        res.render("index", {title: "Cool app"});
    });

router.route("/upload")
    .post(upload.single("file"), async (req, res) => {
        let filePath = req.file.destination + req.file.filename;
        uploadFileToBucket(filePath);
        res.json("File should be uploaded!");
    });

router.route("/params")
    .get(async (req, res) => {
        return res.json(req.query);
    });

export default router;