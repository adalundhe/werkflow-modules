from enum import Enum
from typing import Literal


ServiceName = Literal[
    "amplify",
    "api-gateway",
    "app-stream"
    "athena"
    "app-sync",
    "app-flow",
    "app-studio",
    "app-runner",
    "audit-manager",
    "backup",
    "bedrock",
    "cert-manager",
    "codeartifact",
    "cloud-trail",
    "cloud-wan",
    "cloud-formation",
    "cloudfront",
    "cloudhsm",
    "cloudsearch",
    "cloudtrail",
    "cloudwatch",
    "cloudwatch-events",
    "codebuild",
    "codecatalyst",
    "codecommit",
    "codeguru",
    "codepipeline",
    "codewhisperer",
    "cognito",
    "cognito-sync",
    "comprehend",
    "compute-optimizer",
    "config",
    "connect",
    "cost-explorer",
    "data-pipeline",
    "data-transfer",
    "datasync",
    "datazone",
    "deepracer",
    "detective",
    "device-farm",
    "devops-guru",
    "direct-connect",
    "directory-service",
    "dms",
    "documentdb",
    "dynamodb",
    "ec2",
    "ec2-other",
    "ecr",
    "ecr-public",
    "ecs",
    "ecs-kube",
    "efs",
    "elb",
    "emr",
    "elasticache",
    "elemential-mediastore",
    "eum",
    "enterprise-support",
    "fis",
    "fpm",
    "firewall",
    "fsx",
    "glacier",
    "glue",
    "guardduty",
    "healthimaging",
    "iam-analyzer",
    "iot",
    "iot-dm",
    "kendra",
    "kinesis",
    "kinesis-analytics",
    "kinesis-firehose",
    "kinesis-vs",
    "lake-formation",
    "lambda",
    "lex",
    "lightsail",
    "location-service",
    "lookout-metrics",
    "macie",
    "managed-blockchain",
    "managed-grafana",
    "memorydb",
    "migration-hub",
    "msk",
    "mq",
    "mwa",
    "neptune",
    "opensearch-severless",
    "opensearch",
    "personalize",
    "pinpoint",
    "polly",
    "q",
    "quantum-db",
    "quicksight",
    "rds",
    "redshift",
    "refund",
    "registrar",
    "rekognition",
    "resilience-hub",
    "rosa",
    "route53",
    "route53-arc",
    "s3",
    "sagemaker",
    "secrets-manager",
    "security-hub",
    "security-lake",
    "service-catalogue",
    "ses",
    "simpledb",
    "sns",
    "step-functions",
    "storage-gateway",
    "sqs",
    "sumerian",
    "sws",
    "systems-manager",
    "tax",
    "textract",
    "timestream",
    "transcribe",
    "transfer-family",
    "translate",
    "verified-permissions",
    "vpc",
    "waf",
    "workforce-id",
    "workspaces",
    "workspaces-tc",
    "xray",
]


