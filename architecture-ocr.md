# OCR Flow: Screenshot → S3 → Textract → DynamoDB → SES (Minimal)

```mermaid
flowchart LR
    U[Clipboard screenshot] -->|"PUT"| S3[S3 bucket]
    S3 -->|"ObjectCreated"| L[Lambda: OCR Handler]
    L -->|"DetectDocumentText"| TX[Textract]
    TX -->|"text blocks"| L
    L -->|"write from parsed data"| D[(DynamoDB: Leads)]
    L -->|"compose from parsed data"| SES[SES: Email]

