from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .aws_cert_manager import AWSACM as AWSACM
    from .aws_api_gateway import AWSAPIGateway as AWSAPIGateway
    from .aws_api_gateway_v2 import AWSAPIGatewayV2 as AWSAPIGatewayV2
    from .aws_iam_analyzer import AWSAccessAnalyzer as AWSAccessAnalyzer
    from .aws_amplify import AWSAmplify as AWSAmplify
    from .aws_app_flow import AWSAppFlow as AWSAppFlow
    from .aws_app_runner import AWSAppRunner as AWSAppRunner
    from .aws_app_stream import AWSAppStream as AWSAppStream
    from .aws_app_sync import AWSAppSync as AWSAppSync
    from .aws_athena import AWSAthena as AWSAthena
    from .aws_audit_manager import AWSAuditManager as AWSAuditManager
    from .aws_autoscaling import AWSAutoScaling as AWSAutoScaling
    from .aws_backup import AWSBackup as AWSBackup
    from .base import AWSBaseService as AWSBaseService
    from .aws_batch import AWSBatch as AWSBatch
    from .aws_bedrock import AWSBedrock as AWSBedrock
    from .aws_bedrock_runtime import AWSBedrockRuntime as AWSBedrockRuntime
    from .aws_cloud_formation import AWSCloudFormation as AWSCloudFormation
    from .aws_cloudfront import AWSCloudFront as AWSCloudFront
    from .aws_cloudhsm import AWSCloudHSM as AWSCloudHSM
    from .aws_cloudsearch import AWSCloudSearch as AWSCloudSearch
    from .aws_cloud_trail import AWSCloudTrail as AWSCloudTrail
    from .aws_cloudwatch_logs import AWSCloudWatchLogs as AWSCloudWatchLogs
    from .aws_cloudwatch import AWSCloudwatch as AWSCloudwatch
    from .aws_codeartifact import AWSCodeArtifact as AWSCodeArtifact
    from .aws_codebuild import AWSCodeBuild as AWSCodeBuild
    from .aws_codecatalyst import AWSCodeCatalyst as AWSCodeCatalyst
    from .aws_codecommit import AWSCodeCommit as AWSCodeCommit
    from .aws_codeguru import AWSCodeGuru as AWSCodeGuru
    from .aws_codepipeline import AWSCodePipeline as AWSCodePipeline
    from .aws_cognito import AWSCognitoIDP as AWSCognitoIDP
    from .aws_cognito_sync import AWSCognitoSync as AWSCognitoSync
    from .aws_comprehend import AWSComprehend as AWSComprehend
    from .aws_compute_optimizer import AWSComputeOptimizer as AWSComputeOptimizer
    from .aws_aws_config import AWSConfigService as AWSConfigService
    from .aws_aws_connect import AWSConnect as AWSConnect
    from .aws_cost_explorer import AWSCostExplorer as AWSCostExplorer
    from .aws_credentials import AWSCredentials as AWSCredentials
    from .aws_dms import AWSDMS as AWSDMS
    from .aws_data_pipeline import AWSDataPipeline as AWSDataPipeline
    from .aws_datasync import AWSDataSync as AWSDataSync
    from .aws_datazone import AWSDataZone as AWSDataZone
    from .aws_detective import AWSDetective as AWSDetective
    from .aws_devops_guru import AWSDevOpsGuru as AWSDevOpsGuru
    from .aws_device_farm import AWSDeviceFarm as AWSDeviceFarm
    from .aws_direct_connect import AWSDirectConnect as AWSDirectConnect
    from .aws_directory_service import AWSDirectoryService as AWSDirectoryService
    from .aws_documentdb import AWSDocumentDB as AWSDocumentDB
    from .aws_dynamodb import AWSDynamoDB as AWSDynamoDB
    from .aws_ec2 import AWSEC2 as AWSEC2
    from .aws_ecr import AWSECR as AWSECR
    from .aws_ecr_public import AWSECRPublic as AWSECRPublic
    from .aws_ecs import AWSECS as AWSECS
    from .aws_efs import AWSEFS as AWSEFS
    from .aws_eks import AWSEKS as AWSEKS
    from .aws_elb import AWSELBv2 as AWSELBv2
    from .aws_emr import AWSEMR as AWSEMR
    from .aws_elasticache import AWSElastiCache as AWSElastiCache
    from .aws_elastic_block_storage import AWSElasticBlockStorage as AWSElasticBlockStorage
    from .aws_eum import AWSEndUserMessaging as AWSEndUserMessaging
    from .aws_cloudwatch_events import AWSEventBridge as AWSEventBridge
    from .aws_fis import AWSFIS as AWSFIS
    from .aws_firewall import AWSFMS as AWSFMS
    from .aws_fsx import AWSFSx as AWSFSx
    from .aws_kinesis_firehose import AWSFirehose as AWSFirehose
    from .aws_glacier import AWSGlacier as AWSGlacier
    from .aws_glue import AWSGlue as AWSGlue
    from .aws_guardduty import AWSGuardDuty as AWSGuardDuty
    from .aws_healthimaging import AWSHealthImaging as AWSHealthImaging
    from .aws_iam import AWSIAM as AWSIAM
    from .aws_workforce_id import AWSIdentityStore as AWSIdentityStore
    from .aws_iot import AWSIoT as AWSIoT
    from .aws_iot_dm import AWSIoTJobsData as AWSIoTJobsData
    from .aws_kms import AWSKMS as AWSKMS
    from .aws_kendra import AWSKendra as AWSKendra
    from .aws_kinesis import AWSKinesis as AWSKinesis
    from .aws_kinesis_analytics import AWSKinesisAnalytics as AWSKinesisAnalytics
    from .aws_kinesis_vs import AWSKinesisVideo as AWSKinesisVideo
    from .aws_lake_formation import AWSLakeFormation as AWSLakeFormation
    from .aws_lambda import AWSLambda as AWSLambda
    from .aws_lex import AWSLex as AWSLex
    from .aws_lightsail import AWSLightsail as AWSLightsail
    from .aws_location_service import AWSLocation as AWSLocation
    from .aws_mq import AWSMQ as AWSMQ
    from .aws_msk import AWSMSK as AWSMSK
    from .aws_mwa import AWSMWAA as AWSMWAA
    from .aws_macie import AWSMacie as AWSMacie
    from .aws_managed_blockchain import AWSManagedBlockchain as AWSManagedBlockchain
    from .aws_managed_grafana import AWSManagedGrafana as AWSManagedGrafana
    from .aws_elemental_mediastore import AWSMediaStore as AWSMediaStore
    from .aws_memorydb import AWSMemoryDB as AWSMemoryDB
    from .aws_migration_hub import AWSMigrationHub as AWSMigrationHub
    from .aws_neptune import AWSNeptune as AWSNeptune
    from .aws_cloud_wan import AWSNetworkManager as AWSNetworkManager
    from .aws_opensearch import AWSOpenSearch as AWSOpenSearch
    from .aws_opensearch_serverless import AWSOpenSearchServerless as AWSOpenSearchServerless
    from .aws_organizations import AWSOrganizations as AWSOrganizations
    from .aws_personalize import AWSPersonalize as AWSPersonalize
    from .aws_pinpoint import AWSPinpoint as AWSPinpoint
    from .aws_polly import AWSPolly as AWSPolly
    from .aws_q_business import AWSQBusiness as AWSQBusiness
    from .aws_quicksight import AWSQuickSight as AWSQuickSight
    from .aws_rds import AWSRDS as AWSRDS
    from .aws_redshift import AWSRedshift as AWSRedshift
    from .aws_rekognition import AWSRekognition as AWSRekognition
    from .aws_resilience_hub import AWSResilienceHub as AWSResilienceHub
    from .aws_route53 import AWSRoute53 as AWSRoute53
    from .aws_route53_arc import AWSRoute53ARC as AWSRoute53ARC
    from .aws_registrar import AWSRoute53Domains as AWSRoute53Domains
    from .aws_ses import AWSSES as AWSSES
    from .aws_sns import AWSSNS as AWSSNS
    from .aws_sqs import AWSSQS as AWSSQS
    from .aws_systems_manager import AWSSSM as AWSSSM
    from .aws_sts import AWSSTS as AWSSTS
    from .aws_sws import AWSSWF as AWSSWF
    from .aws_sagemaker import AWSSageMaker as AWSSageMaker
    from .aws_scheduler import AWSScheduler as AWSScheduler
    from .aws_secrets_manager import AWSSecretsManager as AWSSecretsManager
    from .aws_security_hub import AWSSecurityHub as AWSSecurityHub
    from .aws_security_lake import AWSSecurityLake as AWSSecurityLake
    from .aws_service_catalogue import AWSServiceCatalog as AWSServiceCatalog
    from .aws_simpledb import AWSSimpleDB as AWSSimpleDB
    from .aws_step_functions import AWSStepFunctions as AWSStepFunctions
    from .aws_storage_gateway import AWSStorageGateway as AWSStorageGateway
    from .aws_enterprise_support import AWSSupport as AWSSupport
    from .aws_tax import AWSTaxSettings as AWSTaxSettings
    from .aws_textract import AWSTextract as AWSTextract
    from .aws_timestream_query import AWSTimestreamQuery as AWSTimestreamQuery
    from .aws_timestream import AWSTimestreamWrite as AWSTimestreamWrite
    from .aws_transcribe import AWSTranscribe as AWSTranscribe
    from .aws_transfer_family import AWSTransfer as AWSTransfer
    from .aws_translate import AWSTranslate as AWSTranslate
    from .aws_verified_permissions import AWSVerifiedPermissions as AWSVerifiedPermissions
    from .aws_waf import AWSWAFv2 as AWSWAFv2
    from .aws_workspaces import AWSWorkSpaces as AWSWorkSpaces
    from .aws_workspaces_tc import AWSWorkSpacesThinClient as AWSWorkSpacesThinClient
    from .aws_xray import AWSXRay as AWSXRay
    from .aws_s3 import AWSs3 as AWSs3

