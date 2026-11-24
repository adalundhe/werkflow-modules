from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class NeptuneClient(ABC):

    @abstractmethod
    def add_role_to_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        RoleArn: str,
        FeatureName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_source_identifier_to_subscription(
        self,
        *,
        SubscriptionName: str,
        SourceIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_tags_to_resource(
        self,
        *,
        ResourceName: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def apply_pending_maintenance_action(
        self,
        *,
        ResourceIdentifier: str,
        ApplyAction: str,
        OptInType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_db_cluster_parameter_group(
        self,
        *,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_db_cluster_snapshot(
        self,
        *,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: str | None = None,
        PreSignedUrl: str | None = None,
        CopyTags: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SourceRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_db_parameter_group(
        self,
        *,
        SourceDBParameterGroupIdentifier: str,
        TargetDBParameterGroupIdentifier: str,
        TargetDBParameterGroupDescription: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        Engine: str,
        AvailabilityZones: list[str] | None = None,
        BackupRetentionPeriod: int | None = None,
        CharacterSetName: str | None = None,
        CopyTagsToSnapshot: bool | None = None,
        DatabaseName: str | None = None,
        DBClusterParameterGroupName: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        DBSubnetGroupName: str | None = None,
        EngineVersion: str | None = None,
        Port: int | None = None,
        MasterUsername: str | None = None,
        MasterUserPassword: str | None = None,
        OptionGroupName: str | None = None,
        PreferredBackupWindow: str | None = None,
        PreferredMaintenanceWindow: str | None = None,
        ReplicationSourceIdentifier: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        StorageEncrypted: bool | None = None,
        KmsKeyId: str | None = None,
        PreSignedUrl: str | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        DeletionProtection: bool | None = None,
        ServerlessV2ScalingConfiguration: dict[str, Any] | None = None,
        GlobalClusterIdentifier: str | None = None,
        StorageType: str | None = None,
        NetworkType: str | None = None,
        SourceRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_cluster_endpoint(
        self,
        *,
        DBClusterIdentifier: str,
        DBClusterEndpointIdentifier: str,
        EndpointType: str,
        StaticMembers: list[str] | None = None,
        ExcludedMembers: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_cluster_parameter_group(
        self,
        *,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_cluster_snapshot(
        self,
        *,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBClusterIdentifier: str,
        DBName: str | None = None,
        AllocatedStorage: int | None = None,
        MasterUsername: str | None = None,
        MasterUserPassword: str | None = None,
        DBSecurityGroups: list[str] | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        AvailabilityZone: str | None = None,
        DBSubnetGroupName: str | None = None,
        PreferredMaintenanceWindow: str | None = None,
        DBParameterGroupName: str | None = None,
        BackupRetentionPeriod: int | None = None,
        PreferredBackupWindow: str | None = None,
        Port: int | None = None,
        MultiAZ: bool | None = None,
        EngineVersion: str | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        LicenseModel: str | None = None,
        Iops: int | None = None,
        OptionGroupName: str | None = None,
        CharacterSetName: str | None = None,
        PubliclyAccessible: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        StorageType: str | None = None,
        TdeCredentialArn: str | None = None,
        TdeCredentialPassword: str | None = None,
        StorageEncrypted: bool | None = None,
        KmsKeyId: str | None = None,
        Domain: str | None = None,
        CopyTagsToSnapshot: bool | None = None,
        MonitoringInterval: int | None = None,
        MonitoringRoleArn: str | None = None,
        DomainIAMRoleName: str | None = None,
        PromotionTier: int | None = None,
        Timezone: str | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        EnablePerformanceInsights: bool | None = None,
        PerformanceInsightsKMSKeyId: str | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        DeletionProtection: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_parameter_group(
        self,
        *,
        DBParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_subnet_group(
        self,
        *,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: list[str],
        Tags: list[dict[str, Any]] | None = None,
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
    def create_global_cluster(
        self,
        *,
        GlobalClusterIdentifier: str,
        SourceDBClusterIdentifier: str | None = None,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        DeletionProtection: bool | None = None,
        DatabaseName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        StorageEncrypted: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool | None = None,
        FinalDBSnapshotIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_cluster_endpoint(
        self,
        *,
        DBClusterEndpointIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_cluster_parameter_group(
        self,
        *,
        DBClusterParameterGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_cluster_snapshot(
        self,
        *,
        DBClusterSnapshotIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        SkipFinalSnapshot: bool | None = None,
        FinalDBSnapshotIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_parameter_group(
        self,
        *,
        DBParameterGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_subnet_group(
        self,
        *,
        DBSubnetGroupName: str,
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
    def delete_global_cluster(
        self,
        *,
        GlobalClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_cluster_endpoints(
        self,
        *,
        DBClusterIdentifier: str | None = None,
        DBClusterEndpointIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_cluster_parameter_groups(
        self,
        *,
        DBClusterParameterGroupName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_cluster_parameters(
        self,
        *,
        DBClusterParameterGroupName: str,
        Source: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_cluster_snapshot_attributes(
        self,
        *,
        DBClusterSnapshotIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_cluster_snapshots(
        self,
        *,
        DBClusterIdentifier: str | None = None,
        DBClusterSnapshotIdentifier: str | None = None,
        SnapshotType: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        IncludeShared: bool | None = None,
        IncludePublic: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_clusters(
        self,
        *,
        DBClusterIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_engine_versions(
        self,
        *,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        DBParameterGroupFamily: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        DefaultOnly: bool | None = None,
        ListSupportedCharacterSets: bool | None = None,
        ListSupportedTimezones: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_instances(
        self,
        *,
        DBInstanceIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_parameter_groups(
        self,
        *,
        DBParameterGroupName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_parameters(
        self,
        *,
        DBParameterGroupName: str,
        Source: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_subnet_groups(
        self,
        *,
        DBSubnetGroupName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_engine_default_cluster_parameters(
        self,
        *,
        DBParameterGroupFamily: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_engine_default_parameters(
        self,
        *,
        DBParameterGroupFamily: str,
        Filters: list[dict[str, Any]] | None = None,
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
    def describe_global_clusters(
        self,
        *,
        GlobalClusterIdentifier: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_orderable_db_instance_options(
        self,
        *,
        Engine: str,
        EngineVersion: str | None = None,
        DBInstanceClass: str | None = None,
        LicenseModel: str | None = None,
        Vpc: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pending_maintenance_actions(
        self,
        *,
        ResourceIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_serverless_v2_platform_versions(
        self,
        *,
        ServerlessV2PlatformVersion: str | None = None,
        Engine: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DefaultOnly: bool | None = None,
        IncludeAll: bool | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_valid_db_instance_modifications(
        self,
        *,
        DBInstanceIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def failover_db_cluster(
        self,
        *,
        DBClusterIdentifier: str | None = None,
        TargetDBInstanceIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def failover_global_cluster(
        self,
        *,
        GlobalClusterIdentifier: str,
        TargetDbClusterIdentifier: str,
        AllowDataLoss: bool | None = None,
        Switchover: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceName: str,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: str | None = None,
        ApplyImmediately: bool | None = None,
        BackupRetentionPeriod: int | None = None,
        DBClusterParameterGroupName: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        Port: int | None = None,
        MasterUserPassword: str | None = None,
        OptionGroupName: str | None = None,
        PreferredBackupWindow: str | None = None,
        PreferredMaintenanceWindow: str | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        CloudwatchLogsExportConfiguration: dict[str, Any] | None = None,
        EngineVersion: str | None = None,
        AllowMajorVersionUpgrade: bool | None = None,
        DBInstanceParameterGroupName: str | None = None,
        DeletionProtection: bool | None = None,
        CopyTagsToSnapshot: bool | None = None,
        ServerlessV2ScalingConfiguration: dict[str, Any] | None = None,
        StorageType: str | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_cluster_endpoint(
        self,
        *,
        DBClusterEndpointIdentifier: str,
        EndpointType: str | None = None,
        StaticMembers: list[str] | None = None,
        ExcludedMembers: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_cluster_parameter_group(
        self,
        *,
        DBClusterParameterGroupName: str,
        Parameters: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_cluster_snapshot_attribute(
        self,
        *,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: list[str] | None = None,
        ValuesToRemove: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        AllocatedStorage: int | None = None,
        DBInstanceClass: str | None = None,
        DBSubnetGroupName: str | None = None,
        DBSecurityGroups: list[str] | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        ApplyImmediately: bool | None = None,
        MasterUserPassword: str | None = None,
        DBParameterGroupName: str | None = None,
        BackupRetentionPeriod: int | None = None,
        PreferredBackupWindow: str | None = None,
        PreferredMaintenanceWindow: str | None = None,
        MultiAZ: bool | None = None,
        EngineVersion: str | None = None,
        AllowMajorVersionUpgrade: bool | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        LicenseModel: str | None = None,
        Iops: int | None = None,
        OptionGroupName: str | None = None,
        NewDBInstanceIdentifier: str | None = None,
        StorageType: str | None = None,
        TdeCredentialArn: str | None = None,
        TdeCredentialPassword: str | None = None,
        CACertificateIdentifier: str | None = None,
        Domain: str | None = None,
        CopyTagsToSnapshot: bool | None = None,
        MonitoringInterval: int | None = None,
        DBPortNumber: int | None = None,
        PubliclyAccessible: bool | None = None,
        MonitoringRoleArn: str | None = None,
        DomainIAMRoleName: str | None = None,
        PromotionTier: int | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        EnablePerformanceInsights: bool | None = None,
        PerformanceInsightsKMSKeyId: str | None = None,
        CloudwatchLogsExportConfiguration: dict[str, Any] | None = None,
        DeletionProtection: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_parameter_group(
        self,
        *,
        DBParameterGroupName: str,
        Parameters: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_subnet_group(
        self,
        *,
        DBSubnetGroupName: str,
        SubnetIds: list[str],
        DBSubnetGroupDescription: str | None = None,
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
    def modify_global_cluster(
        self,
        *,
        GlobalClusterIdentifier: str,
        NewGlobalClusterIdentifier: str | None = None,
        DeletionProtection: bool | None = None,
        EngineVersion: str | None = None,
        AllowMajorVersionUpgrade: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def promote_read_replica_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        ForceFailover: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_from_global_cluster(
        self,
        *,
        GlobalClusterIdentifier: str,
        DbClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_role_from_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        RoleArn: str,
        FeatureName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_source_identifier_from_subscription(
        self,
        *,
        SubscriptionName: str,
        SourceIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags_from_resource(
        self,
        *,
        ResourceName: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_db_cluster_parameter_group(
        self,
        *,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool | None = None,
        Parameters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_db_parameter_group(
        self,
        *,
        DBParameterGroupName: str,
        ResetAllParameters: bool | None = None,
        Parameters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_db_cluster_from_snapshot(
        self,
        *,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: list[str] | None = None,
        EngineVersion: str | None = None,
        Port: int | None = None,
        DBSubnetGroupName: str | None = None,
        DatabaseName: str | None = None,
        OptionGroupName: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        KmsKeyId: str | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        DBClusterParameterGroupName: str | None = None,
        DeletionProtection: bool | None = None,
        CopyTagsToSnapshot: bool | None = None,
        ServerlessV2ScalingConfiguration: dict[str, Any] | None = None,
        StorageType: str | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_db_cluster_to_point_in_time(
        self,
        *,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreType: str | None = None,
        RestoreToTime: datetime.datetime | str | None = None,
        UseLatestRestorableTime: bool | None = None,
        Port: int | None = None,
        DBSubnetGroupName: str | None = None,
        OptionGroupName: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        KmsKeyId: str | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        DBClusterParameterGroupName: str | None = None,
        DeletionProtection: bool | None = None,
        ServerlessV2ScalingConfiguration: dict[str, Any] | None = None,
        StorageType: str | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def switchover_global_cluster(
        self,
        *,
        GlobalClusterIdentifier: str,
        TargetDbClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
