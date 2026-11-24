from werkflow_aws.models.kinesis_analytics import (
    KinesisAnalyticsAddApplicationCloudWatchLoggingOptionRequest,
    KinesisAnalyticsAddApplicationCloudWatchLoggingOptionResponse,
    KinesisAnalyticsAddApplicationInputProcessingConfigurationRequest,
    KinesisAnalyticsAddApplicationInputProcessingConfigurationResponse,
    KinesisAnalyticsAddApplicationInputRequest,
    KinesisAnalyticsAddApplicationInputResponse,
    KinesisAnalyticsAddApplicationOutputRequest,
    KinesisAnalyticsAddApplicationOutputResponse,
    KinesisAnalyticsAddApplicationReferenceDataSourceRequest,
    KinesisAnalyticsAddApplicationReferenceDataSourceResponse,
    KinesisAnalyticsAddApplicationVpcConfigurationRequest,
    KinesisAnalyticsAddApplicationVpcConfigurationResponse,
    KinesisAnalyticsCreateApplicationPresignedUrlRequest,
    KinesisAnalyticsCreateApplicationPresignedUrlResponse,
    KinesisAnalyticsCreateApplicationRequest,
    KinesisAnalyticsCreateApplicationResponse,
    KinesisAnalyticsCreateApplicationSnapshotRequest,
    KinesisAnalyticsCreateApplicationSnapshotResponse,
    KinesisAnalyticsCreateSnapshotRequest,
    KinesisAnalyticsCreateSnapshotResponse,
    KinesisAnalyticsDeleteApplicationCloudWatchLoggingOptionRequest,
    KinesisAnalyticsDeleteApplicationCloudWatchLoggingOptionResponse,
    KinesisAnalyticsDeleteApplicationInputProcessingConfigurationRequest,
    KinesisAnalyticsDeleteApplicationInputProcessingConfigurationResponse,
    KinesisAnalyticsDeleteApplicationOutputRequest,
    KinesisAnalyticsDeleteApplicationOutputResponse,
    KinesisAnalyticsDeleteApplicationReferenceDataSourceRequest,
    KinesisAnalyticsDeleteApplicationReferenceDataSourceResponse,
    KinesisAnalyticsDeleteApplicationRequest,
    KinesisAnalyticsDeleteApplicationResponse,
    KinesisAnalyticsDeleteApplicationSnapshotRequest,
    KinesisAnalyticsDeleteApplicationSnapshotResponse,
    KinesisAnalyticsDeleteApplicationVpcConfigurationRequest,
    KinesisAnalyticsDeleteApplicationVpcConfigurationResponse,
    KinesisAnalyticsDeleteSnapshotRequest,
    KinesisAnalyticsDeleteSnapshotResponse,
    KinesisAnalyticsDescribeApplicationOperationRequest,
    KinesisAnalyticsDescribeApplicationOperationResponse,
    KinesisAnalyticsDescribeApplicationRequest,
    KinesisAnalyticsDescribeApplicationResponse,
    KinesisAnalyticsDescribeApplicationSnapshotRequest,
    KinesisAnalyticsDescribeApplicationSnapshotResponse,
    KinesisAnalyticsDescribeApplicationVersionRequest,
    KinesisAnalyticsDescribeApplicationVersionResponse,
    KinesisAnalyticsDescribeSnapshotOperationRequest,
    KinesisAnalyticsDescribeSnapshotOperationResponse,
    KinesisAnalyticsDescribeSnapshotRequest,
    KinesisAnalyticsDescribeSnapshotResponse,
    KinesisAnalyticsDiscoverInputSchemaRequest,
    KinesisAnalyticsDiscoverInputSchemaResponse,
    KinesisAnalyticsExportSnapshotRequest,
    KinesisAnalyticsExportSnapshotResponse,
    KinesisAnalyticsImportSnapshotRequest,
    KinesisAnalyticsImportSnapshotResponse,
    KinesisAnalyticsListApplicationOperationsRequest,
    KinesisAnalyticsListApplicationOperationsResponse,
    KinesisAnalyticsListApplicationSnapshotsRequest,
    KinesisAnalyticsListApplicationSnapshotsResponse,
    KinesisAnalyticsListApplicationVersionsRequest,
    KinesisAnalyticsListApplicationVersionsResponse,
    KinesisAnalyticsListApplicationsRequest,
    KinesisAnalyticsListApplicationsResponse,
    KinesisAnalyticsListSnapshotOperationsRequest,
    KinesisAnalyticsListSnapshotOperationsResponse,
    KinesisAnalyticsListSnapshotsRequest,
    KinesisAnalyticsListSnapshotsResponse,
    KinesisAnalyticsListTagsForResourceRequest,
    KinesisAnalyticsListTagsForResourceResponse,
    KinesisAnalyticsRollbackApplicationRequest,
    KinesisAnalyticsRollbackApplicationResponse,
    KinesisAnalyticsStartApplicationRequest,
    KinesisAnalyticsStartApplicationResponse,
    KinesisAnalyticsStopApplicationRequest,
    KinesisAnalyticsStopApplicationResponse,
    KinesisAnalyticsTagResourceRequest,
    KinesisAnalyticsTagResourceResponse,
    KinesisAnalyticsUntagResourceRequest,
    KinesisAnalyticsUntagResourceResponse,
    KinesisAnalyticsUpdateApplicationMaintenanceConfigurationRequest,
    KinesisAnalyticsUpdateApplicationMaintenanceConfigurationResponse,
    KinesisAnalyticsUpdateApplicationRequest,
    KinesisAnalyticsUpdateApplicationResponse,
)
from werkflow_aws.types.kinesis_analytics_client import KinesisAnalyticsClient
from .base import AWSBaseService


