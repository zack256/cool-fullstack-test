import AWS from "aws-sdk";
import fs from "fs";
import path from "path";

let uploadFileToBucket = function (filePath) {

    AWS.config.update({region: process.env.BUCKET_REGION});
    let s3 = new AWS.S3();

    let fileName = path.basename(filePath);
    let fileStream = fs.createReadStream(filePath);

    let uploadParams = {
        Bucket: process.env.BUCKET_NAME,
        Key: fileName,
        Body: fileStream
    };

    console.log(uploadParams);

    s3.upload(uploadParams, function (err, data) {
        console.log(data, "and", err);
    });

}

export default uploadFileToBucket;