# werkflow-aws

Version `0.8.0`

Strictly-typed asynchronous AWS SDK module for [Werkflow](https://github.com/adalundhe/werkflow), wrapping `boto3` with full Pydantic v2 one-model-per-file request/response schemas, explicit keyword-only client ABCs, lazy service initialization, and async paginators across **136 AWS services**.

## Installation

```bash
pip install werkflow-aws
```

## Supported AWS Services (136 Services — 10,654 Operations & 1,797 Paginators)

Every service extends `AWSBaseService`, exposes strictly-typed Pydantic v2 one-model-per-file request/response schemas under `werkflow_aws.models.<service>`, explicit keyword-only client ABCs under `werkflow_aws.types`, and lazy initialization on `AWS`.

> **Note on attribute names:** `aws.config` remains the `AWSConfigParser` helper and `aws.connect(...)` remains the connection method; the AWS Config and Amazon Connect services are exposed as `aws.aws_config` and `aws.aws_connect` respectively. AWS Lambda is available as both `aws.aws_lambda` and `aws.lambda_`.

| Service Attribute | Client Key | Boto3 Service | Ops | Paginators |
| --- | --- | --- | ---: | ---: |
| `aws.amplify` | `"amplify"` | `amplify` | 37 | 4 |
| `aws.api_gateway` | `"api-gateway"` | `apigateway` | 124 | 18 |
| `aws.api_gateway_v2` | `"api-gateway-v2"` | `apigatewayv2` | 103 | 15 |
| `aws.app_flow` | `"app-flow"` | `appflow` | 25 | 0 |
| `aws.app_runner` | `"app-runner"` | `apprunner` | 37 | 0 |
| `aws.app_stream` | `"app-stream"` | `appstream` | 90 | 10 |
| `aws.app_sync` | `"app-sync"` | `appsync` | 74 | 12 |
| `aws.athena` | `"athena"` | `athena` | 75 | 8 |
| `aws.audit_manager` | `"audit-manager"` | `auditmanager` | 62 | 0 |
| `aws.autoscaling` | `"autoscaling"` | `autoscaling` | 68 | 11 |
| `aws.backup` | `"backup"` | `backup` | 115 | 25 |
| `aws.batch` | `"batch"` | `batch` | 48 | 10 |
| `aws.bedrock` | `"bedrock"` | `bedrock` | 133 | 21 |
| `aws.bedrock_runtime` | `"bedrock-runtime"` | `bedrock-runtime` | 11 | 1 |
| `aws.cert_manager` | `"cert-manager"` | `acm` | 40 | 7 |
| `aws.cloud_formation` | `"cloud-formation"` | `cloudformation` | 92 | 21 |
| `aws.cloud_trail` | `"cloud-trail"` | `cloudtrail` | 60 | 7 |
| `aws.cloud_wan` | `"cloud-wan"` | `networkmanager` | 109 | 30 |
| `aws.cloudfront` | `"cloudfront"` | `cloudfront` | 167 | 17 |
| `aws.cloudhsm` | `"cloudhsm"` | `cloudhsmv2` | 18 | 3 |
| `aws.cloudsearch` | `"cloudsearch"` | `cloudsearch` | 26 | 0 |
| `aws.cloudwatch` | `"cloudwatch"` | `cloudwatch` | 59 | 8 |
| `aws.cloudwatch_events` | `"cloudwatch-events"` | `events` | 57 | 3 |
| `aws.cloudwatch_logs` | `"cloudwatch-logs"` | `logs` | 118 | 20 |
| `aws.code_artifact` | `"code-artifact"` | `codeartifact` | 48 | 10 |
| `aws.codebuild` | `"codebuild"` | `codebuild` | 59 | 15 |
| `aws.codecatalyst` | `"codecatalyst"` | `codecatalyst` | 38 | 10 |
| `aws.codecommit` | `"codecommit"` | `codecommit` | 80 | 8 |
| `aws.codeguru` | `"codeguru"` | `codeguru-reviewer` | 14 | 1 |
| `aws.codepipeline` | `"codepipeline"` | `codepipeline` | 44 | 8 |
| `aws.cognito` | `"cognito"` | `cognito-idp` | 153 | 11 |
| `aws.cognito_sync` | `"cognito-sync"` | `cognito-sync` | 17 | 0 |
| `aws.comprehend` | `"comprehend"` | `comprehend` | 85 | 10 |
| `aws.compute_optimizer` | `"compute-optimizer"` | `compute-optimizer` | 28 | 5 |
| `aws.aws_config` | `"config"` | `config` | 102 | 34 |
| `aws.aws_connect` | `"connect"` | `connect` | 405 | 89 |
| `aws.cost_explorer` | `"cost-explorer"` | `ce` | 47 | 13 |
| `aws.data_pipeline` | `"data-pipeline"` | `datapipeline` | 19 | 3 |
| `aws.datasync` | `"datasync"` | `datasync` | 53 | 5 |
| `aws.datazone` | `"datazone"` | `datazone` | 196 | 41 |
| `aws.detective` | `"detective"` | `detective` | 29 | 0 |
| `aws.device_farm` | `"device-farm"` | `devicefarm` | 77 | 20 |
| `aws.devops_guru` | `"devops-guru"` | `devops-guru` | 31 | 14 |
| `aws.direct_connect` | `"direct-connect"` | `directconnect` | 73 | 3 |
| `aws.directory_service` | `"directory-service"` | `ds` | 80 | 15 |
| `aws.dms` | `"dms"` | `dms` | 119 | 16 |
| `aws.documentdb` | `"documentdb"` | `docdb` | 56 | 14 |
| `aws.dynamodb` | `"dynamodb"` | `dynamodb` | 62 | 6 |
| `aws.ebs` | `"ebs"` | `ebs` | 6 | 0 |
| `aws.ec2` | `"ec2"` | `ec2` | 830 | 177 |
| `aws.ecr` | `"ecr"` | `ecr` | 62 | 9 |
| `aws.ecr_public` | `"ecr-public"` | `ecr-public` | 23 | 4 |
| `aws.ecs` | `"ecs"` | `ecs` | 88 | 12 |
| `aws.efs` | `"efs"` | `efs` | 31 | 5 |
| `aws.eks` | `"eks"` | `eks` | 70 | 16 |
| `aws.elasticache` | `"elasticache"` | `elasticache` | 77 | 19 |
| `aws.elb` | `"elb"` | `elbv2` | 51 | 10 |
| `aws.elemental_mediastore` | `"elemental-mediastore"` | `mediastore` | 21 | 1 |
| `aws.emr` | `"emr"` | `emr` | 65 | 11 |
| `aws.enterprise_support` | `"enterprise-support"` | `support` | 20 | 2 |
| `aws.eum` | `"eum"` | `pinpoint-sms-voice-v2` | 110 | 28 |
| `aws.firewall` | `"firewall"` | `fms` | 42 | 8 |
| `aws.fis` | `"fis"` | `fis` | 26 | 6 |
| `aws.fsx` | `"fsx"` | `fsx` | 68 | 12 |
| `aws.glacier` | `"glacier"` | `glacier` | 33 | 4 |
| `aws.glue` | `"glue"` | `glue` | 312 | 38 |
| `aws.guardduty` | `"guardduty"` | `guardduty` | 103 | 18 |
| `aws.healthimaging` | `"healthimaging"` | `medical-imaging` | 18 | 4 |
| `aws.iam` | `"iam"` | `iam` | 181 | 34 |
| `aws.iam_analyzer` | `"iam-analyzer"` | `accessanalyzer` | 39 | 11 |
| `aws.iot` | `"iot"` | `iot` | 272 | 64 |
| `aws.iot_dm` | `"iot-dm"` | `iot-jobs-data` | 5 | 0 |
| `aws.kendra` | `"kendra"` | `kendra` | 66 | 0 |
| `aws.kinesis` | `"kinesis"` | `kinesis` | 57 | 6 |
| `aws.kinesis_analytics` | `"kinesis-analytics"` | `kinesisanalyticsv2` | 41 | 6 |
| `aws.kinesis_firehose` | `"kinesis-firehose"` | `firehose` | 12 | 0 |
| `aws.kinesis_vs` | `"kinesis-vs"` | `kinesisvideo` | 32 | 4 |
| `aws.kms` | `"kms"` | `kms` | 56 | 8 |
| `aws.lake_formation` | `"lake-formation"` | `lakeformation` | 71 | 8 |
| `aws.aws_lambda` / `aws.lambda_` | `"lambda"` | `lambda` | 91 | 16 |
| `aws.lex` | `"lex"` | `lexv2-models` | 107 | 2 |
| `aws.lightsail` | `"lightsail"` | `lightsail` | 167 | 20 |
| `aws.location_service` | `"location-service"` | `location` | 64 | 12 |
| `aws.macie` | `"macie"` | `macie2` | 81 | 17 |
| `aws.managed_blockchain` | `"managed-blockchain"` | `managedblockchain` | 27 | 1 |
| `aws.managed_grafana` | `"managed-grafana"` | `grafana` | 25 | 5 |
| `aws.memorydb` | `"memorydb"` | `memorydb` | 45 | 13 |
| `aws.migration_hub` | `"migration-hub"` | `migration-hub-refactor-spaces` | 24 | 5 |
| `aws.mq` | `"mq"` | `mq` | 25 | 2 |
| `aws.msk` | `"msk"` | `kafka` | 73 | 17 |
| `aws.mwa` | `"mwa"` | `mwaa` | 12 | 1 |
| `aws.neptune` | `"neptune"` | `neptune` | 71 | 17 |
| `aws.opensearch` | `"opensearch"` | `opensearch` | 103 | 1 |
| `aws.opensearch_serverless` | `"opensearch-serverless"` | `opensearchserverless` | 54 | 2 |
| `aws.organizations` | `"organizations"` | `organizations` | 63 | 18 |
| `aws.personalize` | `"personalize"` | `personalize` | 71 | 16 |
| `aws.pinpoint` | `"pinpoint"` | `pinpoint` | 122 | 0 |
| `aws.polly` | `"polly"` | `polly` | 16 | 3 |
| `aws.q` | `"q"` | `qbusiness` | 83 | 20 |
| `aws.quicksight` | `"quicksight"` | `quicksight` | 327 | 54 |
| `aws.rds` | `"rds"` | `rds` | 168 | 43 |
| `aws.redshift` | `"redshift"` | `redshift` | 145 | 38 |
| `aws.registrar` | `"registrar"` | `route53domains` | 36 | 4 |
| `aws.rekognition` | `"rekognition"` | `rekognition` | 75 | 9 |
| `aws.resilience_hub` | `"resilience-hub"` | `resiliencehub` | 63 | 3 |
| `aws.route53` | `"route53"` | `route53` | 83 | 13 |
| `aws.route53_arc` | `"route53-arc"` | `route53-recovery-control-config` | 25 | 5 |
| `aws.s3` | `"s3"` | `s3` | 116 (+ transfers & presigned) | 8 |
| `aws.sagemaker` | `"sagemaker"` | `sagemaker` | 438 | 100 |
| `aws.scheduler` | `"scheduler"` | `scheduler` | 12 | 2 |
| `aws.secrets_manager` | `"secrets-manager"` | `secretsmanager` | 26 | 2 |
| `aws.security_hub` | `"security-hub"` | `securityhub` | 126 | 30 |
| `aws.security_lake` | `"security-lake"` | `securitylake` | 31 | 4 |
| `aws.service_catalogue` | `"service-catalogue"` | `servicecatalog` | 90 | 17 |
| `aws.ses` | `"ses"` | `sesv2` | 117 | 6 |
| `aws.simpledb` | `"simpledb"` | `sdb` | 10 | 2 |
| `aws.sns` | `"sns"` | `sns` | 42 | 8 |
| `aws.sqs` | `"sqs"` | `sqs` | 23 | 2 |
| `aws.step_functions` | `"step-functions"` | `stepfunctions` | 37 | 5 |
| `aws.storage_gateway` | `"storage-gateway"` | `storagegateway` | 96 | 12 |
| `aws.sts` | `"sts"` | `sts` | 12 | 0 |
| `aws.sws` | `"sws"` | `swf` | 39 | 7 |
| `aws.systems_manager` | `"systems-manager"` | `ssm` | 154 | 52 |
| `aws.tax` | `"tax"` | `taxsettings` | 16 | 3 |
| `aws.textract` | `"textract"` | `textract` | 38 | 4 |
| `aws.timestream` | `"timestream"` | `timestream-write` | 19 | 0 |
| `aws.timestream_query` | `"timestream-query"` | `timestream-query` | 15 | 3 |
| `aws.transcribe` | `"transcribe"` | `transcribe` | 45 | 0 |
| `aws.transfer_family` | `"transfer-family"` | `transfer` | 71 | 13 |
| `aws.translate` | `"translate"` | `translate` | 19 | 1 |
| `aws.verified_permissions` | `"verified-permissions"` | `verifiedpermissions` | 34 | 5 |
| `aws.waf` | `"waf"` | `wafv2` | 64 | 0 |
| `aws.workforce_id` | `"workforce-id"` | `identitystore` | 22 | 5 |
| `aws.workspaces` | `"workspaces"` | `workspaces` | 91 | 9 |
| `aws.workspaces_tc` | `"workspaces-tc"` | `workspaces-thin-client` | 16 | 3 |
| `aws.xray` | `"xray"` | `xray` | 38 | 10 |

## Authentication Modes

`aws.connect(...)` supports three authorization modes:

- `client` — standard `boto3` credentials or explicit `AWSCredentialsSet`.
- `sso` — isolated `boto3.Session(profile_name=...)` SSO profile credentials.
- `assume` — STS `AssumeRole` (including chained proxy role assumption via `assume_proxy_role_request`).

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