class AWSKinesisAnalytics(AWSBaseService[KinesisAnalyticsClient]):
    service_name = 'kinesis-analytics'
    boto3_service_name = 'kinesisanalyticsv2'

    def __init__(self) -> None:
        super().__init__(service_name='kinesis-analytics', boto3_service_name='kinesisanalyticsv2')

    async def add_application_cloud_watch_logging_option(
        self,
        request: KinesisAnalyticsAddApplicationCloudWatchLoggingOptionRequest,
    ) -> KinesisAnalyticsAddApplicationCloudWatchLoggingOptionResponse:
        client = self._require_client()
        return await self._execute(client.add_application_cloud_watch_logging_option, request, KinesisAnalyticsAddApplicationCloudWatchLoggingOptionResponse)

    async def add_application_input(
        self,
        request: KinesisAnalyticsAddApplicationInputRequest,
    ) -> KinesisAnalyticsAddApplicationInputResponse:
        client = self._require_client()
        return await self._execute(client.add_application_input, request, KinesisAnalyticsAddApplicationInputResponse)

    async def add_application_input_processing_configuration(
        self,
        request: KinesisAnalyticsAddApplicationInputProcessingConfigurationRequest,
    ) -> KinesisAnalyticsAddApplicationInputProcessingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.add_application_input_processing_configuration, request, KinesisAnalyticsAddApplicationInputProcessingConfigurationResponse)

    async def add_application_output(
        self,
        request: KinesisAnalyticsAddApplicationOutputRequest,
    ) -> KinesisAnalyticsAddApplicationOutputResponse:
        client = self._require_client()
        return await self._execute(client.add_application_output, request, KinesisAnalyticsAddApplicationOutputResponse)

    async def add_application_reference_data_source(
        self,
        request: KinesisAnalyticsAddApplicationReferenceDataSourceRequest,
    ) -> KinesisAnalyticsAddApplicationReferenceDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.add_application_reference_data_source, request, KinesisAnalyticsAddApplicationReferenceDataSourceResponse)

    async def add_application_vpc_configuration(
        self,
        request: KinesisAnalyticsAddApplicationVpcConfigurationRequest,
    ) -> KinesisAnalyticsAddApplicationVpcConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.add_application_vpc_configuration, request, KinesisAnalyticsAddApplicationVpcConfigurationResponse)

    async def create_application(
        self,
        request: KinesisAnalyticsCreateApplicationRequest,
    ) -> KinesisAnalyticsCreateApplicationResponse:
        client = self._require_client()
        return await self._execute(client.create_application, request, KinesisAnalyticsCreateApplicationResponse)

    async def create_application_presigned_url(
        self,
        request: KinesisAnalyticsCreateApplicationPresignedUrlRequest,
    ) -> KinesisAnalyticsCreateApplicationPresignedUrlResponse:
        client = self._require_client()
        return await self._execute(client.create_application_presigned_url, request, KinesisAnalyticsCreateApplicationPresignedUrlResponse)

    async def create_application_snapshot(
        self,
        request: KinesisAnalyticsCreateApplicationSnapshotRequest,
    ) -> KinesisAnalyticsCreateApplicationSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_application_snapshot, request, KinesisAnalyticsCreateApplicationSnapshotResponse)

    async def create_snapshot(
        self,
        request: KinesisAnalyticsCreateSnapshotRequest,
    ) -> KinesisAnalyticsCreateSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_snapshot, request, KinesisAnalyticsCreateSnapshotResponse)

    async def delete_application(
        self,
        request: KinesisAnalyticsDeleteApplicationRequest,
    ) -> KinesisAnalyticsDeleteApplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_application, request, KinesisAnalyticsDeleteApplicationResponse)

    async def delete_application_cloud_watch_logging_option(
        self,
        request: KinesisAnalyticsDeleteApplicationCloudWatchLoggingOptionRequest,
    ) -> KinesisAnalyticsDeleteApplicationCloudWatchLoggingOptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_application_cloud_watch_logging_option, request, KinesisAnalyticsDeleteApplicationCloudWatchLoggingOptionResponse)

    async def delete_application_input_processing_configuration(
        self,
        request: KinesisAnalyticsDeleteApplicationInputProcessingConfigurationRequest,
    ) -> KinesisAnalyticsDeleteApplicationInputProcessingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_application_input_processing_configuration, request, KinesisAnalyticsDeleteApplicationInputProcessingConfigurationResponse)

    async def delete_application_output(
        self,
        request: KinesisAnalyticsDeleteApplicationOutputRequest,
    ) -> KinesisAnalyticsDeleteApplicationOutputResponse:
        client = self._require_client()
        return await self._execute(client.delete_application_output, request, KinesisAnalyticsDeleteApplicationOutputResponse)

    async def delete_application_reference_data_source(
        self,
        request: KinesisAnalyticsDeleteApplicationReferenceDataSourceRequest,
    ) -> KinesisAnalyticsDeleteApplicationReferenceDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_application_reference_data_source, request, KinesisAnalyticsDeleteApplicationReferenceDataSourceResponse)

    async def delete_application_snapshot(
        self,
        request: KinesisAnalyticsDeleteApplicationSnapshotRequest,
    ) -> KinesisAnalyticsDeleteApplicationSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_application_snapshot, request, KinesisAnalyticsDeleteApplicationSnapshotResponse)

    async def delete_application_vpc_configuration(
        self,
        request: KinesisAnalyticsDeleteApplicationVpcConfigurationRequest,
    ) -> KinesisAnalyticsDeleteApplicationVpcConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_application_vpc_configuration, request, KinesisAnalyticsDeleteApplicationVpcConfigurationResponse)

    async def delete_snapshot(
        self,
        request: KinesisAnalyticsDeleteSnapshotRequest,
    ) -> KinesisAnalyticsDeleteSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_snapshot, request, KinesisAnalyticsDeleteSnapshotResponse)

    async def describe_application(
        self,
        request: KinesisAnalyticsDescribeApplicationRequest,
    ) -> KinesisAnalyticsDescribeApplicationResponse:
        client = self._require_client()
        return await self._execute(client.describe_application, request, KinesisAnalyticsDescribeApplicationResponse)

    async def describe_application_operation(
        self,
        request: KinesisAnalyticsDescribeApplicationOperationRequest,
    ) -> KinesisAnalyticsDescribeApplicationOperationResponse:
        client = self._require_client()
        return await self._execute(client.describe_application_operation, request, KinesisAnalyticsDescribeApplicationOperationResponse)

    async def describe_application_snapshot(
        self,
        request: KinesisAnalyticsDescribeApplicationSnapshotRequest,
    ) -> KinesisAnalyticsDescribeApplicationSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.describe_application_snapshot, request, KinesisAnalyticsDescribeApplicationSnapshotResponse)

    async def describe_application_version(
        self,
        request: KinesisAnalyticsDescribeApplicationVersionRequest,
    ) -> KinesisAnalyticsDescribeApplicationVersionResponse:
        client = self._require_client()
        return await self._execute(client.describe_application_version, request, KinesisAnalyticsDescribeApplicationVersionResponse)

    async def describe_snapshot(
        self,
        request: KinesisAnalyticsDescribeSnapshotRequest,
    ) -> KinesisAnalyticsDescribeSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapshot, request, KinesisAnalyticsDescribeSnapshotResponse)

    async def describe_snapshot_operation(
        self,
        request: KinesisAnalyticsDescribeSnapshotOperationRequest,
    ) -> KinesisAnalyticsDescribeSnapshotOperationResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapshot_operation, request, KinesisAnalyticsDescribeSnapshotOperationResponse)

    async def discover_input_schema(
        self,
        request: KinesisAnalyticsDiscoverInputSchemaRequest,
    ) -> KinesisAnalyticsDiscoverInputSchemaResponse:
        client = self._require_client()
        return await self._execute(client.discover_input_schema, request, KinesisAnalyticsDiscoverInputSchemaResponse)

    async def export_snapshot(
        self,
        request: KinesisAnalyticsExportSnapshotRequest,
    ) -> KinesisAnalyticsExportSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.export_snapshot, request, KinesisAnalyticsExportSnapshotResponse)

    async def import_snapshot(
        self,
        request: KinesisAnalyticsImportSnapshotRequest,
    ) -> KinesisAnalyticsImportSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.import_snapshot, request, KinesisAnalyticsImportSnapshotResponse)

    async def list_application_operations(
        self,
        request: KinesisAnalyticsListApplicationOperationsRequest,
    ) -> KinesisAnalyticsListApplicationOperationsResponse:
        client = self._require_client()
        return await self._execute(client.list_application_operations, request, KinesisAnalyticsListApplicationOperationsResponse)

    async def list_application_operations_paginated(
        self,
        request: KinesisAnalyticsListApplicationOperationsRequest,
    ) -> list[KinesisAnalyticsListApplicationOperationsResponse]:
        return await self._paginate('list_application_operations', request, KinesisAnalyticsListApplicationOperationsResponse)

    async def list_application_snapshots(
        self,
        request: KinesisAnalyticsListApplicationSnapshotsRequest,
    ) -> KinesisAnalyticsListApplicationSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.list_application_snapshots, request, KinesisAnalyticsListApplicationSnapshotsResponse)

    async def list_application_snapshots_paginated(
        self,
        request: KinesisAnalyticsListApplicationSnapshotsRequest,
    ) -> list[KinesisAnalyticsListApplicationSnapshotsResponse]:
        return await self._paginate('list_application_snapshots', request, KinesisAnalyticsListApplicationSnapshotsResponse)

    async def list_application_versions(
        self,
        request: KinesisAnalyticsListApplicationVersionsRequest,
    ) -> KinesisAnalyticsListApplicationVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_application_versions, request, KinesisAnalyticsListApplicationVersionsResponse)

    async def list_application_versions_paginated(
        self,
        request: KinesisAnalyticsListApplicationVersionsRequest,
    ) -> list[KinesisAnalyticsListApplicationVersionsResponse]:
        return await self._paginate('list_application_versions', request, KinesisAnalyticsListApplicationVersionsResponse)

    async def list_applications(
        self,
        request: KinesisAnalyticsListApplicationsRequest | None = None,
    ) -> KinesisAnalyticsListApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.list_applications, request, KinesisAnalyticsListApplicationsResponse)

    async def list_applications_paginated(
        self,
        request: KinesisAnalyticsListApplicationsRequest | None = None,
    ) -> list[KinesisAnalyticsListApplicationsResponse]:
        return await self._paginate('list_applications', request, KinesisAnalyticsListApplicationsResponse)

    async def list_snapshot_operations(
        self,
        request: KinesisAnalyticsListSnapshotOperationsRequest,
    ) -> KinesisAnalyticsListSnapshotOperationsResponse:
        client = self._require_client()
        return await self._execute(client.list_snapshot_operations, request, KinesisAnalyticsListSnapshotOperationsResponse)

    async def list_snapshot_operations_paginated(
        self,
        request: KinesisAnalyticsListSnapshotOperationsRequest,
    ) -> list[KinesisAnalyticsListSnapshotOperationsResponse]:
        return await self._paginate('list_snapshot_operations', request, KinesisAnalyticsListSnapshotOperationsResponse)

    async def list_snapshots(
        self,
        request: KinesisAnalyticsListSnapshotsRequest | None = None,
    ) -> KinesisAnalyticsListSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.list_snapshots, request, KinesisAnalyticsListSnapshotsResponse)

    async def list_snapshots_paginated(
        self,
        request: KinesisAnalyticsListSnapshotsRequest | None = None,
    ) -> list[KinesisAnalyticsListSnapshotsResponse]:
        return await self._paginate('list_snapshots', request, KinesisAnalyticsListSnapshotsResponse)

    async def list_tags_for_resource(
        self,
        request: KinesisAnalyticsListTagsForResourceRequest,
    ) -> KinesisAnalyticsListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, KinesisAnalyticsListTagsForResourceResponse)

    async def rollback_application(
        self,
        request: KinesisAnalyticsRollbackApplicationRequest,
    ) -> KinesisAnalyticsRollbackApplicationResponse:
        client = self._require_client()
        return await self._execute(client.rollback_application, request, KinesisAnalyticsRollbackApplicationResponse)

    async def start_application(
        self,
        request: KinesisAnalyticsStartApplicationRequest,
    ) -> KinesisAnalyticsStartApplicationResponse:
        client = self._require_client()
        return await self._execute(client.start_application, request, KinesisAnalyticsStartApplicationResponse)

    async def stop_application(
        self,
        request: KinesisAnalyticsStopApplicationRequest,
    ) -> KinesisAnalyticsStopApplicationResponse:
        client = self._require_client()
        return await self._execute(client.stop_application, request, KinesisAnalyticsStopApplicationResponse)

    async def tag_resource(
        self,
        request: KinesisAnalyticsTagResourceRequest,
    ) -> KinesisAnalyticsTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, KinesisAnalyticsTagResourceResponse)

    async def untag_resource(
        self,
        request: KinesisAnalyticsUntagResourceRequest,
    ) -> KinesisAnalyticsUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, KinesisAnalyticsUntagResourceResponse)

    async def update_application(
        self,
        request: KinesisAnalyticsUpdateApplicationRequest,
    ) -> KinesisAnalyticsUpdateApplicationResponse:
        client = self._require_client()
        return await self._execute(client.update_application, request, KinesisAnalyticsUpdateApplicationResponse)

    async def update_application_maintenance_configuration(
        self,
        request: KinesisAnalyticsUpdateApplicationMaintenanceConfigurationRequest,
    ) -> KinesisAnalyticsUpdateApplicationMaintenanceConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_application_maintenance_configuration, request, KinesisAnalyticsUpdateApplicationMaintenanceConfigurationResponse)
