from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class KinesisClient(ABC):

    @abstractmethod
    def acknowledge_dead_letter_queue_records(
        self,
        *,
        QueueARN: str,
        Entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def acknowledge_queue_records(
        self,
        *,
        QueueARN: str,
        Entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_tags_to_stream(
        self,
        *,
        Tags: dict[str, str],
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_channel(
        self,
        *,
        ChannelName: str,
        ServiceExecutionRoleARN: str,
        StreamConfigurationList: list[dict[str, Any]],
        S3DestinationConfiguration: dict[str, Any] | None = None,
        S3TablesDestinationConfiguration: dict[str, Any] | None = None,
        EncryptionConfiguration: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        LoggingConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_queue(
        self,
        *,
        QueueName: str,
        StreamConfigurationList: list[dict[str, Any]],
        QueueAttributes: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stream(
        self,
        *,
        StreamName: str,
        ShardCount: int | None = None,
        StreamModeDetails: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        WarmThroughputMiBps: int | None = None,
        MaxRecordSizeInKiB: int | None = None,
        RecordDistributionStrategy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def decrease_stream_retention_period(
        self,
        *,
        RetentionPeriodHours: int,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_channel(
        self,
        *,
        ChannelARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_queue(
        self,
        *,
        QueueARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        ResourceARN: str,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_stream(
        self,
        *,
        StreamName: str | None = None,
        EnforceConsumerDeletion: bool | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_stream_consumer(
        self,
        *,
        StreamARN: str | None = None,
        ConsumerName: str | None = None,
        ConsumerARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_settings(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_channel(
        self,
        *,
        ChannelARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_limits(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_queue(
        self,
        *,
        QueueARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stream(
        self,
        *,
        StreamName: str | None = None,
        Limit: int | None = None,
        ExclusiveStartShardId: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stream_consumer(
        self,
        *,
        StreamARN: str | None = None,
        ConsumerName: str | None = None,
        ConsumerARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stream_summary(
        self,
        *,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_enhanced_monitoring(
        self,
        *,
        ShardLevelMetrics: list[str],
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_enhanced_monitoring(
        self,
        *,
        ShardLevelMetrics: list[str],
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_records(
        self,
        *,
        ShardIterator: str,
        Limit: int | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        ResourceARN: str,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_shard_iterator(
        self,
        *,
        ShardId: str,
        ShardIteratorType: str,
        StreamName: str | None = None,
        StartingSequenceNumber: str | None = None,
        Timestamp: datetime.datetime | str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def increase_stream_retention_period(
        self,
        *,
        RetentionPeriodHours: int,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_channels(
        self,
        *,
        StreamFilter: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_queues(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        StreamFilter: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_shards(
        self,
        *,
        StreamName: str | None = None,
        NextToken: str | None = None,
        ExclusiveStartShardId: str | None = None,
        MaxResults: int | None = None,
        StreamCreationTimestamp: datetime.datetime | str | None = None,
        ShardFilter: dict[str, Any] | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stream_consumers(
        self,
        *,
        StreamARN: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        StreamCreationTimestamp: datetime.datetime | str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_streams(
        self,
        *,
        Limit: int | None = None,
        ExclusiveStartStreamName: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_stream(
        self,
        *,
        StreamName: str | None = None,
        ExclusiveStartTagKey: str | None = None,
        Limit: int | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def merge_shards(
        self,
        *,
        ShardToMerge: str,
        AdjacentShardToMerge: str,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_record(
        self,
        *,
        Data: bytes | BinaryIO | str,
        StreamName: str | None = None,
        PartitionKey: str | None = None,
        ExplicitHashKey: str | None = None,
        SequenceNumberForOrdering: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_records(
        self,
        *,
        Records: list[dict[str, Any]],
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        ResourceARN: str,
        Policy: str,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def receive_dead_letter_queue_records(
        self,
        *,
        QueueARN: str,
        Limit: int | None = None,
        WaitTimeSeconds: int | None = None,
        VisibilityTimeoutSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def receive_queue_records(
        self,
        *,
        QueueARN: str,
        Limit: int | None = None,
        WaitTimeSeconds: int | None = None,
        VisibilityTimeoutSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_stream_consumer(
        self,
        *,
        StreamARN: str,
        ConsumerName: str,
        StreamId: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags_from_stream(
        self,
        *,
        TagKeys: list[str],
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_dead_letter_queue_records(
        self,
        *,
        QueueARN: str,
        Entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def split_shard(
        self,
        *,
        ShardToSplit: str,
        NewStartingHashKey: str,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_stream_encryption(
        self,
        *,
        EncryptionType: str,
        KeyId: str,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_stream_encryption(
        self,
        *,
        EncryptionType: str,
        KeyId: str,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def subscribe_to_shard(
        self,
        *,
        ConsumerARN: str,
        ShardId: str,
        StartingPosition: dict[str, Any],
        StreamId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        Tags: dict[str, str],
        ResourceARN: str,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        TagKeys: list[str],
        ResourceARN: str,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_account_settings(
        self,
        *,
        MinimumThroughputBillingCommitment: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_channel(
        self,
        *,
        ChannelARN: str,
        S3DestinationConfiguration: dict[str, Any] | None = None,
        S3TablesDestinationConfiguration: dict[str, Any] | None = None,
        LoggingConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dead_letter_queue_records_visibility(
        self,
        *,
        QueueARN: str,
        Entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_max_record_size(
        self,
        *,
        MaxRecordSizeInKiB: int,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_queue(
        self,
        *,
        QueueARN: str,
        QueueAttributes: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_queue_records_visibility(
        self,
        *,
        QueueARN: str,
        Entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_shard_count(
        self,
        *,
        TargetShardCount: int,
        ScalingType: str,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stream_mode(
        self,
        *,
        StreamARN: str,
        StreamModeDetails: dict[str, Any],
        StreamId: str | None = None,
        WarmThroughputMiBps: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stream_record_distribution_strategy(
        self,
        *,
        StreamARN: str,
        RecordDistributionStrategy: str,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stream_warm_throughput(
        self,
        *,
        WarmThroughputMiBps: int,
        StreamARN: str | None = None,
        StreamName: str | None = None,
        StreamId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
