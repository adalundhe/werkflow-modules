from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class ElastiCacheClient(ABC):

    @abstractmethod
    def describe_cache_clusters(
        self,
        *,
        CacheClusterId: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        ShowCacheNodeInfo: bool | None = None,
        ShowCacheClustersNotInReplicationGroups: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_groups(
        self,
        *,
        ReplicationGroupId: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cache_cluster(
        self,
        *,
        CacheClusterId: str,
        ReplicationGroupId: str | None = None,
        AZMode: str | None = None,
        PreferredAvailabilityZone: str | None = None,
        PreferredAvailabilityZones: list[str] | None = None,
        NumCacheNodes: int | None = None,
        CacheNodeType: str | None = None,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        CacheParameterGroupName: str | None = None,
        CacheSubnetGroupName: str | None = None,
        CacheSecurityGroupNames: list[str] | None = None,
        SecurityGroupIds: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SnapshotArns: list[str] | None = None,
        SnapshotName: str | None = None,
        PreferredMaintenanceWindow: str | None = None,
        Port: int | None = None,
        NotificationTopicArn: str | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        SnapshotRetentionLimit: int | None = None,
        SnapshotWindow: str | None = None,
        AuthToken: str | None = None,
        OutpostMode: str | None = None,
        PreferredOutpostArn: str | None = None,
        PreferredOutpostArns: list[str] | None = None,
        LogDeliveryConfigurations: list[dict[str, Any]] | None = None,
        TransitEncryptionEnabled: bool | None = None,
        NetworkType: str | None = None,
        IpDiscovery: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cache_cluster(
        self,
        *,
        CacheClusterId: str,
        FinalSnapshotIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cache_cluster(
        self,
        *,
        CacheClusterId: str,
        NumCacheNodes: int | None = None,
        CacheNodeIdsToRemove: list[str] | None = None,
        AZMode: str | None = None,
        NewAvailabilityZones: list[str] | None = None,
        CacheSecurityGroupNames: list[str] | None = None,
        SecurityGroupIds: list[str] | None = None,
        PreferredMaintenanceWindow: str | None = None,
        NotificationTopicArn: str | None = None,
        CacheParameterGroupName: str | None = None,
        NotificationTopicStatus: str | None = None,
        ApplyImmediately: bool | None = None,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        SnapshotRetentionLimit: int | None = None,
        SnapshotWindow: str | None = None,
        CacheNodeType: str | None = None,
        AuthToken: str | None = None,
        AuthTokenUpdateStrategy: str | None = None,
        LogDeliveryConfigurations: list[dict[str, Any]] | None = None,
        IpDiscovery: str | None = None,
        ScaleConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_cache_cluster(
        self,
        *,
        CacheClusterId: str,
        CacheNodeIdsToReboot: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_replication_group(
        self,
        *,
        ReplicationGroupId: str,
        ReplicationGroupDescription: str,
        GlobalReplicationGroupId: str | None = None,
        PrimaryClusterId: str | None = None,
        AutomaticFailoverEnabled: bool | None = None,
        MultiAZEnabled: bool | None = None,
        NumCacheClusters: int | None = None,
        PreferredCacheClusterAZs: list[str] | None = None,
        NumNodeGroups: int | None = None,
        ReplicasPerNodeGroup: int | None = None,
        NodeGroupConfiguration: list[dict[str, Any]] | None = None,
        CacheNodeType: str | None = None,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        CacheParameterGroupName: str | None = None,
        CacheSubnetGroupName: str | None = None,
        CacheSecurityGroupNames: list[str] | None = None,
        SecurityGroupIds: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SnapshotArns: list[str] | None = None,
        SnapshotName: str | None = None,
        PreferredMaintenanceWindow: str | None = None,
        Port: int | None = None,
        NotificationTopicArn: str | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        SnapshotRetentionLimit: int | None = None,
        SnapshotWindow: str | None = None,
        AuthToken: str | None = None,
        TransitEncryptionEnabled: bool | None = None,
        AtRestEncryptionEnabled: bool | None = None,
        KmsKeyId: str | None = None,
        UserGroupIds: list[str] | None = None,
        LogDeliveryConfigurations: list[dict[str, Any]] | None = None,
        DataTieringEnabled: bool | None = None,
        NetworkType: str | None = None,
        IpDiscovery: str | None = None,
        TransitEncryptionMode: str | None = None,
        ClusterMode: str | None = None,
        ServerlessCacheSnapshotName: str | None = None,
        Durability: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_replication_group(
        self,
        *,
        ReplicationGroupId: str,
        RetainPrimaryCluster: bool | None = None,
        FinalSnapshotIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_replication_group(
        self,
        *,
        ReplicationGroupId: str,
        ReplicationGroupDescription: str | None = None,
        PrimaryClusterId: str | None = None,
        SnapshottingClusterId: str | None = None,
        AutomaticFailoverEnabled: bool | None = None,
        MultiAZEnabled: bool | None = None,
        NodeGroupId: str | None = None,
        CacheSecurityGroupNames: list[str] | None = None,
        SecurityGroupIds: list[str] | None = None,
        PreferredMaintenanceWindow: str | None = None,
        NotificationTopicArn: str | None = None,
        CacheParameterGroupName: str | None = None,
        NotificationTopicStatus: str | None = None,
        ApplyImmediately: bool | None = None,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        SnapshotRetentionLimit: int | None = None,
        SnapshotWindow: str | None = None,
        CacheNodeType: str | None = None,
        AuthToken: str | None = None,
        AuthTokenUpdateStrategy: str | None = None,
        UserGroupIdsToAdd: list[str] | None = None,
        UserGroupIdsToRemove: list[str] | None = None,
        RemoveUserGroups: bool | None = None,
        LogDeliveryConfigurations: list[dict[str, Any]] | None = None,
        IpDiscovery: str | None = None,
        TransitEncryptionEnabled: bool | None = None,
        TransitEncryptionMode: str | None = None,
        ClusterMode: str | None = None,
        Durability: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshots(
        self,
        *,
        ReplicationGroupId: str | None = None,
        CacheClusterId: str | None = None,
        SnapshotName: str | None = None,
        SnapshotSource: str | None = None,
        Marker: str | None = None,
        MaxRecords: int | None = None,
        ShowNodeGroupConfig: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshot(
        self,
        *,
        SnapshotName: str,
        ReplicationGroupId: str | None = None,
        CacheClusterId: str | None = None,
        KmsKeyId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_snapshot(
        self,
        *,
        SnapshotName: str,
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
    def authorize_cache_security_group_ingress(
        self,
        *,
        CacheSecurityGroupName: str,
        EC2SecurityGroupName: str,
        EC2SecurityGroupOwnerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_apply_update_action(
        self,
        *,
        ServiceUpdateName: str,
        ReplicationGroupIds: list[str] | None = None,
        CacheClusterIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_stop_update_action(
        self,
        *,
        ServiceUpdateName: str,
        ReplicationGroupIds: list[str] | None = None,
        CacheClusterIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def complete_migration(
        self,
        *,
        ReplicationGroupId: str | None = None,
        ServerlessCacheName: str | None = None,
        Force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_serverless_cache_snapshot(
        self,
        *,
        SourceServerlessCacheSnapshotName: str,
        TargetServerlessCacheSnapshotName: str,
        KmsKeyId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_snapshot(
        self,
        *,
        SourceSnapshotName: str,
        TargetSnapshotName: str,
        TargetBucket: str | None = None,
        KmsKeyId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cache_parameter_group(
        self,
        *,
        CacheParameterGroupName: str,
        CacheParameterGroupFamily: str,
        Description: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cache_security_group(
        self,
        *,
        CacheSecurityGroupName: str,
        Description: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cache_subnet_group(
        self,
        *,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: str,
        SubnetIds: list[str],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_global_replication_group(
        self,
        *,
        GlobalReplicationGroupIdSuffix: str,
        PrimaryReplicationGroupId: str,
        GlobalReplicationGroupDescription: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_serverless_cache(
        self,
        *,
        ServerlessCacheName: str,
        Engine: str,
        Description: str | None = None,
        MajorEngineVersion: str | None = None,
        CacheUsageLimits: dict[str, Any] | None = None,
        KmsKeyId: str | None = None,
        SecurityGroupIds: list[str] | None = None,
        SnapshotArnsToRestore: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        UserGroupId: str | None = None,
        SubnetIds: list[str] | None = None,
        SnapshotRetentionLimit: int | None = None,
        DailySnapshotTime: str | None = None,
        NetworkType: str | None = None,
        ConnectionType: str | None = None,
        Integrations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_serverless_cache_snapshot(
        self,
        *,
        ServerlessCacheSnapshotName: str,
        ServerlessCacheName: str,
        KmsKeyId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user(
        self,
        *,
        UserId: str,
        UserName: str,
        Engine: str,
        AccessString: str,
        Passwords: list[str] | None = None,
        NoPasswordRequired: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        AuthenticationMode: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user_group(
        self,
        *,
        UserGroupId: str,
        Engine: str,
        UserIds: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def decrease_node_groups_in_global_replication_group(
        self,
        *,
        GlobalReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        GlobalNodeGroupsToRemove: list[str] | None = None,
        GlobalNodeGroupsToRetain: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def decrease_replica_count(
        self,
        *,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int | None = None,
        ReplicaConfiguration: list[dict[str, Any]] | None = None,
        ReplicasToRemove: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cache_parameter_group(
        self,
        *,
        CacheParameterGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cache_security_group(
        self,
        *,
        CacheSecurityGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cache_subnet_group(
        self,
        *,
        CacheSubnetGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_global_replication_group(
        self,
        *,
        GlobalReplicationGroupId: str,
        RetainPrimaryReplicationGroup: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_serverless_cache(
        self,
        *,
        ServerlessCacheName: str,
        FinalSnapshotName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_serverless_cache_snapshot(
        self,
        *,
        ServerlessCacheSnapshotName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        UserId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_group(
        self,
        *,
        UserGroupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cache_engine_versions(
        self,
        *,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        CacheParameterGroupFamily: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        DefaultOnly: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cache_parameter_groups(
        self,
        *,
        CacheParameterGroupName: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cache_parameters(
        self,
        *,
        CacheParameterGroupName: str,
        Source: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cache_security_groups(
        self,
        *,
        CacheSecurityGroupName: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cache_subnet_groups(
        self,
        *,
        CacheSubnetGroupName: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_engine_default_parameters(
        self,
        *,
        CacheParameterGroupFamily: str,
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
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_global_replication_groups(
        self,
        *,
        GlobalReplicationGroupId: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
        ShowMemberInfo: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_cache_nodes(
        self,
        *,
        ReservedCacheNodeId: str | None = None,
        ReservedCacheNodesOfferingId: str | None = None,
        CacheNodeType: str | None = None,
        Duration: str | None = None,
        ProductDescription: str | None = None,
        OfferingType: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_cache_nodes_offerings(
        self,
        *,
        ReservedCacheNodesOfferingId: str | None = None,
        CacheNodeType: str | None = None,
        Duration: str | None = None,
        ProductDescription: str | None = None,
        OfferingType: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_serverless_cache_snapshots(
        self,
        *,
        ServerlessCacheName: str | None = None,
        ServerlessCacheSnapshotName: str | None = None,
        SnapshotType: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_serverless_caches(
        self,
        *,
        ServerlessCacheName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service_updates(
        self,
        *,
        ServiceUpdateName: str | None = None,
        ServiceUpdateStatus: list[str] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_update_actions(
        self,
        *,
        ServiceUpdateName: str | None = None,
        ReplicationGroupIds: list[str] | None = None,
        CacheClusterIds: list[str] | None = None,
        Engine: str | None = None,
        ServiceUpdateStatus: list[str] | None = None,
        ServiceUpdateTimeRange: dict[str, Any] | None = None,
        UpdateActionStatus: list[str] | None = None,
        ShowNodeLevelUpdateStatus: bool | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user_groups(
        self,
        *,
        UserGroupId: str | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_users(
        self,
        *,
        Engine: str | None = None,
        UserId: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxRecords: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_global_replication_group(
        self,
        *,
        GlobalReplicationGroupId: str,
        ReplicationGroupId: str,
        ReplicationGroupRegion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_serverless_cache_snapshot(
        self,
        *,
        ServerlessCacheSnapshotName: str,
        S3BucketName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def failover_global_replication_group(
        self,
        *,
        GlobalReplicationGroupId: str,
        PrimaryRegion: str,
        PrimaryReplicationGroupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def increase_node_groups_in_global_replication_group(
        self,
        *,
        GlobalReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        RegionalConfigurations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def increase_replica_count(
        self,
        *,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int | None = None,
        ReplicaConfiguration: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_allowed_node_type_modifications(
        self,
        *,
        CacheClusterId: str | None = None,
        ReplicationGroupId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cache_parameter_group(
        self,
        *,
        CacheParameterGroupName: str,
        ParameterNameValues: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_cache_subnet_group(
        self,
        *,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: str | None = None,
        SubnetIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_global_replication_group(
        self,
        *,
        GlobalReplicationGroupId: str,
        ApplyImmediately: bool,
        CacheNodeType: str | None = None,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        CacheParameterGroupName: str | None = None,
        GlobalReplicationGroupDescription: str | None = None,
        AutomaticFailoverEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_replication_group_shard_configuration(
        self,
        *,
        ReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        ReshardingConfiguration: list[dict[str, Any]] | None = None,
        NodeGroupsToRemove: list[str] | None = None,
        NodeGroupsToRetain: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_serverless_cache(
        self,
        *,
        ServerlessCacheName: str,
        Description: str | None = None,
        CacheUsageLimits: dict[str, Any] | None = None,
        RemoveUserGroup: bool | None = None,
        UserGroupId: str | None = None,
        SecurityGroupIds: list[str] | None = None,
        SnapshotRetentionLimit: int | None = None,
        DailySnapshotTime: str | None = None,
        Engine: str | None = None,
        MajorEngineVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_user(
        self,
        *,
        UserId: str,
        AccessString: str | None = None,
        AppendAccessString: str | None = None,
        Passwords: list[str] | None = None,
        NoPasswordRequired: bool | None = None,
        AuthenticationMode: dict[str, Any] | None = None,
        Engine: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_user_group(
        self,
        *,
        UserGroupId: str,
        UserIdsToAdd: list[str] | None = None,
        UserIdsToRemove: list[str] | None = None,
        Engine: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def prepare_migration(
        self,
        *,
        ServerlessCacheName: str,
        CustomerNodeEndpointList: list[dict[str, Any]],
        SourceAuthenticationConfiguration: dict[str, Any] | None = None,
        SourceTlsConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purchase_reserved_cache_nodes_offering(
        self,
        *,
        ReservedCacheNodesOfferingId: str,
        ReservedCacheNodeId: str | None = None,
        CacheNodeCount: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def rebalance_slots_in_global_replication_group(
        self,
        *,
        GlobalReplicationGroupId: str,
        ApplyImmediately: bool,
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
    def reset_cache_parameter_group(
        self,
        *,
        CacheParameterGroupName: str,
        ResetAllParameters: bool | None = None,
        ParameterNameValues: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_cache_security_group_ingress(
        self,
        *,
        CacheSecurityGroupName: str,
        EC2SecurityGroupName: str,
        EC2SecurityGroupOwnerId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_migration(
        self,
        *,
        ServerlessCacheName: str | None = None,
        ReplicationGroupId: str | None = None,
        CustomerNodeEndpointList: list[dict[str, Any]] | None = None,
        AutoCutover: bool | None = None,
        ClearTargetCacheData: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_migration(
        self,
        *,
        ServerlessCacheName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_failover(
        self,
        *,
        ReplicationGroupId: str,
        NodeGroupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_migration(
        self,
        *,
        ReplicationGroupId: str,
        CustomerNodeEndpointList: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
