from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .cert_manager_client import ACMClient as ACMClient
    from .api_gateway_client import APIGatewayClient as APIGatewayClient
    from .api_gateway_v2_client import APIGatewayV2Client as APIGatewayV2Client
    from .iam_analyzer_client import AccessAnalyzerClient as AccessAnalyzerClient
    from .amplify_client import AmplifyClient as AmplifyClient
    from .app_flow_client import AppFlowClient as AppFlowClient
    from .app_runner_client import AppRunnerClient as AppRunnerClient
    from .app_stream_client import AppStreamClient as AppStreamClient
    from .app_sync_client import AppSyncClient as AppSyncClient
    from .athena_client import AthenaClient as AthenaClient
    from .audit_manager_client import AuditManagerClient as AuditManagerClient
    from .autoscaling_client import AutoScalingClient as AutoScalingClient
    from .backup_client import BackupClient as BackupClient
    from .batch_client import BatchClient as BatchClient
    from .bedrock_client import BedrockClient as BedrockClient
    from .bedrock_runtime_client import BedrockRuntimeClient as BedrockRuntimeClient
    from .cloud_formation_client import CloudFormationClient as CloudFormationClient
    from .cloudfront_client import CloudFrontClient as CloudFrontClient
    from .cloudhsm_client import CloudHSMClient as CloudHSMClient
    from .cloudsearch_client import CloudSearchClient as CloudSearchClient
    from .cloud_trail_client import CloudTrailClient as CloudTrailClient
    from .cloudwatch_client import CloudWatchClient as CloudWatchClient
    from .cloudwatch_logs_client import CloudWatchLogsClient as CloudWatchLogsClient
    from .codeartifact_client import CodeArtifactClient as CodeArtifactClient
    from .codeartifact_format import CodeArtifactFormat as CodeArtifactFormat
    from .codebuild_client import CodeBuildClient as CodeBuildClient
    from .codecatalyst_client import CodeCatalystClient as CodeCatalystClient
    from .codecommit_client import CodeCommitClient as CodeCommitClient
    from .codeguru_client import CodeGuruClient as CodeGuruClient
    from .codepipeline_client import CodePipelineClient as CodePipelineClient
    from .cognito_client import CognitoIDPClient as CognitoIDPClient
    from .cognito_sync_client import CognitoSyncClient as CognitoSyncClient
    from .comprehend_client import ComprehendClient as ComprehendClient
    from .compute_optimizer_client import ComputeOptimizerClient as ComputeOptimizerClient
    from .aws_config_client import ConfigServiceClient as ConfigServiceClient
    from .aws_connect_client import ConnectClient as ConnectClient
    from .cost_explorer_client import CostExplorerClient as CostExplorerClient
    from .dms_client import DMSClient as DMSClient
    from .data_pipeline_client import DataPipelineClient as DataPipelineClient
    from .datasync_client import DataSyncClient as DataSyncClient
    from .datazone_client import DataZoneClient as DataZoneClient
    from .detective_client import DetectiveClient as DetectiveClient
    from .devops_guru_client import DevOpsGuruClient as DevOpsGuruClient
    from .device_farm_client import DeviceFarmClient as DeviceFarmClient
    from .direct_connect_client import DirectConnectClient as DirectConnectClient
    from .directory_service_client import DirectoryServiceClient as DirectoryServiceClient
    from .documentdb_client import DocumentDBClient as DocumentDBClient
    from .dynamodb_client import DynamoDBClient as DynamoDBClient
    from .ebs_client import EBSClient as EBSClient
    from .ec2_client import EC2Client as EC2Client
    from .ecr_client import ECRClient as ECRClient
    from .ecr_public_client import ECRPublicClient as ECRPublicClient
    from .ecs_client import ECSClient as ECSClient
    from .efs_client import EFSClient as EFSClient
    from .eks_client import EKSClient as EKSClient
    from .elb_client import ELBv2Client as ELBv2Client
    from .emr_client import EMRClient as EMRClient
    from .elasticache_client import ElastiCacheClient as ElastiCacheClient
    from .eum_client import EndUserMessagingClient as EndUserMessagingClient
    from .cloudwatch_events_client import EventBridgeClient as EventBridgeClient
    from .fis_client import FISClient as FISClient
    from .firewall_client import FMSClient as FMSClient
    from .fsx_client import FSxClient as FSxClient
    from .kinesis_firehose_client import FirehoseClient as FirehoseClient
    from .glacier_client import GlacierClient as GlacierClient
    from .glue_client import GlueClient as GlueClient
    from .guardduty_client import GuardDutyClient as GuardDutyClient
    from .healthimaging_client import HealthImagingClient as HealthImagingClient
    from .iam_client import IAMClient as IAMClient
    from .workforce_id_client import IdentityStoreClient as IdentityStoreClient
    from .iot_client import IoTClient as IoTClient
    from .iot_dm_client import IoTJobsDataClient as IoTJobsDataClient
    from .kms_client import KMSClient as KMSClient
    from .kendra_client import KendraClient as KendraClient
    from .kinesis_analytics_client import KinesisAnalyticsClient as KinesisAnalyticsClient
    from .kinesis_client import KinesisClient as KinesisClient
    from .kinesis_vs_client import KinesisVideoClient as KinesisVideoClient
    from .lake_formation_client import LakeFormationClient as LakeFormationClient
    from .lambda_client import LambdaClient as LambdaClient
    from .lex_client import LexClient as LexClient
    from .lightsail_client import LightsailClient as LightsailClient
    from .location_service_client import LocationClient as LocationClient
    from .mq_client import MQClient as MQClient
    from .msk_client import MSKClient as MSKClient
    from .mwa_client import MWAAClient as MWAAClient
    from .macie_client import MacieClient as MacieClient
    from .managed_blockchain_client import ManagedBlockchainClient as ManagedBlockchainClient
    from .managed_grafana_client import ManagedGrafanaClient as ManagedGrafanaClient
    from .elemental_mediastore_client import MediaStoreClient as MediaStoreClient
    from .memorydb_client import MemoryDBClient as MemoryDBClient
    from .migration_hub_client import MigrationHubClient as MigrationHubClient
    from .neptune_client import NeptuneClient as NeptuneClient
    from .cloud_wan_client import NetworkManagerClient as NetworkManagerClient
    from .opensearch_client import OpenSearchClient as OpenSearchClient
    from .opensearch_serverless_client import OpenSearchServerlessClient as OpenSearchServerlessClient
    from .organizations_client import OrganizationsClient as OrganizationsClient
    from .personalize_client import PersonalizeClient as PersonalizeClient
    from .pinpoint_client import PinpointClient as PinpointClient
    from .polly_client import PollyClient as PollyClient
    from .q_business_client import QBusinessClient as QBusinessClient
    from .quicksight_client import QuickSightClient as QuickSightClient
    from .rds_client import RDSClient as RDSClient
    from .redshift_client import RedshiftClient as RedshiftClient
    from .rekognition_client import RekognitionClient as RekognitionClient
    from .resilience_hub_client import ResilienceHubClient as ResilienceHubClient
    from .route53_arc_client import Route53ARCClient as Route53ARCClient
    from .route53_client import Route53Client as Route53Client
    from .registrar_client import Route53DomainsClient as Route53DomainsClient
    from .ses_client import SESClient as SESClient
    from .sns_client import SNSClient as SNSClient
    from .sqs_client import SQSClient as SQSClient
    from .systems_manager_client import SSMClient as SSMClient
    from .sts_client import STSClient as STSClient
    from .sws_client import SWFClient as SWFClient
    from .sagemaker_client import SageMakerClient as SageMakerClient
    from .scheduler_client import SchedulerClient as SchedulerClient
    from .secrets_manager_client import SecretsManagerClient as SecretsManagerClient
    from .security_hub_client import SecurityHubClient as SecurityHubClient
    from .security_lake_client import SecurityLakeClient as SecurityLakeClient
    from .service_catalogue_client import ServiceCatalogClient as ServiceCatalogClient
    from .simpledb_client import SimpleDBClient as SimpleDBClient
    from .step_functions_client import StepFunctionsClient as StepFunctionsClient
    from .storage_gateway_client import StorageGatewayClient as StorageGatewayClient
    from .enterprise_support_client import SupportClient as SupportClient
    from .tax_client import TaxSettingsClient as TaxSettingsClient
    from .textract_client import TextractClient as TextractClient
    from .timestream_query_client import TimestreamQueryClient as TimestreamQueryClient
    from .timestream_client import TimestreamWriteClient as TimestreamWriteClient
    from .transcribe_client import TranscribeClient as TranscribeClient
    from .transfer_family_client import TransferClient as TransferClient
    from .translate_client import TranslateClient as TranslateClient
    from .verified_permissions_client import VerifiedPermissionsClient as VerifiedPermissionsClient
    from .waf_client import WAFv2Client as WAFv2Client
    from .workspaces_client import WorkSpacesClient as WorkSpacesClient
    from .workspaces_tc_client import WorkSpacesThinClientClient as WorkSpacesThinClientClient
    from .xray_client import XRayClient as XRayClient
    from .s3_client import s3Client as s3Client
    from .s3_multipart_upload_part import s3MultipartUploadPart as s3MultipartUploadPart
    from .s3_tag import s3Tag as s3Tag

