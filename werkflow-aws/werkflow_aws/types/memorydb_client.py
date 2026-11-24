from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class MemoryDBClient(ABC):

    @abstractmethod
    def batch_update_cluster(
        self,
        *,
        ClusterNames: list[str],
        ServiceUpdate: dict[str, Any] | None = None,
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
    def create_acl(
        self,
        *,
        ACLName: str,
        UserNames: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster(
        self,
        *,
        ClusterName: str,
        NodeType: str,
        ACLName: str,
        MultiRegionClusterName: str | None = None,
        ParameterGroupName: str | None = None,
        Description: str | None = None,
        NumShards: int | None = None,
        NumReplicasPerShard: int | None = None,
        SubnetGroupName: str | None = None,
        SecurityGroupIds: list[str] | None = None,
        MaintenanceWindow: str | None = None,
        Port: int | None = None,
        SnsTopicArn: str | None = None,
        TLSEnabled: bool | None = None,
        KmsKeyId: str | None = None,
        SnapshotArns: list[str] | None = None,
        SnapshotName: str | None = None,
        SnapshotRetentionLimit: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SnapshotWindow: str | None = None,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        AutoMinorVersionUpgrade: bool | None = None,
        DataTiering: bool | None = None,
        NetworkType: str | None = None,
        IpDiscovery: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_multi_region_cluster(
        self,
        *,
        MultiRegionClusterNameSuffix: str,
        NodeType: str,
        Description: str | None = None,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        MultiRegionParameterGroupName: str | None = None,
        NumShards: int | None = None,
        TLSEnabled: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_parameter_group(
        self,
        *,
        ParameterGroupName: str,
        Family: str,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshot(
        self,
        *,
        ClusterName: str,
        SnapshotName: str,
        KmsKeyId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_subnet_group(
        self,
        *,
        SubnetGroupName: str,
        SubnetIds: list[str],
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user(
        self,
        *,
        UserName: str,
        AuthenticationMode: dict[str, Any],
        AccessString: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_acl(
        self,
        *,
        ACLName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster(
        self,
        *,
        ClusterName: str,
        MultiRegionClusterName: str | None = None,
        FinalSnapshotName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_multi_region_cluster(
        self,
        *,
        MultiRegionClusterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_parameter_group(
        self,
        *,
        ParameterGroupName: str,
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
    def delete_subnet_group(
        self,
        *,
        SubnetGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        UserName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_acls(
        self,
        *,
        ACLName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_clusters(
        self,
        *,
        ClusterName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        ShowShardDetails: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_engine_versions(
        self,
        *,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        ParameterGroupFamily: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DefaultOnly: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_events(
        self,
        *,
        SourceName: str | None = None,
        SourceType: str | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        Duration: int | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_multi_region_clusters(
        self,
        *,
        MultiRegionClusterName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        ShowClusterDetails: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_multi_region_parameter_groups(
        self,
        *,
        MultiRegionParameterGroupName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_multi_region_parameters(
        self,
        *,
        MultiRegionParameterGroupName: str,
        Source: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_parameter_groups(
        self,
        *,
        ParameterGroupName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_parameters(
        self,
        *,
        ParameterGroupName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_nodes(
        self,
        *,
        ReservationId: str | None = None,
        ReservedNodesOfferingId: str | None = None,
        NodeType: str | None = None,
        Duration: str | None = None,
        OfferingType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_nodes_offerings(
        self,
        *,
        ReservedNodesOfferingId: str | None = None,
        NodeType: str | None = None,
        Duration: str | None = None,
        OfferingType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service_updates(
        self,
        *,
        ServiceUpdateName: str | None = None,
        ClusterNames: list[str] | None = None,
        Status: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshots(
        self,
        *,
        ClusterName: str | None = None,
        SnapshotName: str | None = None,
        Source: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ShowDetail: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_subnet_groups(
        self,
        *,
        SubnetGroupName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_users(
        self,
        *,
        UserName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def failover_shard(
        self,
        *,
        ClusterName: str,
        ShardName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_allowed_multi_region_cluster_updates(
        self,
        *,
        MultiRegionClusterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_allowed_node_type_updates(
        self,
        *,
        ClusterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purchase_reserved_nodes_offering(
        self,
        *,
        ReservedNodesOfferingId: str,
        ReservationId: str | None = None,
        NodeCount: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_parameter_group(
        self,
        *,
        ParameterGroupName: str,
        AllParameters: bool | None = None,
        ParameterNames: list[str] | None = None,
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
    def update_acl(
        self,
        *,
        ACLName: str,
        UserNamesToAdd: list[str] | None = None,
        UserNamesToRemove: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster(
        self,
        *,
        ClusterName: str,
        Description: str | None = None,
        SecurityGroupIds: list[str] | None = None,
        MaintenanceWindow: str | None = None,
        SnsTopicArn: str | None = None,
        SnsTopicStatus: str | None = None,
        ParameterGroupName: str | None = None,
        SnapshotWindow: str | None = None,
        SnapshotRetentionLimit: int | None = None,
        NodeType: str | None = None,
        Engine: str | None = None,
        EngineVersion: str | None = None,
        ReplicaConfiguration: dict[str, Any] | None = None,
        ShardConfiguration: dict[str, Any] | None = None,
        ACLName: str | None = None,
        IpDiscovery: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_multi_region_cluster(
        self,
        *,
        MultiRegionClusterName: str,
        NodeType: str | None = None,
        Description: str | None = None,
        EngineVersion: str | None = None,
        ShardConfiguration: dict[str, Any] | None = None,
        MultiRegionParameterGroupName: str | None = None,
        UpdateStrategy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_parameter_group(
        self,
        *,
        ParameterGroupName: str,
        ParameterNameValues: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_subnet_group(
        self,
        *,
        SubnetGroupName: str,
        Description: str | None = None,
        SubnetIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user(
        self,
        *,
        UserName: str,
        AuthenticationMode: dict[str, Any] | None = None,
        AccessString: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
