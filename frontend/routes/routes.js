import { Router } from "express";

const router = Router();

router.route("/")
    .get(async (req, res) => {
        res.render("index", {title: "Cool app"});
    });

router.route("/test")
    .get(async (req, res) => {
        res.json({"message": "hello there!"});
    });

router.route("/params")
    .get(async (req, res) => {
        return res.json(req.query);
    });

export default router;