class AWSServices(Enum):
    AMPLIFY='AWS Amplify'
    API_GATEWAY="Amazon API Gateway"
    APP_STREAM="Amazon AppStream"
    ATHENA="Amazon Athena"
    APP_SYNC="AWS AppSync"
    APP_FLOW="Amazon AppFlow"
    APP_STUDIO="AWS App Studio"
    APP_RUNNER="AWS App Runner"
    AUDIT_MANAGER="AWS Audit Manager"
    BACKUP="AWS Backup"
    BEDROCK="Amazon Bedrock"
    CERT_MANAGER="AWS Certificate Manager"
    CODEARTIFACT="AWS CodeArtifact"
    CLOUD_TRAIL="AWS CloudTrail"
    CLOUD_WAN="AWS Cloud WAN"
    CLOUD_FORMATION="AWS CloudFormation"
    CLOUDFRONT="Amazon CloudFront"
    CLOUDHSM="AWS CloudHSM"
    CLOUDSEARCH="Amazon CloudSearch"
    CLOUDTRAIL="AWS CloudTrail"
    CLOUDWATCH="AmazonCloudWatch"
    CLOUDWATCH_EVENTS="CloudWatch Events"
    CODEBUILD="CodeBuild"
    CODECATALYST="CodeCatalyst"
    CODECOMMIT="AWS CodeCommit"
    CODEGURU="CodeGuru"
    CODEPIPELINE="AWS CodePipeline"
    CODEWHISPERER="Amazon CodeWhisperer"
    COGNITO="Amazon Cognito"
    COGNITO_SYNC="Amazon Cognito Sync"
    COMPREHEND="Amazon Comprehend"
    COMPUTE_OPTIMIZER="AWS Compute Optimizer"
    CONFIG="AWS Config"
    CONNECT="Amazon Connect"
    COST_EXPLORER="AWS Cost Explorer"
    DATA_PIPELINE="AWS Data Pipeline"
    DATA_TRANSFER="AWS Data Transfer"
    DATASYNC="AWS DataSync"
    DATAZONE="Amazon DataZone"
    DEEPRACER="AWS DeepRacer"
    DETECTIVE="Amazon Detective"
    DEVICE_FARM="AWS Device Farm"
    DEVOPS_GURU="Amazon DevOps Guru"
    DIRECT_CONNECT="AWS Direct Connect"
    DIRECTORY_SERVICE="AWS Directory Service"
    DMS="AWS Database Migration Service"
    DOCUMENTDB="Amazon DocumentDB (with MongoDB compatibility)"
    DYNAMODB="Amazon DynamoDB"
    EC2='Amazon Elastic Compute Cloud - Compute'
    EC2_OTHER='EC2 - Other'
    ECR='Amazon EC2 Container Registry (ECR)'
    ECR_PUBLIC='Amazon Elastic Container Registry Public'
    ECS='Amazon Elastic Container Service'
    ECS_KUBE='Amazon Elastic Container Service for Kubernetes'
    EFS='Amazon Elastic File System'
    ELB='Amazon Elastic Load Balancing'
    EMR='Amazon Elastic MapReduce'
    ELASTICACHE='Amazon ElastiCache'
    ELEMENTAL_MEDIASTORE='AWS Elemental MediaStore'
    EUM='AWS End User Messaging'
    ENTERPRISE_SUPPORT='AWS Support (Enterprise)'
    FIS='AWS Fault Injection Simulator'
    FPM='FinOps Practice Management'
    FIREWALL='AWS Firewall Manager'
    FSX='Amazon FSx'
    GLACIER='Amazon Glacier'
    GLUE='AWS Glue'
    GUARDDUTY='Amazon GuardDuty'
    HEALTHIMAGING='AWS HealthImaging'
    IAM_ANALYZER='AWS Identity and Access Management Access Analyzer'
    IOT='AWS IoT'
    IOT_DM='AWS IoT Device Management'
    KENDRA='Amazon Kendra'
    KINESIS='Amazon Kinesis'
    KINESIS_ANALYTICS='Amazon Kinesis Analytics'
    KINESIS_FIREHOSE='Amazon Kinesis Firehose'
    KINESIS_VS='Amazon Kinesis Video Streams'
    LAKE_FORMATION='AWS Lake Formation'
    LAMBDA='AWS Lambda'
    LEX='Amazon Lex'
    LIGHTSAIL='Amazon Lightsail'
    LOCATION_SERVICE='Amazon Location Service'
    LOOKOUT_METRICS='Amazon Lookout for Metrics'
    MACIE='Amazon Macie'
    MANAGED_BLOCKCHAIN='Amazon Managed Blockchain'
    MANAGED_GRAFANA='Amazon Managed Grafana'
    MEMORYDB='Amazon MemoryDB'
    MIGRATION_HUB='AWS Migration Hub Refactor Spaces'
    MSK='Amazon Managed Streaming for Apache Kafka'
    MQ='Amazon MQ'
    MWA='Amazon Managed Workflows for Apache Airflow'
    NEPTUNE='Amazon Neptune'
    OPENSEARCH_SEVERLESS='Amazon OpenSearch Serverless'
    OPENSEARCH='Amazon OpenSearch Service'
    PERSONALIZE='Amazon Personalize'
    PINPOINT='Amazon Pinpoint'
    POLLY='Amazon Polly'
    Q='Amazon Q'
    QUANTUM_DB='Amazon Quantum Ledger Database'
    QUICKSIGHT='Amazon QuickSight'
    RDS='Amazon Relational Database Service'
    REDSHIFT='Amazon Redshift'
    REFUND='Refund'
    REGISTRAR='Amazon Registrar'
    REKOGNITION='Amazon Rekognition'
    RESILIENCE_HUB='AWS Resilience Hub'
    ROSA='Red Hat OpenShift Service on AWS'
    ROUTE53='Amazon Route 53'
    ROUTE53_ARC='AWS Route 53 Application Recovery Controller'
    S3='Amazon Simple Storage Service'
    SAGEMAKER='Amazon SageMaker'
    SECRETS_MANAGER='AWS Secrets Manager'
    SECURITY_HUB='AWS Security Hub'
    SECURITY_LAKE='Amazon Security Lake'
    SERVICE_CATALOGUE='AWS Service Catalog'
    SES='Amazon Simple Email Service'
    SIMPLEDB='Amazon SimpleDB'
    SNS='Amazon Simple Notification Service'
    STEP_FUNCTIONS='AWS Step Functions'
    STORAGE_GATEWAY='AWS Storage Gateway'
    SQS='Amazon Simple Queue Service'
    SUMERIAN='Amazon Sumerian'
    SWS='Amazon Simple Workflow Service'
    SYSTEMS_MANAGER='AWS Systems Manager'
    TAX='Tax'
    TEXTRACT='Amazon Textract'
    TIMESTREAM='Amazon Timestream'
    TRANSCRIBE='Amazon Transcribe'
    TRANSFER_FAMILY='AWS Transfer Family'
    TRANSLATE='Amazon Translate'
    VERIFIED_PERMISSIONS='Amazon Verified Permissions'
    VPC='Amazon Virtual Private Cloud'
    WAF='AWS WAF'
    WORKFORCE_ID='Workforce Identity Solutions'
    WORKSPACES='Amazon WorkSpaces'
    WORKSPACES_TC='Amazon WorkSpaces Thin Client'
    XRAY='AWS X-Ray'


class AWSServicesMap:
    
    def __init__(self):
        self._services_map: dict[
            ServiceName,
            str,
        ] = {
            service.name.lower().replace(
                '_',
                '-'
            ): service.value for service in AWSServices
        }

    def get(self, service_name: ServiceName):
        return self._services_map[service_name]