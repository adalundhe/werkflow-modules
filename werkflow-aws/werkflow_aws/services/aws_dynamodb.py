from werkflow_aws.models.dynamodb import (
    DynamoDBBatchGetItemRequest,
    DynamoDBBatchGetItemResponse,
    DynamoDBBatchWriteItemRequest,
    DynamoDBBatchWriteItemResponse,
    DynamoDBCreateTableRequest,
    DynamoDBCreateTableResponse,
    DynamoDBDeleteItemRequest,
    DynamoDBDeleteItemResponse,
    DynamoDBDeleteTableRequest,
    DynamoDBDeleteTableResponse,
    DynamoDBDescribeTableRequest,
    DynamoDBDescribeTableResponse,
    DynamoDBDescribeTimeToLiveRequest,
    DynamoDBDescribeTimeToLiveResponse,
    DynamoDBGetItemRequest,
    DynamoDBGetItemResponse,
    DynamoDBListTablesRequest,
    DynamoDBListTablesResponse,
    DynamoDBListTagsOfResourceRequest,
    DynamoDBListTagsOfResourceResponse,
    DynamoDBPutItemRequest,
    DynamoDBPutItemResponse,
    DynamoDBQueryRequest,
    DynamoDBQueryResponse,
    DynamoDBScanRequest,
    DynamoDBScanResponse,
    DynamoDBTagResourceRequest,
    DynamoDBTagResourceResponse,
    DynamoDBTransactGetItemsRequest,
    DynamoDBTransactGetItemsResponse,
    DynamoDBTransactWriteItemsRequest,
    DynamoDBTransactWriteItemsResponse,
    DynamoDBUntagResourceRequest,
    DynamoDBUntagResourceResponse,
    DynamoDBUpdateItemRequest,
    DynamoDBUpdateItemResponse,
    DynamoDBUpdateTableRequest,
    DynamoDBUpdateTableResponse,
    DynamoDBUpdateTimeToLiveRequest,
    DynamoDBUpdateTimeToLiveResponse,
)
from werkflow_aws.types.dynamodb_client import DynamoDBClient
from .base import AWSBaseService
from werkflow_aws.models.dynamodb import (
    DynamoDBBatchExecuteStatementRequest,
    DynamoDBBatchExecuteStatementResponse,
    DynamoDBCancelBulkOperationRequest,
    DynamoDBCancelBulkOperationResponse,
    DynamoDBCreateBackupRequest,
    DynamoDBCreateBackupResponse,
    DynamoDBCreateGlobalTableRequest,
    DynamoDBCreateGlobalTableResponse,
    DynamoDBDeleteBackupRequest,
    DynamoDBDeleteBackupResponse,
    DynamoDBDeleteResourcePolicyRequest,
    DynamoDBDeleteResourcePolicyResponse,
    DynamoDBDescribeBackupRequest,
    DynamoDBDescribeBackupResponse,
    DynamoDBDescribeBulkOperationRequest,
    DynamoDBDescribeBulkOperationResponse,
    DynamoDBDescribeContinuousBackupsRequest,
    DynamoDBDescribeContinuousBackupsResponse,
    DynamoDBDescribeContributorInsightsRequest,
    DynamoDBDescribeContributorInsightsResponse,
    DynamoDBDescribeEndpointsRequest,
    DynamoDBDescribeEndpointsResponse,
    DynamoDBDescribeExportRequest,
    DynamoDBDescribeExportResponse,
    DynamoDBDescribeGlobalTableRequest,
    DynamoDBDescribeGlobalTableResponse,
    DynamoDBDescribeGlobalTableSettingsRequest,
    DynamoDBDescribeGlobalTableSettingsResponse,
    DynamoDBDescribeImportRequest,
    DynamoDBDescribeImportResponse,
    DynamoDBDescribeKinesisStreamingDestinationRequest,
    DynamoDBDescribeKinesisStreamingDestinationResponse,
    DynamoDBDescribeLimitsRequest,
    DynamoDBDescribeLimitsResponse,
    DynamoDBDescribeTableReplicaAutoScalingRequest,
    DynamoDBDescribeTableReplicaAutoScalingResponse,
    DynamoDBDisableKinesisStreamingDestinationRequest,
    DynamoDBDisableKinesisStreamingDestinationResponse,
    DynamoDBEnableKinesisStreamingDestinationRequest,
    DynamoDBEnableKinesisStreamingDestinationResponse,
    DynamoDBExecuteStatementRequest,
    DynamoDBExecuteStatementResponse,
    DynamoDBExecuteTransactionRequest,
    DynamoDBExecuteTransactionResponse,
    DynamoDBExportTableToPointInTimeRequest,
    DynamoDBExportTableToPointInTimeResponse,
    DynamoDBGetResourcePolicyRequest,
    DynamoDBGetResourcePolicyResponse,
    DynamoDBImportTableRequest,
    DynamoDBImportTableResponse,
    DynamoDBListBackupsRequest,
    DynamoDBListBackupsResponse,
    DynamoDBListBulkOperationsRequest,
    DynamoDBListBulkOperationsResponse,
    DynamoDBListContributorInsightsRequest,
    DynamoDBListContributorInsightsResponse,
    DynamoDBListExportsRequest,
    DynamoDBListExportsResponse,
    DynamoDBListGlobalTablesRequest,
    DynamoDBListGlobalTablesResponse,
    DynamoDBListImportsRequest,
    DynamoDBListImportsResponse,
    DynamoDBPutResourcePolicyRequest,
    DynamoDBPutResourcePolicyResponse,
    DynamoDBRestoreTableFromBackupRequest,
    DynamoDBRestoreTableFromBackupResponse,
    DynamoDBRestoreTableToPointInTimeRequest,
    DynamoDBRestoreTableToPointInTimeResponse,
    DynamoDBSearchVectorsRequest,
    DynamoDBSearchVectorsResponse,
    DynamoDBStartBulkPutItemsRequest,
    DynamoDBStartBulkPutItemsResponse,
    DynamoDBUpdateContinuousBackupsRequest,
    DynamoDBUpdateContinuousBackupsResponse,
    DynamoDBUpdateContributorInsightsRequest,
    DynamoDBUpdateContributorInsightsResponse,
    DynamoDBUpdateGlobalTableRequest,
    DynamoDBUpdateGlobalTableResponse,
    DynamoDBUpdateGlobalTableSettingsRequest,
    DynamoDBUpdateGlobalTableSettingsResponse,
    DynamoDBUpdateKinesisStreamingDestinationRequest,
    DynamoDBUpdateKinesisStreamingDestinationResponse,
    DynamoDBUpdateTableReplicaAutoScalingRequest,
    DynamoDBUpdateTableReplicaAutoScalingResponse,
)


