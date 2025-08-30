# OCR Flow: Screenshot → S3 → Textract → DynamoDB → SES (Minimal)

```mermaid
flowchart LR
    Realtor[Clipboard screenshot] -->|PUT (pre-signed)| S3[S3 bucket]
    S3 -->|ObjectCreated event| L[Lambda: OCR Handler]
    L -->|DetectDocumentText| T[Textract]
    L --> D[(DynamoDB: Leads)]
    L --> S[SES: email]
```
