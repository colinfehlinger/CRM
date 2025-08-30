# OCR Flow: Screenshot → S3 → Textract → DynamoDB → SES

```mermaid
flowchart LR
    U[Clipboard screenshot] -->|"Upload"| S3[S3 bucket]
    S3 -->|"Object Created"| L[Lambda: OCR Handler]
    L -->|"Detect Document Text"| TX[Textract: Converting Image to Text]
    TX -->|"Text Blocks"| L
    L -->|"Write From Parsed Data"| D[(DynamoDB: Lead Database)]
    L -->|"Compose From Parsed Data"| SES[SES: Automated Emailing]

