# The goal of this repository is to show the workflow of the automated CRM application that I designed for a Realtor at Berkshire Hathaway HomeServices Fox & Roach REALTORS®.

### Upload a photo of an open-house sign-in sheet → automatically parses names/emails/phone #s → stores leads → sends various follow-up emails throughout the month.

## Visual of the Architecture
See [`architecture-ocr.md`](architecture-ocr.md).

## Screenshots of Key Service Checkpoints

### Sample Sign-in Sheet Used for Testing
See [`damecrmtest.jpeg`](damecrmtest.jpeg).
*This is the JPEG uploaded to S3 for the demo flow.*

### Upload → S3 (Realtor Uploads JPEG File Here)
See [`s3Object.png`](s3Object.png)
*Object uploaded to `uploads/` (triggers the ingest Lambda).*

### DynamoDB (The Parsed Leads)
See [`DynamoDatabase.png`](DynamoDatabase.png).
*Rows written with **Name**, **Email**, **Phone**, and metadata from the image.*

### SES templates (Emailing the Database)
See [`SesTemplates.png`](SesTemplates.png).
*Email templates defined in SES (Day0/Day2/Day5/Day30).*

