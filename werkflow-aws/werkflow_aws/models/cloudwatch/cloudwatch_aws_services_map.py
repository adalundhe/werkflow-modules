from enum import Enum
from typing import Literal


CloudWatchServiceName = Literal[
    'access-analyzer',
    'amazon-emr',
    'amazon-lex',
    'amazon-personalize',
    'amazon-s3-glacier',
    'amazon-workmail',
    'api-gateway',
    'appflow',
    'appintegrations',
    'appstream',
    'athena',
    'audit-manager',
    'aws-appconfig',
    'aws-codeartifact',
    'aws-config',
    'aws-health-imaging',
    'aws-user-notifications',
    'backup',
    'batch',
    'bedrock',
    'certificate-manager',
    'clean-rooms',
    'cloud-map',
    'cloudformation',
    'cloudhsm',
    'cloudshell',
    'cloudtrail',
    'cloudwatch',
    'cloudwatch-application-insights',
    'codebuild',
    'codecommit',
    'code-pipeline',
    'codestart-notifications',
    'cognito-user-pool',
    'comprehend',
    'computeoptimizer',
    'connect',
    'customer-profiles',
    'data-exchange',
    'data-lifecycle-manager',
    'database-migration-service',
    'databrew',
    'datasync',
    'directive',
    'directory-service',
    'dynamodb',
    'dynamodb-accelerator',
    'ec2',
    'ec2-auto-scaling',
    'ecr',
    'ecs',
    'efs',
    'elastic-beanstalk',
    'elastic-load-balancing',
    'elasticache',
    'emr',
    'emr-containers',
    'emr-serverless',
    'eventbridge',
    'fraud-detector',
    'gramelift',
    'grafana',
    'greengrass',
    'ground-station',
    'guardduty',
    'image-builder',
    'iot',
    'iot-events',
    'iot-sitwise',
    'iot-twinmaker',
    'iot-wireless',
    'ivs',
    'kendra',
    'kinesis-analytics',
    'kinesis-data-streams',
    'kinesis-video-streams',
    'kms',
    'lambda',
    'lightsail',
    'location',
    'logs',
    'macie',
    'mediaconnect',
    'mediaconvert',
    'memorydb',
    'neptunegraph',
    'network-firewall',
    'outposts',
    'pinpoint',
    'private-certificate-authority',
    'qldb',
    'rds',
    'redshift',
    'resource-access-manager',
    'resource-groups',
    'resource-groups-tagging-api',
    'robo-maker',
    'route-53-resolver',
    's3',
    'sagemaker',
    'scheduler',
    'secrets-manager',
    'security-hub',
    'service-catalog-appregistry',
    'ses',
    'sns',
    'ssm',
    'storage-gateway',
    'transcribe',
    'transfer',
    'translate',
    'workspaces',
    'x-ray'
]


