from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class GlueClient(ABC):

    @abstractmethod
    def associate_glossary_terms(
        self,
        *,
        AssetIdentifier: str,
        GlossaryTermIdentifiers: list[str],
        IterableFormName: str | None = None,
        ItemIdentifier: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_create_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionInputList: list[dict[str, Any]],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_connection(
        self,
        *,
        ConnectionNameList: list[str],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionsToDelete: list[dict[str, Any]],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_table(
        self,
        *,
        DatabaseName: str,
        TablesToDelete: list[str],
        CatalogId: str | None = None,
        TransactionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_table_version(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        VersionIds: list[str],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_blueprints(
        self,
        *,
        Names: list[str],
        IncludeBlueprint: bool | None = None,
        IncludeParameterSpec: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_crawlers(
        self,
        *,
        CrawlerNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_custom_entity_types(
        self,
        *,
        Names: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_data_quality_result(
        self,
        *,
        ResultIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_data_quality_result_v2(
        self,
        *,
        ResultIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_data_quality_ruleset_evaluation_run(
        self,
        *,
        RunIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_dev_endpoints(
        self,
        *,
        DevEndpointNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_iterable_forms(
        self,
        *,
        AssetIdentifier: str,
        IterableFormName: str,
        ItemIdentifiers: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_jobs(
        self,
        *,
        JobNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionsToGet: list[dict[str, Any]],
        CatalogId: str | None = None,
        AuditContext: dict[str, Any] | None = None,
        QuerySessionContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_table_optimizer(
        self,
        *,
        Entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_triggers(
        self,
        *,
        TriggerNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_workflows(
        self,
        *,
        Names: list[str],
        IncludeGraph: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_put_data_quality_statistic_annotation(
        self,
        *,
        InclusionAnnotations: list[dict[str, Any]],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_stop_job_run(
        self,
        *,
        JobName: str,
        JobRunIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_update_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        Entries: list[dict[str, Any]],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_data_quality_rule_recommendation_run(
        self,
        *,
        RunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_data_quality_ruleset_evaluation_run(
        self,
        *,
        RunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_ml_task_run(
        self,
        *,
        TransformId: str,
        TaskRunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_statement(
        self,
        *,
        SessionId: str,
        Id: int,
        RequestOrigin: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def check_schema_version_validity(
        self,
        *,
        DataFormat: str,
        SchemaDefinition: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_blueprint(
        self,
        *,
        Name: str,
        BlueprintLocation: str,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_catalog(
        self,
        *,
        Name: str,
        CatalogInput: dict[str, Any],
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_classifier(
        self,
        *,
        GrokClassifier: dict[str, Any] | None = None,
        XMLClassifier: dict[str, Any] | None = None,
        JsonClassifier: dict[str, Any] | None = None,
        CsvClassifier: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_column_statistics_task_settings(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        Role: str,
        Schedule: str | None = None,
        ColumnNameList: list[str] | None = None,
        SampleSize: float | int | None = None,
        CatalogID: str | None = None,
        SecurityConfiguration: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connection(
        self,
        *,
        ConnectionInput: dict[str, Any],
        CatalogId: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_crawler(
        self,
        *,
        Name: str,
        Role: str,
        Targets: dict[str, Any],
        DatabaseName: str | None = None,
        Description: str | None = None,
        Schedule: str | None = None,
        Classifiers: list[str] | None = None,
        TablePrefix: str | None = None,
        SchemaChangePolicy: dict[str, Any] | None = None,
        RecrawlPolicy: dict[str, Any] | None = None,
        LineageConfiguration: dict[str, Any] | None = None,
        LakeFormationConfiguration: dict[str, Any] | None = None,
        Configuration: str | None = None,
        CrawlerSecurityConfiguration: str | None = None,
        Tags: dict[str, str] | None = None,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_entity_type(
        self,
        *,
        Name: str,
        RegexString: str,
        ContextWords: list[str] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_quality_evaluation_config(
        self,
        *,
        Name: str,
        Level: str,
        DataSource: dict[str, Any],
        Role: str,
        RulesetName: str | None = None,
        ManagedRulesetName: str | None = None,
        Triggers: list[str] | None = None,
        ScheduleExpression: str | None = None,
        StartAt: datetime.datetime | str | None = None,
        EndAt: datetime.datetime | str | None = None,
        NumberOfWorkers: int | None = None,
        Timeout: int | None = None,
        AdditionalRunOptions: dict[str, Any] | None = None,
        AdditionalDataSources: dict[str, dict[str, Any]] | None = None,
        Tags: dict[str, str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_quality_ruleset(
        self,
        *,
        Name: str,
        Ruleset: str,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
        TargetTable: dict[str, Any] | None = None,
        DataQualitySecurityConfiguration: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_database(
        self,
        *,
        DatabaseInput: dict[str, Any],
        CatalogId: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dev_endpoint(
        self,
        *,
        EndpointName: str,
        RoleArn: str,
        SecurityGroupIds: list[str] | None = None,
        SubnetId: str | None = None,
        PublicKey: str | None = None,
        PublicKeys: list[str] | None = None,
        NumberOfNodes: int | None = None,
        WorkerType: str | None = None,
        GlueVersion: str | None = None,
        NumberOfWorkers: int | None = None,
        ExtraPythonLibsS3Path: str | None = None,
        ExtraJarsS3Path: str | None = None,
        SecurityConfiguration: str | None = None,
        Tags: dict[str, str] | None = None,
        Arguments: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_glossary(
        self,
        *,
        Name: str,
        Description: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_glossary_term(
        self,
        *,
        GlossaryIdentifier: str,
        Name: str,
        ShortDescription: str | None = None,
        LongDescription: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_glue_identity_center_configuration(
        self,
        *,
        InstanceArn: str,
        Scopes: list[str] | None = None,
        UserBackgroundSessionsEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_integration(
        self,
        *,
        IntegrationName: str,
        SourceArn: str,
        TargetArn: str,
        Description: str | None = None,
        DataFilter: str | None = None,
        KmsKeyId: str | None = None,
        AdditionalEncryptionContext: dict[str, str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        IntegrationConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_integration_resource_property(
        self,
        *,
        ResourceArn: str,
        SourceProcessingProperties: dict[str, Any] | None = None,
        TargetProcessingProperties: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_integration_table_properties(
        self,
        *,
        ResourceArn: str,
        TableName: str,
        SourceTableConfig: dict[str, Any] | None = None,
        TargetTableConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_job(
        self,
        *,
        Name: str,
        Role: str,
        Command: dict[str, Any],
        JobMode: str | None = None,
        JobRunQueuingEnabled: bool | None = None,
        Description: str | None = None,
        LogUri: str | None = None,
        ExecutionProperty: dict[str, Any] | None = None,
        DefaultArguments: dict[str, str] | None = None,
        NonOverridableArguments: dict[str, str] | None = None,
        Connections: dict[str, Any] | None = None,
        MaxRetries: int | None = None,
        AllocatedCapacity: int | None = None,
        Timeout: int | None = None,
        MaxCapacity: float | int | None = None,
        SecurityConfiguration: str | None = None,
        Tags: dict[str, str] | None = None,
        NotificationProperty: dict[str, Any] | None = None,
        GlueVersion: str | None = None,
        NumberOfWorkers: int | None = None,
        WorkerType: str | None = None,
        CodeGenConfigurationNodes: dict[str, dict[str, Any]] | None = None,
        ExecutionClass: str | None = None,
        SourceControlDetails: dict[str, Any] | None = None,
        MaintenanceWindow: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ml_transform(
        self,
        *,
        Name: str,
        InputRecordTables: list[dict[str, Any]],
        Parameters: dict[str, Any],
        Role: str,
        Description: str | None = None,
        GlueVersion: str | None = None,
        MaxCapacity: float | int | None = None,
        WorkerType: str | None = None,
        NumberOfWorkers: int | None = None,
        Timeout: int | None = None,
        MaxRetries: int | None = None,
        Tags: dict[str, str] | None = None,
        TransformEncryption: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionInput: dict[str, Any],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_partition_index(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionIndex: dict[str, Any],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_registry(
        self,
        *,
        RegistryName: str,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_schema(
        self,
        *,
        SchemaName: str,
        DataFormat: str,
        RegistryId: dict[str, Any] | None = None,
        Compatibility: str | None = None,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
        SchemaDefinition: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_script(
        self,
        *,
        DagNodes: list[dict[str, Any]] | None = None,
        DagEdges: list[dict[str, Any]] | None = None,
        Language: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_security_configuration(
        self,
        *,
        Name: str,
        EncryptionConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_session(
        self,
        *,
        Id: str,
        Role: str,
        Command: dict[str, Any],
        Description: str | None = None,
        Timeout: int | None = None,
        IdleTimeout: int | None = None,
        DefaultArguments: dict[str, str] | None = None,
        Connections: dict[str, Any] | None = None,
        MaxCapacity: float | int | None = None,
        NumberOfWorkers: int | None = None,
        WorkerType: str | None = None,
        SecurityConfiguration: str | None = None,
        GlueVersion: str | None = None,
        Tags: dict[str, str] | None = None,
        RequestOrigin: str | None = None,
        SessionType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_table(
        self,
        *,
        DatabaseName: str,
        CatalogId: str | None = None,
        Name: str | None = None,
        TableInput: dict[str, Any] | None = None,
        PartitionIndexes: list[dict[str, Any]] | None = None,
        TransactionId: str | None = None,
        OpenTableFormatInput: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_table_optimizer(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        TableName: str,
        Type: str,
        TableOptimizerConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_trigger(
        self,
        *,
        Name: str,
        Type: str,
        Actions: list[dict[str, Any]],
        WorkflowName: str | None = None,
        Schedule: str | None = None,
        Predicate: dict[str, Any] | None = None,
        Description: str | None = None,
        StartOnCreation: bool | None = None,
        Tags: dict[str, str] | None = None,
        EventBatchingCondition: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_usage_profile(
        self,
        *,
        Name: str,
        Configuration: dict[str, Any],
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user_defined_function(
        self,
        *,
        DatabaseName: str,
        FunctionInput: dict[str, Any],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workflow(
        self,
        *,
        Name: str,
        Description: str | None = None,
        DefaultRunProperties: dict[str, str] | None = None,
        Tags: dict[str, str] | None = None,
        MaxConcurrentRuns: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_asset(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_attachment(
        self,
        *,
        AssetIdentifier: str,
        AttachmentName: str,
        IterableFormName: str | None = None,
        ItemIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_blueprint(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_catalog(
        self,
        *,
        CatalogId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_classifier(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_column_statistics_for_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValues: list[str],
        ColumnName: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_column_statistics_for_table(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        ColumnName: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_column_statistics_task_settings(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogID: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connection(
        self,
        *,
        ConnectionName: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connection_type(
        self,
        *,
        ConnectionType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_crawler(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_entity_type(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_quality_evaluation_config(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_quality_ruleset(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_database(
        self,
        *,
        Name: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dev_endpoint(
        self,
        *,
        EndpointName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_form_type(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_glossary(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_glossary_term(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_glue_identity_center_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_integration(
        self,
        *,
        IntegrationIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_integration_resource_property(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_integration_table_properties(
        self,
        *,
        ResourceArn: str,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_job(
        self,
        *,
        JobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ml_transform(
        self,
        *,
        TransformId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValues: list[str],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_partition_index(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        IndexName: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_registry(
        self,
        *,
        RegistryId: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        PolicyHashCondition: str | None = None,
        ResourceArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_schema(
        self,
        *,
        SchemaId: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_schema_versions(
        self,
        *,
        SchemaId: dict[str, Any],
        Versions: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_security_configuration(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_session(
        self,
        *,
        Id: str,
        RequestOrigin: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_table(
        self,
        *,
        DatabaseName: str,
        Name: str,
        CatalogId: str | None = None,
        TransactionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_table_optimizer(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        TableName: str,
        Type: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_table_version(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        VersionId: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_trigger(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_usage_profile(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_defined_function(
        self,
        *,
        DatabaseName: str,
        FunctionName: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workflow(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connection_type(
        self,
        *,
        ConnectionType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_entity(
        self,
        *,
        ConnectionName: str,
        EntityName: str,
        CatalogId: str | None = None,
        NextToken: str | None = None,
        DataStoreApiVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_inbound_integrations(
        self,
        *,
        IntegrationArn: str | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
        TargetArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_integrations(
        self,
        *,
        IntegrationIdentifier: str | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_glossary_terms(
        self,
        *,
        AssetIdentifier: str,
        GlossaryTermIdentifiers: list[str],
        IterableFormName: str | None = None,
        ItemIdentifier: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_asset(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_asset_type(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_blueprint(
        self,
        *,
        Name: str,
        IncludeBlueprint: bool | None = None,
        IncludeParameterSpec: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_blueprint_run(
        self,
        *,
        BlueprintName: str,
        RunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_blueprint_runs(
        self,
        *,
        BlueprintName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_catalog(
        self,
        *,
        CatalogId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_catalog_import_status(
        self,
        *,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_catalogs(
        self,
        *,
        ParentCatalogId: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Recursive: bool | None = None,
        IncludeRoot: bool | None = None,
        HasDatabases: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_classifier(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_classifiers(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_column_statistics_for_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValues: list[str],
        ColumnNames: list[str],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_column_statistics_for_table(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        ColumnNames: list[str],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_column_statistics_task_run(
        self,
        *,
        ColumnStatisticsTaskRunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_column_statistics_task_runs(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        CatalogID: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_column_statistics_task_settings(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogID: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connection(
        self,
        *,
        Name: str,
        CatalogId: str | None = None,
        HidePassword: bool | None = None,
        ApplyOverrideForComputeEnvironment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connections(
        self,
        *,
        CatalogId: str | None = None,
        Filter: dict[str, Any] | None = None,
        HidePassword: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_crawler(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_crawler_metrics(
        self,
        *,
        CrawlerNameList: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_crawlers(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_custom_entity_type(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dashboard_url(
        self,
        *,
        ResourceId: str,
        ResourceType: str,
        RequestOrigin: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_catalog_encryption_settings(
        self,
        *,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_catalog_export_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_quality_evaluation_config(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_quality_model(
        self,
        *,
        ProfileId: str,
        StatisticId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_quality_model_result(
        self,
        *,
        StatisticId: str,
        ProfileId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_quality_result(
        self,
        *,
        ResultId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_quality_result_v2(
        self,
        *,
        ResultId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_quality_rule_recommendation_run(
        self,
        *,
        RunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_quality_ruleset(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_quality_ruleset_evaluation_run(
        self,
        *,
        RunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_database(
        self,
        *,
        Name: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_databases(
        self,
        *,
        CatalogId: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ResourceShareType: str | None = None,
        AttributesToGet: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dataflow_graph(
        self,
        *,
        PythonScript: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dev_endpoint(
        self,
        *,
        EndpointName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dev_endpoints(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_entity_records(
        self,
        *,
        EntityName: str,
        Limit: int,
        ConnectionName: str | None = None,
        CatalogId: str | None = None,
        NextToken: str | None = None,
        DataStoreApiVersion: str | None = None,
        ConnectionOptions: dict[str, str] | None = None,
        FilterPredicate: str | None = None,
        OrderBy: str | None = None,
        SelectedFields: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_form_type(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_glossary(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_glossary_term(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_glue_identity_center_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_integration_resource_property(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_integration_table_properties(
        self,
        *,
        ResourceArn: str,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job(
        self,
        *,
        JobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job_bookmark(
        self,
        *,
        JobName: str,
        RunId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job_run(
        self,
        *,
        JobName: str,
        RunId: str,
        PredecessorsIncluded: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job_runs(
        self,
        *,
        JobName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job_upgrade_analysis(
        self,
        *,
        analysisId: str,
        jobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_jobs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ml_task_run(
        self,
        *,
        TransformId: str,
        TaskRunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ml_task_runs(
        self,
        *,
        TransformId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filter: dict[str, Any] | None = None,
        Sort: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ml_transform(
        self,
        *,
        TransformId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ml_transforms(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filter: dict[str, Any] | None = None,
        Sort: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_mapping(
        self,
        *,
        Source: dict[str, Any],
        Sinks: list[dict[str, Any]] | None = None,
        Location: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_materialized_view_refresh_task_run(
        self,
        *,
        CatalogId: str,
        MaterializedViewRefreshTaskRunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValues: list[str],
        CatalogId: str | None = None,
        AuditContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_partition_indexes(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogId: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_partitions(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogId: str | None = None,
        Expression: str | None = None,
        NextToken: str | None = None,
        Segment: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        ExcludeColumnSchema: bool | None = None,
        TransactionId: str | None = None,
        QueryAsOfTime: datetime.datetime | str | None = None,
        AuditContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_plan(
        self,
        *,
        Mapping: list[dict[str, Any]],
        Source: dict[str, Any],
        Sinks: list[dict[str, Any]] | None = None,
        Location: dict[str, Any] | None = None,
        Language: str | None = None,
        AdditionalPlanOptionsMap: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_registry(
        self,
        *,
        RegistryId: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policies(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        ResourceArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_schema(
        self,
        *,
        SchemaId: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_schema_by_definition(
        self,
        *,
        SchemaId: dict[str, Any],
        SchemaDefinition: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_schema_version(
        self,
        *,
        SchemaId: dict[str, Any] | None = None,
        SchemaVersionId: str | None = None,
        SchemaVersionNumber: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_schema_versions_diff(
        self,
        *,
        SchemaId: dict[str, Any],
        FirstSchemaVersionNumber: dict[str, Any],
        SecondSchemaVersionNumber: dict[str, Any],
        SchemaDiffType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_security_configuration(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_security_configurations(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_session(
        self,
        *,
        Id: str,
        RequestOrigin: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_session_endpoint(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_statement(
        self,
        *,
        SessionId: str,
        Id: int,
        RequestOrigin: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_system_logs_for_job_run(
        self,
        *,
        JobName: str,
        RunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_system_logs_for_session(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_table(
        self,
        *,
        DatabaseName: str,
        Name: str,
        CatalogId: str | None = None,
        TransactionId: str | None = None,
        QueryAsOfTime: datetime.datetime | str | None = None,
        AuditContext: dict[str, Any] | None = None,
        IncludeStatusDetails: bool | None = None,
        AttributesToGet: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_table_optimizer(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        TableName: str,
        Type: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_table_version(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogId: str | None = None,
        VersionId: str | None = None,
        AuditContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_table_versions(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogId: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        AuditContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tables(
        self,
        *,
        DatabaseName: str,
        CatalogId: str | None = None,
        Expression: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        TransactionId: str | None = None,
        QueryAsOfTime: datetime.datetime | str | None = None,
        AuditContext: dict[str, Any] | None = None,
        ResourceShareType: str | None = None,
        IncludeStatusDetails: bool | None = None,
        AttributesToGet: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tags(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trigger(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_triggers(
        self,
        *,
        NextToken: str | None = None,
        DependentJobName: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_unfiltered_partition_metadata(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        TableName: str,
        PartitionValues: list[str],
        SupportedPermissionTypes: list[str],
        Region: str | None = None,
        AuditContext: dict[str, Any] | None = None,
        QuerySessionContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_unfiltered_partitions_metadata(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        TableName: str,
        SupportedPermissionTypes: list[str],
        Region: str | None = None,
        Expression: str | None = None,
        AuditContext: dict[str, Any] | None = None,
        NextToken: str | None = None,
        Segment: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        QuerySessionContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_unfiltered_table_metadata(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        Name: str,
        SupportedPermissionTypes: list[str],
        Region: str | None = None,
        AuditContext: dict[str, Any] | None = None,
        ParentResourceArn: str | None = None,
        RootResourceArn: str | None = None,
        SupportedDialect: dict[str, Any] | None = None,
        Permissions: list[str] | None = None,
        QuerySessionContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_usage_profile(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_defined_function(
        self,
        *,
        DatabaseName: str,
        FunctionName: str,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_defined_functions(
        self,
        *,
        Pattern: str,
        CatalogId: str | None = None,
        DatabaseName: str | None = None,
        FunctionType: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_workflow(
        self,
        *,
        Name: str,
        IncludeGraph: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_workflow_run(
        self,
        *,
        Name: str,
        RunId: str,
        IncludeGraph: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_workflow_run_properties(
        self,
        *,
        Name: str,
        RunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_workflow_runs(
        self,
        *,
        Name: str,
        IncludeGraph: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_catalog_to_glue(
        self,
        *,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_asset_types(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_blueprints(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_column_statistics_task_runs(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connection_types(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_crawlers(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_crawls(
        self,
        *,
        CrawlerName: str,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_custom_entity_types(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_quality_evaluation_configs(
        self,
        *,
        Level: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_quality_results(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_quality_results_v2(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_quality_rule_recommendation_runs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_quality_ruleset_evaluation_runs(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_quality_rulesets(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filter: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_quality_statistic_annotations(
        self,
        *,
        StatisticId: str | None = None,
        ProfileId: str | None = None,
        TimestampFilter: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_quality_statistics(
        self,
        *,
        StatisticId: str | None = None,
        ProfileId: str | None = None,
        TimestampFilter: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dev_endpoints(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_entities(
        self,
        *,
        ConnectionName: str | None = None,
        CatalogId: str | None = None,
        ParentEntityName: str | None = None,
        NextToken: str | None = None,
        DataStoreApiVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_form_types(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_glossaries(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_glossary_terms(
        self,
        *,
        GlossaryIdentifier: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_integration_resource_properties(
        self,
        *,
        Marker: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_integration_table_properties(
        self,
        *,
        Marker: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_iterable_forms(
        self,
        *,
        AssetIdentifier: str,
        IterableFormName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_jobs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ml_transforms(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filter: dict[str, Any] | None = None,
        Sort: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_materialized_view_refresh_task_runs(
        self,
        *,
        CatalogId: str,
        DatabaseName: str | None = None,
        TableName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_registries(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_schema_versions(
        self,
        *,
        SchemaId: dict[str, Any],
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_schemas(
        self,
        *,
        RegistryId: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sessions(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Tags: dict[str, str] | None = None,
        RequestOrigin: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_statements(
        self,
        *,
        SessionId: str,
        RequestOrigin: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_table_optimizer_runs(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        TableName: str,
        Type: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_triggers(
        self,
        *,
        NextToken: str | None = None,
        DependentJobName: str | None = None,
        MaxResults: int | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_usage_profiles(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workflows(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_integration(
        self,
        *,
        IntegrationIdentifier: str,
        Description: str | None = None,
        DataFilter: str | None = None,
        IntegrationConfig: dict[str, Any] | None = None,
        IntegrationName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def publish_data_quality_result_v2(
        self,
        *,
        Dimensions: dict[str, str],
        Score: float | int,
        RuleResults: list[dict[str, Any]],
        EvaluationContext: str,
        Tags: dict[str, str] | None = None,
        ExecutionStartedOn: datetime.datetime | str | None = None,
        ExecutionCompletedOn: datetime.datetime | str | None = None,
        AnalyzerResults: list[dict[str, Any]] | None = None,
        Observations: list[dict[str, Any]] | None = None,
        AggregatedMetrics: dict[str, Any] | None = None,
        Statistics: list[dict[str, Any]] | None = None,
        RunConfiguration: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        Descriptors: dict[str, str] | None = None,
        RulesetName: str | None = None,
        DataQualitySecurityConfiguration: str | None = None,
        Telemetry: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_asset(
        self,
        *,
        Identifier: str,
        Name: str,
        Forms: dict[str, dict[str, Any]],
        AssetTypeIdentifier: str | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_attachment(
        self,
        *,
        AssetIdentifier: str,
        AttachmentName: str,
        Content: str,
        IterableFormName: str | None = None,
        ItemIdentifier: str | None = None,
        FormTypeIdentifier: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_data_catalog_encryption_settings(
        self,
        *,
        DataCatalogEncryptionSettings: dict[str, Any],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_data_catalog_export_configuration(
        self,
        *,
        ClientToken: str | None = None,
        S3TablesConfiguration: dict[str, Any] | None = None,
        Assets: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_data_quality_profile_annotation(
        self,
        *,
        ProfileId: str,
        InclusionAnnotation: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_form_type(
        self,
        *,
        Name: str,
        Schema: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        PolicyInJson: str,
        ResourceArn: str | None = None,
        PolicyHashCondition: str | None = None,
        PolicyExistsCondition: str | None = None,
        EnableHybrid: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_schema_version_metadata(
        self,
        *,
        MetadataKeyValue: dict[str, Any],
        SchemaId: dict[str, Any] | None = None,
        SchemaVersionNumber: dict[str, Any] | None = None,
        SchemaVersionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_workflow_run_properties(
        self,
        *,
        Name: str,
        RunId: str,
        RunProperties: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def query_schema_version_metadata(
        self,
        *,
        SchemaId: dict[str, Any] | None = None,
        SchemaVersionNumber: dict[str, Any] | None = None,
        SchemaVersionId: str | None = None,
        MetadataList: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_connection_type(
        self,
        *,
        ConnectionType: str,
        IntegrationType: str,
        ConnectionProperties: dict[str, Any],
        ConnectorAuthenticationConfiguration: dict[str, Any],
        RestConfiguration: dict[str, Any],
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_schema_version(
        self,
        *,
        SchemaId: dict[str, Any],
        SchemaDefinition: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_schema_version_metadata(
        self,
        *,
        MetadataKeyValue: dict[str, Any],
        SchemaId: dict[str, Any] | None = None,
        SchemaVersionNumber: dict[str, Any] | None = None,
        SchemaVersionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_job_bookmark(
        self,
        *,
        JobName: str,
        RunId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resume_workflow_run(
        self,
        *,
        Name: str,
        RunId: str,
        NodeIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def run_statement(
        self,
        *,
        SessionId: str,
        Code: str,
        RequestOrigin: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_assets(
        self,
        *,
        SearchText: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Sort: dict[str, Any] | None = None,
        FilterClause: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_tables(
        self,
        *,
        CatalogId: str | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        SearchText: str | None = None,
        SortCriteria: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        ResourceShareType: str | None = None,
        IncludeStatusDetails: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_blueprint_run(
        self,
        *,
        BlueprintName: str,
        RoleArn: str,
        Parameters: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_column_statistics_task_run(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        Role: str,
        ColumnNameList: list[str] | None = None,
        SampleSize: float | int | None = None,
        CatalogID: str | None = None,
        SecurityConfiguration: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_column_statistics_task_run_schedule(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogID: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_crawler(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_crawler_schedule(
        self,
        *,
        CrawlerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_data_quality_rule_recommendation_run(
        self,
        *,
        DataSource: dict[str, Any],
        Role: str,
        NumberOfWorkers: int | None = None,
        Timeout: int | None = None,
        CreatedRulesetName: str | None = None,
        DataQualitySecurityConfiguration: str | None = None,
        ClientToken: str | None = None,
        AdditionalRunOptions: dict[str, Any] | None = None,
        RecommendationMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_data_quality_ruleset_evaluation_run(
        self,
        *,
        DataSource: dict[str, Any],
        Role: str,
        RulesetNames: list[str],
        NumberOfWorkers: int | None = None,
        Timeout: int | None = None,
        ClientToken: str | None = None,
        AdditionalRunOptions: dict[str, Any] | None = None,
        AdditionalDataSources: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_export_labels_task_run(
        self,
        *,
        TransformId: str,
        OutputS3Path: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_import_labels_task_run(
        self,
        *,
        TransformId: str,
        InputS3Path: str,
        ReplaceAllLabels: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_job_run(
        self,
        *,
        JobName: str,
        JobRunQueuingEnabled: bool | None = None,
        JobRunId: str | None = None,
        Arguments: dict[str, str] | None = None,
        AllocatedCapacity: int | None = None,
        Timeout: int | None = None,
        MaxCapacity: float | int | None = None,
        SecurityConfiguration: str | None = None,
        NotificationProperty: dict[str, Any] | None = None,
        WorkerType: str | None = None,
        NumberOfWorkers: int | None = None,
        ExecutionClass: str | None = None,
        ExecutionRoleSessionPolicy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_job_upgrade_analysis(
        self,
        *,
        jobName: str,
        analysisId: str | None = None,
        upgradeConsent: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_ml_evaluation_task_run(
        self,
        *,
        TransformId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_ml_labeling_set_generation_task_run(
        self,
        *,
        TransformId: str,
        OutputS3Path: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_materialized_view_refresh_task_run(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        TableName: str,
        FullRefresh: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_trigger(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_workflow_run(
        self,
        *,
        Name: str,
        RunProperties: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_column_statistics_task_run(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogID: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_column_statistics_task_run_schedule(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogID: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_crawler(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_crawler_schedule(
        self,
        *,
        CrawlerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_job_upgrade_analysis(
        self,
        *,
        jobName: str,
        analysisId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_materialized_view_refresh_task_run(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        TableName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_session(
        self,
        *,
        Id: str,
        RequestOrigin: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_trigger(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_workflow_run(
        self,
        *,
        Name: str,
        RunId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        TagsToAdd: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_connection(
        self,
        *,
        ConnectionName: str | None = None,
        CatalogId: str | None = None,
        TestConnectionInput: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagsToRemove: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_asset(
        self,
        *,
        Identifier: str,
        Name: str | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_blueprint(
        self,
        *,
        Name: str,
        BlueprintLocation: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_catalog(
        self,
        *,
        CatalogId: str,
        CatalogInput: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_classifier(
        self,
        *,
        GrokClassifier: dict[str, Any] | None = None,
        XMLClassifier: dict[str, Any] | None = None,
        JsonClassifier: dict[str, Any] | None = None,
        CsvClassifier: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_column_statistics_for_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValues: list[str],
        ColumnStatisticsList: list[dict[str, Any]],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_column_statistics_for_table(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        ColumnStatisticsList: list[dict[str, Any]],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_column_statistics_task_settings(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        Role: str | None = None,
        Schedule: str | None = None,
        ColumnNameList: list[str] | None = None,
        SampleSize: float | int | None = None,
        CatalogID: str | None = None,
        SecurityConfiguration: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connection(
        self,
        *,
        Name: str,
        ConnectionInput: dict[str, Any],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_crawler(
        self,
        *,
        Name: str,
        Role: str | None = None,
        DatabaseName: str | None = None,
        Description: str | None = None,
        Targets: dict[str, Any] | None = None,
        Schedule: str | None = None,
        Classifiers: list[str] | None = None,
        TablePrefix: str | None = None,
        SchemaChangePolicy: dict[str, Any] | None = None,
        RecrawlPolicy: dict[str, Any] | None = None,
        LineageConfiguration: dict[str, Any] | None = None,
        LakeFormationConfiguration: dict[str, Any] | None = None,
        Configuration: str | None = None,
        CrawlerSecurityConfiguration: str | None = None,
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_crawler_schedule(
        self,
        *,
        CrawlerName: str,
        Schedule: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_quality_evaluation_config(
        self,
        *,
        Name: str,
        DataSource: dict[str, Any] | None = None,
        RulesetName: str | None = None,
        ManagedRulesetName: str | None = None,
        Triggers: list[str] | None = None,
        ScheduleExpression: str | None = None,
        StartAt: datetime.datetime | str | None = None,
        EndAt: datetime.datetime | str | None = None,
        PauseRuns: bool | None = None,
        Role: str | None = None,
        NumberOfWorkers: int | None = None,
        Timeout: int | None = None,
        AdditionalRunOptions: dict[str, Any] | None = None,
        AdditionalDataSources: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_quality_ruleset(
        self,
        *,
        Name: str,
        Description: str | None = None,
        Ruleset: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_database(
        self,
        *,
        Name: str,
        DatabaseInput: dict[str, Any],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dev_endpoint(
        self,
        *,
        EndpointName: str,
        PublicKey: str | None = None,
        AddPublicKeys: list[str] | None = None,
        DeletePublicKeys: list[str] | None = None,
        CustomLibraries: dict[str, Any] | None = None,
        UpdateEtlLibraries: bool | None = None,
        DeleteArguments: list[str] | None = None,
        AddArguments: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_glossary(
        self,
        *,
        Identifier: str,
        Name: str | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_glossary_term(
        self,
        *,
        Identifier: str,
        Name: str | None = None,
        ShortDescription: str | None = None,
        LongDescription: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_glue_identity_center_configuration(
        self,
        *,
        Scopes: list[str] | None = None,
        UserBackgroundSessionsEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_integration_resource_property(
        self,
        *,
        ResourceArn: str,
        SourceProcessingProperties: dict[str, Any] | None = None,
        TargetProcessingProperties: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_integration_table_properties(
        self,
        *,
        ResourceArn: str,
        TableName: str,
        SourceTableConfig: dict[str, Any] | None = None,
        TargetTableConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_job(
        self,
        *,
        JobName: str,
        JobUpdate: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_job_from_source_control(
        self,
        *,
        JobName: str | None = None,
        Provider: str | None = None,
        RepositoryName: str | None = None,
        RepositoryOwner: str | None = None,
        BranchName: str | None = None,
        Folder: str | None = None,
        CommitId: str | None = None,
        AuthStrategy: str | None = None,
        AuthToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_ml_transform(
        self,
        *,
        TransformId: str,
        Name: str | None = None,
        Description: str | None = None,
        Parameters: dict[str, Any] | None = None,
        Role: str | None = None,
        GlueVersion: str | None = None,
        MaxCapacity: float | int | None = None,
        WorkerType: str | None = None,
        NumberOfWorkers: int | None = None,
        Timeout: int | None = None,
        MaxRetries: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValueList: list[str],
        PartitionInput: dict[str, Any],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_registry(
        self,
        *,
        RegistryId: dict[str, Any],
        Description: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_schema(
        self,
        *,
        SchemaId: dict[str, Any],
        SchemaVersionNumber: dict[str, Any] | None = None,
        Compatibility: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_source_control_from_job(
        self,
        *,
        JobName: str | None = None,
        Provider: str | None = None,
        RepositoryName: str | None = None,
        RepositoryOwner: str | None = None,
        BranchName: str | None = None,
        Folder: str | None = None,
        CommitId: str | None = None,
        AuthStrategy: str | None = None,
        AuthToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_table(
        self,
        *,
        DatabaseName: str,
        CatalogId: str | None = None,
        Name: str | None = None,
        TableInput: dict[str, Any] | None = None,
        SkipArchive: bool | None = None,
        TransactionId: str | None = None,
        VersionId: str | None = None,
        ViewUpdateAction: str | None = None,
        Force: bool | None = None,
        UpdateOpenTableFormatInput: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_table_optimizer(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        TableName: str,
        Type: str,
        TableOptimizerConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_trigger(
        self,
        *,
        Name: str,
        TriggerUpdate: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_usage_profile(
        self,
        *,
        Name: str,
        Configuration: dict[str, Any],
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_defined_function(
        self,
        *,
        DatabaseName: str,
        FunctionName: str,
        FunctionInput: dict[str, Any],
        CatalogId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workflow(
        self,
        *,
        Name: str,
        Description: str | None = None,
        DefaultRunProperties: dict[str, str] | None = None,
        MaxConcurrentRuns: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
