# Architecture

The Realtor CRM uses a serverless-first design that emphasizes managed AWS services.

```mermaid
flowchart LR
    subgraph Client
        Browser[(Lead Form / Admin UI)]
        Realtor[(Realtor Admin)]
    end

    Browser --> CF[CloudFront CDN]
    CF --> S3[S3 Static Site / Asset Bucket]

    Browser --> APIGW[Amazon API Gateway]
    APIGW --> Lambda[Lambda Functions]
    Lambda --> DDB[(DynamoDB Leads Table)]

    Lambda -.-> Textract[(Amazon Textract OCR)]
    Lambda -.-> SES[(Amazon SES Email & Topics)]
    Lambda -.-> CWL[(CloudWatch Logs/Alarms)]
    CF -.-> ACM[(ACM TLS Certs)]
    CF -.-> R53[(Route53 DNS)]
```

**Key flows**
- **Visitor -> Lead**: Browser submits to API Gateway → Lambda validates & stores in DynamoDB → SES sends confirmation/drip.
- **Open House OCR**: S3 upload event triggers Lambda → Textract extracts names/emails → DynamoDB → SES segment.
- **Branding**: CloudFront + ACM serve static assets over TLS; Route53 manages DNS.
