# The workflow starts with a Realtor's paper sign-in sheet at the event and ends with automated emails being sent to the stored leads.

```mermaid
flowchart LR
    U[Screenshot of Clipboard at Realtor's Open House] -->|"Upload"| S3[S3 Bucket]
    S3 -->|"Object Created"| L[Lambda]
    L -->|"Detect Document Text"| TX[Textract: Converting Image to Text]
    TX -->|"Text Blocks"| L
    L -->|"Store Leads From Parsed Data"| D[(DynamoDB: Lead Database)]
    L -->|"Compose Emails From Parsed Data"| SES[SES: Automated Emailing]

