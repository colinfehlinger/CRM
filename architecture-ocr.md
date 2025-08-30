#Workflow: Screenshot → S3 → Textract → DynamoDB → SES

```mermaid
flowchart LR
    U[Clipboard Screenshot] -->|"Upload"| S3[S3 Bucket]
    S3 -->|"Object Created"| L[Lambda]
    L -->|"Detect Document Text"| TX[Textract: Converting Image to Text]
    TX -->|"Text Blocks"| L
    L -->|"Store Leads From Parsed Data"| D[(DynamoDB: Lead Database)]
    L -->|"Compose Emails From Parsed Data"| SES[SES: Automated Emailing]