_SERVICE_EXPORTS: dict[str, tuple[str, str]] = {
    'AWSACM': ('.aws_cert_manager', 'AWSACM'),
    'AWSAPIGateway': ('.aws_api_gateway', 'AWSAPIGateway'),
    'AWSAPIGatewayV2': ('.aws_api_gateway_v2', 'AWSAPIGatewayV2'),
    'AWSAccessAnalyzer': ('.aws_iam_analyzer', 'AWSAccessAnalyzer'),
    'AWSAmplify': ('.aws_amplify', 'AWSAmplify'),
    'AWSAppFlow': ('.aws_app_flow', 'AWSAppFlow'),
    'AWSAppRunner': ('.aws_app_runner', 'AWSAppRunner'),
    'AWSAppStream': ('.aws_app_stream', 'AWSAppStream'),
    'AWSAppSync': ('.aws_app_sync', 'AWSAppSync'),
    'AWSAthena': ('.aws_athena', 'AWSAthena'),
    'AWSAuditManager': ('.aws_audit_manager', 'AWSAuditManager'),
    'AWSAutoScaling': ('.aws_autoscaling', 'AWSAutoScaling'),
    'AWSBackup': ('.aws_backup', 'AWSBackup'),
    'AWSBaseService': ('.base', 'AWSBaseService'),
    'AWSBatch': ('.aws_batch', 'AWSBatch'),
    'AWSBedrock': ('.aws_bedrock', 'AWSBedrock'),
    'AWSBedrockRuntime': ('.aws_bedrock_runtime', 'AWSBedrockRuntime'),
    'AWSCloudFormation': ('.aws_cloud_formation', 'AWSCloudFormation'),
    'AWSCloudFront': ('.aws_cloudfront', 'AWSCloudFront'),
    'AWSCloudHSM': ('.aws_cloudhsm', 'AWSCloudHSM'),
    'AWSCloudSearch': ('.aws_cloudsearch', 'AWSCloudSearch'),
    'AWSCloudTrail': ('.aws_cloud_trail', 'AWSCloudTrail'),
    'AWSCloudWatchLogs': ('.aws_cloudwatch_logs', 'AWSCloudWatchLogs'),
    'AWSCloudwatch': ('.aws_cloudwatch', 'AWSCloudwatch'),
    'AWSCodeArtifact': ('.aws_codeartifact', 'AWSCodeArtifact'),
    'AWSCodeBuild': ('.aws_codebuild', 'AWSCodeBuild'),
    'AWSCodeCatalyst': ('.aws_codecatalyst', 'AWSCodeCatalyst'),
    'AWSCodeCommit': ('.aws_codecommit', 'AWSCodeCommit'),
    'AWSCodeGuru': ('.aws_codeguru', 'AWSCodeGuru'),
    'AWSCodePipeline': ('.aws_codepipeline', 'AWSCodePipeline'),
    'AWSCognitoIDP': ('.aws_cognito', 'AWSCognitoIDP'),
    'AWSCognitoSync': ('.aws_cognito_sync', 'AWSCognitoSync'),
    'AWSComprehend': ('.aws_comprehend', 'AWSComprehend'),
    'AWSComputeOptimizer': ('.aws_compute_optimizer', 'AWSComputeOptimizer'),
    'AWSConfigService': ('.aws_aws_config', 'AWSConfigService'),
    'AWSConnect': ('.aws_aws_connect', 'AWSConnect'),
    'AWSCostExplorer': ('.aws_cost_explorer', 'AWSCostExplorer'),
    'AWSCredentials': ('.aws_credentials', 'AWSCredentials'),
    'AWSDMS': ('.aws_dms', 'AWSDMS'),
    'AWSDataPipeline': ('.aws_data_pipeline', 'AWSDataPipeline'),
    'AWSDataSync': ('.aws_datasync', 'AWSDataSync'),
    'AWSDataZone': ('.aws_datazone', 'AWSDataZone'),
    'AWSDetective': ('.aws_detective', 'AWSDetective'),
    'AWSDevOpsGuru': ('.aws_devops_guru', 'AWSDevOpsGuru'),
    'AWSDeviceFarm': ('.aws_device_farm', 'AWSDeviceFarm'),
    'AWSDirectConnect': ('.aws_direct_connect', 'AWSDirectConnect'),
    'AWSDirectoryService': ('.aws_directory_service', 'AWSDirectoryService'),
    'AWSDocumentDB': ('.aws_documentdb', 'AWSDocumentDB'),
    'AWSDynamoDB': ('.aws_dynamodb', 'AWSDynamoDB'),
    'AWSEC2': ('.aws_ec2', 'AWSEC2'),
    'AWSECR': ('.aws_ecr', 'AWSECR'),
    'AWSECRPublic': ('.aws_ecr_public', 'AWSECRPublic'),
    'AWSECS': ('.aws_ecs', 'AWSECS'),
    'AWSEFS': ('.aws_efs', 'AWSEFS'),
    'AWSEKS': ('.aws_eks', 'AWSEKS'),
    'AWSELBv2': ('.aws_elb', 'AWSELBv2'),
    'AWSEMR': ('.aws_emr', 'AWSEMR'),
    'AWSElastiCache': ('.aws_elasticache', 'AWSElastiCache'),
    'AWSElasticBlockStorage': ('.aws_elastic_block_storage', 'AWSElasticBlockStorage'),
    'AWSEndUserMessaging': ('.aws_eum', 'AWSEndUserMessaging'),
    'AWSEventBridge': ('.aws_cloudwatch_events', 'AWSEventBridge'),
    'AWSFIS': ('.aws_fis', 'AWSFIS'),
    'AWSFMS': ('.aws_firewall', 'AWSFMS'),
    'AWSFSx': ('.aws_fsx', 'AWSFSx'),
    'AWSFirehose': ('.aws_kinesis_firehose', 'AWSFirehose'),
    'AWSGlacier': ('.aws_glacier', 'AWSGlacier'),
    'AWSGlue': ('.aws_glue', 'AWSGlue'),
    'AWSGuardDuty': ('.aws_guardduty', 'AWSGuardDuty'),
    'AWSHealthImaging': ('.aws_healthimaging', 'AWSHealthImaging'),
    'AWSIAM': ('.aws_iam', 'AWSIAM'),
    'AWSIdentityStore': ('.aws_workforce_id', 'AWSIdentityStore'),
    'AWSIoT': ('.aws_iot', 'AWSIoT'),
    'AWSIoTJobsData': ('.aws_iot_dm', 'AWSIoTJobsData'),
    'AWSKMS': ('.aws_kms', 'AWSKMS'),
    'AWSKendra': ('.aws_kendra', 'AWSKendra'),
    'AWSKinesis': ('.aws_kinesis', 'AWSKinesis'),
    'AWSKinesisAnalytics': ('.aws_kinesis_analytics', 'AWSKinesisAnalytics'),
    'AWSKinesisVideo': ('.aws_kinesis_vs', 'AWSKinesisVideo'),
    'AWSLakeFormation': ('.aws_lake_formation', 'AWSLakeFormation'),
    'AWSLambda': ('.aws_lambda', 'AWSLambda'),
    'AWSLex': ('.aws_lex', 'AWSLex'),
    'AWSLightsail': ('.aws_lightsail', 'AWSLightsail'),
    'AWSLocation': ('.aws_location_service', 'AWSLocation'),
    'AWSMQ': ('.aws_mq', 'AWSMQ'),
    'AWSMSK': ('.aws_msk', 'AWSMSK'),
    'AWSMWAA': ('.aws_mwa', 'AWSMWAA'),
    'AWSMacie': ('.aws_macie', 'AWSMacie'),
    'AWSManagedBlockchain': ('.aws_managed_blockchain', 'AWSManagedBlockchain'),
    'AWSManagedGrafana': ('.aws_managed_grafana', 'AWSManagedGrafana'),
    'AWSMediaStore': ('.aws_elemental_mediastore', 'AWSMediaStore'),
    'AWSMemoryDB': ('.aws_memorydb', 'AWSMemoryDB'),
    'AWSMigrationHub': ('.aws_migration_hub', 'AWSMigrationHub'),
    'AWSNeptune': ('.aws_neptune', 'AWSNeptune'),
    'AWSNetworkManager': ('.aws_cloud_wan', 'AWSNetworkManager'),
    'AWSOpenSearch': ('.aws_opensearch', 'AWSOpenSearch'),
    'AWSOpenSearchServerless': ('.aws_opensearch_serverless', 'AWSOpenSearchServerless'),
    'AWSOrganizations': ('.aws_organizations', 'AWSOrganizations'),
    'AWSPersonalize': ('.aws_personalize', 'AWSPersonalize'),
    'AWSPinpoint': ('.aws_pinpoint', 'AWSPinpoint'),
    'AWSPolly': ('.aws_polly', 'AWSPolly'),
    'AWSQBusiness': ('.aws_q_business', 'AWSQBusiness'),
    'AWSQuickSight': ('.aws_quicksight', 'AWSQuickSight'),
    'AWSRDS': ('.aws_rds', 'AWSRDS'),
    'AWSRedshift': ('.aws_redshift', 'AWSRedshift'),
    'AWSRekognition': ('.aws_rekognition', 'AWSRekognition'),
    'AWSResilienceHub': ('.aws_resilience_hub', 'AWSResilienceHub'),
    'AWSRoute53': ('.aws_route53', 'AWSRoute53'),
    'AWSRoute53ARC': ('.aws_route53_arc', 'AWSRoute53ARC'),
    'AWSRoute53Domains': ('.aws_registrar', 'AWSRoute53Domains'),
    'AWSSES': ('.aws_ses', 'AWSSES'),
    'AWSSNS': ('.aws_sns', 'AWSSNS'),
    'AWSSQS': ('.aws_sqs', 'AWSSQS'),
    'AWSSSM': ('.aws_systems_manager', 'AWSSSM'),
    'AWSSTS': ('.aws_sts', 'AWSSTS'),
    'AWSSWF': ('.aws_sws', 'AWSSWF'),
    'AWSSageMaker': ('.aws_sagemaker', 'AWSSageMaker'),
    'AWSScheduler': ('.aws_scheduler', 'AWSScheduler'),
    'AWSSecretsManager': ('.aws_secrets_manager', 'AWSSecretsManager'),
    'AWSSecurityHub': ('.aws_security_hub', 'AWSSecurityHub'),
    'AWSSecurityLake': ('.aws_security_lake', 'AWSSecurityLake'),
    'AWSServiceCatalog': ('.aws_service_catalogue', 'AWSServiceCatalog'),
    'AWSSimpleDB': ('.aws_simpledb', 'AWSSimpleDB'),
    'AWSStepFunctions': ('.aws_step_functions', 'AWSStepFunctions'),
    'AWSStorageGateway': ('.aws_storage_gateway', 'AWSStorageGateway'),
    'AWSSupport': ('.aws_enterprise_support', 'AWSSupport'),
    'AWSTaxSettings': ('.aws_tax', 'AWSTaxSettings'),
    'AWSTextract': ('.aws_textract', 'AWSTextract'),
    'AWSTimestreamQuery': ('.aws_timestream_query', 'AWSTimestreamQuery'),
    'AWSTimestreamWrite': ('.aws_timestream', 'AWSTimestreamWrite'),
    'AWSTranscribe': ('.aws_transcribe', 'AWSTranscribe'),
    'AWSTransfer': ('.aws_transfer_family', 'AWSTransfer'),
    'AWSTranslate': ('.aws_translate', 'AWSTranslate'),
    'AWSVerifiedPermissions': ('.aws_verified_permissions', 'AWSVerifiedPermissions'),
    'AWSWAFv2': ('.aws_waf', 'AWSWAFv2'),
    'AWSWorkSpaces': ('.aws_workspaces', 'AWSWorkSpaces'),
    'AWSWorkSpacesThinClient': ('.aws_workspaces_tc', 'AWSWorkSpacesThinClient'),
    'AWSXRay': ('.aws_xray', 'AWSXRay'),
    'AWSs3': ('.aws_s3', 'AWSs3'),
}

__all__ = sorted(_SERVICE_EXPORTS.keys())


def __getattr__(name: str) -> Any:
    target = _SERVICE_EXPORTS.get(name)
    if target is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module_name, attr_name = target
    module = importlib.import_module(module_name, __name__)
    value = getattr(module, attr_name)
    globals()[name] = value
    return value
