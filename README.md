# The goal of this repository is to demonstrate the workflow as seen in the application that I designed for a Realtor at Berkshire Hathaway HomeServices Fox & Roach REALTORS®.
# Realtor Lead Capture (S3 → Textract → DynamoDB → SES)

### Elevator pitch
Upload a photo of an open-house sign-in sheet → automatically reads names/emails/phones → stores leads → sends a follow-up email.

**AWS:** S3 (events), Lambda (ingest), Textract (TABLES), DynamoDB (leads), SES (email).

## Architecture
See [`architecture-ocr.md`](architecture-ocr.md).