class CloudWatchAWSService(Enum):
    ACCESS_ANALYZER='Access Analyzer'
    AMAZON_EMR='Amazon EMR'
    AMAZON_LEX='Amazon Lex'
    AMAZON_PERSONALIZE='Amazon Personalize'
    AMAZON_S3_GLACIER='Amazon S3 Glacier'
    AMAZON_WORKMAIL='Amazon WorkMail'
    API_GATEWAY='API Gateway'
    APPFLOW='AppFlow'
    APPINTEGRATIONS='AppIntegrations'
    APPSTREAM='AppStream'
    ATHENA='Athena'
    AUDIT_MANAGER='Audit Manager'
    AWS_APPCONFIG='AWS AppConfig'
    AWS_CODEARTIFACT='AWS CodeArtifact'
    AWS_CONFIG='AWS Config'
    AWS_HEALTH_IMAGING='AWS Health Imaging'
    AWS_USER_NOTIFICATIONS='AWS User Notifications'
    BACKUP='Backup'
    BATCH='Batch'
    BEDROCK='Bedrock'
    CERTIFICATE_MANGER='Certificate Manager'
    CLEAN_ROOMS='Clean Rooms'
    CLOUD_MAP='Cloud Map'
    CLOUDFORMATION='CloudFormation'
    CLOUDHSM='CloudHSM'
    CLOUDSHELL='CloudShell'
    CLOUDTRAIL='CloudTrail'
    CLOUDWATCH='CloudWatch'
    CLOUDWATCH_APPLICATION_INSIGHTS='CloudWatch Application Insights'
    CODEBUILD='CodeBuild'
    CODECOMMIT='CodeCommit'
    CODE_PIPELINE='CodePipeline'
    CODESTART_NOTIFICATIONS='CodeStar Notifications'
    COGNITO_USER_POOL='Cognito User Pool'
    COMPREHEND='Comprehend'
    COMPUTEOPTIMIZER='ComputeOptimizer'
    CONNECT='Connect'
    CUSTOMER_PROFILES='Customer Profiles'
    DATA_EXCHANGE='Data Exchange'
    DATA_LIFECYCLE_MANAGER='Data Lifecycle Manager'
    DATABASE_MIGRATION_SERVICE='Database Migration Service'
    DATABREW='DataBrew'
    DATASYNC='DataSync'
    DIRECTIVE='Directive'
    DIRECTORY_SERVICE='Directory Service'
    DYNAMODB='DynamoDB'
    DYNAMODB_ACCELERATOR='DynamoDB Accelerator'
    EC2='EC2'
    EC2_AUTO_SCALING='EC2 Auto Scaling'
    ECR='ECR'
    ECS='ECS'
    EFS='EFS'
    ELASTIC_BEANSTALK='Elastic Beanstalk'
    ELASTIC_LOAD_BALANCING='Elastic Load Balancing'
    ELASTICACHE='ElastiCache'
    EMR='EMR'
    EMR_CONTAINERS='EMR Containers'
    EMR_SERVERLESS='EMR Serverless'
    EVENTBRIDGE='EventBridge'
    FRAUD_DETECTOR='Fraud Detector'
    GAMELIFT='GameLift'
    GRAFANA='Grafana'
    GREENGRASS='Greengrass'
    GROUND_STATION='Ground Station'
    GUARDDUTY='GuardDuty'
    IMAGE_BUILDER='Image Builder'
    IOT='IoT'
    IOT_EVENTS='IoT Events'
    IOT_SITEWISE='IoT SiteWise'
    IOT_TWINMAKER='IoT TwinMaker'
    IOT_WIRELESS='IoT Wireless'
    IVS='IVS'
    KENDRA='Kendra'
    KINESIS_ANALYTICS='Kinesis Analytics'
    KINESIS_DATA_STREAMS='Kinesis Data Streams'
    KINESIS_VIDEO_STREAMS='Kinesis Video Streams'
    KMS='KMS'
    LAMBDA='Lambda'
    LIGHTSAIL='Lightsail'
    LOCATION='Location'
    LOGS='Logs'
    MACIE='Macie'
    MEDIACONNECT='MediaConnect'
    MEDIACONVERT='MediaConvert'
    MEMORYDB='MemoryDB'
    NEPTUNEGRAPH='NeptuneGraph'
    NETWORK_FIREWALL='Network Firewall'
    OUTPOSTS='Outposts'
    PINPOINT='Pinpoint'
    PRIVATE_CERTIFICATE_AUTHORITY='Private Certificate Authority'
    QLDB='QLDB'
    RDS='RDS'
    REDSHIFT='Redshift'
    RECOURCE_ACCESS_MANAGER='Resource Access Manager'
    RESOURCE_GROUPS='Resource Groups'
    RESOURCE_GROUPS_TAGGING_API='Resource Groups Tagging API'
    ROBO_MAKER='RoboMaker'
    ROUTE_53_RESOLVER='Route 53 Resolver'
    S3='S3'
    SAGEMAKER='SageMaker'
    SCHEDULER='Scheduler'
    SECRETS_MANAGER='Secrets Manager'
    SECURITY_HUB='Security Hub'
    SERVICE_CATALOG_APPREGISTRY='Service Catalog AppRegistry'
    SES='SES'
    SNS='SNS'
    SSM='SSM'
    STORAGE_GATEWAY='Storage Gateway'
    TRANSCRIBE='Transcribe'
    TRANSFER='Transfer'
    TRANSLATE='Translate'
    WORKSPACES='WorkSpaces'
    X_RAY='X-Ray'



class CloudWatchAWSServicesMap:

    def __init__(self):
        self._services_map: dict[
            CloudWatchServiceName,
            CloudWatchAWSService
        ] = {
            service.name.lower().replace(
                '_',
                '-'
            ): service for service in CloudWatchAWSService
        }

    def get(self, service_name: CloudWatchServiceName):
        return self._services_map[service_name]