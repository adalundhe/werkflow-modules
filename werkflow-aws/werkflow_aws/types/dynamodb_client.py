from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class DynamoDBClient(ABC):

    @abstractmethod
    def list_tables(
        self,
        *,
        ExclusiveStartTableName: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_table(
        self,
        *,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_table(
        self,
        *,
        TableName: str,
        AttributeDefinitions: list[dict[str, Any]] | None = None,
        KeySchema: list[dict[str, Any]] | None = None,
        LocalSecondaryIndexes: list[dict[str, Any]] | None = None,
        GlobalSecondaryIndexes: list[dict[str, Any]] | None = None,
        BillingMode: str | None = None,
        ProvisionedThroughput: dict[str, Any] | None = None,
        StreamSpecification: dict[str, Any] | None = None,
        SSESpecification: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        TableClass: str | None = None,
        DeletionProtectionEnabled: bool | None = None,
        WarmThroughput: dict[str, Any] | None = None,
        ResourcePolicy: str | None = None,
        OnDemandThroughput: dict[str, Any] | None = None,
        GlobalTableSourceArn: str | None = None,
        GlobalTableSettingsReplicationMode: str | None = None,
        VectorIndexes: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_table(
        self,
        *,
        TableName: str,
        AttributeDefinitions: list[dict[str, Any]] | None = None,
        BillingMode: str | None = None,
        ProvisionedThroughput: dict[str, Any] | None = None,
        GlobalSecondaryIndexUpdates: list[dict[str, Any]] | None = None,
        StreamSpecification: dict[str, Any] | None = None,
        SSESpecification: dict[str, Any] | None = None,
        ReplicaUpdates: list[dict[str, Any]] | None = None,
        TableClass: str | None = None,
        DeletionProtectionEnabled: bool | None = None,
        MultiRegionConsistency: str | None = None,
        GlobalTableWitnessUpdates: list[dict[str, Any]] | None = None,
        OnDemandThroughput: dict[str, Any] | None = None,
        WarmThroughput: dict[str, Any] | None = None,
        GlobalTableSettingsReplicationMode: str | None = None,
        DisassociationProtectionEnabled: bool | None = None,
        VectorIndexUpdates: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_table(
        self,
        *,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_time_to_live(
        self,
        *,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_time_to_live(
        self,
        *,
        TableName: str,
        TimeToLiveSpecification: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_item(
        self,
        *,
        TableName: str,
        Key: dict[str, dict[str, Any]],
        AttributesToGet: list[str] | None = None,
        ConsistentRead: bool | None = None,
        ReturnConsumedCapacity: str | None = None,
        ProjectionExpression: str | None = None,
        ExpressionAttributeNames: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_item(
        self,
        *,
        TableName: str,
        Item: dict[str, dict[str, Any]],
        Expected: dict[str, dict[str, Any]] | None = None,
        ReturnValues: str | None = None,
        ReturnConsumedCapacity: str | None = None,
        ReturnItemCollectionMetrics: str | None = None,
        ConditionalOperator: str | None = None,
        ConditionExpression: str | None = None,
        ExpressionAttributeNames: dict[str, str] | None = None,
        ExpressionAttributeValues: dict[str, dict[str, Any]] | None = None,
        ReturnValuesOnConditionCheckFailure: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_item(
        self,
        *,
        TableName: str,
        Key: dict[str, dict[str, Any]],
        AttributeUpdates: dict[str, dict[str, Any]] | None = None,
        Expected: dict[str, dict[str, Any]] | None = None,
        ConditionalOperator: str | None = None,
        ReturnValues: str | None = None,
        ReturnConsumedCapacity: str | None = None,
        ReturnItemCollectionMetrics: str | None = None,
        UpdateExpression: str | None = None,
        ConditionExpression: str | None = None,
        ExpressionAttributeNames: dict[str, str] | None = None,
        ExpressionAttributeValues: dict[str, dict[str, Any]] | None = None,
        ReturnValuesOnConditionCheckFailure: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_item(
        self,
        *,
        TableName: str,
        Key: dict[str, dict[str, Any]],
        Expected: dict[str, dict[str, Any]] | None = None,
        ConditionalOperator: str | None = None,
        ReturnValues: str | None = None,
        ReturnConsumedCapacity: str | None = None,
        ReturnItemCollectionMetrics: str | None = None,
        ConditionExpression: str | None = None,
        ExpressionAttributeNames: dict[str, str] | None = None,
        ExpressionAttributeValues: dict[str, dict[str, Any]] | None = None,
        ReturnValuesOnConditionCheckFailure: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def query(
        self,
        *,
        TableName: str,
        IndexName: str | None = None,
        Select: str | None = None,
        AttributesToGet: list[str] | None = None,
        Limit: int | None = None,
        ConsistentRead: bool | None = None,
        KeyConditions: dict[str, dict[str, Any]] | None = None,
        QueryFilter: dict[str, dict[str, Any]] | None = None,
        ConditionalOperator: str | None = None,
        ScanIndexForward: bool | None = None,
        ExclusiveStartKey: dict[str, dict[str, Any]] | None = None,
        ReturnConsumedCapacity: str | None = None,
        ProjectionExpression: str | None = None,
        FilterExpression: str | None = None,
        KeyConditionExpression: str | None = None,
        ExpressionAttributeNames: dict[str, str] | None = None,
        ExpressionAttributeValues: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def scan(
        self,
        *,
        TableName: str,
        IndexName: str | None = None,
        AttributesToGet: list[str] | None = None,
        Limit: int | None = None,
        Select: str | None = None,
        ScanFilter: dict[str, dict[str, Any]] | None = None,
        ConditionalOperator: str | None = None,
        ExclusiveStartKey: dict[str, dict[str, Any]] | None = None,
        ReturnConsumedCapacity: str | None = None,
        TotalSegments: int | None = None,
        Segment: int | None = None,
        ProjectionExpression: str | None = None,
        FilterExpression: str | None = None,
        ExpressionAttributeNames: dict[str, str] | None = None,
        ExpressionAttributeValues: dict[str, dict[str, Any]] | None = None,
        ConsistentRead: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_item(
        self,
        *,
        RequestItems: dict[str, dict[str, Any]],
        ReturnConsumedCapacity: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_write_item(
        self,
        *,
        RequestItems: dict[str, list[dict[str, Any]]],
        ReturnConsumedCapacity: str | None = None,
        ReturnItemCollectionMetrics: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def transact_get_items(
        self,
        *,
        TransactItems: list[dict[str, Any]],
        ReturnConsumedCapacity: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def transact_write_items(
        self,
        *,
        TransactItems: list[dict[str, Any]],
        ReturnConsumedCapacity: str | None = None,
        ReturnItemCollectionMetrics: str | None = None,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_of_resource(
        self,
        *,
        ResourceArn: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_execute_statement(
        self,
        *,
        Statements: list[dict[str, Any]],
        ReturnConsumedCapacity: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_bulk_operation(
        self,
        *,
        BulkOperationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_backup(
        self,
        *,
        TableName: str,
        BackupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_global_table(
        self,
        *,
        GlobalTableName: str,
        ReplicationGroup: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_backup(
        self,
        *,
        BackupArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        ResourceArn: str,
        ExpectedRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_backup(
        self,
        *,
        BackupArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bulk_operation(
        self,
        *,
        BulkOperationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_continuous_backups(
        self,
        *,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_contributor_insights(
        self,
        *,
        TableName: str,
        IndexName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoints(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_export(
        self,
        *,
        ExportArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_global_table(
        self,
        *,
        GlobalTableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_global_table_settings(
        self,
        *,
        GlobalTableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_import(
        self,
        *,
        ImportArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_kinesis_streaming_destination(
        self,
        *,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_limits(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_table_replica_auto_scaling(
        self,
        *,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_kinesis_streaming_destination(
        self,
        *,
        TableName: str,
        StreamArn: str,
        EnableKinesisStreamingConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_kinesis_streaming_destination(
        self,
        *,
        TableName: str,
        StreamArn: str,
        EnableKinesisStreamingConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute_statement(
        self,
        *,
        Statement: str,
        Parameters: list[dict[str, Any]] | None = None,
        ConsistentRead: bool | None = None,
        NextToken: str | None = None,
        ReturnConsumedCapacity: str | None = None,
        Limit: int | None = None,
        ReturnValuesOnConditionCheckFailure: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute_transaction(
        self,
        *,
        TransactStatements: list[dict[str, Any]],
        ClientRequestToken: str | None = None,
        ReturnConsumedCapacity: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_table_to_point_in_time(
        self,
        *,
        TableArn: str,
        S3Bucket: str,
        ExportTime: datetime.datetime | str | None = None,
        ClientToken: str | None = None,
        S3BucketOwner: str | None = None,
        S3Prefix: str | None = None,
        S3SseAlgorithm: str | None = None,
        S3SseKmsKeyId: str | None = None,
        ExportFormat: str | None = None,
        ExportType: str | None = None,
        IncrementalExportSpecification: dict[str, Any] | None = None,
        FilterSpecification: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_table(
        self,
        *,
        S3BucketSource: dict[str, Any],
        InputFormat: str,
        TableCreationParameters: dict[str, Any],
        ClientToken: str | None = None,
        InputFormatOptions: dict[str, Any] | None = None,
        InputCompressionType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_backups(
        self,
        *,
        TableName: str | None = None,
        Limit: int | None = None,
        TimeRangeLowerBound: datetime.datetime | str | None = None,
        TimeRangeUpperBound: datetime.datetime | str | None = None,
        ExclusiveStartBackupArn: str | None = None,
        BackupType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bulk_operations(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contributor_insights(
        self,
        *,
        TableName: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_exports(
        self,
        *,
        TableArn: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_global_tables(
        self,
        *,
        ExclusiveStartGlobalTableName: str | None = None,
        Limit: int | None = None,
        RegionName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_imports(
        self,
        *,
        TableArn: str | None = None,
        PageSize: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        ResourceArn: str,
        Policy: str,
        ExpectedRevisionId: str | None = None,
        ConfirmRemoveSelfResourceAccess: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_table_from_backup(
        self,
        *,
        TargetTableName: str,
        BackupArn: str,
        BillingModeOverride: str | None = None,
        GlobalSecondaryIndexOverride: list[dict[str, Any]] | None = None,
        LocalSecondaryIndexOverride: list[dict[str, Any]] | None = None,
        ProvisionedThroughputOverride: dict[str, Any] | None = None,
        OnDemandThroughputOverride: dict[str, Any] | None = None,
        SSESpecificationOverride: dict[str, Any] | None = None,
        VectorIndexOverride: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_table_to_point_in_time(
        self,
        *,
        TargetTableName: str,
        SourceTableArn: str | None = None,
        SourceTableName: str | None = None,
        UseLatestRestorableTime: bool | None = None,
        RestoreDateTime: datetime.datetime | str | None = None,
        BillingModeOverride: str | None = None,
        GlobalSecondaryIndexOverride: list[dict[str, Any]] | None = None,
        LocalSecondaryIndexOverride: list[dict[str, Any]] | None = None,
        ProvisionedThroughputOverride: dict[str, Any] | None = None,
        OnDemandThroughputOverride: dict[str, Any] | None = None,
        SSESpecificationOverride: dict[str, Any] | None = None,
        VectorIndexOverride: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_vectors(
        self,
        *,
        TableName: str,
        IndexName: str,
        SearchVector: list[dict[str, Any]],
        TopK: int,
        ReturnConsumedCapacity: str | None = None,
        ExpressionAttributeNames: dict[str, str] | None = None,
        ExpressionAttributeValues: dict[str, dict[str, Any]] | None = None,
        ProjectionExpression: str | None = None,
        SearchConditionExpression: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_bulk_put_items(
        self,
        *,
        InputS3Configuration: dict[str, Any],
        OutputS3Configuration: dict[str, Any],
        TableName: str,
        ClientToken: str | None = None,
        MaxWriteRequestUnits: int | None = None,
        PerformanceTier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_continuous_backups(
        self,
        *,
        TableName: str,
        PointInTimeRecoverySpecification: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contributor_insights(
        self,
        *,
        TableName: str,
        ContributorInsightsAction: str,
        IndexName: str | None = None,
        ContributorInsightsMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_global_table(
        self,
        *,
        GlobalTableName: str,
        ReplicaUpdates: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_global_table_settings(
        self,
        *,
        GlobalTableName: str,
        GlobalTableBillingMode: str | None = None,
        GlobalTableProvisionedWriteCapacityUnits: int | None = None,
        GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: dict[str, Any] | None = None,
        GlobalTableGlobalSecondaryIndexSettingsUpdate: list[dict[str, Any]] | None = None,
        ReplicaSettingsUpdate: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_kinesis_streaming_destination(
        self,
        *,
        TableName: str,
        StreamArn: str,
        UpdateKinesisStreamingConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_table_replica_auto_scaling(
        self,
        *,
        TableName: str,
        GlobalSecondaryIndexUpdates: list[dict[str, Any]] | None = None,
        ProvisionedWriteCapacityAutoScalingUpdate: dict[str, Any] | None = None,
        ReplicaUpdates: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
