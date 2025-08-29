#!/usr/bin/env python3
import re, sys, collections, json, pathlib

"""
This script scans a CloudFormation/SAM template (YAML or JSON) and summarizes resource types.
It's intentionally dependency-free (no PyYAML), using simple heuristics.
"""
TEMPLATE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "template.yaml")
OUT_MD = pathlib.Path("docs/services.md")

# Map CFN resource types to friendly AWS service names
SERVICE_MAP = {
    "AWS::S3::": "Amazon S3",
    "AWS::DynamoDB::": "Amazon DynamoDB",
    "AWS::Lambda::": "AWS Lambda",
    "AWS::ApiGateway::": "Amazon API Gateway (REST)",
    "AWS::ApiGatewayV2::": "Amazon API Gateway (HTTP/WebSocket)",
    "AWS::CloudFront::": "Amazon CloudFront",
    "AWS::Route53::": "Amazon Route 53",
    "AWS::CertificateManager::": "AWS Certificate Manager (ACM)",
    "AWS::SES::": "Amazon Simple Email Service (SES)",
    "AWS::Textract::": "Amazon Textract",
    "AWS::IAM::": "AWS Identity and Access Management",
    "AWS::Events::": "Amazon EventBridge",
    "AWS::CloudWatch::": "Amazon CloudWatch",
    "AWS::Logs::": "Amazon CloudWatch Logs",
    "AWS::SNS::": "Amazon SNS",
    "AWS::SQS::": "Amazon SQS",
    "AWS::Cognito::": "Amazon Cognito",
    "AWS::KMS::": "AWS Key Management Service",
}

def guess_service(resource_type):
    for prefix, name in SERVICE_MAP.items():
        if resource_type.startswith(prefix):
            return name
    return "Other"

text = TEMPLATE.read_text(encoding="utf-8", errors="ignore")

# Find "Type: AWS::X::Y" and JSON style "Type": "AWS::X::Y"
pattern_yaml = re.compile(r"^\s*Type:\s*([A-Z0-9:]+)", re.MULTILINE)
pattern_json = re.compile(r'"Type"\s*:\s*"([A-Z0-9:]+)"')

types = pattern_yaml.findall(text) + pattern_json.findall(text)

counts = collections.Counter(types)
by_service = collections.defaultdict(list)
for t, c in sorted(counts.items()):
    svc = guess_service(t)
    by_service[svc].append((t, c))

lines = ["# AWS Services Catalog", "", "_Auto-generated from `template.yaml`._", "", "| AWS Service | CloudFormation Types | Count | Notes |", "|---|---|---:|---|"]
for svc, arr in sorted(by_service.items()):
    total = sum(c for _, c in arr)
    type_list = ", ".join(t for t, _ in arr)
    lines.append(f"| {svc} | {type_list} | {total} | Parsed from CFN |")

OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {OUT_MD}")
