from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any, cast

from werkflow_core import Module
from werkflow_aws.models import (
    AWSCredentialsSet,
    RegionName,
)
from werkflow_aws.models.sts import AssumeRoleRequest
from .authorization_type import AuthorizationType
from .parsers import AWSConfigParser
from .services.aws_credentials import AWSCredentials
from .supported_clients import SupportedClients

if TYPE_CHECKING:
    from .services import (
        AWSBaseService,
        AWSACM,
        AWSAPIGateway,
        AWSAPIGatewayV2,
        AWSAccessAnalyzer,
        AWSAmplify,
        AWSAppFlow,
        AWSAppRunner,
        AWSAppStream,
        AWSAppSync,
        AWSAthena,
        AWSAuditManager,
        AWSAutoScaling,
        AWSBackup,
        AWSBatch,
        AWSBedrock,
        AWSBedrockRuntime,
        AWSCloudFormation,
        AWSCloudFront,
        AWSCloudHSM,
        AWSCloudSearch,
        AWSCloudTrail,
        AWSCloudWatchLogs,
        AWSCloudwatch,
        AWSCodeArtifact,
        AWSCodeBuild,
        AWSCodeCatalyst,
        AWSCodeCommit,
        AWSCodeGuru,
        AWSCodePipeline,
        AWSCognitoIDP,
        AWSCognitoSync,
        AWSComprehend,
        AWSComputeOptimizer,
        AWSConfigService,
        AWSConnect,
        AWSCostExplorer,
        AWSDMS,
        AWSDataPipeline,
        AWSDataSync,
        AWSDataZone,
        AWSDetective,
        AWSDevOpsGuru,
        AWSDeviceFarm,
        AWSDirectConnect,
        AWSDirectoryService,
        AWSDocumentDB,
        AWSDynamoDB,
        AWSEC2,
        AWSECR,
        AWSECRPublic,
        AWSECS,
        AWSEFS,
        AWSEKS,
        AWSELBv2,
        AWSEMR,
        AWSElastiCache,
        AWSElasticBlockStorage,
        AWSEndUserMessaging,
        AWSEventBridge,
        AWSFIS,
        AWSFMS,
        AWSFSx,
        AWSFirehose,
        AWSGlacier,
        AWSGlue,
        AWSGuardDuty,
        AWSHealthImaging,
        AWSIAM,
        AWSIdentityStore,
        AWSIoT,
        AWSIoTJobsData,
        AWSKMS,
        AWSKendra,
        AWSKinesis,
        AWSKinesisAnalytics,
        AWSKinesisVideo,
        AWSLakeFormation,
        AWSLambda,
        AWSLex,
        AWSLightsail,
        AWSLocation,
        AWSMQ,
        AWSMSK,
        AWSMWAA,
        AWSMacie,
        AWSManagedBlockchain,
        AWSManagedGrafana,
        AWSMediaStore,
        AWSMemoryDB,
        AWSMigrationHub,
        AWSNeptune,
        AWSNetworkManager,
        AWSOpenSearch,
        AWSOpenSearchServerless,
        AWSOrganizations,
        AWSPersonalize,
        AWSPinpoint,
        AWSPolly,
        AWSQBusiness,
        AWSQuickSight,
        AWSRDS,
        AWSRedshift,
        AWSRekognition,
        AWSResilienceHub,
        AWSRoute53,
        AWSRoute53ARC,
        AWSRoute53Domains,
        AWSSES,
        AWSSNS,
        AWSSQS,
        AWSSSM,
        AWSSTS,
        AWSSWF,
        AWSSageMaker,
        AWSScheduler,
        AWSSecretsManager,
        AWSSecurityHub,
        AWSSecurityLake,
        AWSServiceCatalog,
        AWSSimpleDB,
        AWSStepFunctions,
        AWSStorageGateway,
        AWSSupport,
        AWSTaxSettings,
        AWSTextract,
        AWSTimestreamQuery,
        AWSTimestreamWrite,
        AWSTranscribe,
        AWSTransfer,
        AWSTranslate,
        AWSVerifiedPermissions,
        AWSWAFv2,
        AWSWorkSpaces,
        AWSWorkSpacesThinClient,
        AWSXRay,
        AWSs3,
    )