_TYPE_EXPORTS: dict[str, tuple[str, str]] = {
    'ACMClient': ('.cert_manager_client', 'ACMClient'),
    'APIGatewayClient': ('.api_gateway_client', 'APIGatewayClient'),
    'APIGatewayV2Client': ('.api_gateway_v2_client', 'APIGatewayV2Client'),
    'AccessAnalyzerClient': ('.iam_analyzer_client', 'AccessAnalyzerClient'),
    'AmplifyClient': ('.amplify_client', 'AmplifyClient'),
    'AppFlowClient': ('.app_flow_client', 'AppFlowClient'),
    'AppRunnerClient': ('.app_runner_client', 'AppRunnerClient'),
    'AppStreamClient': ('.app_stream_client', 'AppStreamClient'),
    'AppSyncClient': ('.app_sync_client', 'AppSyncClient'),
    'AthenaClient': ('.athena_client', 'AthenaClient'),
    'AuditManagerClient': ('.audit_manager_client', 'AuditManagerClient'),
    'AutoScalingClient': ('.autoscaling_client', 'AutoScalingClient'),
    'BackupClient': ('.backup_client', 'BackupClient'),
    'BatchClient': ('.batch_client', 'BatchClient'),
    'BedrockClient': ('.bedrock_client', 'BedrockClient'),
    'BedrockRuntimeClient': ('.bedrock_runtime_client', 'BedrockRuntimeClient'),
    'CloudFormationClient': ('.cloud_formation_client', 'CloudFormationClient'),
    'CloudFrontClient': ('.cloudfront_client', 'CloudFrontClient'),
    'CloudHSMClient': ('.cloudhsm_client', 'CloudHSMClient'),
    'CloudSearchClient': ('.cloudsearch_client', 'CloudSearchClient'),
    'CloudTrailClient': ('.cloud_trail_client', 'CloudTrailClient'),
    'CloudWatchClient': ('.cloudwatch_client', 'CloudWatchClient'),
    'CloudWatchLogsClient': ('.cloudwatch_logs_client', 'CloudWatchLogsClient'),
    'CodeArtifactClient': ('.codeartifact_client', 'CodeArtifactClient'),
    'CodeArtifactFormat': ('.codeartifact_format', 'CodeArtifactFormat'),
    'CodeBuildClient': ('.codebuild_client', 'CodeBuildClient'),
    'CodeCatalystClient': ('.codecatalyst_client', 'CodeCatalystClient'),
    'CodeCommitClient': ('.codecommit_client', 'CodeCommitClient'),
    'CodeGuruClient': ('.codeguru_client', 'CodeGuruClient'),
    'CodePipelineClient': ('.codepipeline_client', 'CodePipelineClient'),
    'CognitoIDPClient': ('.cognito_client', 'CognitoIDPClient'),
    'CognitoSyncClient': ('.cognito_sync_client', 'CognitoSyncClient'),
    'ComprehendClient': ('.comprehend_client', 'ComprehendClient'),
    'ComputeOptimizerClient': ('.compute_optimizer_client', 'ComputeOptimizerClient'),
    'ConfigServiceClient': ('.aws_config_client', 'ConfigServiceClient'),
    'ConnectClient': ('.aws_connect_client', 'ConnectClient'),
    'CostExplorerClient': ('.cost_explorer_client', 'CostExplorerClient'),
    'DMSClient': ('.dms_client', 'DMSClient'),
    'DataPipelineClient': ('.data_pipeline_client', 'DataPipelineClient'),
    'DataSyncClient': ('.datasync_client', 'DataSyncClient'),
    'DataZoneClient': ('.datazone_client', 'DataZoneClient'),
    'DetectiveClient': ('.detective_client', 'DetectiveClient'),
    'DevOpsGuruClient': ('.devops_guru_client', 'DevOpsGuruClient'),
    'DeviceFarmClient': ('.device_farm_client', 'DeviceFarmClient'),
    'DirectConnectClient': ('.direct_connect_client', 'DirectConnectClient'),
    'DirectoryServiceClient': ('.directory_service_client', 'DirectoryServiceClient'),
    'DocumentDBClient': ('.documentdb_client', 'DocumentDBClient'),
    'DynamoDBClient': ('.dynamodb_client', 'DynamoDBClient'),
    'EBSClient': ('.ebs_client', 'EBSClient'),
    'EC2Client': ('.ec2_client', 'EC2Client'),
    'ECRClient': ('.ecr_client', 'ECRClient'),
    'ECRPublicClient': ('.ecr_public_client', 'ECRPublicClient'),
    'ECSClient': ('.ecs_client', 'ECSClient'),
    'EFSClient': ('.efs_client', 'EFSClient'),
    'EKSClient': ('.eks_client', 'EKSClient'),
    'ELBv2Client': ('.elb_client', 'ELBv2Client'),
    'EMRClient': ('.emr_client', 'EMRClient'),
    'ElastiCacheClient': ('.elasticache_client', 'ElastiCacheClient'),
    'EndUserMessagingClient': ('.eum_client', 'EndUserMessagingClient'),
    'EventBridgeClient': ('.cloudwatch_events_client', 'EventBridgeClient'),
    'FISClient': ('.fis_client', 'FISClient'),
    'FMSClient': ('.firewall_client', 'FMSClient'),
    'FSxClient': ('.fsx_client', 'FSxClient'),
    'FirehoseClient': ('.kinesis_firehose_client', 'FirehoseClient'),
    'GlacierClient': ('.glacier_client', 'GlacierClient'),
    'GlueClient': ('.glue_client', 'GlueClient'),
    'GuardDutyClient': ('.guardduty_client', 'GuardDutyClient'),
    'HealthImagingClient': ('.healthimaging_client', 'HealthImagingClient'),
    'IAMClient': ('.iam_client', 'IAMClient'),
    'IdentityStoreClient': ('.workforce_id_client', 'IdentityStoreClient'),
    'IoTClient': ('.iot_client', 'IoTClient'),
    'IoTJobsDataClient': ('.iot_dm_client', 'IoTJobsDataClient'),
    'KMSClient': ('.kms_client', 'KMSClient'),
    'KendraClient': ('.kendra_client', 'KendraClient'),
    'KinesisAnalyticsClient': ('.kinesis_analytics_client', 'KinesisAnalyticsClient'),
    'KinesisClient': ('.kinesis_client', 'KinesisClient'),
    'KinesisVideoClient': ('.kinesis_vs_client', 'KinesisVideoClient'),
    'LakeFormationClient': ('.lake_formation_client', 'LakeFormationClient'),
    'LambdaClient': ('.lambda_client', 'LambdaClient'),
    'LexClient': ('.lex_client', 'LexClient'),
    'LightsailClient': ('.lightsail_client', 'LightsailClient'),
    'LocationClient': ('.location_service_client', 'LocationClient'),
    'MQClient': ('.mq_client', 'MQClient'),
    'MSKClient': ('.msk_client', 'MSKClient'),
    'MWAAClient': ('.mwa_client', 'MWAAClient'),
    'MacieClient': ('.macie_client', 'MacieClient'),
    'ManagedBlockchainClient': ('.managed_blockchain_client', 'ManagedBlockchainClient'),
    'ManagedGrafanaClient': ('.managed_grafana_client', 'ManagedGrafanaClient'),
    'MediaStoreClient': ('.elemental_mediastore_client', 'MediaStoreClient'),
    'MemoryDBClient': ('.memorydb_client', 'MemoryDBClient'),
    'MigrationHubClient': ('.migration_hub_client', 'MigrationHubClient'),
    'NeptuneClient': ('.neptune_client', 'NeptuneClient'),
    'NetworkManagerClient': ('.cloud_wan_client', 'NetworkManagerClient'),
    'OpenSearchClient': ('.opensearch_client', 'OpenSearchClient'),
    'OpenSearchServerlessClient': ('.opensearch_serverless_client', 'OpenSearchServerlessClient'),
    'OrganizationsClient': ('.organizations_client', 'OrganizationsClient'),
    'PersonalizeClient': ('.personalize_client', 'PersonalizeClient'),
    'PinpointClient': ('.pinpoint_client', 'PinpointClient'),
    'PollyClient': ('.polly_client', 'PollyClient'),
    'QBusinessClient': ('.q_business_client', 'QBusinessClient'),
    'QuickSightClient': ('.quicksight_client', 'QuickSightClient'),
    'RDSClient': ('.rds_client', 'RDSClient'),
    'RedshiftClient': ('.redshift_client', 'RedshiftClient'),
    'RekognitionClient': ('.rekognition_client', 'RekognitionClient'),
    'ResilienceHubClient': ('.resilience_hub_client', 'ResilienceHubClient'),
    'Route53ARCClient': ('.route53_arc_client', 'Route53ARCClient'),
    'Route53Client': ('.route53_client', 'Route53Client'),
    'Route53DomainsClient': ('.registrar_client', 'Route53DomainsClient'),
    'SESClient': ('.ses_client', 'SESClient'),
    'SNSClient': ('.sns_client', 'SNSClient'),
    'SQSClient': ('.sqs_client', 'SQSClient'),
    'SSMClient': ('.systems_manager_client', 'SSMClient'),
    'STSClient': ('.sts_client', 'STSClient'),
    'SWFClient': ('.sws_client', 'SWFClient'),
    'SageMakerClient': ('.sagemaker_client', 'SageMakerClient'),
    'SchedulerClient': ('.scheduler_client', 'SchedulerClient'),
    'SecretsManagerClient': ('.secrets_manager_client', 'SecretsManagerClient'),
    'SecurityHubClient': ('.security_hub_client', 'SecurityHubClient'),
    'SecurityLakeClient': ('.security_lake_client', 'SecurityLakeClient'),
    'ServiceCatalogClient': ('.service_catalogue_client', 'ServiceCatalogClient'),
    'SimpleDBClient': ('.simpledb_client', 'SimpleDBClient'),
    'StepFunctionsClient': ('.step_functions_client', 'StepFunctionsClient'),
    'StorageGatewayClient': ('.storage_gateway_client', 'StorageGatewayClient'),
    'SupportClient': ('.enterprise_support_client', 'SupportClient'),
    'TaxSettingsClient': ('.tax_client', 'TaxSettingsClient'),
    'TextractClient': ('.textract_client', 'TextractClient'),
    'TimestreamQueryClient': ('.timestream_query_client', 'TimestreamQueryClient'),
    'TimestreamWriteClient': ('.timestream_client', 'TimestreamWriteClient'),
    'TranscribeClient': ('.transcribe_client', 'TranscribeClient'),
    'TransferClient': ('.transfer_family_client', 'TransferClient'),
    'TranslateClient': ('.translate_client', 'TranslateClient'),
    'VerifiedPermissionsClient': ('.verified_permissions_client', 'VerifiedPermissionsClient'),
    'WAFv2Client': ('.waf_client', 'WAFv2Client'),
    'WorkSpacesClient': ('.workspaces_client', 'WorkSpacesClient'),
    'WorkSpacesThinClientClient': ('.workspaces_tc_client', 'WorkSpacesThinClientClient'),
    'XRayClient': ('.xray_client', 'XRayClient'),
    's3Client': ('.s3_client', 's3Client'),
    's3MultipartUploadPart': ('.s3_multipart_upload_part', 's3MultipartUploadPart'),
    's3Tag': ('.s3_tag', 's3Tag'),
}

__all__ = sorted(_TYPE_EXPORTS.keys())


def __getattr__(name: str) -> Any:
    target = _TYPE_EXPORTS.get(name)
    if target is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module_name, attr_name = target
    module = importlib.import_module(module_name, __name__)
    value = getattr(module, attr_name)
    globals()[name] = value
    return value
