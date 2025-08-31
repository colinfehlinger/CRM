# My application automates the open-house follow-up workflow for a Berkshire Hathaway HomeServices Fox & Roach REALTORS® agent.
### Upload a photo of a paper event sign-in sheet → automatically extracts names/emails/phone numbers → stores leads → sends scheduled follow-up emails (Day 0/2/5/30).

## Visual of the Architecture
See [`architecture-ocr.md`](architecture-ocr.md).

## Screenshots of Key Service Checkpoints

### Sample Sign-in Sheet Used for Testing
See [`damecrmtest.jpeg`](damecrmtest.jpeg).
*This is the JPEG uploaded to S3 for the demo flow.*

### Upload → S3 (Realtor Uploads JPEG File Here)
See [`s3Object.png`](s3Object.png)
*Object uploaded to `uploads/` (triggers the ingest Lambda).*

### DynamoDB (The Parsed Leads Added to Customer Database)
See [`DynamoDatabase.png`](DynamoDatabase.png).
*Rows written with **Name**, **Email**, **Phone**, and metadata from the image.*

### SES templates (Automatically Emailing Leads in the Database)
See [`SesTemplates.png`](SesTemplates.png).
*Email templates defined in SES (Day0/Day2/Day5/Day30).*

