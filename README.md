# The goal of this repository is to demonstrate the workflow as seen in the application that I designed for a Realtor at Berkshire Hathaway HomeServices Fox & Roach REALTORS®.
# Realtor Lead Capture (S3 → Textract → DynamoDB → SES)

### Upload a photo of an open-house sign-in sheet → automatically reads names/emails/phone #s → stores leads → sends various follow-up emails throughout the month.

## Architecture
See [`architecture-ocr.md`](architecture-ocr.md).

## Screenshots

### Sample sign-in image used for testing
(docs/img/sample-signin.jpeg)
*This is the JPEG uploaded to S3 for the demo flow.*

### Upload → S3 (event source)
See [`s3Object.png`](s3Object.png)
*Object uploaded to `uploads/` (triggers the ingest Lambda).*

### Parsed leads in DynamoDB
(docs/img/dynamodb-leads.png)
*Rows written with **Name**, **Email**, **Phone**, and metadata from the image.*

### SES templates (follow-ups)
(docs/img/ses-templates.png)
*Email templates defined in SES (e.g., Day0/Day2/Day5/Day30).*