class AWSDynamoDB(AWSBaseService[DynamoDBClient]):
    service_name = 'DynamoDB'
    boto3_service_name = 'dynamodb'

    def __init__(self) -> None:
        super().__init__(
            service_name='DynamoDB',
            boto3_service_name='dynamodb',
        )

    async def list_tables(
        self,
        request: DynamoDBListTablesRequest | None = None,
    ) -> DynamoDBListTablesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_tables,
            request or DynamoDBListTablesRequest(),
            DynamoDBListTablesResponse,
        )

    async def list_tables_paginated(
        self,
        request: DynamoDBListTablesRequest | None = None,
    ) -> list[DynamoDBListTablesResponse]:
        return await self._paginate(
            'list_tables',
            request or DynamoDBListTablesRequest(),
            DynamoDBListTablesResponse,
        )

    async def describe_table(
        self,
        request: DynamoDBDescribeTableRequest,
    ) -> DynamoDBDescribeTableResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_table,
            request,
            DynamoDBDescribeTableResponse,
        )

    async def create_table(
        self,
        request: DynamoDBCreateTableRequest,
    ) -> DynamoDBCreateTableResponse:
        client = self._require_client()
        return await self._execute(
            client.create_table,
            request,
            DynamoDBCreateTableResponse,
        )

    async def update_table(
        self,
        request: DynamoDBUpdateTableRequest,
    ) -> DynamoDBUpdateTableResponse:
        client = self._require_client()
        return await self._execute(
            client.update_table,
            request,
            DynamoDBUpdateTableResponse,
        )

    async def delete_table(
        self,
        request: DynamoDBDeleteTableRequest,
    ) -> DynamoDBDeleteTableResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_table,
            request,
            DynamoDBDeleteTableResponse,
        )

    async def describe_time_to_live(
        self,
        request: DynamoDBDescribeTimeToLiveRequest,
    ) -> DynamoDBDescribeTimeToLiveResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_time_to_live,
            request,
            DynamoDBDescribeTimeToLiveResponse,
        )

    async def update_time_to_live(
        self,
        request: DynamoDBUpdateTimeToLiveRequest,
    ) -> DynamoDBUpdateTimeToLiveResponse:
        client = self._require_client()
        return await self._execute(
            client.update_time_to_live,
            request,
            DynamoDBUpdateTimeToLiveResponse,
        )

    async def get_item(
        self,
        request: DynamoDBGetItemRequest,
    ) -> DynamoDBGetItemResponse:
        client = self._require_client()
        return await self._execute(
            client.get_item,
            request,
            DynamoDBGetItemResponse,
        )

    async def put_item(
        self,
        request: DynamoDBPutItemRequest,
    ) -> DynamoDBPutItemResponse:
        client = self._require_client()
        return await self._execute(
            client.put_item,
            request,
            DynamoDBPutItemResponse,
        )

    async def update_item(
        self,
        request: DynamoDBUpdateItemRequest,
    ) -> DynamoDBUpdateItemResponse:
        client = self._require_client()
        return await self._execute(
            client.update_item,
            request,
            DynamoDBUpdateItemResponse,
        )

    async def delete_item(
        self,
        request: DynamoDBDeleteItemRequest,
    ) -> DynamoDBDeleteItemResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_item,
            request,
            DynamoDBDeleteItemResponse,
        )

    async def query(
        self,
        request: DynamoDBQueryRequest,
    ) -> DynamoDBQueryResponse:
        client = self._require_client()
        return await self._execute(
            client.query,
            request,
            DynamoDBQueryResponse,
        )

    async def query_paginated(
        self,
        request: DynamoDBQueryRequest,
    ) -> list[DynamoDBQueryResponse]:
        return await self._paginate(
            'query',
            request,
            DynamoDBQueryResponse,
        )

    async def scan(
        self,
        request: DynamoDBScanRequest,
    ) -> DynamoDBScanResponse:
        client = self._require_client()
        return await self._execute(
            client.scan,
            request,
            DynamoDBScanResponse,
        )

    async def scan_paginated(
        self,
        request: DynamoDBScanRequest,
    ) -> list[DynamoDBScanResponse]:
        return await self._paginate(
            'scan',
            request,
            DynamoDBScanResponse,
        )

    async def batch_get_item(
        self,
        request: DynamoDBBatchGetItemRequest,
    ) -> DynamoDBBatchGetItemResponse:
        client = self._require_client()
        return await self._execute(
            client.batch_get_item,
            request,
            DynamoDBBatchGetItemResponse,
        )

    async def batch_write_item(
        self,
        request: DynamoDBBatchWriteItemRequest,
    ) -> DynamoDBBatchWriteItemResponse:
        client = self._require_client()
        return await self._execute(
            client.batch_write_item,
            request,
            DynamoDBBatchWriteItemResponse,
        )

    async def transact_get_items(
        self,
        request: DynamoDBTransactGetItemsRequest,
    ) -> DynamoDBTransactGetItemsResponse:
        client = self._require_client()
        return await self._execute(
            client.transact_get_items,
            request,
            DynamoDBTransactGetItemsResponse,
        )

    async def transact_write_items(
        self,
        request: DynamoDBTransactWriteItemsRequest,
    ) -> DynamoDBTransactWriteItemsResponse:
        client = self._require_client()
        return await self._execute(
            client.transact_write_items,
            request,
            DynamoDBTransactWriteItemsResponse,
        )

    async def tag_resource(
        self,
        request: DynamoDBTagResourceRequest,
    ) -> DynamoDBTagResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.tag_resource,
            request,
            DynamoDBTagResourceResponse,
        )

    async def untag_resource(
        self,
        request: DynamoDBUntagResourceRequest,
    ) -> DynamoDBUntagResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.untag_resource,
            request,
            DynamoDBUntagResourceResponse,
        )

    async def list_tags_of_resource(
        self,
        request: DynamoDBListTagsOfResourceRequest,
    ) -> DynamoDBListTagsOfResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.list_tags_of_resource,
            request,
            DynamoDBListTagsOfResourceResponse,
        )

    async def list_tags_of_resource_paginated(
        self,
        request: DynamoDBListTagsOfResourceRequest,
    ) -> list[DynamoDBListTagsOfResourceResponse]:
        return await self._paginate(
            'list_tags_of_resource',
            request,
            DynamoDBListTagsOfResourceResponse,
        )

    async def batch_execute_statement(
        self,
        request: DynamoDBBatchExecuteStatementRequest,
    ) -> DynamoDBBatchExecuteStatementResponse:
        client = self._require_client()
        return await self._execute(client.batch_execute_statement, request, DynamoDBBatchExecuteStatementResponse)

    async def cancel_bulk_operation(
        self,
        request: DynamoDBCancelBulkOperationRequest,
    ) -> DynamoDBCancelBulkOperationResponse:
        client = self._require_client()
        return await self._execute(client.cancel_bulk_operation, request, DynamoDBCancelBulkOperationResponse)

    async def create_backup(
        self,
        request: DynamoDBCreateBackupRequest,
    ) -> DynamoDBCreateBackupResponse:
        client = self._require_client()
        return await self._execute(client.create_backup, request, DynamoDBCreateBackupResponse)

    async def create_global_table(
        self,
        request: DynamoDBCreateGlobalTableRequest,
    ) -> DynamoDBCreateGlobalTableResponse:
        client = self._require_client()
        return await self._execute(client.create_global_table, request, DynamoDBCreateGlobalTableResponse)

    async def delete_backup(
        self,
        request: DynamoDBDeleteBackupRequest,
    ) -> DynamoDBDeleteBackupResponse:
        client = self._require_client()
        return await self._execute(client.delete_backup, request, DynamoDBDeleteBackupResponse)

    async def delete_resource_policy(
        self,
        request: DynamoDBDeleteResourcePolicyRequest,
    ) -> DynamoDBDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, DynamoDBDeleteResourcePolicyResponse)

    async def describe_backup(
        self,
        request: DynamoDBDescribeBackupRequest,
    ) -> DynamoDBDescribeBackupResponse:
        client = self._require_client()
        return await self._execute(client.describe_backup, request, DynamoDBDescribeBackupResponse)

    async def describe_bulk_operation(
        self,
        request: DynamoDBDescribeBulkOperationRequest,
    ) -> DynamoDBDescribeBulkOperationResponse:
        client = self._require_client()
        return await self._execute(client.describe_bulk_operation, request, DynamoDBDescribeBulkOperationResponse)

    async def describe_continuous_backups(
        self,
        request: DynamoDBDescribeContinuousBackupsRequest,
    ) -> DynamoDBDescribeContinuousBackupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_continuous_backups, request, DynamoDBDescribeContinuousBackupsResponse)

    async def describe_contributor_insights(
        self,
        request: DynamoDBDescribeContributorInsightsRequest,
    ) -> DynamoDBDescribeContributorInsightsResponse:
        client = self._require_client()
        return await self._execute(client.describe_contributor_insights, request, DynamoDBDescribeContributorInsightsResponse)

    async def describe_endpoints(
        self,
        request: DynamoDBDescribeEndpointsRequest | None = None,
    ) -> DynamoDBDescribeEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_endpoints, request, DynamoDBDescribeEndpointsResponse)

    async def describe_export(
        self,
        request: DynamoDBDescribeExportRequest,
    ) -> DynamoDBDescribeExportResponse:
        client = self._require_client()
        return await self._execute(client.describe_export, request, DynamoDBDescribeExportResponse)

    async def describe_global_table(
        self,
        request: DynamoDBDescribeGlobalTableRequest,
    ) -> DynamoDBDescribeGlobalTableResponse:
        client = self._require_client()
        return await self._execute(client.describe_global_table, request, DynamoDBDescribeGlobalTableResponse)

    async def describe_global_table_settings(
        self,
        request: DynamoDBDescribeGlobalTableSettingsRequest,
    ) -> DynamoDBDescribeGlobalTableSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_global_table_settings, request, DynamoDBDescribeGlobalTableSettingsResponse)

    async def describe_import(
        self,
        request: DynamoDBDescribeImportRequest,
    ) -> DynamoDBDescribeImportResponse:
        client = self._require_client()
        return await self._execute(client.describe_import, request, DynamoDBDescribeImportResponse)

    async def describe_kinesis_streaming_destination(
        self,
        request: DynamoDBDescribeKinesisStreamingDestinationRequest,
    ) -> DynamoDBDescribeKinesisStreamingDestinationResponse:
        client = self._require_client()
        return await self._execute(client.describe_kinesis_streaming_destination, request, DynamoDBDescribeKinesisStreamingDestinationResponse)

    async def describe_limits(
        self,
        request: DynamoDBDescribeLimitsRequest | None = None,
    ) -> DynamoDBDescribeLimitsResponse:
        client = self._require_client()
        return await self._execute(client.describe_limits, request, DynamoDBDescribeLimitsResponse)

    async def describe_table_replica_auto_scaling(
        self,
        request: DynamoDBDescribeTableReplicaAutoScalingRequest,
    ) -> DynamoDBDescribeTableReplicaAutoScalingResponse:
        client = self._require_client()
        return await self._execute(client.describe_table_replica_auto_scaling, request, DynamoDBDescribeTableReplicaAutoScalingResponse)

    async def disable_kinesis_streaming_destination(
        self,
        request: DynamoDBDisableKinesisStreamingDestinationRequest,
    ) -> DynamoDBDisableKinesisStreamingDestinationResponse:
        client = self._require_client()
        return await self._execute(client.disable_kinesis_streaming_destination, request, DynamoDBDisableKinesisStreamingDestinationResponse)

    async def enable_kinesis_streaming_destination(
        self,
        request: DynamoDBEnableKinesisStreamingDestinationRequest,
    ) -> DynamoDBEnableKinesisStreamingDestinationResponse:
        client = self._require_client()
        return await self._execute(client.enable_kinesis_streaming_destination, request, DynamoDBEnableKinesisStreamingDestinationResponse)

    async def execute_statement(
        self,
        request: DynamoDBExecuteStatementRequest,
    ) -> DynamoDBExecuteStatementResponse:
        client = self._require_client()
        return await self._execute(client.execute_statement, request, DynamoDBExecuteStatementResponse)

    async def execute_transaction(
        self,
        request: DynamoDBExecuteTransactionRequest,
    ) -> DynamoDBExecuteTransactionResponse:
        client = self._require_client()
        return await self._execute(client.execute_transaction, request, DynamoDBExecuteTransactionResponse)

    async def export_table_to_point_in_time(
        self,
        request: DynamoDBExportTableToPointInTimeRequest,
    ) -> DynamoDBExportTableToPointInTimeResponse:
        client = self._require_client()
        return await self._execute(client.export_table_to_point_in_time, request, DynamoDBExportTableToPointInTimeResponse)

    async def get_resource_policy(
        self,
        request: DynamoDBGetResourcePolicyRequest,
    ) -> DynamoDBGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, DynamoDBGetResourcePolicyResponse)

    async def import_table(
        self,
        request: DynamoDBImportTableRequest,
    ) -> DynamoDBImportTableResponse:
        client = self._require_client()
        return await self._execute(client.import_table, request, DynamoDBImportTableResponse)

    async def list_backups(
        self,
        request: DynamoDBListBackupsRequest | None = None,
    ) -> DynamoDBListBackupsResponse:
        client = self._require_client()
        return await self._execute(client.list_backups, request, DynamoDBListBackupsResponse)

    async def list_backups_paginated(
        self,
        request: DynamoDBListBackupsRequest | None = None,
    ) -> list[DynamoDBListBackupsResponse]:
        return await self._paginate('list_backups', request, DynamoDBListBackupsResponse)

    async def list_bulk_operations(
        self,
        request: DynamoDBListBulkOperationsRequest | None = None,
    ) -> DynamoDBListBulkOperationsResponse:
        client = self._require_client()
        return await self._execute(client.list_bulk_operations, request, DynamoDBListBulkOperationsResponse)

    async def list_bulk_operations_paginated(
        self,
        request: DynamoDBListBulkOperationsRequest | None = None,
    ) -> list[DynamoDBListBulkOperationsResponse]:
        return await self._paginate('list_bulk_operations', request, DynamoDBListBulkOperationsResponse)

    async def list_contributor_insights(
        self,
        request: DynamoDBListContributorInsightsRequest | None = None,
    ) -> DynamoDBListContributorInsightsResponse:
        client = self._require_client()
        return await self._execute(client.list_contributor_insights, request, DynamoDBListContributorInsightsResponse)

    async def list_exports(
        self,
        request: DynamoDBListExportsRequest | None = None,
    ) -> DynamoDBListExportsResponse:
        client = self._require_client()
        return await self._execute(client.list_exports, request, DynamoDBListExportsResponse)

    async def list_global_tables(
        self,
        request: DynamoDBListGlobalTablesRequest | None = None,
    ) -> DynamoDBListGlobalTablesResponse:
        client = self._require_client()
        return await self._execute(client.list_global_tables, request, DynamoDBListGlobalTablesResponse)

    async def list_imports(
        self,
        request: DynamoDBListImportsRequest | None = None,
    ) -> DynamoDBListImportsResponse:
        client = self._require_client()
        return await self._execute(client.list_imports, request, DynamoDBListImportsResponse)

    async def put_resource_policy(
        self,
        request: DynamoDBPutResourcePolicyRequest,
    ) -> DynamoDBPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, DynamoDBPutResourcePolicyResponse)

    async def restore_table_from_backup(
        self,
        request: DynamoDBRestoreTableFromBackupRequest,
    ) -> DynamoDBRestoreTableFromBackupResponse:
        client = self._require_client()
        return await self._execute(client.restore_table_from_backup, request, DynamoDBRestoreTableFromBackupResponse)

    async def restore_table_to_point_in_time(
        self,
        request: DynamoDBRestoreTableToPointInTimeRequest,
    ) -> DynamoDBRestoreTableToPointInTimeResponse:
        client = self._require_client()
        return await self._execute(client.restore_table_to_point_in_time, request, DynamoDBRestoreTableToPointInTimeResponse)

    async def search_vectors(
        self,
        request: DynamoDBSearchVectorsRequest,
    ) -> DynamoDBSearchVectorsResponse:
        client = self._require_client()
        return await self._execute(client.search_vectors, request, DynamoDBSearchVectorsResponse)

    async def start_bulk_put_items(
        self,
        request: DynamoDBStartBulkPutItemsRequest,
    ) -> DynamoDBStartBulkPutItemsResponse:
        client = self._require_client()
        return await self._execute(client.start_bulk_put_items, request, DynamoDBStartBulkPutItemsResponse)

    async def update_continuous_backups(
        self,
        request: DynamoDBUpdateContinuousBackupsRequest,
    ) -> DynamoDBUpdateContinuousBackupsResponse:
        client = self._require_client()
        return await self._execute(client.update_continuous_backups, request, DynamoDBUpdateContinuousBackupsResponse)

    async def update_contributor_insights(
        self,
        request: DynamoDBUpdateContributorInsightsRequest,
    ) -> DynamoDBUpdateContributorInsightsResponse:
        client = self._require_client()
        return await self._execute(client.update_contributor_insights, request, DynamoDBUpdateContributorInsightsResponse)

    async def update_global_table(
        self,
        request: DynamoDBUpdateGlobalTableRequest,
    ) -> DynamoDBUpdateGlobalTableResponse:
        client = self._require_client()
        return await self._execute(client.update_global_table, request, DynamoDBUpdateGlobalTableResponse)

    async def update_global_table_settings(
        self,
        request: DynamoDBUpdateGlobalTableSettingsRequest,
    ) -> DynamoDBUpdateGlobalTableSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_global_table_settings, request, DynamoDBUpdateGlobalTableSettingsResponse)

    async def update_kinesis_streaming_destination(
        self,
        request: DynamoDBUpdateKinesisStreamingDestinationRequest,
    ) -> DynamoDBUpdateKinesisStreamingDestinationResponse:
        client = self._require_client()
        return await self._execute(client.update_kinesis_streaming_destination, request, DynamoDBUpdateKinesisStreamingDestinationResponse)

    async def update_table_replica_auto_scaling(
        self,
        request: DynamoDBUpdateTableReplicaAutoScalingRequest,
    ) -> DynamoDBUpdateTableReplicaAutoScalingResponse:
        client = self._require_client()
        return await self._execute(client.update_table_replica_auto_scaling, request, DynamoDBUpdateTableReplicaAutoScalingResponse)

