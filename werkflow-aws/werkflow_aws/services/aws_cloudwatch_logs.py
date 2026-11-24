from werkflow_aws.models.cloudwatch_logs import (
    CloudWatchLogsAssociateKmsKeyRequest,
    CloudWatchLogsAssociateKmsKeyResponse,
    CloudWatchLogsAssociateSourceToS3TableIntegrationRequest,
    CloudWatchLogsAssociateSourceToS3TableIntegrationResponse,
    CloudWatchLogsCancelExportTaskRequest,
    CloudWatchLogsCancelExportTaskResponse,
    CloudWatchLogsCancelImportTaskRequest,
    CloudWatchLogsCancelImportTaskResponse,
    CloudWatchLogsCreateDeliveryRequest,
    CloudWatchLogsCreateDeliveryResponse,
    CloudWatchLogsCreateExportTaskRequest,
    CloudWatchLogsCreateExportTaskResponse,
    CloudWatchLogsCreateImportTaskRequest,
    CloudWatchLogsCreateImportTaskResponse,
    CloudWatchLogsCreateLogAnomalyDetectorRequest,
    CloudWatchLogsCreateLogAnomalyDetectorResponse,
    CloudWatchLogsCreateLogGroupRequest,
    CloudWatchLogsCreateLogGroupResponse,
    CloudWatchLogsCreateLogStreamRequest,
    CloudWatchLogsCreateLogStreamResponse,
    CloudWatchLogsCreateLookupTableRequest,
    CloudWatchLogsCreateLookupTableResponse,
    CloudWatchLogsCreateScheduledQueryRequest,
    CloudWatchLogsCreateScheduledQueryResponse,
    CloudWatchLogsDeleteAccountPolicyRequest,
    CloudWatchLogsDeleteAccountPolicyResponse,
    CloudWatchLogsDeleteDataProtectionPolicyRequest,
    CloudWatchLogsDeleteDataProtectionPolicyResponse,
    CloudWatchLogsDeleteDeliveryDestinationPolicyRequest,
    CloudWatchLogsDeleteDeliveryDestinationPolicyResponse,
    CloudWatchLogsDeleteDeliveryDestinationRequest,
    CloudWatchLogsDeleteDeliveryDestinationResponse,
    CloudWatchLogsDeleteDeliveryRequest,
    CloudWatchLogsDeleteDeliveryResponse,
    CloudWatchLogsDeleteDeliverySourceRequest,
    CloudWatchLogsDeleteDeliverySourceResponse,
    CloudWatchLogsDeleteDestinationRequest,
    CloudWatchLogsDeleteDestinationResponse,
    CloudWatchLogsDeleteIndexPolicyRequest,
    CloudWatchLogsDeleteIndexPolicyResponse,
    CloudWatchLogsDeleteIntegrationRequest,
    CloudWatchLogsDeleteIntegrationResponse,
    CloudWatchLogsDeleteLogAnomalyDetectorRequest,
    CloudWatchLogsDeleteLogAnomalyDetectorResponse,
    CloudWatchLogsDeleteLogGroupRequest,
    CloudWatchLogsDeleteLogGroupResponse,
    CloudWatchLogsDeleteLogStreamRequest,
    CloudWatchLogsDeleteLogStreamResponse,
    CloudWatchLogsDeleteLookupTableRequest,
    CloudWatchLogsDeleteLookupTableResponse,
    CloudWatchLogsDeleteMetricFilterRequest,
    CloudWatchLogsDeleteMetricFilterResponse,
    CloudWatchLogsDeleteQueryDefinitionRequest,
    CloudWatchLogsDeleteQueryDefinitionResponse,
    CloudWatchLogsDeleteResourcePolicyRequest,
    CloudWatchLogsDeleteResourcePolicyResponse,
    CloudWatchLogsDeleteRetentionPolicyRequest,
    CloudWatchLogsDeleteRetentionPolicyResponse,
    CloudWatchLogsDeleteScheduledQueryRequest,
    CloudWatchLogsDeleteScheduledQueryResponse,
    CloudWatchLogsDeleteSubscriptionFilterRequest,
    CloudWatchLogsDeleteSubscriptionFilterResponse,
    CloudWatchLogsDeleteSyslogConfigurationRequest,
    CloudWatchLogsDeleteSyslogConfigurationResponse,
    CloudWatchLogsDeleteTransformerRequest,
    CloudWatchLogsDeleteTransformerResponse,
    CloudWatchLogsDescribeAccountPoliciesRequest,
    CloudWatchLogsDescribeAccountPoliciesResponse,
    CloudWatchLogsDescribeConfigurationTemplatesRequest,
    CloudWatchLogsDescribeConfigurationTemplatesResponse,
    CloudWatchLogsDescribeDeliveriesRequest,
    CloudWatchLogsDescribeDeliveriesResponse,
    CloudWatchLogsDescribeDeliveryDestinationsRequest,
    CloudWatchLogsDescribeDeliveryDestinationsResponse,
    CloudWatchLogsDescribeDeliverySourcesRequest,
    CloudWatchLogsDescribeDeliverySourcesResponse,
    CloudWatchLogsDescribeDestinationsRequest,
    CloudWatchLogsDescribeDestinationsResponse,
    CloudWatchLogsDescribeExportTasksRequest,
    CloudWatchLogsDescribeExportTasksResponse,
    CloudWatchLogsDescribeFieldIndexesRequest,
    CloudWatchLogsDescribeFieldIndexesResponse,
    CloudWatchLogsDescribeImportTaskBatchesRequest,
    CloudWatchLogsDescribeImportTaskBatchesResponse,
    CloudWatchLogsDescribeImportTasksRequest,
    CloudWatchLogsDescribeImportTasksResponse,
    CloudWatchLogsDescribeIndexPoliciesRequest,
    CloudWatchLogsDescribeIndexPoliciesResponse,
    CloudWatchLogsDescribeLogGroupsRequest,
    CloudWatchLogsDescribeLogGroupsResponse,
    CloudWatchLogsDescribeLogStreamsRequest,
    CloudWatchLogsDescribeLogStreamsResponse,
    CloudWatchLogsDescribeLookupTablesRequest,
    CloudWatchLogsDescribeLookupTablesResponse,
    CloudWatchLogsDescribeMetricFiltersRequest,
    CloudWatchLogsDescribeMetricFiltersResponse,
    CloudWatchLogsDescribeQueriesRequest,
    CloudWatchLogsDescribeQueriesResponse,
    CloudWatchLogsDescribeQueryDefinitionsRequest,
    CloudWatchLogsDescribeQueryDefinitionsResponse,
    CloudWatchLogsDescribeResourcePoliciesRequest,
    CloudWatchLogsDescribeResourcePoliciesResponse,
    CloudWatchLogsDescribeSubscriptionFiltersRequest,
    CloudWatchLogsDescribeSubscriptionFiltersResponse,
    CloudWatchLogsDisassociateKmsKeyRequest,
    CloudWatchLogsDisassociateKmsKeyResponse,
    CloudWatchLogsDisassociateSourceFromS3TableIntegrationRequest,
    CloudWatchLogsDisassociateSourceFromS3TableIntegrationResponse,
    CloudWatchLogsFilterLogEventsRequest,
    CloudWatchLogsFilterLogEventsResponse,
    CloudWatchLogsGetDataProtectionPolicyRequest,
    CloudWatchLogsGetDataProtectionPolicyResponse,
    CloudWatchLogsGetDeliveryDestinationPolicyRequest,
    CloudWatchLogsGetDeliveryDestinationPolicyResponse,
    CloudWatchLogsGetDeliveryDestinationRequest,
    CloudWatchLogsGetDeliveryDestinationResponse,
    CloudWatchLogsGetDeliveryRequest,
    CloudWatchLogsGetDeliveryResponse,
    CloudWatchLogsGetDeliverySourceRequest,
    CloudWatchLogsGetDeliverySourceResponse,
    CloudWatchLogsGetIntegrationRequest,
    CloudWatchLogsGetIntegrationResponse,
    CloudWatchLogsGetLogAnomalyDetectorRequest,
    CloudWatchLogsGetLogAnomalyDetectorResponse,
    CloudWatchLogsGetLogEventsRequest,
    CloudWatchLogsGetLogEventsResponse,
    CloudWatchLogsGetLogFieldsRequest,
    CloudWatchLogsGetLogFieldsResponse,
    CloudWatchLogsGetLogGroupFieldsRequest,
    CloudWatchLogsGetLogGroupFieldsResponse,
    CloudWatchLogsGetLogObjectRequest,
    CloudWatchLogsGetLogObjectResponse,
    CloudWatchLogsGetLogRecordRequest,
    CloudWatchLogsGetLogRecordResponse,
    CloudWatchLogsGetLookupTableRequest,
    CloudWatchLogsGetLookupTableResponse,
    CloudWatchLogsGetQueryResultsRequest,
    CloudWatchLogsGetQueryResultsResponse,
    CloudWatchLogsGetScheduledQueryHistoryRequest,
    CloudWatchLogsGetScheduledQueryHistoryResponse,
    CloudWatchLogsGetScheduledQueryRequest,
    CloudWatchLogsGetScheduledQueryResponse,
    CloudWatchLogsGetStorageTierPolicyRequest,
    CloudWatchLogsGetStorageTierPolicyResponse,
    CloudWatchLogsGetTransformerRequest,
    CloudWatchLogsGetTransformerResponse,
    CloudWatchLogsListAggregateLogGroupSummariesRequest,
    CloudWatchLogsListAggregateLogGroupSummariesResponse,
    CloudWatchLogsListAnomaliesRequest,
    CloudWatchLogsListAnomaliesResponse,
    CloudWatchLogsListIntegrationsRequest,
    CloudWatchLogsListIntegrationsResponse,
    CloudWatchLogsListLogAnomalyDetectorsRequest,
    CloudWatchLogsListLogAnomalyDetectorsResponse,
    CloudWatchLogsListLogGroupsForQueryRequest,
    CloudWatchLogsListLogGroupsForQueryResponse,
    CloudWatchLogsListLogGroupsRequest,
    CloudWatchLogsListLogGroupsResponse,
    CloudWatchLogsListScheduledQueriesRequest,
    CloudWatchLogsListScheduledQueriesResponse,
    CloudWatchLogsListSourcesForS3TableIntegrationRequest,
    CloudWatchLogsListSourcesForS3TableIntegrationResponse,
    CloudWatchLogsListSyslogConfigurationsRequest,
    CloudWatchLogsListSyslogConfigurationsResponse,
    CloudWatchLogsListTagsForResourceRequest,
    CloudWatchLogsListTagsForResourceResponse,
    CloudWatchLogsListTagsLogGroupRequest,
    CloudWatchLogsListTagsLogGroupResponse,
    CloudWatchLogsPutAccountPolicyRequest,
    CloudWatchLogsPutAccountPolicyResponse,
    CloudWatchLogsPutBearerTokenAuthenticationRequest,
    CloudWatchLogsPutBearerTokenAuthenticationResponse,
    CloudWatchLogsPutDataProtectionPolicyRequest,
    CloudWatchLogsPutDataProtectionPolicyResponse,
    CloudWatchLogsPutDeliveryDestinationPolicyRequest,
    CloudWatchLogsPutDeliveryDestinationPolicyResponse,
    CloudWatchLogsPutDeliveryDestinationRequest,
    CloudWatchLogsPutDeliveryDestinationResponse,
    CloudWatchLogsPutDeliverySourceRequest,
    CloudWatchLogsPutDeliverySourceResponse,
    CloudWatchLogsPutDestinationPolicyRequest,
    CloudWatchLogsPutDestinationPolicyResponse,
    CloudWatchLogsPutDestinationRequest,
    CloudWatchLogsPutDestinationResponse,
    CloudWatchLogsPutIndexPolicyRequest,
    CloudWatchLogsPutIndexPolicyResponse,
    CloudWatchLogsPutIntegrationRequest,
    CloudWatchLogsPutIntegrationResponse,
    CloudWatchLogsPutLogEventsRequest,
    CloudWatchLogsPutLogEventsResponse,
    CloudWatchLogsPutLogGroupDeletionProtectionRequest,
    CloudWatchLogsPutLogGroupDeletionProtectionResponse,
    CloudWatchLogsPutMetricFilterRequest,
    CloudWatchLogsPutMetricFilterResponse,
    CloudWatchLogsPutQueryDefinitionRequest,
    CloudWatchLogsPutQueryDefinitionResponse,
    CloudWatchLogsPutResourcePolicyRequest,
    CloudWatchLogsPutResourcePolicyResponse,
    CloudWatchLogsPutRetentionPolicyRequest,
    CloudWatchLogsPutRetentionPolicyResponse,
    CloudWatchLogsPutStorageTierPolicyRequest,
    CloudWatchLogsPutStorageTierPolicyResponse,
    CloudWatchLogsPutSubscriptionFilterRequest,
    CloudWatchLogsPutSubscriptionFilterResponse,
    CloudWatchLogsPutSyslogConfigurationRequest,
    CloudWatchLogsPutSyslogConfigurationResponse,
    CloudWatchLogsPutTransformerRequest,
    CloudWatchLogsPutTransformerResponse,
    CloudWatchLogsStartLiveTailRequest,
    CloudWatchLogsStartLiveTailResponse,
    CloudWatchLogsStartQueryRequest,
    CloudWatchLogsStartQueryResponse,
    CloudWatchLogsStopQueryRequest,
    CloudWatchLogsStopQueryResponse,
    CloudWatchLogsTagLogGroupRequest,
    CloudWatchLogsTagLogGroupResponse,
    CloudWatchLogsTagResourceRequest,
    CloudWatchLogsTagResourceResponse,
    CloudWatchLogsTestMetricFilterRequest,
    CloudWatchLogsTestMetricFilterResponse,
    CloudWatchLogsTestTransformerRequest,
    CloudWatchLogsTestTransformerResponse,
    CloudWatchLogsUntagLogGroupRequest,
    CloudWatchLogsUntagLogGroupResponse,
    CloudWatchLogsUntagResourceRequest,
    CloudWatchLogsUntagResourceResponse,
    CloudWatchLogsUpdateAnomalyRequest,
    CloudWatchLogsUpdateAnomalyResponse,
    CloudWatchLogsUpdateDeliveryConfigurationRequest,
    CloudWatchLogsUpdateDeliveryConfigurationResponse,
    CloudWatchLogsUpdateLogAnomalyDetectorRequest,
    CloudWatchLogsUpdateLogAnomalyDetectorResponse,
    CloudWatchLogsUpdateLookupTableRequest,
    CloudWatchLogsUpdateLookupTableResponse,
    CloudWatchLogsUpdateScheduledQueryRequest,
    CloudWatchLogsUpdateScheduledQueryResponse,
)
from werkflow_aws.types.cloudwatch_logs_client import CloudWatchLogsClient
from .base import AWSBaseService


