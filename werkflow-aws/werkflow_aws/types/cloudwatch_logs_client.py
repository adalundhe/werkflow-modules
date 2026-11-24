from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class CloudWatchLogsClient(ABC):

    @abstractmethod
    def associate_kms_key(
        self,
        *,
        kmsKeyId: str,
        logGroupName: str | None = None,
        resourceIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_source_to_s3_table_integration(
        self,
        *,
        integrationArn: str,
        dataSource: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_export_task(
        self,
        *,
        taskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_import_task(
        self,
        *,
        importId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_delivery(
        self,
        *,
        deliverySourceName: str,
        deliveryDestinationArn: str,
        recordFields: list[str] | None = None,
        fieldDelimiter: str | None = None,
        s3DeliveryConfiguration: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_export_task(
        self,
        *,
        logGroupName: str,
        to: int,
        destination: str,
        taskName: str | None = None,
        logStreamNamePrefix: str | None = None,
        destinationPrefix: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_import_task(
        self,
        *,
        importSourceArn: str,
        importRoleArn: str,
        importFilter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_log_anomaly_detector(
        self,
        *,
        logGroupArnList: list[str],
        detectorName: str | None = None,
        evaluationFrequency: str | None = None,
        filterPattern: str | None = None,
        kmsKeyId: str | None = None,
        anomalyVisibilityTime: int | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_log_group(
        self,
        *,
        logGroupName: str,
        kmsKeyId: str | None = None,
        tags: dict[str, str] | None = None,
        logGroupClass: str | None = None,
        deletionProtectionEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_log_stream(
        self,
        *,
        logGroupName: str,
        logStreamName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_lookup_table(
        self,
        *,
        lookupTableName: str,
        description: str | None = None,
        tableBody: str | None = None,
        queryId: str | None = None,
        kmsKeyId: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_scheduled_query(
        self,
        *,
        name: str,
        queryLanguage: str,
        queryString: str,
        scheduleExpression: str,
        executionRoleArn: str,
        description: str | None = None,
        logGroupIdentifiers: list[str] | None = None,
        timezone: str | None = None,
        startTimeOffset: int | None = None,
        endTimeOffset: int | None = None,
        destinationConfiguration: dict[str, Any] | None = None,
        scheduleStartTime: int | None = None,
        scheduleEndTime: int | None = None,
        state: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_policy(
        self,
        *,
        policyName: str,
        policyType: str,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_protection_policy(
        self,
        *,
        logGroupIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_delivery(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_delivery_destination(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_delivery_destination_policy(
        self,
        *,
        deliveryDestinationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_delivery_source(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_destination(
        self,
        *,
        destinationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_index_policy(
        self,
        *,
        logGroupIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_integration(
        self,
        *,
        integrationName: str,
        force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_log_anomaly_detector(
        self,
        *,
        anomalyDetectorArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_log_group(
        self,
        *,
        logGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_log_stream(
        self,
        *,
        logGroupName: str,
        logStreamName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lookup_table(
        self,
        *,
        lookupTableArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_metric_filter(
        self,
        *,
        logGroupName: str,
        filterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_query_definition(
        self,
        *,
        queryDefinitionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        policyName: str | None = None,
        resourceArn: str | None = None,
        expectedRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_retention_policy(
        self,
        *,
        logGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_scheduled_query(
        self,
        *,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_subscription_filter(
        self,
        *,
        logGroupName: str,
        filterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_syslog_configuration(
        self,
        *,
        logGroupIdentifier: str,
        vpcEndpointId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transformer(
        self,
        *,
        logGroupIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_policies(
        self,
        *,
        policyType: str,
        policyName: str | None = None,
        accountIdentifiers: list[str] | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_configuration_templates(
        self,
        *,
        service: str | None = None,
        logTypes: list[str] | None = None,
        resourceTypes: list[str] | None = None,
        deliveryDestinationTypes: list[str] | None = None,
        nextToken: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_deliveries(
        self,
        *,
        nextToken: str | None = None,
        limit: int | None = None,
        deliverySourceNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_delivery_destinations(
        self,
        *,
        nextToken: str | None = None,
        limit: int | None = None,
        names: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_delivery_sources(
        self,
        *,
        nextToken: str | None = None,
        limit: int | None = None,
        resourceArns: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_destinations(
        self,
        *,
        DestinationNamePrefix: str | None = None,
        nextToken: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_export_tasks(
        self,
        *,
        taskId: str | None = None,
        statusCode: str | None = None,
        nextToken: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_field_indexes(
        self,
        *,
        logGroupIdentifiers: list[str],
        indexCategories: list[str] | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_import_task_batches(
        self,
        *,
        importId: str,
        batchImportStatus: list[str] | None = None,
        limit: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_import_tasks(
        self,
        *,
        importId: str | None = None,
        importStatus: str | None = None,
        importSourceArn: str | None = None,
        limit: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_index_policies(
        self,
        *,
        logGroupIdentifiers: list[str],
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_log_groups(
        self,
        *,
        accountIdentifiers: list[str] | None = None,
        logGroupNamePrefix: str | None = None,
        logGroupNamePattern: str | None = None,
        nextToken: str | None = None,
        limit: int | None = None,
        includeLinkedAccounts: bool | None = None,
        logGroupClass: str | None = None,
        logGroupIdentifiers: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_log_streams(
        self,
        *,
        logGroupName: str | None = None,
        logGroupIdentifier: str | None = None,
        logStreamNamePrefix: str | None = None,
        orderBy: str | None = None,
        descending: bool | None = None,
        nextToken: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_lookup_tables(
        self,
        *,
        lookupTableNamePrefix: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metric_filters(
        self,
        *,
        logGroupName: str | None = None,
        filterNamePrefix: str | None = None,
        nextToken: str | None = None,
        limit: int | None = None,
        metricName: str | None = None,
        metricNamespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_queries(
        self,
        *,
        logGroupName: str | None = None,
        status: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        queryLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_query_definitions(
        self,
        *,
        queryLanguage: str | None = None,
        queryDefinitionNamePrefix: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resource_policies(
        self,
        *,
        nextToken: str | None = None,
        limit: int | None = None,
        resourceArn: str | None = None,
        policyScope: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_subscription_filters(
        self,
        *,
        logGroupName: str,
        filterNamePrefix: str | None = None,
        nextToken: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_kms_key(
        self,
        *,
        logGroupName: str | None = None,
        resourceIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_source_from_s3_table_integration(
        self,
        *,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def filter_log_events(
        self,
        *,
        logGroupName: str | None = None,
        logGroupIdentifier: str | None = None,
        logStreamNames: list[str] | None = None,
        logStreamNamePrefix: str | None = None,
        startTime: int | None = None,
        endTime: int | None = None,
        filterPattern: str | None = None,
        nextToken: str | None = None,
        limit: int | None = None,
        startFromHead: bool | None = None,
        interleaved: bool | None = None,
        unmask: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_protection_policy(
        self,
        *,
        logGroupIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_delivery(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_delivery_destination(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_delivery_destination_policy(
        self,
        *,
        deliveryDestinationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_delivery_source(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_integration(
        self,
        *,
        integrationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_log_anomaly_detector(
        self,
        *,
        anomalyDetectorArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_log_events(
        self,
        *,
        logStreamName: str,
        logGroupName: str | None = None,
        logGroupIdentifier: str | None = None,
        startTime: int | None = None,
        endTime: int | None = None,
        nextToken: str | None = None,
        limit: int | None = None,
        startFromHead: bool | None = None,
        unmask: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_log_fields(
        self,
        *,
        dataSourceName: str,
        dataSourceType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_log_group_fields(
        self,
        *,
        logGroupName: str | None = None,
        time: int | None = None,
        logGroupIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_log_object(
        self,
        *,
        logObjectPointer: str,
        unmask: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_log_record(
        self,
        *,
        logRecordPointer: str,
        unmask: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lookup_table(
        self,
        *,
        lookupTableArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_query_results(
        self,
        *,
        queryId: str,
        nextToken: str | None = None,
        maxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_scheduled_query(
        self,
        *,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_scheduled_query_history(
        self,
        *,
        identifier: str,
        startTime: int,
        endTime: int,
        executionStatuses: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_storage_tier_policy(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transformer(
        self,
        *,
        logGroupIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_aggregate_log_group_summaries(
        self,
        *,
        groupBy: str,
        accountIdentifiers: list[str] | None = None,
        includeLinkedAccounts: bool | None = None,
        logGroupClass: str | None = None,
        logGroupNamePattern: str | None = None,
        dataSources: list[dict[str, Any]] | None = None,
        nextToken: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_anomalies(
        self,
        *,
        anomalyDetectorArn: str | None = None,
        suppressionState: str | None = None,
        limit: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_integrations(
        self,
        *,
        integrationNamePrefix: str | None = None,
        integrationType: str | None = None,
        integrationStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_log_anomaly_detectors(
        self,
        *,
        filterLogGroupArn: str | None = None,
        limit: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_log_groups(
        self,
        *,
        logGroupNamePattern: str | None = None,
        logGroupClass: str | None = None,
        includeLinkedAccounts: bool | None = None,
        accountIdentifiers: list[str] | None = None,
        nextToken: str | None = None,
        limit: int | None = None,
        dataSources: list[dict[str, Any]] | None = None,
        fieldIndexNames: list[str] | None = None,
        logGroupTags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_log_groups_for_query(
        self,
        *,
        queryId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_scheduled_queries(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        state: str | None = None,
        scheduleType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sources_for_s3_table_integration(
        self,
        *,
        integrationArn: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_syslog_configurations(
        self,
        *,
        logGroupIdentifier: str | None = None,
        vpcEndpointId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_log_group(
        self,
        *,
        logGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_policy(
        self,
        *,
        policyName: str,
        policyDocument: str,
        policyType: str,
        scope: str | None = None,
        selectionCriteria: str | None = None,
        dryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_bearer_token_authentication(
        self,
        *,
        logGroupIdentifier: str,
        bearerTokenAuthenticationEnabled: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_data_protection_policy(
        self,
        *,
        logGroupIdentifier: str,
        policyDocument: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_delivery_destination(
        self,
        *,
        name: str,
        outputFormat: str | None = None,
        deliveryDestinationConfiguration: dict[str, Any] | None = None,
        deliveryDestinationType: str | None = None,
        roleArn: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_delivery_destination_policy(
        self,
        *,
        deliveryDestinationName: str,
        deliveryDestinationPolicy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_delivery_source(
        self,
        *,
        name: str,
        resourceArn: str,
        logType: str,
        tags: dict[str, str] | None = None,
        deliverySourceConfiguration: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_destination(
        self,
        *,
        destinationName: str,
        targetArn: str,
        roleArn: str,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_destination_policy(
        self,
        *,
        destinationName: str,
        accessPolicy: str,
        forceUpdate: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_index_policy(
        self,
        *,
        logGroupIdentifier: str,
        policyDocument: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_integration(
        self,
        *,
        integrationName: str,
        resourceConfig: dict[str, Any],
        integrationType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_log_events(
        self,
        *,
        logGroupName: str,
        logStreamName: str,
        logEvents: list[dict[str, Any]],
        sequenceToken: str | None = None,
        entity: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_log_group_deletion_protection(
        self,
        *,
        logGroupIdentifier: str,
        deletionProtectionEnabled: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_metric_filter(
        self,
        *,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        metricTransformations: list[dict[str, Any]],
        applyOnTransformedLogs: bool | None = None,
        fieldSelectionCriteria: str | None = None,
        emitSystemFieldDimensions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_query_definition(
        self,
        *,
        name: str,
        queryString: str,
        queryLanguage: str | None = None,
        queryDefinitionId: str | None = None,
        logGroupNames: list[str] | None = None,
        clientToken: str | None = None,
        parameters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        policyName: str | None = None,
        policyDocument: str | None = None,
        resourceArn: str | None = None,
        expectedRevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_retention_policy(
        self,
        *,
        logGroupName: str,
        retentionInDays: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_storage_tier_policy(
        self,
        *,
        storageTier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_subscription_filter(
        self,
        *,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        destinationArn: str,
        roleArn: str | None = None,
        distribution: str | None = None,
        applyOnTransformedLogs: bool | None = None,
        fieldSelectionCriteria: str | None = None,
        emitSystemFields: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_syslog_configuration(
        self,
        *,
        logGroupIdentifier: str,
        vpcEndpointId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_transformer(
        self,
        *,
        logGroupIdentifier: str,
        transformerConfig: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_live_tail(
        self,
        *,
        logGroupIdentifiers: list[str],
        logStreamNames: list[str] | None = None,
        logStreamNamePrefixes: list[str] | None = None,
        logEventFilterPattern: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_query(
        self,
        *,
        startTime: int,
        endTime: int,
        queryString: str,
        queryLanguage: str | None = None,
        logGroupName: str | None = None,
        logGroupNames: list[str] | None = None,
        logGroupIdentifiers: list[str] | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_query(
        self,
        *,
        queryId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_log_group(
        self,
        *,
        logGroupName: str,
        tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_metric_filter(
        self,
        *,
        filterPattern: str,
        logEventMessages: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_transformer(
        self,
        *,
        transformerConfig: list[dict[str, Any]],
        logEventMessages: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_log_group(
        self,
        *,
        logGroupName: str,
        tags: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_anomaly(
        self,
        *,
        anomalyDetectorArn: str,
        anomalyId: str | None = None,
        patternId: str | None = None,
        suppressionType: str | None = None,
        suppressionPeriod: dict[str, Any] | None = None,
        baseline: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_delivery_configuration(
        self,
        *,
        id: str,
        recordFields: list[str] | None = None,
        fieldDelimiter: str | None = None,
        s3DeliveryConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_log_anomaly_detector(
        self,
        *,
        anomalyDetectorArn: str,
        enabled: bool,
        evaluationFrequency: str | None = None,
        filterPattern: str | None = None,
        anomalyVisibilityTime: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_lookup_table(
        self,
        *,
        lookupTableArn: str,
        description: str | None = None,
        tableBody: str | None = None,
        queryId: str | None = None,
        kmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_scheduled_query(
        self,
        *,
        identifier: str,
        queryLanguage: str,
        queryString: str,
        scheduleExpression: str,
        executionRoleArn: str,
        description: str | None = None,
        logGroupIdentifiers: list[str] | None = None,
        timezone: str | None = None,
        startTimeOffset: int | None = None,
        endTimeOffset: int | None = None,
        destinationConfiguration: dict[str, Any] | None = None,
        scheduleStartTime: int | None = None,
        scheduleEndTime: int | None = None,
        state: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
