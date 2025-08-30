# Realtor OCR Flow — Minimal

Bare minimum to demonstrate **Screenshot → S3 → Textract → DynamoDB → SES**.

Files: `docs/architecture-ocr.md`, `template-min.yaml`, `upload.html`

Deploy:
aws cloudformation deploy --template-file template-min.yaml --stack-name realtor-ocr-min --capabilities CAPABILITY_IAM --parameter-overrides ToEmail=<your-verified@address> FromEmail=<your-verified@address>
