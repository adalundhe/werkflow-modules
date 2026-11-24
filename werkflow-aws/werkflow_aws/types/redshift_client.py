from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class RedshiftClient(ABC):

    @abstractmethod
    def accept_reserved_node_exchange(
        self,
        *,
        ReservedNodeId: str,
        TargetReservedNodeOfferingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_partner(
        self,
        *,
        AccountId: str,
        ClusterIdentifier: str,
        DatabaseName: str,
        PartnerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_data_share_consumer(
        self,
        *,
        DataShareArn: str,
        AssociateEntireAccount: bool | None = None,
        ConsumerArn: str | None = None,
        ConsumerRegion: str | None = None,
        AllowWrites: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def authorize_cluster_security_group_ingress(
        self,
        *,
        ClusterSecurityGroupName: str,
        CIDRIP: str | None = None,
        EC2SecurityGroupName: str | None = None,
        EC2SecurityGroupOwnerId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def authorize_data_share(
        self,
        *,
        DataShareArn: str,
        ConsumerIdentifier: str,
        AllowWrites: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def authorize_endpoint_access(
        self,
        *,
        Account: str,
        ClusterIdentifier: str | None = None,
        VpcIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def authorize_snapshot_access(
        self,
        *,
        AccountWithRestoreAccess: str,
        SnapshotIdentifier: str | None = None,
        SnapshotArn: str | None = None,
        SnapshotClusterIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_cluster_snapshots(
        self,
        *,
        Identifiers: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_modify_cluster_snapshots(
        self,
        *,
        SnapshotIdentifierList: list[str],
        ManualSnapshotRetentionPeriod: int | None = None,
        Force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_resize(
        self,
        *,
        ClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_cluster_snapshot(
        self,
        *,
        SourceSnapshotIdentifier: str,
        TargetSnapshotIdentifier: str,
        SourceSnapshotClusterIdentifier: str | None = None,
        ManualSnapshotRetentionPeriod: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_authentication_profile(
        self,
        *,
        AuthenticationProfileName: str,
        AuthenticationProfileContent: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster(
        self,
        *,
        ClusterIdentifier: str,
        NodeType: str,
        MasterUsername: str,
        DBName: str | None = None,
        ClusterType: str | None = None,
        MasterUserPassword: str | None = None,
        ClusterSecurityGroups: list[str] | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        ClusterSubnetGroupName: str | None = None,
        AvailabilityZone: str | None = None,
        PreferredMaintenanceWindow: str | None = None,
        ClusterParameterGroupName: str | None = None,
        AutomatedSnapshotRetentionPeriod: int | None = None,
        ManualSnapshotRetentionPeriod: int | None = None,
        Port: int | None = None,
        ClusterVersion: str | None = None,
        AllowVersionUpgrade: bool | None = None,
        NumberOfNodes: int | None = None,
        PubliclyAccessible: bool | None = None,
        Encrypted: bool | None = None,
        HsmClientCertificateIdentifier: str | None = None,
        HsmConfigurationIdentifier: str | None = None,
        ElasticIp: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        KmsKeyId: str | None = None,
        EnhancedVpcRouting: bool | None = None,
        AdditionalInfo: str | None = None,
        IamRoles: list[str] | None = None,
        MaintenanceTrackName: str | None = None,
        SnapshotScheduleIdentifier: str | None = None,
        AvailabilityZoneRelocation: bool | None = None,
        AquaConfigurationStatus: str | None = None,
        DefaultIamRoleArn: str | None = None,
        LoadSampleData: str | None = None,
        ManageMasterPassword: bool | None = None,
        MasterPasswordSecretKmsKeyId: str | None = None,
        IpAddressType: str | None = None,
        MultiAZ: bool | None = None,
        RedshiftIdcApplicationArn: str | None = None,
        CatalogName: str | None = None,
        ExtraComputeForAutomaticOptimization: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster_parameter_group(
        self,
        *,
        ParameterGroupName: str,
        ParameterGroupFamily: str,
        Description: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster_security_group(
        self,
        *,
        ClusterSecurityGroupName: str,
        Description: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster_snapshot(
        self,
        *,
        SnapshotIdentifier: str,
        ClusterIdentifier: str,
        ManualSnapshotRetentionPeriod: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster_subnet_group(
        self,
        *,
        ClusterSubnetGroupName: str,
        Description: str,
        SubnetIds: list[str],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_domain_association(
        self,
        *,
        CustomDomainName: str,
        CustomDomainCertificateArn: str,
        ClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_endpoint_access(
        self,
        *,
        EndpointName: str,
        SubnetGroupName: str,
        ClusterIdentifier: str | None = None,
        ResourceOwner: str | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str | None = None,
        SourceIds: list[str] | None = None,
        EventCategories: list[str] | None = None,
        Severity: str | None = None,
        Enabled: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_hsm_client_certificate(
        self,
        *,
        HsmClientCertificateIdentifier: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_hsm_configuration(
        self,
        *,
        HsmConfigurationIdentifier: str,
        Description: str,
        HsmIpAddress: str,
        HsmPartitionName: str,
        HsmPartitionPassword: str,
        HsmServerPublicCertificate: str,
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
        TagList: list[dict[str, Any]] | None = None,
        AdditionalEncryptionContext: dict[str, str] | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_qev2_idc_application(
        self,
        *,
        IdcInstanceArn: str,
        Qev2IdcApplicationName: str,
        IdcDisplayName: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_redshift_idc_application(
        self,
        *,
        IdcInstanceArn: str,
        RedshiftIdcApplicationName: str,
        IdcDisplayName: str,
        IamRoleArn: str,
        IdentityNamespace: str | None = None,
        AuthorizedTokenIssuerList: list[dict[str, Any]] | None = None,
        ServiceIntegrations: list[dict[str, Any]] | None = None,
        ApplicationType: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SsoTagKeys: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_scheduled_action(
        self,
        *,
        ScheduledActionName: str,
        TargetAction: dict[str, Any],
        Schedule: str,
        IamRole: str,
        ScheduledActionDescription: str | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        Enable: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshot_copy_grant(
        self,
        *,
        SnapshotCopyGrantName: str,
        KmsKeyId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshot_schedule(
        self,
        *,
        ScheduleDefinitions: list[str] | None = None,
        ScheduleIdentifier: str | None = None,
        ScheduleDescription: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        NextInvocations: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tags(
        self,
        *,
        ResourceName: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_usage_limit(
        self,
        *,
        ClusterIdentifier: str,
        FeatureType: str,
        LimitType: str,
        Amount: int,
        Period: str | None = None,
        BreachAction: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deauthorize_data_share(
        self,
        *,
        DataShareArn: str,
        ConsumerIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_authentication_profile(
        self,
        *,
        AuthenticationProfileName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster(
        self,
        *,
        ClusterIdentifier: str,
        SkipFinalClusterSnapshot: bool | None = None,
        FinalClusterSnapshotIdentifier: str | None = None,
        FinalClusterSnapshotRetentionPeriod: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster_parameter_group(
        self,
        *,
        ParameterGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster_security_group(
        self,
        *,
        ClusterSecurityGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster_snapshot(
        self,
        *,
        SnapshotIdentifier: str,
        SnapshotClusterIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster_subnet_group(
        self,
        *,
        ClusterSubnetGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_domain_association(
        self,
        *,
        ClusterIdentifier: str,
        CustomDomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_endpoint_access(
        self,
        *,
        EndpointName: str,
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
    def delete_hsm_client_certificate(
        self,
        *,
        HsmClientCertificateIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_hsm_configuration(
        self,
        *,
        HsmConfigurationIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_integration(
        self,
        *,
        IntegrationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_partner(
        self,
        *,
        AccountId: str,
        ClusterIdentifier: str,
        DatabaseName: str,
        PartnerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_qev2_idc_application(
        self,
        *,
        Qev2IdcApplicationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_redshift_idc_application(
        self,
        *,
        RedshiftIdcApplicationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_scheduled_action(
        self,
        *,
        ScheduledActionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_snapshot_copy_grant(
        self,
        *,
        SnapshotCopyGrantName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_snapshot_schedule(
        self,
        *,
        ScheduleIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tags(
        self,
        *,
        ResourceName: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_usage_limit(
        self,
        *,
        UsageLimitId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_namespace(
        self,
        *,
        NamespaceIdentifier: dict[str, Any],
        ConsumerIdentifiers: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_attributes(
        self,
        *,
        AttributeNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_authentication_profiles(
        self,
        *,
        AuthenticationProfileName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_db_revisions(
        self,
        *,
        ClusterIdentifier: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_parameter_groups(
        self,
        *,
        ParameterGroupName: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_parameters(
        self,
        *,
        ParameterGroupName: str,
        Source: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_security_groups(
        self,
        *,
        ClusterSecurityGroupName: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_snapshots(
        self,
        *,
        ClusterIdentifier: str | None = None,
        SnapshotIdentifier: str | None = None,
        SnapshotArn: str | None = None,
        SnapshotType: str | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        OwnerAccount: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
        ClusterExists: bool | None = None,
        SortingEntities: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_subnet_groups(
        self,
        *,
        ClusterSubnetGroupName: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_tracks(
        self,
        *,
        MaintenanceTrackName: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_versions(
        self,
        *,
        ClusterVersion: str | None = None,
        ClusterParameterGroupFamily: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_clusters(
        self,
        *,
        ClusterIdentifier: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_custom_domain_associations(
        self,
        *,
        CustomDomainName: str | None = None,
        CustomDomainCertificateArn: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_shares(
        self,
        *,
        DataShareArn: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_shares_for_consumer(
        self,
        *,
        ConsumerArn: str | None = None,
        Status: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_shares_for_producer(
        self,
        *,
        ProducerArn: str | None = None,
        Status: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_default_cluster_parameters(
        self,
        *,
        ParameterGroupFamily: str,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoint_access(
        self,
        *,
        ClusterIdentifier: str | None = None,
        ResourceOwner: str | None = None,
        EndpointName: str | None = None,
        VpcId: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoint_authorization(
        self,
        *,
        ClusterIdentifier: str | None = None,
        Account: str | None = None,
        Grantee: bool | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_event_categories(
        self,
        *,
        SourceType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_event_subscriptions(
        self,
        *,
        SubscriptionName: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
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
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_hsm_client_certificates(
        self,
        *,
        HsmClientCertificateIdentifier: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_hsm_configurations(
        self,
        *,
        HsmConfigurationIdentifier: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_inbound_integrations(
        self,
        *,
        IntegrationArn: str | None = None,
        TargetArn: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_integrations(
        self,
        *,
        IntegrationArn: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_logging_status(
        self,
        *,
        ClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_node_configuration_options(
        self,
        *,
        ActionType: str,
        ClusterIdentifier: str | None = None,
        SnapshotIdentifier: str | None = None,
        SnapshotArn: str | None = None,
        OwnerAccount: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_orderable_cluster_options(
        self,
        *,
        ClusterVersion: str | None = None,
        NodeType: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_partners(
        self,
        *,
        AccountId: str,
        ClusterIdentifier: str,
        DatabaseName: str | None = None,
        PartnerName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_qev2_idc_applications(
        self,
        *,
        Qev2IdcApplicationArn: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_redshift_idc_applications(
        self,
        *,
        RedshiftIdcApplicationArn: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_node_exchange_status(
        self,
        *,
        ReservedNodeId: str | None = None,
        ReservedNodeExchangeRequestId: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_node_offerings(
        self,
        *,
        ReservedNodeOfferingId: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_nodes(
        self,
        *,
        ReservedNodeId: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resize(
        self,
        *,
        ClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_scheduled_actions(
        self,
        *,
        ScheduledActionName: str | None = None,
        TargetActionType: str | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        Active: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshot_copy_grants(
        self,
        *,
        SnapshotCopyGrantName: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshot_schedules(
        self,
        *,
        ClusterIdentifier: str | None = None,
        ScheduleIdentifier: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_storage(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_table_restore_status(
        self,
        *,
        ClusterIdentifier: str | None = None,
        TableRestoreRequestId: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tags(
        self,
        *,
        ResourceName: str | None = None,
        ResourceType: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_usage_limits(
        self,
        *,
        UsageLimitId: str | None = None,
        ClusterIdentifier: str | None = None,
        FeatureType: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        TagKeys: list[str] | None = None,
        TagValues: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_logging(
        self,
        *,
        ClusterIdentifier: str,
        LogDestinationType: str | None = None,
        LogExports: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_snapshot_copy(
        self,
        *,
        ClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_data_share_consumer(
        self,
        *,
        DataShareArn: str,
        DisassociateEntireAccount: bool | None = None,
        ConsumerArn: str | None = None,
        ConsumerRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_logging(
        self,
        *,
        ClusterIdentifier: str,
        BucketName: str | None = None,
        S3KeyPrefix: str | None = None,
        LogDestinationType: str | None = None,
        LogExports: list[str] | None = None,
        S3TableKmsKeyId: str | None = None,
        S3TableGranularity: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_snapshot_copy(
        self,
        *,
        ClusterIdentifier: str,
        DestinationRegion: str,
        RetentionPeriod: int | None = None,
        SnapshotCopyGrantName: str | None = None,
        ManualSnapshotRetentionPeriod: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def failover_primary_compute(
        self,
        *,
        ClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cluster_credentials(
        self,
        *,
        DbUser: str,
        DbName: str | None = None,
        ClusterIdentifier: str | None = None,
        DurationSeconds: int | None = None,
        AutoCreate: bool | None = None,
        DbGroups: list[str] | None = None,
        CustomDomainName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cluster_credentials_with_iam(
        self,
        *,
        DbName: str | None = None,
        ClusterIdentifier: str | None = None,
        DurationSeconds: int | None = None,
        CustomDomainName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_identity_center_auth_token(
        self,
        *,
        ClusterIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_reserved_node_exchange_configuration_options(
        self,
        *,
        ActionType: str,
        ClusterIdentifier: str | None = None,
        SnapshotIdentifier: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_reserved_node_exchange_offerings(
        self,
        *,
        ReservedNodeId: str,
        MaxRecords: int | None = None,
        Marker: str | None = None,
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
    def list_recommendations(
        self,
        *,
        ClusterIdentifier: str | None = None,
        NamespaceArn: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_aqua_configuration(
        self,
        *,
        ClusterIdentifier: str,
        AquaConfigurationStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_authentication_profile(
        self,
        *,
        AuthenticationProfileName: str,
        AuthenticationProfileContent: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cluster(
        self,
        *,
        ClusterIdentifier: str,
        ClusterType: str | None = None,
        NodeType: str | None = None,
        NumberOfNodes: int | None = None,
        ClusterSecurityGroups: list[str] | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        MasterUserPassword: str | None = None,
        ClusterParameterGroupName: str | None = None,
        AutomatedSnapshotRetentionPeriod: int | None = None,
        ManualSnapshotRetentionPeriod: int | None = None,
        PreferredMaintenanceWindow: str | None = None,
        ClusterVersion: str | None = None,
        AllowVersionUpgrade: bool | None = None,
        HsmClientCertificateIdentifier: str | None = None,
        HsmConfigurationIdentifier: str | None = None,
        NewClusterIdentifier: str | None = None,
        PubliclyAccessible: bool | None = None,
        ElasticIp: str | None = None,
        EnhancedVpcRouting: bool | None = None,
        MaintenanceTrackName: str | None = None,
        Encrypted: bool | None = None,
        KmsKeyId: str | None = None,
        AvailabilityZoneRelocation: bool | None = None,
        AvailabilityZone: str | None = None,
        Port: int | None = None,
        ManageMasterPassword: bool | None = None,
        MasterPasswordSecretKmsKeyId: str | None = None,
        IpAddressType: str | None = None,
        MultiAZ: bool | None = None,
        ExtraComputeForAutomaticOptimization: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cluster_db_revision(
        self,
        *,
        ClusterIdentifier: str,
        RevisionTarget: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cluster_iam_roles(
        self,
        *,
        ClusterIdentifier: str,
        AddIamRoles: list[str] | None = None,
        RemoveIamRoles: list[str] | None = None,
        DefaultIamRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cluster_maintenance(
        self,
        *,
        ClusterIdentifier: str,
        DeferMaintenance: bool | None = None,
        DeferMaintenanceIdentifier: str | None = None,
        DeferMaintenanceStartTime: datetime.datetime | str | None = None,
        DeferMaintenanceEndTime: datetime.datetime | str | None = None,
        DeferMaintenanceDuration: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cluster_parameter_group(
        self,
        *,
        ParameterGroupName: str,
        Parameters: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cluster_snapshot(
        self,
        *,
        SnapshotIdentifier: str,
        ManualSnapshotRetentionPeriod: int | None = None,
        Force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cluster_snapshot_schedule(
        self,
        *,
        ClusterIdentifier: str,
        ScheduleIdentifier: str | None = None,
        DisassociateSchedule: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cluster_subnet_group(
        self,
        *,
        ClusterSubnetGroupName: str,
        SubnetIds: list[str],
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_custom_domain_association(
        self,
        *,
        CustomDomainName: str,
        CustomDomainCertificateArn: str,
        ClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_endpoint_access(
        self,
        *,
        EndpointName: str,
        VpcSecurityGroupIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str | None = None,
        SourceType: str | None = None,
        SourceIds: list[str] | None = None,
        EventCategories: list[str] | None = None,
        Severity: str | None = None,
        Enabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_integration(
        self,
        *,
        IntegrationArn: str,
        Description: str | None = None,
        IntegrationName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_lakehouse_configuration(
        self,
        *,
        ClusterIdentifier: str,
        LakehouseRegistration: str | None = None,
        CatalogName: str | None = None,
        LakehouseIdcRegistration: str | None = None,
        LakehouseIdcApplicationArn: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_qev2_idc_application(
        self,
        *,
        Qev2IdcApplicationArn: str,
        IdcDisplayName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_redshift_idc_application(
        self,
        *,
        RedshiftIdcApplicationArn: str,
        IdentityNamespace: str | None = None,
        IamRoleArn: str | None = None,
        IdcDisplayName: str | None = None,
        AuthorizedTokenIssuerList: list[dict[str, Any]] | None = None,
        ServiceIntegrations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_scheduled_action(
        self,
        *,
        ScheduledActionName: str,
        TargetAction: dict[str, Any] | None = None,
        Schedule: str | None = None,
        IamRole: str | None = None,
        ScheduledActionDescription: str | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        Enable: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_snapshot_copy_retention_period(
        self,
        *,
        ClusterIdentifier: str,
        RetentionPeriod: int,
        Manual: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_snapshot_schedule(
        self,
        *,
        ScheduleIdentifier: str,
        ScheduleDefinitions: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_usage_limit(
        self,
        *,
        UsageLimitId: str,
        Amount: int | None = None,
        BreachAction: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def pause_cluster(
        self,
        *,
        ClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purchase_reserved_node_offering(
        self,
        *,
        ReservedNodeOfferingId: str,
        NodeCount: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        ResourceArn: str,
        Policy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_cluster(
        self,
        *,
        ClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_namespace(
        self,
        *,
        NamespaceIdentifier: dict[str, Any],
        ConsumerIdentifiers: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_data_share(
        self,
        *,
        DataShareArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_cluster_parameter_group(
        self,
        *,
        ParameterGroupName: str,
        ResetAllParameters: bool | None = None,
        Parameters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resize_cluster(
        self,
        *,
        ClusterIdentifier: str,
        ClusterType: str | None = None,
        NodeType: str | None = None,
        NumberOfNodes: int | None = None,
        Classic: bool | None = None,
        ReservedNodeId: str | None = None,
        TargetReservedNodeOfferingId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_from_cluster_snapshot(
        self,
        *,
        ClusterIdentifier: str,
        SnapshotIdentifier: str | None = None,
        SnapshotArn: str | None = None,
        SnapshotClusterIdentifier: str | None = None,
        Port: int | None = None,
        AvailabilityZone: str | None = None,
        AllowVersionUpgrade: bool | None = None,
        ClusterSubnetGroupName: str | None = None,
        PubliclyAccessible: bool | None = None,
        OwnerAccount: str | None = None,
        HsmClientCertificateIdentifier: str | None = None,
        HsmConfigurationIdentifier: str | None = None,
        ElasticIp: str | None = None,
        ClusterParameterGroupName: str | None = None,
        ClusterSecurityGroups: list[str] | None = None,
        VpcSecurityGroupIds: list[str] | None = None,
        PreferredMaintenanceWindow: str | None = None,
        AutomatedSnapshotRetentionPeriod: int | None = None,
        ManualSnapshotRetentionPeriod: int | None = None,
        KmsKeyId: str | None = None,
        NodeType: str | None = None,
        EnhancedVpcRouting: bool | None = None,
        AdditionalInfo: str | None = None,
        IamRoles: list[str] | None = None,
        MaintenanceTrackName: str | None = None,
        SnapshotScheduleIdentifier: str | None = None,
        NumberOfNodes: int | None = None,
        AvailabilityZoneRelocation: bool | None = None,
        AquaConfigurationStatus: str | None = None,
        DefaultIamRoleArn: str | None = None,
        ReservedNodeId: str | None = None,
        TargetReservedNodeOfferingId: str | None = None,
        Encrypted: bool | None = None,
        ManageMasterPassword: bool | None = None,
        MasterPasswordSecretKmsKeyId: str | None = None,
        IpAddressType: str | None = None,
        MultiAZ: bool | None = None,
        CatalogName: str | None = None,
        RedshiftIdcApplicationArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_table_from_cluster_snapshot(
        self,
        *,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SourceDatabaseName: str,
        SourceTableName: str,
        NewTableName: str,
        SourceSchemaName: str | None = None,
        TargetDatabaseName: str | None = None,
        TargetSchemaName: str | None = None,
        EnableCaseSensitiveIdentifier: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resume_cluster(
        self,
        *,
        ClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_cluster_security_group_ingress(
        self,
        *,
        ClusterSecurityGroupName: str,
        CIDRIP: str | None = None,
        EC2SecurityGroupName: str | None = None,
        EC2SecurityGroupOwnerId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_endpoint_access(
        self,
        *,
        ClusterIdentifier: str | None = None,
        Account: str | None = None,
        VpcIds: list[str] | None = None,
        Force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_snapshot_access(
        self,
        *,
        AccountWithRestoreAccess: str,
        SnapshotIdentifier: str | None = None,
        SnapshotArn: str | None = None,
        SnapshotClusterIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def rotate_encryption_key(
        self,
        *,
        ClusterIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_partner_status(
        self,
        *,
        AccountId: str,
        ClusterIdentifier: str,
        DatabaseName: str,
        PartnerName: str,
        Status: str,
        StatusMessage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