_CLIENT_FACTORY_MAP: dict[SupportedClients, tuple[str, str]] = {
    "amplify": ("werkflow_aws.services.aws_amplify", "AWSAmplify"),
    "api-gateway": ("werkflow_aws.services.aws_api_gateway", "AWSAPIGateway"),
    "api-gateway-v2": ("werkflow_aws.services.aws_api_gateway_v2", "AWSAPIGatewayV2"),
    "app-flow": ("werkflow_aws.services.aws_app_flow", "AWSAppFlow"),
    "app-runner": ("werkflow_aws.services.aws_app_runner", "AWSAppRunner"),
    "app-stream": ("werkflow_aws.services.aws_app_stream", "AWSAppStream"),
    "app-sync": ("werkflow_aws.services.aws_app_sync", "AWSAppSync"),
    "athena": ("werkflow_aws.services.aws_athena", "AWSAthena"),
    "audit-manager": ("werkflow_aws.services.aws_audit_manager", "AWSAuditManager"),
    "autoscaling": ("werkflow_aws.services.aws_autoscaling", "AWSAutoScaling"),
    "backup": ("werkflow_aws.services.aws_backup", "AWSBackup"),
    "batch": ("werkflow_aws.services.aws_batch", "AWSBatch"),
    "bedrock": ("werkflow_aws.services.aws_bedrock", "AWSBedrock"),
    "bedrock-runtime": ("werkflow_aws.services.aws_bedrock_runtime", "AWSBedrockRuntime"),
    "cert-manager": ("werkflow_aws.services.aws_cert_manager", "AWSACM"),
    "cloud-formation": ("werkflow_aws.services.aws_cloud_formation", "AWSCloudFormation"),
    "cloud-trail": ("werkflow_aws.services.aws_cloud_trail", "AWSCloudTrail"),
    "cloud-wan": ("werkflow_aws.services.aws_cloud_wan", "AWSNetworkManager"),
    "cloudfront": ("werkflow_aws.services.aws_cloudfront", "AWSCloudFront"),
    "cloudhsm": ("werkflow_aws.services.aws_cloudhsm", "AWSCloudHSM"),
    "cloudsearch": ("werkflow_aws.services.aws_cloudsearch", "AWSCloudSearch"),
    "cloudwatch": ("werkflow_aws.services.aws_cloudwatch", "AWSCloudwatch"),
    "cloudwatch-events": ("werkflow_aws.services.aws_cloudwatch_events", "AWSEventBridge"),
    "cloudwatch-logs": ("werkflow_aws.services.aws_cloudwatch_logs", "AWSCloudWatchLogs"),
    "code-artifact": ("werkflow_aws.services.aws_codeartifact", "AWSCodeArtifact"),
    "codebuild": ("werkflow_aws.services.aws_codebuild", "AWSCodeBuild"),
    "codecatalyst": ("werkflow_aws.services.aws_codecatalyst", "AWSCodeCatalyst"),
    "codecommit": ("werkflow_aws.services.aws_codecommit", "AWSCodeCommit"),
    "codeguru": ("werkflow_aws.services.aws_codeguru", "AWSCodeGuru"),
    "codepipeline": ("werkflow_aws.services.aws_codepipeline", "AWSCodePipeline"),
    "cognito": ("werkflow_aws.services.aws_cognito", "AWSCognitoIDP"),
    "cognito-sync": ("werkflow_aws.services.aws_cognito_sync", "AWSCognitoSync"),
    "comprehend": ("werkflow_aws.services.aws_comprehend", "AWSComprehend"),
    "compute-optimizer": ("werkflow_aws.services.aws_compute_optimizer", "AWSComputeOptimizer"),
    "config": ("werkflow_aws.services.aws_aws_config", "AWSConfigService"),
    "connect": ("werkflow_aws.services.aws_aws_connect", "AWSConnect"),
    "cost-explorer": ("werkflow_aws.services.aws_cost_explorer", "AWSCostExplorer"),
    "data-pipeline": ("werkflow_aws.services.aws_data_pipeline", "AWSDataPipeline"),
    "datasync": ("werkflow_aws.services.aws_datasync", "AWSDataSync"),
    "datazone": ("werkflow_aws.services.aws_datazone", "AWSDataZone"),
    "detective": ("werkflow_aws.services.aws_detective", "AWSDetective"),
    "device-farm": ("werkflow_aws.services.aws_device_farm", "AWSDeviceFarm"),
    "devops-guru": ("werkflow_aws.services.aws_devops_guru", "AWSDevOpsGuru"),
    "direct-connect": ("werkflow_aws.services.aws_direct_connect", "AWSDirectConnect"),
    "directory-service": ("werkflow_aws.services.aws_directory_service", "AWSDirectoryService"),
    "dms": ("werkflow_aws.services.aws_dms", "AWSDMS"),
    "documentdb": ("werkflow_aws.services.aws_documentdb", "AWSDocumentDB"),
    "dynamodb": ("werkflow_aws.services.aws_dynamodb", "AWSDynamoDB"),
    "ebs": ("werkflow_aws.services.aws_elastic_block_storage", "AWSElasticBlockStorage"),
    "ec2": ("werkflow_aws.services.aws_ec2", "AWSEC2"),
    "ecr": ("werkflow_aws.services.aws_ecr", "AWSECR"),
    "ecr-public": ("werkflow_aws.services.aws_ecr_public", "AWSECRPublic"),
    "ecs": ("werkflow_aws.services.aws_ecs", "AWSECS"),
    "efs": ("werkflow_aws.services.aws_efs", "AWSEFS"),
    "eks": ("werkflow_aws.services.aws_eks", "AWSEKS"),
    "elasticache": ("werkflow_aws.services.aws_elasticache", "AWSElastiCache"),
    "elb": ("werkflow_aws.services.aws_elb", "AWSELBv2"),
    "elemental-mediastore": ("werkflow_aws.services.aws_elemental_mediastore", "AWSMediaStore"),
    "emr": ("werkflow_aws.services.aws_emr", "AWSEMR"),
    "enterprise-support": ("werkflow_aws.services.aws_enterprise_support", "AWSSupport"),
    "eum": ("werkflow_aws.services.aws_eum", "AWSEndUserMessaging"),
    "firewall": ("werkflow_aws.services.aws_firewall", "AWSFMS"),
    "fis": ("werkflow_aws.services.aws_fis", "AWSFIS"),
    "fsx": ("werkflow_aws.services.aws_fsx", "AWSFSx"),
    "glacier": ("werkflow_aws.services.aws_glacier", "AWSGlacier"),
    "glue": ("werkflow_aws.services.aws_glue", "AWSGlue"),
    "guardduty": ("werkflow_aws.services.aws_guardduty", "AWSGuardDuty"),
    "healthimaging": ("werkflow_aws.services.aws_healthimaging", "AWSHealthImaging"),
    "iam": ("werkflow_aws.services.aws_iam", "AWSIAM"),
    "iam-analyzer": ("werkflow_aws.services.aws_iam_analyzer", "AWSAccessAnalyzer"),
    "iot": ("werkflow_aws.services.aws_iot", "AWSIoT"),
    "iot-dm": ("werkflow_aws.services.aws_iot_dm", "AWSIoTJobsData"),
    "kendra": ("werkflow_aws.services.aws_kendra", "AWSKendra"),
    "kinesis": ("werkflow_aws.services.aws_kinesis", "AWSKinesis"),
    "kinesis-analytics": ("werkflow_aws.services.aws_kinesis_analytics", "AWSKinesisAnalytics"),
    "kinesis-firehose": ("werkflow_aws.services.aws_kinesis_firehose", "AWSFirehose"),
    "kinesis-vs": ("werkflow_aws.services.aws_kinesis_vs", "AWSKinesisVideo"),
    "kms": ("werkflow_aws.services.aws_kms", "AWSKMS"),
    "lake-formation": ("werkflow_aws.services.aws_lake_formation", "AWSLakeFormation"),
    "lambda": ("werkflow_aws.services.aws_lambda", "AWSLambda"),
    "lex": ("werkflow_aws.services.aws_lex", "AWSLex"),
    "lightsail": ("werkflow_aws.services.aws_lightsail", "AWSLightsail"),
    "location-service": ("werkflow_aws.services.aws_location_service", "AWSLocation"),
    "macie": ("werkflow_aws.services.aws_macie", "AWSMacie"),
    "managed-blockchain": ("werkflow_aws.services.aws_managed_blockchain", "AWSManagedBlockchain"),
    "managed-grafana": ("werkflow_aws.services.aws_managed_grafana", "AWSManagedGrafana"),
    "memorydb": ("werkflow_aws.services.aws_memorydb", "AWSMemoryDB"),
    "migration-hub": ("werkflow_aws.services.aws_migration_hub", "AWSMigrationHub"),
    "mq": ("werkflow_aws.services.aws_mq", "AWSMQ"),
    "msk": ("werkflow_aws.services.aws_msk", "AWSMSK"),
    "mwa": ("werkflow_aws.services.aws_mwa", "AWSMWAA"),
    "neptune": ("werkflow_aws.services.aws_neptune", "AWSNeptune"),
    "opensearch": ("werkflow_aws.services.aws_opensearch", "AWSOpenSearch"),
    "opensearch-serverless": ("werkflow_aws.services.aws_opensearch_serverless", "AWSOpenSearchServerless"),
    "organizations": ("werkflow_aws.services.aws_organizations", "AWSOrganizations"),
    "personalize": ("werkflow_aws.services.aws_personalize", "AWSPersonalize"),
    "pinpoint": ("werkflow_aws.services.aws_pinpoint", "AWSPinpoint"),
    "polly": ("werkflow_aws.services.aws_polly", "AWSPolly"),
    "q": ("werkflow_aws.services.aws_q_business", "AWSQBusiness"),
    "quicksight": ("werkflow_aws.services.aws_quicksight", "AWSQuickSight"),
    "rds": ("werkflow_aws.services.aws_rds", "AWSRDS"),
    "redshift": ("werkflow_aws.services.aws_redshift", "AWSRedshift"),
    "registrar": ("werkflow_aws.services.aws_registrar", "AWSRoute53Domains"),
    "rekognition": ("werkflow_aws.services.aws_rekognition", "AWSRekognition"),
    "resilience-hub": ("werkflow_aws.services.aws_resilience_hub", "AWSResilienceHub"),
    "route53": ("werkflow_aws.services.aws_route53", "AWSRoute53"),
    "route53-arc": ("werkflow_aws.services.aws_route53_arc", "AWSRoute53ARC"),
    "s3": ("werkflow_aws.services.aws_s3", "AWSs3"),
    "sagemaker": ("werkflow_aws.services.aws_sagemaker", "AWSSageMaker"),
    "scheduler": ("werkflow_aws.services.aws_scheduler", "AWSScheduler"),
    "secrets-manager": ("werkflow_aws.services.aws_secrets_manager", "AWSSecretsManager"),
    "security-hub": ("werkflow_aws.services.aws_security_hub", "AWSSecurityHub"),
    "security-lake": ("werkflow_aws.services.aws_security_lake", "AWSSecurityLake"),
    "service-catalogue": ("werkflow_aws.services.aws_service_catalogue", "AWSServiceCatalog"),
    "ses": ("werkflow_aws.services.aws_ses", "AWSSES"),
    "simpledb": ("werkflow_aws.services.aws_simpledb", "AWSSimpleDB"),
    "sns": ("werkflow_aws.services.aws_sns", "AWSSNS"),
    "sqs": ("werkflow_aws.services.aws_sqs", "AWSSQS"),
    "step-functions": ("werkflow_aws.services.aws_step_functions", "AWSStepFunctions"),
    "storage-gateway": ("werkflow_aws.services.aws_storage_gateway", "AWSStorageGateway"),
    "sts": ("werkflow_aws.services.aws_sts", "AWSSTS"),
    "sws": ("werkflow_aws.services.aws_sws", "AWSSWF"),
    "systems-manager": ("werkflow_aws.services.aws_systems_manager", "AWSSSM"),
    "tax": ("werkflow_aws.services.aws_tax", "AWSTaxSettings"),
    "textract": ("werkflow_aws.services.aws_textract", "AWSTextract"),
    "timestream": ("werkflow_aws.services.aws_timestream", "AWSTimestreamWrite"),
    "timestream-query": ("werkflow_aws.services.aws_timestream_query", "AWSTimestreamQuery"),
    "transcribe": ("werkflow_aws.services.aws_transcribe", "AWSTranscribe"),
    "transfer-family": ("werkflow_aws.services.aws_transfer_family", "AWSTransfer"),
    "translate": ("werkflow_aws.services.aws_translate", "AWSTranslate"),
    "verified-permissions": ("werkflow_aws.services.aws_verified_permissions", "AWSVerifiedPermissions"),
    "waf": ("werkflow_aws.services.aws_waf", "AWSWAFv2"),
    "workforce-id": ("werkflow_aws.services.aws_workforce_id", "AWSIdentityStore"),
    "workspaces": ("werkflow_aws.services.aws_workspaces", "AWSWorkSpaces"),
    "workspaces-tc": ("werkflow_aws.services.aws_workspaces_tc", "AWSWorkSpacesThinClient"),
    "xray": ("werkflow_aws.services.aws_xray", "AWSXRay"),
}


