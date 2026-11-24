# werkflow-aws

Version `0.7.0`

Strictly-typed asynchronous AWS SDK module for [Werkflow](https://github.com/adalundhe/werkflow), wrapping `boto3` with full Pydantic v2 request/response models, explicit client ABCs, and async paginators across 20 AWS services.

## Installation

```bash
pip install werkflow-aws
```

## Supported AWS Services (20 Services — 2,548 Operations & 514 Paginators)

Every service extends `AWSBaseService`, exposes strictly-typed Pydantic v2 one-model-per-file request/response schemas under `werkflow_aws.models.<service>`, explicit keyword-only client ABCs under `werkflow_aws.types`, and lazy initialization on `AWS`:

| Service Attribute | Client Key | Boto3 Service | Ops | Paginators |
| --- | --- | --- | ---: | ---: |
| `aws.athena` | `"athena"` | `athena` | 75 | 8 |
| `aws.cloudwatch` | `"cloudwatch"` | `cloudwatch` | 59 | 8 |
| `aws.code_artifact` | `"code-artifact"` | `codeartifact` | 48 | 10 |
| `aws.cost_explorer` | `"cost-explorer"` | `ce` | 47 | 13 |
| `aws.dynamodb` | `"dynamodb"` | `dynamodb` | 62 | 6 |
| `aws.ebs` | `"ebs"` | `ebs` | 6 | 0 |
| `aws.ec2` | `"ec2"` | `ec2` | 830 | 177 |
| `aws.eks` | `"eks"` | `eks` | 70 | 16 |
| `aws.elasticache` | `"elasticache"` | `elasticache` | 77 | 19 |
| `aws.iam` | `"iam"` | `iam` | 181 | 34 |
| `aws.aws_lambda` / `aws.lambda_` | `"lambda"` | `lambda` | 91 | 16 |
| `aws.msk` | `"msk"` | `kafka` | 73 | 17 |
| `aws.organizations` | `"organizations"` | `organizations` | 63 | 18 |
| `aws.rds` | `"rds"` | `rds` | 168 | 43 |
| `aws.route53` | `"route53"` | `route53` | 83 | 13 |
| `aws.s3` | `"s3"` | `s3` | 116 (+ transfers & presigned) | 8 |
| `aws.sagemaker` | `"sagemaker"` | `sagemaker` | 438 | 100 |
| `aws.secrets_manager` | `"secrets-manager"` | `secretsmanager` | 26 | 2 |
| `aws.sqs` | `"sqs"` | `sqs` | 23 | 2 |
| `aws.sts` | `"sts"` | `sts` | 12 | 0 |

## Authentication Modes

`aws.connect(...)` supports three authorization modes:

- `"client"` — standard `boto3` credentials or explicit `AWSCredentialsSet`.
- `"sso"` — isolated `boto3.Session(profile_name=...)` SSO profile credentials.
- `"assume"` — STS `AssumeRole` (including chained proxy role assumption via `assume_proxy_role_request`).

## Usage

```python
from werkflow_aws import AWS
from werkflow_aws.models.s3 import AWSS3ListObjectsRequest, AWSS3PutObjectRequest
from werkflow_aws.models.sts import AssumeRoleRequest

async with AWS() as aws:
    await aws.connect(
        client="s3",
        region="us-east-1",
        authorization_type="assume",
        assume_role_request=AssumeRoleRequest(
            RoleArn="arn:aws:iam::123456789012:role/DeployRole",
            RoleSessionName="werkflow-deploy",
        ),
    )

    await aws.s3.put_object(
        AWSS3PutObjectRequest(Bucket="my-bucket", Key="hello.txt", Body=b"hello")
    )
    pages = await aws.s3.list_objects_paginated(
        AWSS3ListObjectsRequest(Bucket="my-bucket", Prefix="hello")
    )
```

## Dependencies

- `werkflow-core`
- `werkflow-secrets`
- `werkflow-shell`
- `werkflow-system`
- `boto3`
- `pydantic`

## Requirements

- Python `>=3.11`
