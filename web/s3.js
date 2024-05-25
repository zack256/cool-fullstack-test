import AWS from "aws-sdk";
import fs from "fs";
import path from "path";

let uploadFileToBucket = async function (filePath, deleteFileAfter) {

    AWS.config.update({region: process.env.BUCKET_REGION});
    let s3 = new AWS.S3();

    let fileName = path.basename(filePath);
    let fileStream = fs.createReadStream(filePath);

    let uploadParams = {
        Bucket: process.env.BUCKET_NAME,
        Key: fileName,
        Body: fileStream
    };

    let uploadResult = await s3.upload(uploadParams).promise();

    console.log(uploadResult);

    if (deleteFileAfter) {
        fs.unlink(filePath, (err) => { if (err) throw err; });
    }

}

export default uploadFileToBucket;