class AWS(Module):
    dependencies = [
        'boto3',
        'pydantic',
        'werkflow-secrets',
        'werkflow-shell',
        'werkflow-system',
    ]

    def __init__(self) -> None:
        super().__init__()
        self.config = AWSConfigParser()
        self.credentials = AWSCredentials()
        self._clients: dict[SupportedClients, AWSBaseService[Any]] = {}

    def _get_service(self, client: SupportedClients) -> AWSBaseService[Any]:
        service = self._clients.get(client)
        if service is not None:
            return service

        factory = _CLIENT_FACTORY_MAP.get(client)
        if factory is None:
            supported = ', '.join(sorted(_CLIENT_FACTORY_MAP.keys()))
            raise ValueError(
                f"Unsupported AWS client {client!r}. Supported clients: {supported}"
            )
        module_name, class_name = factory
        module = importlib.import_module(module_name)
        service_cls = getattr(module, class_name)
        instance: AWSBaseService[Any] = service_cls()
        self._clients[client] = instance
        return instance

    @property
    def amplify(self) -> AWSAmplify:
        return cast('AWSAmplify', self._get_service('amplify'))

    @property
    def api_gateway(self) -> AWSAPIGateway:
        return cast('AWSAPIGateway', self._get_service('api-gateway'))

    @property
    def api_gateway_v2(self) -> AWSAPIGatewayV2:
        return cast('AWSAPIGatewayV2', self._get_service('api-gateway-v2'))

    @property
    def app_flow(self) -> AWSAppFlow:
        return cast('AWSAppFlow', self._get_service('app-flow'))

    @property
    def app_runner(self) -> AWSAppRunner:
        return cast('AWSAppRunner', self._get_service('app-runner'))

    @property
    def app_stream(self) -> AWSAppStream:
        return cast('AWSAppStream', self._get_service('app-stream'))

    @property
    def app_sync(self) -> AWSAppSync:
        return cast('AWSAppSync', self._get_service('app-sync'))

    @property
    def athena(self) -> AWSAthena:
        return cast('AWSAthena', self._get_service('athena'))

    @property
    def audit_manager(self) -> AWSAuditManager:
        return cast('AWSAuditManager', self._get_service('audit-manager'))

    @property
    def autoscaling(self) -> AWSAutoScaling:
        return cast('AWSAutoScaling', self._get_service('autoscaling'))

    @property
    def aws_config(self) -> AWSConfigService:
        return cast('AWSConfigService', self._get_service('config'))

    @property
    def aws_connect(self) -> AWSConnect:
        return cast('AWSConnect', self._get_service('connect'))

    @property
    def aws_lambda(self) -> AWSLambda:
        return cast('AWSLambda', self._get_service('lambda'))

    @property
    def backup(self) -> AWSBackup:
        return cast('AWSBackup', self._get_service('backup'))

    @property
    def batch(self) -> AWSBatch:
        return cast('AWSBatch', self._get_service('batch'))

    @property
    def bedrock(self) -> AWSBedrock:
        return cast('AWSBedrock', self._get_service('bedrock'))

    @property
    def bedrock_runtime(self) -> AWSBedrockRuntime:
        return cast('AWSBedrockRuntime', self._get_service('bedrock-runtime'))

    @property
    def cert_manager(self) -> AWSACM:
        return cast('AWSACM', self._get_service('cert-manager'))

    @property
    def cloud_formation(self) -> AWSCloudFormation:
        return cast('AWSCloudFormation', self._get_service('cloud-formation'))

    @property
    def cloud_trail(self) -> AWSCloudTrail:
        return cast('AWSCloudTrail', self._get_service('cloud-trail'))

    @property
    def cloud_wan(self) -> AWSNetworkManager:
        return cast('AWSNetworkManager', self._get_service('cloud-wan'))

    @property
    def cloudfront(self) -> AWSCloudFront:
        return cast('AWSCloudFront', self._get_service('cloudfront'))

    @property
    def cloudhsm(self) -> AWSCloudHSM:
        return cast('AWSCloudHSM', self._get_service('cloudhsm'))

    @property
    def cloudsearch(self) -> AWSCloudSearch:
        return cast('AWSCloudSearch', self._get_service('cloudsearch'))

    @property
    def cloudwatch(self) -> AWSCloudwatch:
        return cast('AWSCloudwatch', self._get_service('cloudwatch'))

    @property
    def cloudwatch_events(self) -> AWSEventBridge:
        return cast('AWSEventBridge', self._get_service('cloudwatch-events'))

    @property
    def cloudwatch_logs(self) -> AWSCloudWatchLogs:
        return cast('AWSCloudWatchLogs', self._get_service('cloudwatch-logs'))

    @property
    def code_artifact(self) -> AWSCodeArtifact:
        return cast('AWSCodeArtifact', self._get_service('code-artifact'))

    @property
    def codebuild(self) -> AWSCodeBuild:
        return cast('AWSCodeBuild', self._get_service('codebuild'))

    @property
    def codecatalyst(self) -> AWSCodeCatalyst:
        return cast('AWSCodeCatalyst', self._get_service('codecatalyst'))

    @property
    def codecommit(self) -> AWSCodeCommit:
        return cast('AWSCodeCommit', self._get_service('codecommit'))

    @property
    def codeguru(self) -> AWSCodeGuru:
        return cast('AWSCodeGuru', self._get_service('codeguru'))

    @property
    def codepipeline(self) -> AWSCodePipeline:
        return cast('AWSCodePipeline', self._get_service('codepipeline'))

    @property
    def cognito(self) -> AWSCognitoIDP:
        return cast('AWSCognitoIDP', self._get_service('cognito'))

    @property
    def cognito_sync(self) -> AWSCognitoSync:
        return cast('AWSCognitoSync', self._get_service('cognito-sync'))

    @property
    def comprehend(self) -> AWSComprehend:
        return cast('AWSComprehend', self._get_service('comprehend'))

    @property
    def compute_optimizer(self) -> AWSComputeOptimizer:
        return cast('AWSComputeOptimizer', self._get_service('compute-optimizer'))

    @property
    def cost_explorer(self) -> AWSCostExplorer:
        return cast('AWSCostExplorer', self._get_service('cost-explorer'))

    @property
    def data_pipeline(self) -> AWSDataPipeline:
        return cast('AWSDataPipeline', self._get_service('data-pipeline'))

    @property
    def datasync(self) -> AWSDataSync:
        return cast('AWSDataSync', self._get_service('datasync'))

    @property
    def datazone(self) -> AWSDataZone:
        return cast('AWSDataZone', self._get_service('datazone'))

    @property
    def detective(self) -> AWSDetective:
        return cast('AWSDetective', self._get_service('detective'))

    @property
    def device_farm(self) -> AWSDeviceFarm:
        return cast('AWSDeviceFarm', self._get_service('device-farm'))

    @property
    def devops_guru(self) -> AWSDevOpsGuru:
        return cast('AWSDevOpsGuru', self._get_service('devops-guru'))

    @property
    def direct_connect(self) -> AWSDirectConnect:
        return cast('AWSDirectConnect', self._get_service('direct-connect'))

    @property
    def directory_service(self) -> AWSDirectoryService:
        return cast('AWSDirectoryService', self._get_service('directory-service'))

    @property
    def dms(self) -> AWSDMS:
        return cast('AWSDMS', self._get_service('dms'))

    @property
    def documentdb(self) -> AWSDocumentDB:
        return cast('AWSDocumentDB', self._get_service('documentdb'))

    @property
    def dynamodb(self) -> AWSDynamoDB:
        return cast('AWSDynamoDB', self._get_service('dynamodb'))

    @property
    def ebs(self) -> AWSElasticBlockStorage:
        return cast('AWSElasticBlockStorage', self._get_service('ebs'))

    @property
    def ec2(self) -> AWSEC2:
        return cast('AWSEC2', self._get_service('ec2'))

    @property
    def ecr(self) -> AWSECR:
        return cast('AWSECR', self._get_service('ecr'))

    @property
    def ecr_public(self) -> AWSECRPublic:
        return cast('AWSECRPublic', self._get_service('ecr-public'))

    @property
    def ecs(self) -> AWSECS:
        return cast('AWSECS', self._get_service('ecs'))

    @property
    def efs(self) -> AWSEFS:
        return cast('AWSEFS', self._get_service('efs'))

    @property
    def eks(self) -> AWSEKS:
        return cast('AWSEKS', self._get_service('eks'))

    @property
    def elasticache(self) -> AWSElastiCache:
        return cast('AWSElastiCache', self._get_service('elasticache'))

    @property
    def elb(self) -> AWSELBv2:
        return cast('AWSELBv2', self._get_service('elb'))

    @property
    def elemental_mediastore(self) -> AWSMediaStore:
        return cast('AWSMediaStore', self._get_service('elemental-mediastore'))

    @property
    def emr(self) -> AWSEMR:
        return cast('AWSEMR', self._get_service('emr'))

    @property
    def enterprise_support(self) -> AWSSupport:
        return cast('AWSSupport', self._get_service('enterprise-support'))

    @property
    def eum(self) -> AWSEndUserMessaging:
        return cast('AWSEndUserMessaging', self._get_service('eum'))

    @property
    def firewall(self) -> AWSFMS:
        return cast('AWSFMS', self._get_service('firewall'))

    @property
    def fis(self) -> AWSFIS:
        return cast('AWSFIS', self._get_service('fis'))

    @property
    def fsx(self) -> AWSFSx:
        return cast('AWSFSx', self._get_service('fsx'))

    @property
    def glacier(self) -> AWSGlacier:
        return cast('AWSGlacier', self._get_service('glacier'))

    @property
    def glue(self) -> AWSGlue:
        return cast('AWSGlue', self._get_service('glue'))

    @property
    def guardduty(self) -> AWSGuardDuty:
        return cast('AWSGuardDuty', self._get_service('guardduty'))

    @property
    def healthimaging(self) -> AWSHealthImaging:
        return cast('AWSHealthImaging', self._get_service('healthimaging'))

    @property
    def iam(self) -> AWSIAM:
        return cast('AWSIAM', self._get_service('iam'))

    @property
    def iam_analyzer(self) -> AWSAccessAnalyzer:
        return cast('AWSAccessAnalyzer', self._get_service('iam-analyzer'))

    @property
    def iot(self) -> AWSIoT:
        return cast('AWSIoT', self._get_service('iot'))

    @property
    def iot_dm(self) -> AWSIoTJobsData:
        return cast('AWSIoTJobsData', self._get_service('iot-dm'))

    @property
    def kendra(self) -> AWSKendra:
        return cast('AWSKendra', self._get_service('kendra'))

    @property
    def kinesis(self) -> AWSKinesis:
        return cast('AWSKinesis', self._get_service('kinesis'))

    @property
    def kinesis_analytics(self) -> AWSKinesisAnalytics:
        return cast('AWSKinesisAnalytics', self._get_service('kinesis-analytics'))

    @property
    def kinesis_firehose(self) -> AWSFirehose:
        return cast('AWSFirehose', self._get_service('kinesis-firehose'))

    @property
    def kinesis_vs(self) -> AWSKinesisVideo:
        return cast('AWSKinesisVideo', self._get_service('kinesis-vs'))

    @property
    def kms(self) -> AWSKMS:
        return cast('AWSKMS', self._get_service('kms'))

    @property
    def lake_formation(self) -> AWSLakeFormation:
        return cast('AWSLakeFormation', self._get_service('lake-formation'))

    @property
    def lex(self) -> AWSLex:
        return cast('AWSLex', self._get_service('lex'))

    @property
    def lightsail(self) -> AWSLightsail:
        return cast('AWSLightsail', self._get_service('lightsail'))

    @property
    def location_service(self) -> AWSLocation:
        return cast('AWSLocation', self._get_service('location-service'))

    @property
    def macie(self) -> AWSMacie:
        return cast('AWSMacie', self._get_service('macie'))

    @property
    def managed_blockchain(self) -> AWSManagedBlockchain:
        return cast('AWSManagedBlockchain', self._get_service('managed-blockchain'))

    @property
    def managed_grafana(self) -> AWSManagedGrafana:
        return cast('AWSManagedGrafana', self._get_service('managed-grafana'))

    @property
    def memorydb(self) -> AWSMemoryDB:
        return cast('AWSMemoryDB', self._get_service('memorydb'))

    @property
    def migration_hub(self) -> AWSMigrationHub:
        return cast('AWSMigrationHub', self._get_service('migration-hub'))

    @property
    def mq(self) -> AWSMQ:
        return cast('AWSMQ', self._get_service('mq'))

    @property
    def msk(self) -> AWSMSK:
        return cast('AWSMSK', self._get_service('msk'))

    @property
    def mwa(self) -> AWSMWAA:
        return cast('AWSMWAA', self._get_service('mwa'))

    @property
    def neptune(self) -> AWSNeptune:
        return cast('AWSNeptune', self._get_service('neptune'))

    @property
    def opensearch(self) -> AWSOpenSearch:
        return cast('AWSOpenSearch', self._get_service('opensearch'))

    @property
    def opensearch_serverless(self) -> AWSOpenSearchServerless:
        return cast('AWSOpenSearchServerless', self._get_service('opensearch-serverless'))

    @property
    def organizations(self) -> AWSOrganizations:
        return cast('AWSOrganizations', self._get_service('organizations'))

    @property
    def personalize(self) -> AWSPersonalize:
        return cast('AWSPersonalize', self._get_service('personalize'))

    @property
    def pinpoint(self) -> AWSPinpoint:
        return cast('AWSPinpoint', self._get_service('pinpoint'))

    @property
    def polly(self) -> AWSPolly:
        return cast('AWSPolly', self._get_service('polly'))

    @property
    def q(self) -> AWSQBusiness:
        return cast('AWSQBusiness', self._get_service('q'))

    @property
    def quicksight(self) -> AWSQuickSight:
        return cast('AWSQuickSight', self._get_service('quicksight'))

    @property
    def rds(self) -> AWSRDS:
        return cast('AWSRDS', self._get_service('rds'))

    @property
    def redshift(self) -> AWSRedshift:
        return cast('AWSRedshift', self._get_service('redshift'))

    @property
    def registrar(self) -> AWSRoute53Domains:
        return cast('AWSRoute53Domains', self._get_service('registrar'))

    @property
    def rekognition(self) -> AWSRekognition:
        return cast('AWSRekognition', self._get_service('rekognition'))

    @property
    def resilience_hub(self) -> AWSResilienceHub:
        return cast('AWSResilienceHub', self._get_service('resilience-hub'))

    @property
    def route53(self) -> AWSRoute53:
        return cast('AWSRoute53', self._get_service('route53'))

    @property
    def route53_arc(self) -> AWSRoute53ARC:
        return cast('AWSRoute53ARC', self._get_service('route53-arc'))

    @property
    def s3(self) -> AWSs3:
        return cast('AWSs3', self._get_service('s3'))

    @property
    def sagemaker(self) -> AWSSageMaker:
        return cast('AWSSageMaker', self._get_service('sagemaker'))

    @property
    def scheduler(self) -> AWSScheduler:
        return cast('AWSScheduler', self._get_service('scheduler'))

    @property
    def secrets_manager(self) -> AWSSecretsManager:
        return cast('AWSSecretsManager', self._get_service('secrets-manager'))

    @property
    def security_hub(self) -> AWSSecurityHub:
        return cast('AWSSecurityHub', self._get_service('security-hub'))

    @property
    def security_lake(self) -> AWSSecurityLake:
        return cast('AWSSecurityLake', self._get_service('security-lake'))

    @property
    def service_catalogue(self) -> AWSServiceCatalog:
        return cast('AWSServiceCatalog', self._get_service('service-catalogue'))

    @property
    def ses(self) -> AWSSES:
        return cast('AWSSES', self._get_service('ses'))

    @property
    def simpledb(self) -> AWSSimpleDB:
        return cast('AWSSimpleDB', self._get_service('simpledb'))

    @property
    def sns(self) -> AWSSNS:
        return cast('AWSSNS', self._get_service('sns'))

    @property
    def sqs(self) -> AWSSQS:
        return cast('AWSSQS', self._get_service('sqs'))

    @property
    def step_functions(self) -> AWSStepFunctions:
        return cast('AWSStepFunctions', self._get_service('step-functions'))

    @property
    def storage_gateway(self) -> AWSStorageGateway:
        return cast('AWSStorageGateway', self._get_service('storage-gateway'))

    @property
    def sts(self) -> AWSSTS:
        return cast('AWSSTS', self._get_service('sts'))

    @property
    def sws(self) -> AWSSWF:
        return cast('AWSSWF', self._get_service('sws'))

    @property
    def systems_manager(self) -> AWSSSM:
        return cast('AWSSSM', self._get_service('systems-manager'))

    @property
    def tax(self) -> AWSTaxSettings:
        return cast('AWSTaxSettings', self._get_service('tax'))

    @property
    def textract(self) -> AWSTextract:
        return cast('AWSTextract', self._get_service('textract'))

    @property
    def timestream(self) -> AWSTimestreamWrite:
        return cast('AWSTimestreamWrite', self._get_service('timestream'))

    @property
    def timestream_query(self) -> AWSTimestreamQuery:
        return cast('AWSTimestreamQuery', self._get_service('timestream-query'))

    @property
    def transcribe(self) -> AWSTranscribe:
        return cast('AWSTranscribe', self._get_service('transcribe'))

    @property
    def transfer_family(self) -> AWSTransfer:
        return cast('AWSTransfer', self._get_service('transfer-family'))

    @property
    def translate(self) -> AWSTranslate:
        return cast('AWSTranslate', self._get_service('translate'))

    @property
    def verified_permissions(self) -> AWSVerifiedPermissions:
        return cast('AWSVerifiedPermissions', self._get_service('verified-permissions'))

    @property
    def waf(self) -> AWSWAFv2:
        return cast('AWSWAFv2', self._get_service('waf'))

    @property
    def workforce_id(self) -> AWSIdentityStore:
        return cast('AWSIdentityStore', self._get_service('workforce-id'))

    @property
    def workspaces(self) -> AWSWorkSpaces:
        return cast('AWSWorkSpaces', self._get_service('workspaces'))

    @property
    def workspaces_tc(self) -> AWSWorkSpacesThinClient:
        return cast('AWSWorkSpacesThinClient', self._get_service('workspaces-tc'))

    @property
    def xray(self) -> AWSXRay:
        return cast('AWSXRay', self._get_service('xray'))

    @property
    def lambda_(self) -> AWSLambda:
        return self.aws_lambda

    async def connect(
        self,
        client: SupportedClients,
        credentials: AWSCredentialsSet | None = None,
        region: RegionName = 'us-east-1',
        authorization_type: AuthorizationType = "client",
        assume_role_request: AssumeRoleRequest | None = None,
        assume_proxy_role_request: AssumeRoleRequest | None = None,
    ) -> None:
        match authorization_type:
            case "assume":
                if assume_role_request is None:
                    raise ValueError(
                        "assume_role_request is required when authorization_type='assume'."
                    )
                await self._connect_assumed_role(
                    client=client,
                    assume_role_request=assume_role_request,
                    assume_proxy_role_request=assume_proxy_role_request,
                    region=region,
                    credentials=credentials,
                )
            case "sso":
                if credentials is None or not credentials.aws_profile:
                    raise ValueError(
                        "credentials with aws_profile set is required when authorization_type='sso'."
                    )
                await self._connect_sso(
                    client=client,
                    credentials=credentials,
                    region=region,
                )
            case "client":
                await self._connect_client(
                    client=client,
                    credentials=credentials,
                    region=region,
                )
            case _:
                raise ValueError(
                    f"Unsupported authorization_type {authorization_type!r}. "
                    "Expected 'client', 'sso', or 'assume'."
                )

    async def _connect_assumed_role(
        self,
        client: SupportedClients,
        assume_role_request: AssumeRoleRequest,
        assume_proxy_role_request: AssumeRoleRequest | None,
        region: RegionName,
        credentials: AWSCredentialsSet | None = None,
    ) -> None:
        if self.sts._client is None:
            await self.sts.connect(region=region, credentials=credentials)

        if assume_proxy_role_request is not None:
            response = await self.sts.assume_role_by_proxy(
                assume_role_request,
                assume_proxy_role_request,
                region,
            )
        else:
            response = await self.sts.assume_role(assume_role_request)

        if response.Credentials is None:
            raise RuntimeError('STS assume_role returned no credentials.')

        await self._connect_client(
            client=client,
            credentials=AWSCredentialsSet(
                aws_access_key_id=response.Credentials.AccessKeyId,
                aws_secret_access_key=response.Credentials.SecretAccessKey,
                aws_session_token=response.Credentials.SessionToken,
            ),
            region=region,
        )

    async def _connect_sso(
        self,
        client: SupportedClients,
        credentials: AWSCredentialsSet,
        region: RegionName | None = None,
    ) -> None:
        if not credentials.aws_profile:
            raise ValueError("credentials.aws_profile must be set for SSO connections.")
        service = self._get_service(client)
        await service.sso(credentials.aws_profile, region=region)

    async def _connect_client(
        self,
        client: SupportedClients,
        credentials: AWSCredentialsSet | None,
        region: RegionName,
    ) -> None:
        service = self._get_service(client)
        await service.connect(region=region, credentials=credentials)

    async def close(self) -> None:
        for service in list(self._clients.values()):
            await service.close()
        self._clients.clear()
        await self.credentials.close()
        await self.config.close()

    def abort(self) -> None:
        for service in list(self._clients.values()):
            service.abort()
        self._clients.clear()
        self.credentials.abort()
        self.config.abort()
