from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class MSKClient(ABC):

    @abstractmethod
    def list_clusters(
        self,
        *,
        ClusterNameFilter: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_clusters_v2(
        self,
        *,
        ClusterNameFilter: str | None = None,
        ClusterTypeFilter: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster(
        self,
        *,
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_v2(
        self,
        *,
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bootstrap_brokers(
        self,
        *,
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_nodes(
        self,
        *,
        ClusterArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster(
        self,
        *,
        BrokerNodeGroupInfo: dict[str, Any],
        ClusterName: str,
        KafkaVersion: str,
        NumberOfBrokerNodes: int,
        Rebalancing: dict[str, Any] | None = None,
        ClientAuthentication: dict[str, Any] | None = None,
        ConfigurationInfo: dict[str, Any] | None = None,
        EncryptionInfo: dict[str, Any] | None = None,
        EnhancedMonitoring: str | None = None,
        OpenMonitoring: dict[str, Any] | None = None,
        LoggingInfo: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        StorageMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster(
        self,
        *,
        ClusterArn: str,
        CurrentVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_configurations(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_configuration(
        self,
        *,
        Arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: dict[str, str],
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
    def batch_associate_scram_secret(
        self,
        *,
        ClusterArn: str,
        SecretArnList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_disassociate_scram_secret(
        self,
        *,
        ClusterArn: str,
        SecretArnList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_assessment(
        self,
        *,
        AssessmentType: str,
        ClusterArn: str,
        AssessmentParameters: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_channel(
        self,
        *,
        ChannelName: str,
        ClusterArn: str,
        TopicConfigurationList: list[dict[str, Any]],
        EncryptionConfiguration: dict[str, Any] | None = None,
        IcebergDestinationConfiguration: dict[str, Any] | None = None,
        S3DestinationConfiguration: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        LoggingInfo: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster_v2(
        self,
        *,
        ClusterName: str,
        Tags: dict[str, str] | None = None,
        Provisioned: dict[str, Any] | None = None,
        Serverless: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_configuration(
        self,
        *,
        Name: str,
        ServerProperties: bytes | BinaryIO | str,
        Description: str | None = None,
        KafkaVersions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_replicator(
        self,
        *,
        KafkaClusters: list[dict[str, Any]],
        ReplicationInfoList: list[dict[str, Any]],
        ReplicatorName: str,
        ServiceExecutionRoleArn: str,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
        LogDelivery: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_topic(
        self,
        *,
        ClusterArn: str,
        TopicName: str,
        PartitionCount: int,
        ReplicationFactor: int,
        Configs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_connection(
        self,
        *,
        TargetClusterArn: str,
        Authentication: str,
        VpcId: str,
        ClientSubnets: list[str],
        SecurityGroups: list[str],
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_assessment(
        self,
        *,
        AssessmentArn: str,
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_channel(
        self,
        *,
        ChannelArn: str,
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster_policy(
        self,
        *,
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_configuration(
        self,
        *,
        Arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_replicator(
        self,
        *,
        ReplicatorArn: str,
        CurrentVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_topic(
        self,
        *,
        ClusterArn: str,
        TopicName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_connection(
        self,
        *,
        Arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_assessment(
        self,
        *,
        AssessmentArn: str,
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_channel(
        self,
        *,
        ChannelArn: str,
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_operation(
        self,
        *,
        ClusterOperationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_operation_v2(
        self,
        *,
        ClusterOperationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_configuration_revision(
        self,
        *,
        Arn: str,
        Revision: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replicator(
        self,
        *,
        ReplicatorArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_topic(
        self,
        *,
        ClusterArn: str,
        TopicName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_topic_partitions(
        self,
        *,
        ClusterArn: str,
        TopicName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_topic_reassignment(
        self,
        *,
        ClusterArn: str,
        TopicReassignmentOperationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_connection(
        self,
        *,
        Arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cluster_policy(
        self,
        *,
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_compatible_kafka_versions(
        self,
        *,
        ClusterArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_assessment_findings(
        self,
        *,
        AssessmentArn: str,
        ClusterArn: str,
        Category: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Severity: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_assessments(
        self,
        *,
        ClusterArn: str,
        AssessmentType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_channels(
        self,
        *,
        ClusterArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        TopicNameFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_client_vpc_connections(
        self,
        *,
        ClusterArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cluster_operations(
        self,
        *,
        ClusterArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cluster_operations_v2(
        self,
        *,
        ClusterArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_configuration_revisions(
        self,
        *,
        Arn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_kafka_versions(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_replicators(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        ReplicatorNameFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_scram_secrets(
        self,
        *,
        ClusterArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_topic_reassignments(
        self,
        *,
        ClusterArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        StatusFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_topics(
        self,
        *,
        ClusterArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        TopicNameFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vpc_connections(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_cluster_policy(
        self,
        *,
        ClusterArn: str,
        Policy: str,
        CurrentVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_broker(
        self,
        *,
        BrokerIds: list[str],
        ClusterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_client_vpc_connection(
        self,
        *,
        ClusterArn: str,
        VpcConnectionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_topic_reassignment(
        self,
        *,
        ClusterArn: str,
        TargetInstanceType: str,
        TopicsToInclude: list[str],
        ClientToken: str | None = None,
        TopicsToExclude: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_topic_reassignment(
        self,
        *,
        ClusterArn: str,
        TopicReassignmentOperationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_broker_count(
        self,
        *,
        ClusterArn: str,
        CurrentVersion: str,
        TargetNumberOfBrokerNodes: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_broker_storage(
        self,
        *,
        ClusterArn: str,
        CurrentVersion: str,
        TargetBrokerEBSVolumeInfo: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_broker_type(
        self,
        *,
        ClusterArn: str,
        CurrentVersion: str,
        TargetInstanceType: str,
        TopicReassignment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_channel(
        self,
        *,
        ChannelArn: str,
        ClusterArn: str,
        IcebergDestinationUpdate: dict[str, Any] | None = None,
        S3DestinationUpdate: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster_configuration(
        self,
        *,
        ClusterArn: str,
        ConfigurationInfo: dict[str, Any],
        CurrentVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster_kafka_version(
        self,
        *,
        ClusterArn: str,
        CurrentVersion: str,
        TargetKafkaVersion: str,
        ConfigurationInfo: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_configuration(
        self,
        *,
        Arn: str,
        ServerProperties: bytes | BinaryIO | str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connectivity(
        self,
        *,
        ClusterArn: str,
        CurrentVersion: str,
        ConnectivityInfo: dict[str, Any] | None = None,
        ZookeeperAccess: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_monitoring(
        self,
        *,
        ClusterArn: str,
        CurrentVersion: str,
        EnhancedMonitoring: str | None = None,
        OpenMonitoring: dict[str, Any] | None = None,
        LoggingInfo: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_rebalancing(
        self,
        *,
        ClusterArn: str,
        CurrentVersion: str,
        Rebalancing: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_replication_info(
        self,
        *,
        CurrentVersion: str,
        ReplicatorArn: str,
        ConsumerGroupReplication: dict[str, Any] | None = None,
        SourceKafkaClusterArn: str | None = None,
        SourceKafkaClusterId: str | None = None,
        TargetKafkaClusterArn: str | None = None,
        TargetKafkaClusterId: str | None = None,
        TopicReplication: dict[str, Any] | None = None,
        LogDelivery: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_security(
        self,
        *,
        ClusterArn: str,
        CurrentVersion: str,
        ClientAuthentication: dict[str, Any] | None = None,
        EncryptionInfo: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_storage(
        self,
        *,
        ClusterArn: str,
        CurrentVersion: str,
        ProvisionedThroughput: dict[str, Any] | None = None,
        StorageMode: str | None = None,
        VolumeSizeGB: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_topic(
        self,
        *,
        ClusterArn: str,
        TopicName: str,
        Configs: str | None = None,
        PartitionCount: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
