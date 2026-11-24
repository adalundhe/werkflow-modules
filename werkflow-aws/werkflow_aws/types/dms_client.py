from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class DMSClient(ABC):

    @abstractmethod
    def add_tags_to_resource(
        self,
        *,
        ResourceArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def apply_pending_maintenance_action(
        self,
        *,
        ReplicationInstanceArn: str,
        ApplyAction: str,
        OptInType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_start_recommendations(
        self,
        *,
        Data: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_metadata_model_conversion(
        self,
        *,
        MigrationProjectIdentifier: str,
        RequestIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_metadata_model_creation(
        self,
        *,
        MigrationProjectIdentifier: str,
        RequestIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_replication_task_assessment_run(
        self,
        *,
        ReplicationTaskAssessmentRunArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_migration(
        self,
        *,
        MigrationProjectIdentifier: str,
        DataMigrationType: str,
        ServiceAccessRoleArn: str,
        DataMigrationName: str | None = None,
        EnableCloudwatchLogs: bool | None = None,
        SourceDataSettings: list[dict[str, Any]] | None = None,
        TargetDataSettings: list[dict[str, Any]] | None = None,
        NumberOfJobs: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SelectionRules: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_provider(
        self,
        *,
        Engine: str,
        Settings: dict[str, Any],
        DataProviderName: str | None = None,
        Description: str | None = None,
        Virtual: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_endpoint(
        self,
        *,
        EndpointIdentifier: str,
        EndpointType: str,
        EngineName: str,
        Username: str | None = None,
        Password: str | None = None,
        ServerName: str | None = None,
        Port: int | None = None,
        DatabaseName: str | None = None,
        ExtraConnectionAttributes: str | None = None,
        KmsKeyId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        CertificateArn: str | None = None,
        SslMode: str | None = None,
        ServiceAccessRoleArn: str | None = None,
        ExternalTableDefinition: str | None = None,
        DynamoDbSettings: dict[str, Any] | None = None,
        S3Settings: dict[str, Any] | None = None,
        DmsTransferSettings: dict[str, Any] | None = None,
        MongoDbSettings: dict[str, Any] | None = None,
        KinesisSettings: dict[str, Any] | None = None,
        KafkaSettings: dict[str, Any] | None = None,
        ElasticsearchSettings: dict[str, Any] | None = None,
        NeptuneSettings: dict[str, Any] | None = None,
        RedshiftSettings: dict[str, Any] | None = None,
        PostgreSQLSettings: dict[str, Any] | None = None,
        MySQLSettings: dict[str, Any] | None = None,
        OracleSettings: dict[str, Any] | None = None,
        SybaseSettings: dict[str, Any] | None = None,
        MicrosoftSQLServerSettings: dict[str, Any] | None = None,
        IBMDb2Settings: dict[str, Any] | None = None,
        ResourceIdentifier: str | None = None,
        DocDbSettings: dict[str, Any] | None = None,
        RedisSettings: dict[str, Any] | None = None,
        GcpMySQLSettings: dict[str, Any] | None = None,
        TimestreamSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str | None = None,
        EventCategories: list[str] | None = None,
        SourceIds: list[str] | None = None,
        Enabled: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_fleet_advisor_collector(
        self,
        *,
        CollectorName: str,
        ServiceAccessRoleArn: str,
        S3BucketName: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_instance_profile(
        self,
        *,
        AvailabilityZone: str | None = None,
        KmsKeyArn: str | None = None,
        PubliclyAccessible: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        NetworkType: str | None = None,
        InstanceProfileName: str | None = None,
        Description: str | None = None,
        SubnetGroupIdentifier: str | None = None,
        VpcSecurityGroups: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_migration_project(
        self,
        *,
        SourceDataProviderDescriptors: list[dict[str, Any]],
        TargetDataProviderDescriptors: list[dict[str, Any]],
        InstanceProfileIdentifier: str,
        MigrationProjectName: str | None = None,
        TransformationRules: str | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SchemaConversionApplicationAttributes: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_replication_config(
        self,
        *,
        ReplicationConfigIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ComputeConfig: dict[str, Any],
        ReplicationType: str,
        TableMappings: str,
        ReplicationSettings: str | None = None,
        SupplementalSettings: str | None = None,
        ResourceIdentifier: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_replication_instance(
        self,
        *,
        ReplicationInstanceIdentifier: str,
        ReplicationInstanceClass: str,
        AllocatedStorage: int | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        AvailabilityZone: str | None = None,
        ReplicationSubnetGroupIdentifier: str | None = None,
        PreferredMaintenanceWindow: str | None = None,
        MultiAZ: bool | None = None,
        EngineVersion: str | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        KmsKeyId: str | None = None,
        PubliclyAccessible: bool | None = None,
        DnsNameServers: str | None = None,
        ResourceIdentifier: str | None = None,
        NetworkType: str | None = None,
        KerberosAuthenticationSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_replication_subnet_group(
        self,
        *,
        ReplicationSubnetGroupIdentifier: str,
        ReplicationSubnetGroupDescription: str,
        SubnetIds: list[str],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_replication_task(
        self,
        *,
        ReplicationTaskIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ReplicationInstanceArn: str,
        MigrationType: str,
        TableMappings: str,
        ReplicationTaskSettings: str | None = None,
        CdcStartTime: datetime.datetime | str | None = None,
        CdcStartPosition: str | None = None,
        CdcStopPosition: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        TaskData: str | None = None,
        ResourceIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_certificate(
        self,
        *,
        CertificateArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connection(
        self,
        *,
        EndpointArn: str,
        ReplicationInstanceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_migration(
        self,
        *,
        DataMigrationIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_provider(
        self,
        *,
        DataProviderIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_endpoint(
        self,
        *,
        EndpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_event_subscription(
        self,
        *,
        SubscriptionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_fleet_advisor_collector(
        self,
        *,
        CollectorReferencedId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_fleet_advisor_databases(
        self,
        *,
        DatabaseIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_instance_profile(
        self,
        *,
        InstanceProfileIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_migration_project(
        self,
        *,
        MigrationProjectIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_replication_config(
        self,
        *,
        ReplicationConfigArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_replication_instance(
        self,
        *,
        ReplicationInstanceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_replication_subnet_group(
        self,
        *,
        ReplicationSubnetGroupIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_replication_task(
        self,
        *,
        ReplicationTaskArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_replication_task_assessment_run(
        self,
        *,
        ReplicationTaskAssessmentRunArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_attributes(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_applicable_individual_assessments(
        self,
        *,
        ReplicationTaskArn: str | None = None,
        ReplicationInstanceArn: str | None = None,
        ReplicationConfigArn: str | None = None,
        SourceEngineName: str | None = None,
        TargetEngineName: str | None = None,
        MigrationType: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_certificates(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_connections(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_conversion_configuration(
        self,
        *,
        MigrationProjectIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_migrations(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        WithoutSettings: bool | None = None,
        WithoutStatistics: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_providers(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoint_settings(
        self,
        *,
        EngineName: str,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoint_types(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoints(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_engine_versions(
        self,
        *,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_event_categories(
        self,
        *,
        SourceType: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_event_subscriptions(
        self,
        *,
        SubscriptionName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_events(
        self,
        *,
        SourceIdentifier: str | None = None,
        SourceType: str | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        Duration: int | None = None,
        EventCategories: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_extension_pack_associations(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fleet_advisor_collectors(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fleet_advisor_databases(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fleet_advisor_lsa_analysis(
        self,
        *,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fleet_advisor_schema_object_summary(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fleet_advisor_schemas(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_profiles(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metadata_model(
        self,
        *,
        SelectionRules: str,
        MigrationProjectIdentifier: str,
        Origin: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metadata_model_assessments(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metadata_model_children(
        self,
        *,
        SelectionRules: str,
        MigrationProjectIdentifier: str,
        Origin: str,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metadata_model_conversions(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metadata_model_creations(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metadata_model_exports_as_script(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metadata_model_exports_to_target(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metadata_model_imports(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_migration_projects(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_orderable_replication_instances(
        self,
        *,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pending_maintenance_actions(
        self,
        *,
        ReplicationInstanceArn: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_recommendation_limitations(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_recommendations(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_refresh_schemas_status(
        self,
        *,
        EndpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_configs(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_instance_task_logs(
        self,
        *,
        ReplicationInstanceArn: str,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_instances(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_subnet_groups(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_table_statistics(
        self,
        *,
        ReplicationConfigArn: str,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_task_assessment_results(
        self,
        *,
        ReplicationTaskArn: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_task_assessment_runs(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_task_individual_assessments(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_tasks(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        WithoutSettings: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replications(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_schemas(
        self,
        *,
        EndpointArn: str,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_table_statistics(
        self,
        *,
        ReplicationTaskArn: str,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_metadata_model_assessment(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        FileName: str | None = None,
        AssessmentReportTypes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_target_selection_rules(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_certificate(
        self,
        *,
        CertificateIdentifier: str,
        CertificatePem: str | None = None,
        CertificateWallet: bytes | BinaryIO | str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        KmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str | None = None,
        ResourceArnList: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_conversion_configuration(
        self,
        *,
        MigrationProjectIdentifier: str,
        ConversionConfiguration: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_data_migration(
        self,
        *,
        DataMigrationIdentifier: str,
        DataMigrationName: str | None = None,
        EnableCloudwatchLogs: bool | None = None,
        ServiceAccessRoleArn: str | None = None,
        DataMigrationType: str | None = None,
        SourceDataSettings: list[dict[str, Any]] | None = None,
        TargetDataSettings: list[dict[str, Any]] | None = None,
        NumberOfJobs: int | None = None,
        SelectionRules: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_data_provider(
        self,
        *,
        DataProviderIdentifier: str,
        DataProviderName: str | None = None,
        Description: str | None = None,
        Engine: str | None = None,
        Virtual: bool | None = None,
        ExactSettings: bool | None = None,
        Settings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_endpoint(
        self,
        *,
        EndpointArn: str,
        EndpointIdentifier: str | None = None,
        EndpointType: str | None = None,
        EngineName: str | None = None,
        Username: str | None = None,
        Password: str | None = None,
        ServerName: str | None = None,
        Port: int | None = None,
        DatabaseName: str | None = None,
        ExtraConnectionAttributes: str | None = None,
        CertificateArn: str | None = None,
        SslMode: str | None = None,
        ServiceAccessRoleArn: str | None = None,
        ExternalTableDefinition: str | None = None,
        DynamoDbSettings: dict[str, Any] | None = None,
        S3Settings: dict[str, Any] | None = None,
        DmsTransferSettings: dict[str, Any] | None = None,
        MongoDbSettings: dict[str, Any] | None = None,
        KinesisSettings: dict[str, Any] | None = None,
        KafkaSettings: dict[str, Any] | None = None,
        ElasticsearchSettings: dict[str, Any] | None = None,
        NeptuneSettings: dict[str, Any] | None = None,
        RedshiftSettings: dict[str, Any] | None = None,
        PostgreSQLSettings: dict[str, Any] | None = None,
        MySQLSettings: dict[str, Any] | None = None,
        OracleSettings: dict[str, Any] | None = None,
        SybaseSettings: dict[str, Any] | None = None,
        MicrosoftSQLServerSettings: dict[str, Any] | None = None,
        IBMDb2Settings: dict[str, Any] | None = None,
        DocDbSettings: dict[str, Any] | None = None,
        RedisSettings: dict[str, Any] | None = None,
        ExactSettings: bool | None = None,
        GcpMySQLSettings: dict[str, Any] | None = None,
        TimestreamSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str | None = None,
        SourceType: str | None = None,
        EventCategories: list[str] | None = None,
        Enabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_profile(
        self,
        *,
        InstanceProfileIdentifier: str,
        AvailabilityZone: str | None = None,
        KmsKeyArn: str | None = None,
        PubliclyAccessible: bool | None = None,
        NetworkType: str | None = None,
        InstanceProfileName: str | None = None,
        Description: str | None = None,
        SubnetGroupIdentifier: str | None = None,
        VpcSecurityGroups: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_migration_project(
        self,
        *,
        MigrationProjectIdentifier: str,
        MigrationProjectName: str | None = None,
        SourceDataProviderDescriptors: list[dict[str, Any]] | None = None,
        TargetDataProviderDescriptors: list[dict[str, Any]] | None = None,
        InstanceProfileIdentifier: str | None = None,
        TransformationRules: str | None = None,
        Description: str | None = None,
        SchemaConversionApplicationAttributes: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_replication_config(
        self,
        *,
        ReplicationConfigArn: str,
        ReplicationConfigIdentifier: str | None = None,
        ReplicationType: str | None = None,
        TableMappings: str | None = None,
        ReplicationSettings: str | None = None,
        SupplementalSettings: str | None = None,
        ComputeConfig: dict[str, Any] | None = None,
        SourceEndpointArn: str | None = None,
        TargetEndpointArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_replication_instance(
        self,
        *,
        ReplicationInstanceArn: str,
        AllocatedStorage: int | None = None,
        ApplyImmediately: bool | None = None,
        ReplicationInstanceClass: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        PreferredMaintenanceWindow: str | None = None,
        MultiAZ: bool | None = None,
        EngineVersion: str | None = None,
        AllowMajorVersionUpgrade: bool | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        ReplicationInstanceIdentifier: str | None = None,
        NetworkType: str | None = None,
        KerberosAuthenticationSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_replication_subnet_group(
        self,
        *,
        ReplicationSubnetGroupIdentifier: str,
        SubnetIds: list[str],
        ReplicationSubnetGroupDescription: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_replication_task(
        self,
        *,
        ReplicationTaskArn: str,
        ReplicationTaskIdentifier: str | None = None,
        MigrationType: str | None = None,
        TableMappings: str | None = None,
        ReplicationTaskSettings: str | None = None,
        CdcStartTime: datetime.datetime | str | None = None,
        CdcStartPosition: str | None = None,
        CdcStopPosition: str | None = None,
        TaskData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def move_replication_task(
        self,
        *,
        ReplicationTaskArn: str,
        TargetReplicationInstanceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_replication_instance(
        self,
        *,
        ReplicationInstanceArn: str,
        ForceFailover: bool | None = None,
        ForcePlannedFailover: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def refresh_schemas(
        self,
        *,
        EndpointArn: str,
        ReplicationInstanceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reload_replication_tables(
        self,
        *,
        ReplicationConfigArn: str,
        TablesToReload: list[dict[str, Any]],
        ReloadOption: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reload_tables(
        self,
        *,
        ReplicationTaskArn: str,
        TablesToReload: list[dict[str, Any]],
        ReloadOption: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags_from_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def run_fleet_advisor_lsa_analysis(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_data_migration(
        self,
        *,
        DataMigrationIdentifier: str,
        StartType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_extension_pack_association(
        self,
        *,
        MigrationProjectIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_metadata_model_assessment(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_metadata_model_conversion(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_metadata_model_creation(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        MetadataModelName: str,
        Properties: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_metadata_model_export_as_script(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        Origin: str,
        FileName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_metadata_model_export_to_target(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        OverwriteExtensionPack: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_metadata_model_import(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        Origin: str,
        Refresh: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_recommendations(
        self,
        *,
        DatabaseId: str,
        Settings: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_replication(
        self,
        *,
        ReplicationConfigArn: str,
        StartReplicationType: str,
        PremigrationAssessmentSettings: str | None = None,
        CdcStartTime: datetime.datetime | str | None = None,
        CdcStartPosition: str | None = None,
        CdcStopPosition: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_replication_task(
        self,
        *,
        ReplicationTaskArn: str,
        StartReplicationTaskType: str,
        CdcStartTime: datetime.datetime | str | None = None,
        CdcStartPosition: str | None = None,
        CdcStopPosition: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_replication_task_assessment(
        self,
        *,
        ReplicationTaskArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_replication_task_assessment_run(
        self,
        *,
        ReplicationTaskArn: str,
        ServiceAccessRoleArn: str,
        ResultLocationBucket: str,
        AssessmentRunName: str,
        ResultLocationFolder: str | None = None,
        ResultEncryptionMode: str | None = None,
        ResultKmsKeyArn: str | None = None,
        IncludeOnly: list[str] | None = None,
        Exclude: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_data_migration(
        self,
        *,
        DataMigrationIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_replication(
        self,
        *,
        ReplicationConfigArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_replication_task(
        self,
        *,
        ReplicationTaskArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_connection(
        self,
        *,
        ReplicationInstanceArn: str,
        EndpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_subscriptions_to_event_bridge(
        self,
        *,
        ForceMove: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
