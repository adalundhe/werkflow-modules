from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class RDSClient(ABC):

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
    def create_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
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
        StorageThroughput: int | None = None,
        OptionGroupName: str | None = None,
        CharacterSetName: str | None = None,
        NcharCharacterSetName: str | None = None,
        PubliclyAccessible: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        DBClusterIdentifier: str | None = None,
        StorageType: str | None = None,
        TdeCredentialArn: str | None = None,
        TdeCredentialPassword: str | None = None,
        StorageEncrypted: bool | None = None,
        KmsKeyId: str | None = None,
        Domain: str | None = None,
        DomainFqdn: str | None = None,
        DomainOu: str | None = None,
        DomainAuthSecretArn: str | None = None,
        DomainDnsIps: list[str] | None = None,
        CopyTagsToSnapshot: bool | None = None,
        MonitoringInterval: int | None = None,
        MonitoringRoleArn: str | None = None,
        DomainIAMRoleName: str | None = None,
        PromotionTier: int | None = None,
        Timezone: str | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        DatabaseInsightsMode: str | None = None,
        EnablePerformanceInsights: bool | None = None,
        PerformanceInsightsKMSKeyId: str | None = None,
        PerformanceInsightsRetentionPeriod: int | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        ProcessorFeatures: list[dict[str, Any]] | None = None,
        DeletionProtection: bool | None = None,
        MaxAllocatedStorage: int | None = None,
        EnableCustomerOwnedIp: bool | None = None,
        NetworkType: str | None = None,
        BackupTarget: str | None = None,
        CustomIamInstanceProfile: str | None = None,
        DBSystemId: str | None = None,
        CACertificateIdentifier: str | None = None,
        ManageMasterUserPassword: bool | None = None,
        MasterUserSecretKmsKeyId: str | None = None,
        MultiTenant: bool | None = None,
        DedicatedLogVolume: bool | None = None,
        EngineLifecycleSupport: str | None = None,
        AdditionalStorageVolumes: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DBCapacityReservationIdentifier: str | None = None,
        MasterUserAuthenticationType: str | None = None,
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
        StorageThroughput: int | None = None,
        OptionGroupName: str | None = None,
        NewDBInstanceIdentifier: str | None = None,
        StorageType: str | None = None,
        TdeCredentialArn: str | None = None,
        TdeCredentialPassword: str | None = None,
        CACertificateIdentifier: str | None = None,
        Domain: str | None = None,
        DomainFqdn: str | None = None,
        DomainOu: str | None = None,
        DomainAuthSecretArn: str | None = None,
        DomainDnsIps: list[str] | None = None,
        DisableDomain: bool | None = None,
        CopyTagsToSnapshot: bool | None = None,
        MonitoringInterval: int | None = None,
        DBPortNumber: int | None = None,
        PubliclyAccessible: bool | None = None,
        MonitoringRoleArn: str | None = None,
        DomainIAMRoleName: str | None = None,
        PromotionTier: int | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        DatabaseInsightsMode: str | None = None,
        EnablePerformanceInsights: bool | None = None,
        PerformanceInsightsKMSKeyId: str | None = None,
        PerformanceInsightsRetentionPeriod: int | None = None,
        CloudwatchLogsExportConfiguration: dict[str, Any] | None = None,
        ProcessorFeatures: list[dict[str, Any]] | None = None,
        UseDefaultProcessorFeatures: bool | None = None,
        DeletionProtection: bool | None = None,
        MaxAllocatedStorage: int | None = None,
        CertificateRotationRestart: bool | None = None,
        ReplicaMode: str | None = None,
        AutomationMode: str | None = None,
        ResumeFullAutomationModeMinutes: int | None = None,
        EnableCustomerOwnedIp: bool | None = None,
        NetworkType: str | None = None,
        AwsBackupRecoveryPointArn: str | None = None,
        ManageMasterUserPassword: bool | None = None,
        RotateMasterUserPassword: bool | None = None,
        MasterUserSecretKmsKeyId: str | None = None,
        MultiTenant: bool | None = None,
        DedicatedLogVolume: bool | None = None,
        Engine: str | None = None,
        AdditionalStorageVolumes: list[dict[str, Any]] | None = None,
        DBCapacityReservationIdentifier: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        MasterUserAuthenticationType: str | None = None,
        EngineLifecycleSupport: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        SkipFinalSnapshot: bool | None = None,
        FinalDBSnapshotIdentifier: str | None = None,
        DeleteAutomatedBackups: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        DBCapacityReservationIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        DBSnapshotIdentifier: str | None = None,
        DetachFromDBCapacityReservation: bool | None = None,
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
    def describe_db_clusters(
        self,
        *,
        DBClusterIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        IncludeShared: bool | None = None,
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
        BacktrackWindow: int | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        EngineMode: str | None = None,
        ScalingConfiguration: dict[str, Any] | None = None,
        RdsCustomClusterConfiguration: dict[str, Any] | None = None,
        DBClusterInstanceClass: str | None = None,
        AllocatedStorage: int | None = None,
        StorageType: str | None = None,
        Iops: int | None = None,
        PubliclyAccessible: bool | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        DeletionProtection: bool | None = None,
        GlobalClusterIdentifier: str | None = None,
        EnableHttpEndpoint: bool | None = None,
        CopyTagsToSnapshot: bool | None = None,
        Domain: str | None = None,
        DomainIAMRoleName: str | None = None,
        EnableGlobalWriteForwarding: bool | None = None,
        NetworkType: str | None = None,
        ServerlessV2ScalingConfiguration: dict[str, Any] | None = None,
        MonitoringInterval: int | None = None,
        MonitoringRoleArn: str | None = None,
        DatabaseInsightsMode: str | None = None,
        EnablePerformanceInsights: bool | None = None,
        PerformanceInsightsKMSKeyId: str | None = None,
        PerformanceInsightsRetentionPeriod: int | None = None,
        EnableLimitlessDatabase: bool | None = None,
        ClusterScalabilityType: str | None = None,
        DBSystemId: str | None = None,
        ManageMasterUserPassword: bool | None = None,
        EnableLocalWriteForwarding: bool | None = None,
        MasterUserSecretKmsKeyId: str | None = None,
        CACertificateIdentifier: str | None = None,
        EngineLifecycleSupport: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        MasterUserAuthenticationType: str | None = None,
        EnableVPCNetworking: bool | None = None,
        WithExpressConfiguration: bool | None = None,
        EnableInternetAccessGateway: bool | None = None,
        AssociatedRoles: list[dict[str, Any]] | None = None,
        SourceRegion: str | None = None,
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
        BacktrackWindow: int | None = None,
        CloudwatchLogsExportConfiguration: dict[str, Any] | None = None,
        EngineVersion: str | None = None,
        AllowMajorVersionUpgrade: bool | None = None,
        DBInstanceParameterGroupName: str | None = None,
        Domain: str | None = None,
        DomainIAMRoleName: str | None = None,
        ScalingConfiguration: dict[str, Any] | None = None,
        DeletionProtection: bool | None = None,
        EnableHttpEndpoint: bool | None = None,
        CopyTagsToSnapshot: bool | None = None,
        EnableGlobalWriteForwarding: bool | None = None,
        DBClusterInstanceClass: str | None = None,
        AllocatedStorage: int | None = None,
        StorageType: str | None = None,
        Iops: int | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        NetworkType: str | None = None,
        ServerlessV2ScalingConfiguration: dict[str, Any] | None = None,
        MonitoringInterval: int | None = None,
        MonitoringRoleArn: str | None = None,
        DatabaseInsightsMode: str | None = None,
        EnablePerformanceInsights: bool | None = None,
        PerformanceInsightsKMSKeyId: str | None = None,
        PerformanceInsightsRetentionPeriod: int | None = None,
        ManageMasterUserPassword: bool | None = None,
        RotateMasterUserPassword: bool | None = None,
        EnableLocalWriteForwarding: bool | None = None,
        MasterUserSecretKmsKeyId: str | None = None,
        EngineMode: str | None = None,
        AllowEngineModeChange: bool | None = None,
        AwsBackupRecoveryPointArn: str | None = None,
        EnableLimitlessDatabase: bool | None = None,
        CACertificateIdentifier: str | None = None,
        MasterUserAuthenticationType: str | None = None,
        EngineLifecycleSupport: str | None = None,
        EnableInternetAccessGateway: bool | None = None,
        EnableVPCNetworking: bool | None = None,
        DBSubnetGroupName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool | None = None,
        FinalDBSnapshotIdentifier: str | None = None,
        DeleteAutomatedBackups: bool | None = None,
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
    def describe_db_snapshots(
        self,
        *,
        DBInstanceIdentifier: str | None = None,
        DBSnapshotIdentifier: str | None = None,
        SnapshotType: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        IncludeShared: bool | None = None,
        IncludePublic: bool | None = None,
        DbiResourceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_snapshot(
        self,
        *,
        DBSnapshotIdentifier: str,
        DBInstanceIdentifier: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_snapshot(
        self,
        *,
        DBSnapshotIdentifier: str,
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
        DbClusterResourceId: str | None = None,
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
    def delete_db_cluster_snapshot(
        self,
        *,
        DBClusterSnapshotIdentifier: str,
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
    def list_tags_for_resource(
        self,
        *,
        ResourceName: str,
        Filters: list[dict[str, Any]] | None = None,
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
    def remove_tags_from_resource(
        self,
        *,
        ResourceName: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

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
    def add_role_to_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        RoleArn: str,
        FeatureName: str,
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
    def apply_pending_maintenance_action(
        self,
        *,
        ResourceIdentifier: str,
        ApplyAction: str,
        OptInType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def authorize_db_security_group_ingress(
        self,
        *,
        DBSecurityGroupName: str,
        CIDRIP: str | None = None,
        EC2SecurityGroupName: str | None = None,
        EC2SecurityGroupId: str | None = None,
        EC2SecurityGroupOwnerId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def backtrack_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        BacktrackTo: datetime.datetime | str,
        Force: bool | None = None,
        UseEarliestTimeOnPointInTimeUnavailable: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_db_capacity_reservation(
        self,
        *,
        DBCapacityReservationIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_export_task(
        self,
        *,
        ExportTaskIdentifier: str,
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
    def copy_db_snapshot(
        self,
        *,
        SourceDBSnapshotIdentifier: str,
        TargetDBSnapshotIdentifier: str,
        KmsKeyId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        CopyTags: bool | None = None,
        PreSignedUrl: str | None = None,
        OptionGroupName: str | None = None,
        TargetCustomAvailabilityZone: str | None = None,
        SnapshotTarget: str | None = None,
        CopyOptionGroup: bool | None = None,
        SnapshotAvailabilityZone: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        SourceRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_option_group(
        self,
        *,
        SourceOptionGroupIdentifier: str,
        TargetOptionGroupIdentifier: str,
        TargetOptionGroupDescription: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_blue_green_deployment(
        self,
        *,
        BlueGreenDeploymentName: str,
        Source: str,
        TargetEngineVersion: str | None = None,
        TargetDBParameterGroupName: str | None = None,
        TargetDBClusterParameterGroupName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        TargetDBInstanceClass: str | None = None,
        UpgradeTargetStorageConfig: bool | None = None,
        TargetIops: int | None = None,
        TargetStorageType: str | None = None,
        TargetAllocatedStorage: int | None = None,
        TargetStorageThroughput: int | None = None,
        TargetResourceConfigurations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_db_engine_version(
        self,
        *,
        Engine: str,
        EngineVersion: str,
        DatabaseInstallationFilesS3BucketName: str | None = None,
        DatabaseInstallationFilesS3Prefix: str | None = None,
        DatabaseInstallationFiles: list[str] | None = None,
        ImageId: str | None = None,
        KMSKeyId: str | None = None,
        SourceCustomDbEngineVersionIdentifier: str | None = None,
        UseAwsProvidedLatestImage: bool | None = None,
        Description: str | None = None,
        Manifest: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_capacity_reservation(
        self,
        *,
        DBCapacityReservationName: str,
        DBInstanceClass: str,
        Engine: str,
        CapacityPerAvailabilityZone: int,
        AvailabilityZones: list[str],
        EndDate: datetime.datetime | str | None = None,
        StartDate: datetime.datetime | str | None = None,
        CommitmentDuration: int | None = None,
        LicenseModel: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
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
    def create_db_instance_read_replica(
        self,
        *,
        DBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str | None = None,
        DBInstanceClass: str | None = None,
        AvailabilityZone: str | None = None,
        Port: int | None = None,
        MultiAZ: bool | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        Iops: int | None = None,
        StorageThroughput: int | None = None,
        OptionGroupName: str | None = None,
        DBParameterGroupName: str | None = None,
        PubliclyAccessible: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        DBSubnetGroupName: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        StorageType: str | None = None,
        CopyTagsToSnapshot: bool | None = None,
        MonitoringInterval: int | None = None,
        MonitoringRoleArn: str | None = None,
        KmsKeyId: str | None = None,
        PreSignedUrl: str | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        DatabaseInsightsMode: str | None = None,
        EnablePerformanceInsights: bool | None = None,
        PerformanceInsightsKMSKeyId: str | None = None,
        PerformanceInsightsRetentionPeriod: int | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        ProcessorFeatures: list[dict[str, Any]] | None = None,
        UseDefaultProcessorFeatures: bool | None = None,
        DeletionProtection: bool | None = None,
        Domain: str | None = None,
        DomainIAMRoleName: str | None = None,
        DomainFqdn: str | None = None,
        DomainOu: str | None = None,
        DomainAuthSecretArn: str | None = None,
        DomainDnsIps: list[str] | None = None,
        ReplicaMode: str | None = None,
        EnableCustomerOwnedIp: bool | None = None,
        NetworkType: str | None = None,
        MaxAllocatedStorage: int | None = None,
        BackupTarget: str | None = None,
        CustomIamInstanceProfile: str | None = None,
        AllocatedStorage: int | None = None,
        SourceDBClusterIdentifier: str | None = None,
        DedicatedLogVolume: bool | None = None,
        UpgradeStorageConfig: bool | None = None,
        CACertificateIdentifier: str | None = None,
        AdditionalStorageVolumes: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DBCapacityReservationIdentifier: str | None = None,
        SourceRegion: str | None = None,
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
    def create_db_proxy(
        self,
        *,
        DBProxyName: str,
        EngineFamily: str,
        RoleArn: str,
        VpcSubnetIds: list[str],
        DefaultAuthScheme: str | None = None,
        Auth: list[dict[str, Any]] | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        RequireTLS: bool | None = None,
        IdleClientTimeout: int | None = None,
        DebugLogging: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        EndpointNetworkType: str | None = None,
        TargetConnectionNetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_proxy_endpoint(
        self,
        *,
        DBProxyName: str,
        DBProxyEndpointName: str,
        VpcSubnetIds: list[str],
        VpcSecurityGroupIds: list[str] | None = None,
        TargetRole: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        EndpointNetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_security_group(
        self,
        *,
        DBSecurityGroupName: str,
        DBSecurityGroupDescription: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_db_shard_group(
        self,
        *,
        DBShardGroupIdentifier: str,
        DBClusterIdentifier: str,
        MaxACU: float | int,
        ComputeRedundancy: int | None = None,
        MinACU: float | int | None = None,
        PubliclyAccessible: bool | None = None,
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
        EngineLifecycleSupport: str | None = None,
        DeletionProtection: bool | None = None,
        DatabaseName: str | None = None,
        StorageEncrypted: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_integration(
        self,
        *,
        SourceArn: str,
        TargetArn: str,
        IntegrationName: str,
        KMSKeyId: str | None = None,
        AdditionalEncryptionContext: dict[str, str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        DataFilter: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_option_group(
        self,
        *,
        OptionGroupName: str,
        EngineName: str,
        MajorEngineVersion: str,
        OptionGroupDescription: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tenant_database(
        self,
        *,
        DBInstanceIdentifier: str,
        TenantDBName: str,
        MasterUsername: str,
        MasterUserPassword: str | None = None,
        CharacterSetName: str | None = None,
        NcharCharacterSetName: str | None = None,
        ManageMasterUserPassword: bool | None = None,
        MasterUserSecretKmsKeyId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_blue_green_deployment(
        self,
        *,
        BlueGreenDeploymentIdentifier: str,
        DeleteTarget: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_db_engine_version(
        self,
        *,
        Engine: str,
        EngineVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_cluster_automated_backup(
        self,
        *,
        DbClusterResourceId: str,
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
    def delete_db_instance_automated_backup(
        self,
        *,
        DbiResourceId: str | None = None,
        DBInstanceAutomatedBackupsArn: str | None = None,
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
    def delete_db_proxy(
        self,
        *,
        DBProxyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_proxy_endpoint(
        self,
        *,
        DBProxyEndpointName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_security_group(
        self,
        *,
        DBSecurityGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_db_shard_group(
        self,
        *,
        DBShardGroupIdentifier: str,
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
    def delete_integration(
        self,
        *,
        IntegrationIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_option_group(
        self,
        *,
        OptionGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tenant_database(
        self,
        *,
        DBInstanceIdentifier: str,
        TenantDBName: str,
        SkipFinalSnapshot: bool | None = None,
        FinalDBSnapshotIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_db_proxy_targets(
        self,
        *,
        DBProxyName: str,
        TargetGroupName: str | None = None,
        DBInstanceIdentifiers: list[str] | None = None,
        DBClusterIdentifiers: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_attributes(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_blue_green_deployments(
        self,
        *,
        BlueGreenDeploymentIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_certificates(
        self,
        *,
        CertificateIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_capacity_reservations(
        self,
        *,
        DBCapacityReservationIdentifier: str | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_cluster_automated_backups(
        self,
        *,
        DbClusterResourceId: str | None = None,
        DBClusterIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_cluster_backtracks(
        self,
        *,
        DBClusterIdentifier: str,
        BacktrackIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
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
        IncludeAll: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_instance_automated_backups(
        self,
        *,
        DbiResourceId: str | None = None,
        DBInstanceIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        DBInstanceAutomatedBackupsArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_log_files(
        self,
        *,
        DBInstanceIdentifier: str,
        FilenameContains: str | None = None,
        FileLastWritten: int | None = None,
        FileSize: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_major_engine_versions(
        self,
        *,
        Engine: str | None = None,
        MajorEngineVersion: str | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
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
    def describe_db_proxies(
        self,
        *,
        DBProxyName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_proxy_endpoints(
        self,
        *,
        DBProxyName: str | None = None,
        DBProxyEndpointName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_proxy_target_groups(
        self,
        *,
        DBProxyName: str,
        TargetGroupName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_proxy_targets(
        self,
        *,
        DBProxyName: str,
        TargetGroupName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_recommendations(
        self,
        *,
        LastUpdatedAfter: datetime.datetime | str | None = None,
        LastUpdatedBefore: datetime.datetime | str | None = None,
        Locale: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_security_groups(
        self,
        *,
        DBSecurityGroupName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_shard_groups(
        self,
        *,
        DBShardGroupIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_snapshot_attributes(
        self,
        *,
        DBSnapshotIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_db_snapshot_tenant_databases(
        self,
        *,
        DBInstanceIdentifier: str | None = None,
        DBSnapshotIdentifier: str | None = None,
        SnapshotType: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        DbiResourceId: str | None = None,
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
    def describe_export_tasks(
        self,
        *,
        ExportTaskIdentifier: str | None = None,
        SourceArn: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
        SourceType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_global_clusters(
        self,
        *,
        GlobalClusterIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_integrations(
        self,
        *,
        IntegrationIdentifier: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_option_group_options(
        self,
        *,
        EngineName: str,
        MajorEngineVersion: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_option_groups(
        self,
        *,
        OptionGroupName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
        EngineName: str | None = None,
        MajorEngineVersion: str | None = None,
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
        AvailabilityZoneGroup: str | None = None,
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
    def describe_reserved_db_instances(
        self,
        *,
        ReservedDBInstanceId: str | None = None,
        ReservedDBInstancesOfferingId: str | None = None,
        DBInstanceClass: str | None = None,
        Duration: str | None = None,
        ProductDescription: str | None = None,
        OfferingType: str | None = None,
        MultiAZ: bool | None = None,
        LeaseId: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_db_instances_offerings(
        self,
        *,
        ReservedDBInstancesOfferingId: str | None = None,
        DBInstanceClass: str | None = None,
        Duration: str | None = None,
        ProductDescription: str | None = None,
        OfferingType: str | None = None,
        MultiAZ: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
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
    def describe_source_regions(
        self,
        *,
        RegionName: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tenant_databases(
        self,
        *,
        DBInstanceIdentifier: str | None = None,
        TenantDBName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
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
    def disable_http_endpoint(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def download_db_log_file_portion(
        self,
        *,
        DBInstanceIdentifier: str,
        LogFileName: str,
        Marker: str | None = None,
        NumberOfLines: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_http_endpoint(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def failover_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
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
    def modify_activity_stream(
        self,
        *,
        ResourceArn: str | None = None,
        AuditPolicyState: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_certificates(
        self,
        *,
        CertificateIdentifier: str | None = None,
        RemoveCustomerOverride: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_current_db_cluster_capacity(
        self,
        *,
        DBClusterIdentifier: str,
        Capacity: int | None = None,
        SecondsBeforeTimeout: int | None = None,
        TimeoutAction: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_custom_db_engine_version(
        self,
        *,
        Engine: str,
        EngineVersion: str,
        Description: str | None = None,
        Status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_capacity_reservation(
        self,
        *,
        DBCapacityReservationIdentifier: str,
        CapacityPerAvailabilityZone: int | None = None,
        EndDateType: str | None = None,
        EndDate: datetime.datetime | str | None = None,
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
    def modify_db_parameter_group(
        self,
        *,
        DBParameterGroupName: str,
        Parameters: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_proxy(
        self,
        *,
        DBProxyName: str,
        NewDBProxyName: str | None = None,
        DefaultAuthScheme: str | None = None,
        Auth: list[dict[str, Any]] | None = None,
        RequireTLS: bool | None = None,
        IdleClientTimeout: int | None = None,
        DebugLogging: bool | None = None,
        RoleArn: str | None = None,
        SecurityGroups: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_proxy_endpoint(
        self,
        *,
        DBProxyEndpointName: str,
        NewDBProxyEndpointName: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_proxy_target_group(
        self,
        *,
        TargetGroupName: str,
        DBProxyName: str,
        ConnectionPoolConfig: dict[str, Any] | None = None,
        NewName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_recommendation(
        self,
        *,
        RecommendationId: str,
        Locale: str | None = None,
        Status: str | None = None,
        RecommendedActionUpdates: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_shard_group(
        self,
        *,
        DBShardGroupIdentifier: str,
        MaxACU: float | int | None = None,
        MinACU: float | int | None = None,
        ComputeRedundancy: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_snapshot(
        self,
        *,
        DBSnapshotIdentifier: str,
        EngineVersion: str | None = None,
        OptionGroupName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_db_snapshot_attribute(
        self,
        *,
        DBSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: list[str] | None = None,
        ValuesToRemove: list[str] | None = None,
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
    def modify_integration(
        self,
        *,
        IntegrationIdentifier: str,
        IntegrationName: str | None = None,
        DataFilter: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_option_group(
        self,
        *,
        OptionGroupName: str,
        OptionsToInclude: list[dict[str, Any]] | None = None,
        OptionsToRemove: list[str] | None = None,
        ApplyImmediately: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_tenant_database(
        self,
        *,
        DBInstanceIdentifier: str,
        TenantDBName: str,
        MasterUserPassword: str | None = None,
        NewTenantDBName: str | None = None,
        ManageMasterUserPassword: bool | None = None,
        RotateMasterUserPassword: bool | None = None,
        MasterUserSecretKmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def promote_read_replica(
        self,
        *,
        DBInstanceIdentifier: str,
        BackupRetentionPeriod: int | None = None,
        PreferredBackupWindow: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
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
    def purchase_reserved_db_instances_offering(
        self,
        *,
        ReservedDBInstancesOfferingId: str,
        ReservedDBInstanceId: str | None = None,
        DBInstanceCount: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_db_shard_group(
        self,
        *,
        DBShardGroupIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_db_proxy_targets(
        self,
        *,
        DBProxyName: str,
        TargetGroupName: str | None = None,
        DBInstanceIdentifiers: list[str] | None = None,
        DBClusterIdentifiers: list[str] | None = None,
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
    def remove_role_from_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        RoleArn: str,
        FeatureName: str,
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
    def restore_db_cluster_from_s3(
        self,
        *,
        DBClusterIdentifier: str,
        Engine: str,
        MasterUsername: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
        AvailabilityZones: list[str] | None = None,
        BackupRetentionPeriod: int | None = None,
        CharacterSetName: str | None = None,
        DatabaseName: str | None = None,
        DBClusterParameterGroupName: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        DBSubnetGroupName: str | None = None,
        EngineVersion: str | None = None,
        Port: int | None = None,
        MasterUserPassword: str | None = None,
        OptionGroupName: str | None = None,
        PreferredBackupWindow: str | None = None,
        PreferredMaintenanceWindow: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        StorageEncrypted: bool | None = None,
        KmsKeyId: str | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        S3Prefix: str | None = None,
        BacktrackWindow: int | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        DeletionProtection: bool | None = None,
        CopyTagsToSnapshot: bool | None = None,
        Domain: str | None = None,
        DomainIAMRoleName: str | None = None,
        StorageType: str | None = None,
        NetworkType: str | None = None,
        ServerlessV2ScalingConfiguration: dict[str, Any] | None = None,
        ManageMasterUserPassword: bool | None = None,
        MasterUserSecretKmsKeyId: str | None = None,
        EngineLifecycleSupport: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        AssociatedRoles: list[dict[str, Any]] | None = None,
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
        BacktrackWindow: int | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        EngineMode: str | None = None,
        ScalingConfiguration: dict[str, Any] | None = None,
        DBClusterParameterGroupName: str | None = None,
        DeletionProtection: bool | None = None,
        CopyTagsToSnapshot: bool | None = None,
        Domain: str | None = None,
        DomainIAMRoleName: str | None = None,
        DBClusterInstanceClass: str | None = None,
        StorageType: str | None = None,
        Iops: int | None = None,
        PubliclyAccessible: bool | None = None,
        NetworkType: str | None = None,
        ServerlessV2ScalingConfiguration: dict[str, Any] | None = None,
        RdsCustomClusterConfiguration: dict[str, Any] | None = None,
        MonitoringInterval: int | None = None,
        MonitoringRoleArn: str | None = None,
        EnablePerformanceInsights: bool | None = None,
        PerformanceInsightsKMSKeyId: str | None = None,
        PerformanceInsightsRetentionPeriod: int | None = None,
        BackupRetentionPeriod: int | None = None,
        PreferredBackupWindow: str | None = None,
        EngineLifecycleSupport: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        EnableVPCNetworking: bool | None = None,
        EnableInternetAccessGateway: bool | None = None,
        AssociatedRoles: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_db_cluster_to_point_in_time(
        self,
        *,
        DBClusterIdentifier: str,
        RestoreType: str | None = None,
        SourceDBClusterIdentifier: str | None = None,
        RestoreToTime: datetime.datetime | str | None = None,
        UseLatestRestorableTime: bool | None = None,
        Port: int | None = None,
        DBSubnetGroupName: str | None = None,
        OptionGroupName: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        KmsKeyId: str | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        BacktrackWindow: int | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        DBClusterParameterGroupName: str | None = None,
        DeletionProtection: bool | None = None,
        CopyTagsToSnapshot: bool | None = None,
        Domain: str | None = None,
        DomainIAMRoleName: str | None = None,
        DBClusterInstanceClass: str | None = None,
        StorageType: str | None = None,
        PubliclyAccessible: bool | None = None,
        Iops: int | None = None,
        NetworkType: str | None = None,
        SourceDbClusterResourceId: str | None = None,
        ServerlessV2ScalingConfiguration: dict[str, Any] | None = None,
        ScalingConfiguration: dict[str, Any] | None = None,
        EngineMode: str | None = None,
        RdsCustomClusterConfiguration: dict[str, Any] | None = None,
        MonitoringInterval: int | None = None,
        MonitoringRoleArn: str | None = None,
        EnablePerformanceInsights: bool | None = None,
        PerformanceInsightsKMSKeyId: str | None = None,
        PerformanceInsightsRetentionPeriod: int | None = None,
        BackupRetentionPeriod: int | None = None,
        PreferredBackupWindow: str | None = None,
        EngineLifecycleSupport: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        EnableVPCNetworking: bool | None = None,
        EnableInternetAccessGateway: bool | None = None,
        AssociatedRoles: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_db_instance_from_db_snapshot(
        self,
        *,
        DBInstanceIdentifier: str,
        DBSnapshotIdentifier: str | None = None,
        DBInstanceClass: str | None = None,
        Port: int | None = None,
        AvailabilityZone: str | None = None,
        DBSubnetGroupName: str | None = None,
        MultiAZ: bool | None = None,
        PubliclyAccessible: bool | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        LicenseModel: str | None = None,
        DBName: str | None = None,
        Engine: str | None = None,
        Iops: int | None = None,
        StorageThroughput: int | None = None,
        OptionGroupName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        StorageType: str | None = None,
        TdeCredentialArn: str | None = None,
        TdeCredentialPassword: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        Domain: str | None = None,
        DomainFqdn: str | None = None,
        DomainOu: str | None = None,
        DomainAuthSecretArn: str | None = None,
        DomainDnsIps: list[str] | None = None,
        CopyTagsToSnapshot: bool | None = None,
        DomainIAMRoleName: str | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        ProcessorFeatures: list[dict[str, Any]] | None = None,
        UseDefaultProcessorFeatures: bool | None = None,
        DBParameterGroupName: str | None = None,
        DeletionProtection: bool | None = None,
        EnableCustomerOwnedIp: bool | None = None,
        NetworkType: str | None = None,
        BackupTarget: str | None = None,
        CustomIamInstanceProfile: str | None = None,
        AllocatedStorage: int | None = None,
        DBClusterSnapshotIdentifier: str | None = None,
        BackupRetentionPeriod: int | None = None,
        PreferredBackupWindow: str | None = None,
        DBCapacityReservationIdentifier: str | None = None,
        DedicatedLogVolume: bool | None = None,
        CACertificateIdentifier: str | None = None,
        EngineLifecycleSupport: str | None = None,
        AdditionalStorageVolumes: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ManageMasterUserPassword: bool | None = None,
        MasterUserSecretKmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_db_instance_from_s3(
        self,
        *,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
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
        StorageThroughput: int | None = None,
        OptionGroupName: str | None = None,
        PubliclyAccessible: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        StorageType: str | None = None,
        StorageEncrypted: bool | None = None,
        KmsKeyId: str | None = None,
        CopyTagsToSnapshot: bool | None = None,
        MonitoringInterval: int | None = None,
        MonitoringRoleArn: str | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        S3Prefix: str | None = None,
        DatabaseInsightsMode: str | None = None,
        EnablePerformanceInsights: bool | None = None,
        PerformanceInsightsKMSKeyId: str | None = None,
        PerformanceInsightsRetentionPeriod: int | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        ProcessorFeatures: list[dict[str, Any]] | None = None,
        UseDefaultProcessorFeatures: bool | None = None,
        DeletionProtection: bool | None = None,
        MaxAllocatedStorage: int | None = None,
        NetworkType: str | None = None,
        ManageMasterUserPassword: bool | None = None,
        MasterUserSecretKmsKeyId: str | None = None,
        DBCapacityReservationIdentifier: str | None = None,
        DedicatedLogVolume: bool | None = None,
        CACertificateIdentifier: str | None = None,
        EngineLifecycleSupport: str | None = None,
        AdditionalStorageVolumes: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_db_instance_to_point_in_time(
        self,
        *,
        TargetDBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str | None = None,
        RestoreTime: datetime.datetime | str | None = None,
        UseLatestRestorableTime: bool | None = None,
        DBInstanceClass: str | None = None,
        Port: int | None = None,
        AvailabilityZone: str | None = None,
        DBSubnetGroupName: str | None = None,
        MultiAZ: bool | None = None,
        PubliclyAccessible: bool | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        LicenseModel: str | None = None,
        DBName: str | None = None,
        Engine: str | None = None,
        Iops: int | None = None,
        StorageThroughput: int | None = None,
        OptionGroupName: str | None = None,
        CopyTagsToSnapshot: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        StorageType: str | None = None,
        TdeCredentialArn: str | None = None,
        TdeCredentialPassword: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        Domain: str | None = None,
        DomainIAMRoleName: str | None = None,
        DomainFqdn: str | None = None,
        DomainOu: str | None = None,
        DomainAuthSecretArn: str | None = None,
        DomainDnsIps: list[str] | None = None,
        EnableIAMDatabaseAuthentication: bool | None = None,
        EnableCloudwatchLogsExports: list[str] | None = None,
        ProcessorFeatures: list[dict[str, Any]] | None = None,
        UseDefaultProcessorFeatures: bool | None = None,
        DBParameterGroupName: str | None = None,
        DeletionProtection: bool | None = None,
        SourceDbiResourceId: str | None = None,
        MaxAllocatedStorage: int | None = None,
        EnableCustomerOwnedIp: bool | None = None,
        NetworkType: str | None = None,
        SourceDBInstanceAutomatedBackupsArn: str | None = None,
        BackupTarget: str | None = None,
        CustomIamInstanceProfile: str | None = None,
        AllocatedStorage: int | None = None,
        BackupRetentionPeriod: int | None = None,
        PreferredBackupWindow: str | None = None,
        DBCapacityReservationIdentifier: str | None = None,
        DedicatedLogVolume: bool | None = None,
        CACertificateIdentifier: str | None = None,
        EngineLifecycleSupport: str | None = None,
        AdditionalStorageVolumes: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ManageMasterUserPassword: bool | None = None,
        MasterUserSecretKmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_db_security_group_ingress(
        self,
        *,
        DBSecurityGroupName: str,
        CIDRIP: str | None = None,
        EC2SecurityGroupName: str | None = None,
        EC2SecurityGroupId: str | None = None,
        EC2SecurityGroupOwnerId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_activity_stream(
        self,
        *,
        ResourceArn: str,
        Mode: str,
        KmsKeyId: str,
        ApplyImmediately: bool | None = None,
        EngineNativeAuditFieldsIncluded: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_db_instance_automated_backups_replication(
        self,
        *,
        SourceDBInstanceArn: str,
        BackupRetentionPeriod: int | None = None,
        KmsKeyId: str | None = None,
        PreSignedUrl: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SourceRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_export_task(
        self,
        *,
        ExportTaskIdentifier: str,
        SourceArn: str,
        S3BucketName: str,
        IamRoleArn: str,
        KmsKeyId: str,
        S3Prefix: str | None = None,
        ExportOnly: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_activity_stream(
        self,
        *,
        ResourceArn: str,
        ApplyImmediately: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_db_instance_automated_backups_replication(
        self,
        *,
        SourceDBInstanceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def switchover_blue_green_deployment(
        self,
        *,
        BlueGreenDeploymentIdentifier: str,
        SwitchoverTimeout: int | None = None,
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
    def switchover_read_replica(
        self,
        *,
        DBInstanceIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