class AWSCloudWatchLogs(AWSBaseService[CloudWatchLogsClient]):
    service_name = 'cloudwatch-logs'
    boto3_service_name = 'logs'

    def __init__(self) -> None:
        super().__init__(service_name='cloudwatch-logs', boto3_service_name='logs')

    async def associate_kms_key(
        self,
        request: CloudWatchLogsAssociateKmsKeyRequest,
    ) -> CloudWatchLogsAssociateKmsKeyResponse:
        client = self._require_client()
        return await self._execute(client.associate_kms_key, request, CloudWatchLogsAssociateKmsKeyResponse)

    async def associate_source_to_s3_table_integration(
        self,
        request: CloudWatchLogsAssociateSourceToS3TableIntegrationRequest,
    ) -> CloudWatchLogsAssociateSourceToS3TableIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.associate_source_to_s3_table_integration, request, CloudWatchLogsAssociateSourceToS3TableIntegrationResponse)

    async def cancel_export_task(
        self,
        request: CloudWatchLogsCancelExportTaskRequest,
    ) -> CloudWatchLogsCancelExportTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_export_task, request, CloudWatchLogsCancelExportTaskResponse)

    async def cancel_import_task(
        self,
        request: CloudWatchLogsCancelImportTaskRequest,
    ) -> CloudWatchLogsCancelImportTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_import_task, request, CloudWatchLogsCancelImportTaskResponse)

    async def create_delivery(
        self,
        request: CloudWatchLogsCreateDeliveryRequest,
    ) -> CloudWatchLogsCreateDeliveryResponse:
        client = self._require_client()
        return await self._execute(client.create_delivery, request, CloudWatchLogsCreateDeliveryResponse)

    async def create_export_task(
        self,
        request: CloudWatchLogsCreateExportTaskRequest,
    ) -> CloudWatchLogsCreateExportTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_export_task, request, CloudWatchLogsCreateExportTaskResponse)

    async def create_import_task(
        self,
        request: CloudWatchLogsCreateImportTaskRequest,
    ) -> CloudWatchLogsCreateImportTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_import_task, request, CloudWatchLogsCreateImportTaskResponse)

    async def create_log_anomaly_detector(
        self,
        request: CloudWatchLogsCreateLogAnomalyDetectorRequest,
    ) -> CloudWatchLogsCreateLogAnomalyDetectorResponse:
        client = self._require_client()
        return await self._execute(client.create_log_anomaly_detector, request, CloudWatchLogsCreateLogAnomalyDetectorResponse)

    async def create_log_group(
        self,
        request: CloudWatchLogsCreateLogGroupRequest,
    ) -> CloudWatchLogsCreateLogGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_log_group, request, CloudWatchLogsCreateLogGroupResponse)

    async def create_log_stream(
        self,
        request: CloudWatchLogsCreateLogStreamRequest,
    ) -> CloudWatchLogsCreateLogStreamResponse:
        client = self._require_client()
        return await self._execute(client.create_log_stream, request, CloudWatchLogsCreateLogStreamResponse)

    async def create_lookup_table(
        self,
        request: CloudWatchLogsCreateLookupTableRequest,
    ) -> CloudWatchLogsCreateLookupTableResponse:
        client = self._require_client()
        return await self._execute(client.create_lookup_table, request, CloudWatchLogsCreateLookupTableResponse)

    async def create_scheduled_query(
        self,
        request: CloudWatchLogsCreateScheduledQueryRequest,
    ) -> CloudWatchLogsCreateScheduledQueryResponse:
        client = self._require_client()
        return await self._execute(client.create_scheduled_query, request, CloudWatchLogsCreateScheduledQueryResponse)

    async def delete_account_policy(
        self,
        request: CloudWatchLogsDeleteAccountPolicyRequest,
    ) -> CloudWatchLogsDeleteAccountPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_policy, request, CloudWatchLogsDeleteAccountPolicyResponse)

    async def delete_data_protection_policy(
        self,
        request: CloudWatchLogsDeleteDataProtectionPolicyRequest,
    ) -> CloudWatchLogsDeleteDataProtectionPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_protection_policy, request, CloudWatchLogsDeleteDataProtectionPolicyResponse)

    async def delete_delivery(
        self,
        request: CloudWatchLogsDeleteDeliveryRequest,
    ) -> CloudWatchLogsDeleteDeliveryResponse:
        client = self._require_client()
        return await self._execute(client.delete_delivery, request, CloudWatchLogsDeleteDeliveryResponse)

    async def delete_delivery_destination(
        self,
        request: CloudWatchLogsDeleteDeliveryDestinationRequest,
    ) -> CloudWatchLogsDeleteDeliveryDestinationResponse:
        client = self._require_client()
        return await self._execute(client.delete_delivery_destination, request, CloudWatchLogsDeleteDeliveryDestinationResponse)

    async def delete_delivery_destination_policy(
        self,
        request: CloudWatchLogsDeleteDeliveryDestinationPolicyRequest,
    ) -> CloudWatchLogsDeleteDeliveryDestinationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_delivery_destination_policy, request, CloudWatchLogsDeleteDeliveryDestinationPolicyResponse)

    async def delete_delivery_source(
        self,
        request: CloudWatchLogsDeleteDeliverySourceRequest,
    ) -> CloudWatchLogsDeleteDeliverySourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_delivery_source, request, CloudWatchLogsDeleteDeliverySourceResponse)

    async def delete_destination(
        self,
        request: CloudWatchLogsDeleteDestinationRequest,
    ) -> CloudWatchLogsDeleteDestinationResponse:
        client = self._require_client()
        return await self._execute(client.delete_destination, request, CloudWatchLogsDeleteDestinationResponse)

    async def delete_index_policy(
        self,
        request: CloudWatchLogsDeleteIndexPolicyRequest,
    ) -> CloudWatchLogsDeleteIndexPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_index_policy, request, CloudWatchLogsDeleteIndexPolicyResponse)

    async def delete_integration(
        self,
        request: CloudWatchLogsDeleteIntegrationRequest,
    ) -> CloudWatchLogsDeleteIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_integration, request, CloudWatchLogsDeleteIntegrationResponse)

    async def delete_log_anomaly_detector(
        self,
        request: CloudWatchLogsDeleteLogAnomalyDetectorRequest,
    ) -> CloudWatchLogsDeleteLogAnomalyDetectorResponse:
        client = self._require_client()
        return await self._execute(client.delete_log_anomaly_detector, request, CloudWatchLogsDeleteLogAnomalyDetectorResponse)

    async def delete_log_group(
        self,
        request: CloudWatchLogsDeleteLogGroupRequest,
    ) -> CloudWatchLogsDeleteLogGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_log_group, request, CloudWatchLogsDeleteLogGroupResponse)

    async def delete_log_stream(
        self,
        request: CloudWatchLogsDeleteLogStreamRequest,
    ) -> CloudWatchLogsDeleteLogStreamResponse:
        client = self._require_client()
        return await self._execute(client.delete_log_stream, request, CloudWatchLogsDeleteLogStreamResponse)

    async def delete_lookup_table(
        self,
        request: CloudWatchLogsDeleteLookupTableRequest,
    ) -> CloudWatchLogsDeleteLookupTableResponse:
        client = self._require_client()
        return await self._execute(client.delete_lookup_table, request, CloudWatchLogsDeleteLookupTableResponse)

    async def delete_metric_filter(
        self,
        request: CloudWatchLogsDeleteMetricFilterRequest,
    ) -> CloudWatchLogsDeleteMetricFilterResponse:
        client = self._require_client()
        return await self._execute(client.delete_metric_filter, request, CloudWatchLogsDeleteMetricFilterResponse)

    async def delete_query_definition(
        self,
        request: CloudWatchLogsDeleteQueryDefinitionRequest,
    ) -> CloudWatchLogsDeleteQueryDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_query_definition, request, CloudWatchLogsDeleteQueryDefinitionResponse)

    async def delete_resource_policy(
        self,
        request: CloudWatchLogsDeleteResourcePolicyRequest | None = None,
    ) -> CloudWatchLogsDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, CloudWatchLogsDeleteResourcePolicyResponse)

    async def delete_retention_policy(
        self,
        request: CloudWatchLogsDeleteRetentionPolicyRequest,
    ) -> CloudWatchLogsDeleteRetentionPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_retention_policy, request, CloudWatchLogsDeleteRetentionPolicyResponse)

    async def delete_scheduled_query(
        self,
        request: CloudWatchLogsDeleteScheduledQueryRequest,
    ) -> CloudWatchLogsDeleteScheduledQueryResponse:
        client = self._require_client()
        return await self._execute(client.delete_scheduled_query, request, CloudWatchLogsDeleteScheduledQueryResponse)

    async def delete_subscription_filter(
        self,
        request: CloudWatchLogsDeleteSubscriptionFilterRequest,
    ) -> CloudWatchLogsDeleteSubscriptionFilterResponse:
        client = self._require_client()
        return await self._execute(client.delete_subscription_filter, request, CloudWatchLogsDeleteSubscriptionFilterResponse)

    async def delete_syslog_configuration(
        self,
        request: CloudWatchLogsDeleteSyslogConfigurationRequest,
    ) -> CloudWatchLogsDeleteSyslogConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_syslog_configuration, request, CloudWatchLogsDeleteSyslogConfigurationResponse)

    async def delete_transformer(
        self,
        request: CloudWatchLogsDeleteTransformerRequest,
    ) -> CloudWatchLogsDeleteTransformerResponse:
        client = self._require_client()
        return await self._execute(client.delete_transformer, request, CloudWatchLogsDeleteTransformerResponse)

    async def describe_account_policies(
        self,
        request: CloudWatchLogsDescribeAccountPoliciesRequest,
    ) -> CloudWatchLogsDescribeAccountPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_policies, request, CloudWatchLogsDescribeAccountPoliciesResponse)

    async def describe_configuration_templates(
        self,
        request: CloudWatchLogsDescribeConfigurationTemplatesRequest | None = None,
    ) -> CloudWatchLogsDescribeConfigurationTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_configuration_templates, request, CloudWatchLogsDescribeConfigurationTemplatesResponse)

    async def describe_configuration_templates_paginated(
        self,
        request: CloudWatchLogsDescribeConfigurationTemplatesRequest | None = None,
    ) -> list[CloudWatchLogsDescribeConfigurationTemplatesResponse]:
        return await self._paginate('describe_configuration_templates', request, CloudWatchLogsDescribeConfigurationTemplatesResponse)

    async def describe_deliveries(
        self,
        request: CloudWatchLogsDescribeDeliveriesRequest | None = None,
    ) -> CloudWatchLogsDescribeDeliveriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_deliveries, request, CloudWatchLogsDescribeDeliveriesResponse)

    async def describe_deliveries_paginated(
        self,
        request: CloudWatchLogsDescribeDeliveriesRequest | None = None,
    ) -> list[CloudWatchLogsDescribeDeliveriesResponse]:
        return await self._paginate('describe_deliveries', request, CloudWatchLogsDescribeDeliveriesResponse)

    async def describe_delivery_destinations(
        self,
        request: CloudWatchLogsDescribeDeliveryDestinationsRequest | None = None,
    ) -> CloudWatchLogsDescribeDeliveryDestinationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_delivery_destinations, request, CloudWatchLogsDescribeDeliveryDestinationsResponse)

    async def describe_delivery_destinations_paginated(
        self,
        request: CloudWatchLogsDescribeDeliveryDestinationsRequest | None = None,
    ) -> list[CloudWatchLogsDescribeDeliveryDestinationsResponse]:
        return await self._paginate('describe_delivery_destinations', request, CloudWatchLogsDescribeDeliveryDestinationsResponse)

    async def describe_delivery_sources(
        self,
        request: CloudWatchLogsDescribeDeliverySourcesRequest | None = None,
    ) -> CloudWatchLogsDescribeDeliverySourcesResponse:
        client = self._require_client()
        return await self._execute(client.describe_delivery_sources, request, CloudWatchLogsDescribeDeliverySourcesResponse)

    async def describe_delivery_sources_paginated(
        self,
        request: CloudWatchLogsDescribeDeliverySourcesRequest | None = None,
    ) -> list[CloudWatchLogsDescribeDeliverySourcesResponse]:
        return await self._paginate('describe_delivery_sources', request, CloudWatchLogsDescribeDeliverySourcesResponse)

    async def describe_destinations(
        self,
        request: CloudWatchLogsDescribeDestinationsRequest | None = None,
    ) -> CloudWatchLogsDescribeDestinationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_destinations, request, CloudWatchLogsDescribeDestinationsResponse)

    async def describe_destinations_paginated(
        self,
        request: CloudWatchLogsDescribeDestinationsRequest | None = None,
    ) -> list[CloudWatchLogsDescribeDestinationsResponse]:
        return await self._paginate('describe_destinations', request, CloudWatchLogsDescribeDestinationsResponse)

    async def describe_export_tasks(
        self,
        request: CloudWatchLogsDescribeExportTasksRequest | None = None,
    ) -> CloudWatchLogsDescribeExportTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_export_tasks, request, CloudWatchLogsDescribeExportTasksResponse)

    async def describe_export_tasks_paginated(
        self,
        request: CloudWatchLogsDescribeExportTasksRequest | None = None,
    ) -> list[CloudWatchLogsDescribeExportTasksResponse]:
        return await self._paginate('describe_export_tasks', request, CloudWatchLogsDescribeExportTasksResponse)

    async def describe_field_indexes(
        self,
        request: CloudWatchLogsDescribeFieldIndexesRequest,
    ) -> CloudWatchLogsDescribeFieldIndexesResponse:
        client = self._require_client()
        return await self._execute(client.describe_field_indexes, request, CloudWatchLogsDescribeFieldIndexesResponse)

    async def describe_import_task_batches(
        self,
        request: CloudWatchLogsDescribeImportTaskBatchesRequest,
    ) -> CloudWatchLogsDescribeImportTaskBatchesResponse:
        client = self._require_client()
        return await self._execute(client.describe_import_task_batches, request, CloudWatchLogsDescribeImportTaskBatchesResponse)

    async def describe_import_tasks(
        self,
        request: CloudWatchLogsDescribeImportTasksRequest | None = None,
    ) -> CloudWatchLogsDescribeImportTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_import_tasks, request, CloudWatchLogsDescribeImportTasksResponse)

    async def describe_index_policies(
        self,
        request: CloudWatchLogsDescribeIndexPoliciesRequest,
    ) -> CloudWatchLogsDescribeIndexPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_index_policies, request, CloudWatchLogsDescribeIndexPoliciesResponse)

    async def describe_log_groups(
        self,
        request: CloudWatchLogsDescribeLogGroupsRequest | None = None,
    ) -> CloudWatchLogsDescribeLogGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_log_groups, request, CloudWatchLogsDescribeLogGroupsResponse)

    async def describe_log_groups_paginated(
        self,
        request: CloudWatchLogsDescribeLogGroupsRequest | None = None,
    ) -> list[CloudWatchLogsDescribeLogGroupsResponse]:
        return await self._paginate('describe_log_groups', request, CloudWatchLogsDescribeLogGroupsResponse)

    async def describe_log_streams(
        self,
        request: CloudWatchLogsDescribeLogStreamsRequest | None = None,
    ) -> CloudWatchLogsDescribeLogStreamsResponse:
        client = self._require_client()
        return await self._execute(client.describe_log_streams, request, CloudWatchLogsDescribeLogStreamsResponse)

    async def describe_log_streams_paginated(
        self,
        request: CloudWatchLogsDescribeLogStreamsRequest | None = None,
    ) -> list[CloudWatchLogsDescribeLogStreamsResponse]:
        return await self._paginate('describe_log_streams', request, CloudWatchLogsDescribeLogStreamsResponse)

    async def describe_lookup_tables(
        self,
        request: CloudWatchLogsDescribeLookupTablesRequest | None = None,
    ) -> CloudWatchLogsDescribeLookupTablesResponse:
        client = self._require_client()
        return await self._execute(client.describe_lookup_tables, request, CloudWatchLogsDescribeLookupTablesResponse)

    async def describe_metric_filters(
        self,
        request: CloudWatchLogsDescribeMetricFiltersRequest | None = None,
    ) -> CloudWatchLogsDescribeMetricFiltersResponse:
        client = self._require_client()
        return await self._execute(client.describe_metric_filters, request, CloudWatchLogsDescribeMetricFiltersResponse)

    async def describe_metric_filters_paginated(
        self,
        request: CloudWatchLogsDescribeMetricFiltersRequest | None = None,
    ) -> list[CloudWatchLogsDescribeMetricFiltersResponse]:
        return await self._paginate('describe_metric_filters', request, CloudWatchLogsDescribeMetricFiltersResponse)

    async def describe_queries(
        self,
        request: CloudWatchLogsDescribeQueriesRequest | None = None,
    ) -> CloudWatchLogsDescribeQueriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_queries, request, CloudWatchLogsDescribeQueriesResponse)

    async def describe_queries_paginated(
        self,
        request: CloudWatchLogsDescribeQueriesRequest | None = None,
    ) -> list[CloudWatchLogsDescribeQueriesResponse]:
        return await self._paginate('describe_queries', request, CloudWatchLogsDescribeQueriesResponse)

    async def describe_query_definitions(
        self,
        request: CloudWatchLogsDescribeQueryDefinitionsRequest | None = None,
    ) -> CloudWatchLogsDescribeQueryDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_query_definitions, request, CloudWatchLogsDescribeQueryDefinitionsResponse)

    async def describe_resource_policies(
        self,
        request: CloudWatchLogsDescribeResourcePoliciesRequest | None = None,
    ) -> CloudWatchLogsDescribeResourcePoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_resource_policies, request, CloudWatchLogsDescribeResourcePoliciesResponse)

    async def describe_resource_policies_paginated(
        self,
        request: CloudWatchLogsDescribeResourcePoliciesRequest | None = None,
    ) -> list[CloudWatchLogsDescribeResourcePoliciesResponse]:
        return await self._paginate('describe_resource_policies', request, CloudWatchLogsDescribeResourcePoliciesResponse)

    async def describe_subscription_filters(
        self,
        request: CloudWatchLogsDescribeSubscriptionFiltersRequest,
    ) -> CloudWatchLogsDescribeSubscriptionFiltersResponse:
        client = self._require_client()
        return await self._execute(client.describe_subscription_filters, request, CloudWatchLogsDescribeSubscriptionFiltersResponse)

    async def describe_subscription_filters_paginated(
        self,
        request: CloudWatchLogsDescribeSubscriptionFiltersRequest,
    ) -> list[CloudWatchLogsDescribeSubscriptionFiltersResponse]:
        return await self._paginate('describe_subscription_filters', request, CloudWatchLogsDescribeSubscriptionFiltersResponse)

    async def disassociate_kms_key(
        self,
        request: CloudWatchLogsDisassociateKmsKeyRequest | None = None,
    ) -> CloudWatchLogsDisassociateKmsKeyResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_kms_key, request, CloudWatchLogsDisassociateKmsKeyResponse)

    async def disassociate_source_from_s3_table_integration(
        self,
        request: CloudWatchLogsDisassociateSourceFromS3TableIntegrationRequest,
    ) -> CloudWatchLogsDisassociateSourceFromS3TableIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_source_from_s3_table_integration, request, CloudWatchLogsDisassociateSourceFromS3TableIntegrationResponse)

    async def filter_log_events(
        self,
        request: CloudWatchLogsFilterLogEventsRequest | None = None,
    ) -> CloudWatchLogsFilterLogEventsResponse:
        client = self._require_client()
        return await self._execute(client.filter_log_events, request, CloudWatchLogsFilterLogEventsResponse)

    async def filter_log_events_paginated(
        self,
        request: CloudWatchLogsFilterLogEventsRequest | None = None,
    ) -> list[CloudWatchLogsFilterLogEventsResponse]:
        return await self._paginate('filter_log_events', request, CloudWatchLogsFilterLogEventsResponse)

    async def get_data_protection_policy(
        self,
        request: CloudWatchLogsGetDataProtectionPolicyRequest,
    ) -> CloudWatchLogsGetDataProtectionPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_data_protection_policy, request, CloudWatchLogsGetDataProtectionPolicyResponse)

    async def get_delivery(
        self,
        request: CloudWatchLogsGetDeliveryRequest,
    ) -> CloudWatchLogsGetDeliveryResponse:
        client = self._require_client()
        return await self._execute(client.get_delivery, request, CloudWatchLogsGetDeliveryResponse)

    async def get_delivery_destination(
        self,
        request: CloudWatchLogsGetDeliveryDestinationRequest,
    ) -> CloudWatchLogsGetDeliveryDestinationResponse:
        client = self._require_client()
        return await self._execute(client.get_delivery_destination, request, CloudWatchLogsGetDeliveryDestinationResponse)

    async def get_delivery_destination_policy(
        self,
        request: CloudWatchLogsGetDeliveryDestinationPolicyRequest,
    ) -> CloudWatchLogsGetDeliveryDestinationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_delivery_destination_policy, request, CloudWatchLogsGetDeliveryDestinationPolicyResponse)

    async def get_delivery_source(
        self,
        request: CloudWatchLogsGetDeliverySourceRequest,
    ) -> CloudWatchLogsGetDeliverySourceResponse:
        client = self._require_client()
        return await self._execute(client.get_delivery_source, request, CloudWatchLogsGetDeliverySourceResponse)

    async def get_integration(
        self,
        request: CloudWatchLogsGetIntegrationRequest,
    ) -> CloudWatchLogsGetIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.get_integration, request, CloudWatchLogsGetIntegrationResponse)

    async def get_log_anomaly_detector(
        self,
        request: CloudWatchLogsGetLogAnomalyDetectorRequest,
    ) -> CloudWatchLogsGetLogAnomalyDetectorResponse:
        client = self._require_client()
        return await self._execute(client.get_log_anomaly_detector, request, CloudWatchLogsGetLogAnomalyDetectorResponse)

    async def get_log_events(
        self,
        request: CloudWatchLogsGetLogEventsRequest,
    ) -> CloudWatchLogsGetLogEventsResponse:
        client = self._require_client()
        return await self._execute(client.get_log_events, request, CloudWatchLogsGetLogEventsResponse)

    async def get_log_fields(
        self,
        request: CloudWatchLogsGetLogFieldsRequest,
    ) -> CloudWatchLogsGetLogFieldsResponse:
        client = self._require_client()
        return await self._execute(client.get_log_fields, request, CloudWatchLogsGetLogFieldsResponse)

    async def get_log_group_fields(
        self,
        request: CloudWatchLogsGetLogGroupFieldsRequest | None = None,
    ) -> CloudWatchLogsGetLogGroupFieldsResponse:
        client = self._require_client()
        return await self._execute(client.get_log_group_fields, request, CloudWatchLogsGetLogGroupFieldsResponse)

    async def get_log_object(
        self,
        request: CloudWatchLogsGetLogObjectRequest,
    ) -> CloudWatchLogsGetLogObjectResponse:
        client = self._require_client()
        return await self._execute(client.get_log_object, request, CloudWatchLogsGetLogObjectResponse)

    async def get_log_record(
        self,
        request: CloudWatchLogsGetLogRecordRequest,
    ) -> CloudWatchLogsGetLogRecordResponse:
        client = self._require_client()
        return await self._execute(client.get_log_record, request, CloudWatchLogsGetLogRecordResponse)

    async def get_lookup_table(
        self,
        request: CloudWatchLogsGetLookupTableRequest,
    ) -> CloudWatchLogsGetLookupTableResponse:
        client = self._require_client()
        return await self._execute(client.get_lookup_table, request, CloudWatchLogsGetLookupTableResponse)

    async def get_query_results(
        self,
        request: CloudWatchLogsGetQueryResultsRequest,
    ) -> CloudWatchLogsGetQueryResultsResponse:
        client = self._require_client()
        return await self._execute(client.get_query_results, request, CloudWatchLogsGetQueryResultsResponse)

    async def get_scheduled_query(
        self,
        request: CloudWatchLogsGetScheduledQueryRequest,
    ) -> CloudWatchLogsGetScheduledQueryResponse:
        client = self._require_client()
        return await self._execute(client.get_scheduled_query, request, CloudWatchLogsGetScheduledQueryResponse)

    async def get_scheduled_query_history(
        self,
        request: CloudWatchLogsGetScheduledQueryHistoryRequest,
    ) -> CloudWatchLogsGetScheduledQueryHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_scheduled_query_history, request, CloudWatchLogsGetScheduledQueryHistoryResponse)

    async def get_scheduled_query_history_paginated(
        self,
        request: CloudWatchLogsGetScheduledQueryHistoryRequest,
    ) -> list[CloudWatchLogsGetScheduledQueryHistoryResponse]:
        return await self._paginate('get_scheduled_query_history', request, CloudWatchLogsGetScheduledQueryHistoryResponse)

    async def get_storage_tier_policy(
        self,
        request: CloudWatchLogsGetStorageTierPolicyRequest | None = None,
    ) -> CloudWatchLogsGetStorageTierPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_storage_tier_policy, request, CloudWatchLogsGetStorageTierPolicyResponse)

    async def get_transformer(
        self,
        request: CloudWatchLogsGetTransformerRequest,
    ) -> CloudWatchLogsGetTransformerResponse:
        client = self._require_client()
        return await self._execute(client.get_transformer, request, CloudWatchLogsGetTransformerResponse)

    async def list_aggregate_log_group_summaries(
        self,
        request: CloudWatchLogsListAggregateLogGroupSummariesRequest,
    ) -> CloudWatchLogsListAggregateLogGroupSummariesResponse:
        client = self._require_client()
        return await self._execute(client.list_aggregate_log_group_summaries, request, CloudWatchLogsListAggregateLogGroupSummariesResponse)

    async def list_aggregate_log_group_summaries_paginated(
        self,
        request: CloudWatchLogsListAggregateLogGroupSummariesRequest,
    ) -> list[CloudWatchLogsListAggregateLogGroupSummariesResponse]:
        return await self._paginate('list_aggregate_log_group_summaries', request, CloudWatchLogsListAggregateLogGroupSummariesResponse)

    async def list_anomalies(
        self,
        request: CloudWatchLogsListAnomaliesRequest | None = None,
    ) -> CloudWatchLogsListAnomaliesResponse:
        client = self._require_client()
        return await self._execute(client.list_anomalies, request, CloudWatchLogsListAnomaliesResponse)

    async def list_anomalies_paginated(
        self,
        request: CloudWatchLogsListAnomaliesRequest | None = None,
    ) -> list[CloudWatchLogsListAnomaliesResponse]:
        return await self._paginate('list_anomalies', request, CloudWatchLogsListAnomaliesResponse)

    async def list_integrations(
        self,
        request: CloudWatchLogsListIntegrationsRequest | None = None,
    ) -> CloudWatchLogsListIntegrationsResponse:
        client = self._require_client()
        return await self._execute(client.list_integrations, request, CloudWatchLogsListIntegrationsResponse)

    async def list_log_anomaly_detectors(
        self,
        request: CloudWatchLogsListLogAnomalyDetectorsRequest | None = None,
    ) -> CloudWatchLogsListLogAnomalyDetectorsResponse:
        client = self._require_client()
        return await self._execute(client.list_log_anomaly_detectors, request, CloudWatchLogsListLogAnomalyDetectorsResponse)

    async def list_log_anomaly_detectors_paginated(
        self,
        request: CloudWatchLogsListLogAnomalyDetectorsRequest | None = None,
    ) -> list[CloudWatchLogsListLogAnomalyDetectorsResponse]:
        return await self._paginate('list_log_anomaly_detectors', request, CloudWatchLogsListLogAnomalyDetectorsResponse)

    async def list_log_groups(
        self,
        request: CloudWatchLogsListLogGroupsRequest | None = None,
    ) -> CloudWatchLogsListLogGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_log_groups, request, CloudWatchLogsListLogGroupsResponse)

    async def list_log_groups_for_query(
        self,
        request: CloudWatchLogsListLogGroupsForQueryRequest,
    ) -> CloudWatchLogsListLogGroupsForQueryResponse:
        client = self._require_client()
        return await self._execute(client.list_log_groups_for_query, request, CloudWatchLogsListLogGroupsForQueryResponse)

    async def list_log_groups_for_query_paginated(
        self,
        request: CloudWatchLogsListLogGroupsForQueryRequest,
    ) -> list[CloudWatchLogsListLogGroupsForQueryResponse]:
        return await self._paginate('list_log_groups_for_query', request, CloudWatchLogsListLogGroupsForQueryResponse)

    async def list_scheduled_queries(
        self,
        request: CloudWatchLogsListScheduledQueriesRequest | None = None,
    ) -> CloudWatchLogsListScheduledQueriesResponse:
        client = self._require_client()
        return await self._execute(client.list_scheduled_queries, request, CloudWatchLogsListScheduledQueriesResponse)

    async def list_scheduled_queries_paginated(
        self,
        request: CloudWatchLogsListScheduledQueriesRequest | None = None,
    ) -> list[CloudWatchLogsListScheduledQueriesResponse]:
        return await self._paginate('list_scheduled_queries', request, CloudWatchLogsListScheduledQueriesResponse)

    async def list_sources_for_s3_table_integration(
        self,
        request: CloudWatchLogsListSourcesForS3TableIntegrationRequest,
    ) -> CloudWatchLogsListSourcesForS3TableIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.list_sources_for_s3_table_integration, request, CloudWatchLogsListSourcesForS3TableIntegrationResponse)

    async def list_sources_for_s3_table_integration_paginated(
        self,
        request: CloudWatchLogsListSourcesForS3TableIntegrationRequest,
    ) -> list[CloudWatchLogsListSourcesForS3TableIntegrationResponse]:
        return await self._paginate('list_sources_for_s3_table_integration', request, CloudWatchLogsListSourcesForS3TableIntegrationResponse)

    async def list_syslog_configurations(
        self,
        request: CloudWatchLogsListSyslogConfigurationsRequest | None = None,
    ) -> CloudWatchLogsListSyslogConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_syslog_configurations, request, CloudWatchLogsListSyslogConfigurationsResponse)

    async def list_tags_for_resource(
        self,
        request: CloudWatchLogsListTagsForResourceRequest,
    ) -> CloudWatchLogsListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, CloudWatchLogsListTagsForResourceResponse)

    async def list_tags_log_group(
        self,
        request: CloudWatchLogsListTagsLogGroupRequest,
    ) -> CloudWatchLogsListTagsLogGroupResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_log_group, request, CloudWatchLogsListTagsLogGroupResponse)

    async def put_account_policy(
        self,
        request: CloudWatchLogsPutAccountPolicyRequest,
    ) -> CloudWatchLogsPutAccountPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_account_policy, request, CloudWatchLogsPutAccountPolicyResponse)

    async def put_bearer_token_authentication(
        self,
        request: CloudWatchLogsPutBearerTokenAuthenticationRequest,
    ) -> CloudWatchLogsPutBearerTokenAuthenticationResponse:
        client = self._require_client()
        return await self._execute(client.put_bearer_token_authentication, request, CloudWatchLogsPutBearerTokenAuthenticationResponse)

    async def put_data_protection_policy(
        self,
        request: CloudWatchLogsPutDataProtectionPolicyRequest,
    ) -> CloudWatchLogsPutDataProtectionPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_data_protection_policy, request, CloudWatchLogsPutDataProtectionPolicyResponse)

    async def put_delivery_destination(
        self,
        request: CloudWatchLogsPutDeliveryDestinationRequest,
    ) -> CloudWatchLogsPutDeliveryDestinationResponse:
        client = self._require_client()
        return await self._execute(client.put_delivery_destination, request, CloudWatchLogsPutDeliveryDestinationResponse)

    async def put_delivery_destination_policy(
        self,
        request: CloudWatchLogsPutDeliveryDestinationPolicyRequest,
    ) -> CloudWatchLogsPutDeliveryDestinationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_delivery_destination_policy, request, CloudWatchLogsPutDeliveryDestinationPolicyResponse)

    async def put_delivery_source(
        self,
        request: CloudWatchLogsPutDeliverySourceRequest,
    ) -> CloudWatchLogsPutDeliverySourceResponse:
        client = self._require_client()
        return await self._execute(client.put_delivery_source, request, CloudWatchLogsPutDeliverySourceResponse)

    async def put_destination(
        self,
        request: CloudWatchLogsPutDestinationRequest,
    ) -> CloudWatchLogsPutDestinationResponse:
        client = self._require_client()
        return await self._execute(client.put_destination, request, CloudWatchLogsPutDestinationResponse)

    async def put_destination_policy(
        self,
        request: CloudWatchLogsPutDestinationPolicyRequest,
    ) -> CloudWatchLogsPutDestinationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_destination_policy, request, CloudWatchLogsPutDestinationPolicyResponse)

    async def put_index_policy(
        self,
        request: CloudWatchLogsPutIndexPolicyRequest,
    ) -> CloudWatchLogsPutIndexPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_index_policy, request, CloudWatchLogsPutIndexPolicyResponse)

    async def put_integration(
        self,
        request: CloudWatchLogsPutIntegrationRequest,
    ) -> CloudWatchLogsPutIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.put_integration, request, CloudWatchLogsPutIntegrationResponse)

    async def put_log_events(
        self,
        request: CloudWatchLogsPutLogEventsRequest,
    ) -> CloudWatchLogsPutLogEventsResponse:
        client = self._require_client()
        return await self._execute(client.put_log_events, request, CloudWatchLogsPutLogEventsResponse)

    async def put_log_group_deletion_protection(
        self,
        request: CloudWatchLogsPutLogGroupDeletionProtectionRequest,
    ) -> CloudWatchLogsPutLogGroupDeletionProtectionResponse:
        client = self._require_client()
        return await self._execute(client.put_log_group_deletion_protection, request, CloudWatchLogsPutLogGroupDeletionProtectionResponse)

    async def put_metric_filter(
        self,
        request: CloudWatchLogsPutMetricFilterRequest,
    ) -> CloudWatchLogsPutMetricFilterResponse:
        client = self._require_client()
        return await self._execute(client.put_metric_filter, request, CloudWatchLogsPutMetricFilterResponse)

    async def put_query_definition(
        self,
        request: CloudWatchLogsPutQueryDefinitionRequest,
    ) -> CloudWatchLogsPutQueryDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.put_query_definition, request, CloudWatchLogsPutQueryDefinitionResponse)

    async def put_resource_policy(
        self,
        request: CloudWatchLogsPutResourcePolicyRequest | None = None,
    ) -> CloudWatchLogsPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, CloudWatchLogsPutResourcePolicyResponse)

    async def put_retention_policy(
        self,
        request: CloudWatchLogsPutRetentionPolicyRequest,
    ) -> CloudWatchLogsPutRetentionPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_retention_policy, request, CloudWatchLogsPutRetentionPolicyResponse)

    async def put_storage_tier_policy(
        self,
        request: CloudWatchLogsPutStorageTierPolicyRequest,
    ) -> CloudWatchLogsPutStorageTierPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_storage_tier_policy, request, CloudWatchLogsPutStorageTierPolicyResponse)

    async def put_subscription_filter(
        self,
        request: CloudWatchLogsPutSubscriptionFilterRequest,
    ) -> CloudWatchLogsPutSubscriptionFilterResponse:
        client = self._require_client()
        return await self._execute(client.put_subscription_filter, request, CloudWatchLogsPutSubscriptionFilterResponse)

    async def put_syslog_configuration(
        self,
        request: CloudWatchLogsPutSyslogConfigurationRequest,
    ) -> CloudWatchLogsPutSyslogConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_syslog_configuration, request, CloudWatchLogsPutSyslogConfigurationResponse)

    async def put_transformer(
        self,
        request: CloudWatchLogsPutTransformerRequest,
    ) -> CloudWatchLogsPutTransformerResponse:
        client = self._require_client()
        return await self._execute(client.put_transformer, request, CloudWatchLogsPutTransformerResponse)

    async def start_live_tail(
        self,
        request: CloudWatchLogsStartLiveTailRequest,
    ) -> CloudWatchLogsStartLiveTailResponse:
        client = self._require_client()
        return await self._execute(client.start_live_tail, request, CloudWatchLogsStartLiveTailResponse)

    async def start_query(
        self,
        request: CloudWatchLogsStartQueryRequest,
    ) -> CloudWatchLogsStartQueryResponse:
        client = self._require_client()
        return await self._execute(client.start_query, request, CloudWatchLogsStartQueryResponse)

    async def stop_query(
        self,
        request: CloudWatchLogsStopQueryRequest,
    ) -> CloudWatchLogsStopQueryResponse:
        client = self._require_client()
        return await self._execute(client.stop_query, request, CloudWatchLogsStopQueryResponse)

    async def tag_log_group(
        self,
        request: CloudWatchLogsTagLogGroupRequest,
    ) -> CloudWatchLogsTagLogGroupResponse:
        client = self._require_client()
        return await self._execute(client.tag_log_group, request, CloudWatchLogsTagLogGroupResponse)

    async def tag_resource(
        self,
        request: CloudWatchLogsTagResourceRequest,
    ) -> CloudWatchLogsTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, CloudWatchLogsTagResourceResponse)

    async def test_metric_filter(
        self,
        request: CloudWatchLogsTestMetricFilterRequest,
    ) -> CloudWatchLogsTestMetricFilterResponse:
        client = self._require_client()
        return await self._execute(client.test_metric_filter, request, CloudWatchLogsTestMetricFilterResponse)

    async def test_transformer(
        self,
        request: CloudWatchLogsTestTransformerRequest,
    ) -> CloudWatchLogsTestTransformerResponse:
        client = self._require_client()
        return await self._execute(client.test_transformer, request, CloudWatchLogsTestTransformerResponse)

    async def untag_log_group(
        self,
        request: CloudWatchLogsUntagLogGroupRequest,
    ) -> CloudWatchLogsUntagLogGroupResponse:
        client = self._require_client()
        return await self._execute(client.untag_log_group, request, CloudWatchLogsUntagLogGroupResponse)

    async def untag_resource(
        self,
        request: CloudWatchLogsUntagResourceRequest,
    ) -> CloudWatchLogsUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, CloudWatchLogsUntagResourceResponse)

    async def update_anomaly(
        self,
        request: CloudWatchLogsUpdateAnomalyRequest,
    ) -> CloudWatchLogsUpdateAnomalyResponse:
        client = self._require_client()
        return await self._execute(client.update_anomaly, request, CloudWatchLogsUpdateAnomalyResponse)

    async def update_delivery_configuration(
        self,
        request: CloudWatchLogsUpdateDeliveryConfigurationRequest,
    ) -> CloudWatchLogsUpdateDeliveryConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_delivery_configuration, request, CloudWatchLogsUpdateDeliveryConfigurationResponse)

    async def update_log_anomaly_detector(
        self,
        request: CloudWatchLogsUpdateLogAnomalyDetectorRequest,
    ) -> CloudWatchLogsUpdateLogAnomalyDetectorResponse:
        client = self._require_client()
        return await self._execute(client.update_log_anomaly_detector, request, CloudWatchLogsUpdateLogAnomalyDetectorResponse)

    async def update_lookup_table(
        self,
        request: CloudWatchLogsUpdateLookupTableRequest,
    ) -> CloudWatchLogsUpdateLookupTableResponse:
        client = self._require_client()
        return await self._execute(client.update_lookup_table, request, CloudWatchLogsUpdateLookupTableResponse)

    async def update_scheduled_query(
        self,
        request: CloudWatchLogsUpdateScheduledQueryRequest,
    ) -> CloudWatchLogsUpdateScheduledQueryResponse:
        client = self._require_client()
        return await self._execute(client.update_scheduled_query, request, CloudWatchLogsUpdateScheduledQueryResponse)
