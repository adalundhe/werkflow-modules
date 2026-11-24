from werkflow_aws.models.kinesis import (
    KinesisAcknowledgeDeadLetterQueueRecordsRequest,
    KinesisAcknowledgeDeadLetterQueueRecordsResponse,
    KinesisAcknowledgeQueueRecordsRequest,
    KinesisAcknowledgeQueueRecordsResponse,
    KinesisAddTagsToStreamRequest,
    KinesisAddTagsToStreamResponse,
    KinesisCreateChannelRequest,
    KinesisCreateChannelResponse,
    KinesisCreateQueueRequest,
    KinesisCreateQueueResponse,
    KinesisCreateStreamRequest,
    KinesisCreateStreamResponse,
    KinesisDecreaseStreamRetentionPeriodRequest,
    KinesisDecreaseStreamRetentionPeriodResponse,
    KinesisDeleteChannelRequest,
    KinesisDeleteChannelResponse,
    KinesisDeleteQueueRequest,
    KinesisDeleteQueueResponse,
    KinesisDeleteResourcePolicyRequest,
    KinesisDeleteResourcePolicyResponse,
    KinesisDeleteStreamRequest,
    KinesisDeleteStreamResponse,
    KinesisDeregisterStreamConsumerRequest,
    KinesisDeregisterStreamConsumerResponse,
    KinesisDescribeAccountSettingsRequest,
    KinesisDescribeAccountSettingsResponse,
    KinesisDescribeChannelRequest,
    KinesisDescribeChannelResponse,
    KinesisDescribeLimitsRequest,
    KinesisDescribeLimitsResponse,
    KinesisDescribeQueueRequest,
    KinesisDescribeQueueResponse,
    KinesisDescribeStreamConsumerRequest,
    KinesisDescribeStreamConsumerResponse,
    KinesisDescribeStreamRequest,
    KinesisDescribeStreamResponse,
    KinesisDescribeStreamSummaryRequest,
    KinesisDescribeStreamSummaryResponse,
    KinesisDisableEnhancedMonitoringRequest,
    KinesisDisableEnhancedMonitoringResponse,
    KinesisEnableEnhancedMonitoringRequest,
    KinesisEnableEnhancedMonitoringResponse,
    KinesisGetRecordsRequest,
    KinesisGetRecordsResponse,
    KinesisGetResourcePolicyRequest,
    KinesisGetResourcePolicyResponse,
    KinesisGetShardIteratorRequest,
    KinesisGetShardIteratorResponse,
    KinesisIncreaseStreamRetentionPeriodRequest,
    KinesisIncreaseStreamRetentionPeriodResponse,
    KinesisListChannelsRequest,
    KinesisListChannelsResponse,
    KinesisListQueuesRequest,
    KinesisListQueuesResponse,
    KinesisListShardsRequest,
    KinesisListShardsResponse,
    KinesisListStreamConsumersRequest,
    KinesisListStreamConsumersResponse,
    KinesisListStreamsRequest,
    KinesisListStreamsResponse,
    KinesisListTagsForResourceRequest,
    KinesisListTagsForResourceResponse,
    KinesisListTagsForStreamRequest,
    KinesisListTagsForStreamResponse,
    KinesisMergeShardsRequest,
    KinesisMergeShardsResponse,
    KinesisPutRecordRequest,
    KinesisPutRecordResponse,
    KinesisPutRecordsRequest,
    KinesisPutRecordsResponse,
    KinesisPutResourcePolicyRequest,
    KinesisPutResourcePolicyResponse,
    KinesisReceiveDeadLetterQueueRecordsRequest,
    KinesisReceiveDeadLetterQueueRecordsResponse,
    KinesisReceiveQueueRecordsRequest,
    KinesisReceiveQueueRecordsResponse,
    KinesisRegisterStreamConsumerRequest,
    KinesisRegisterStreamConsumerResponse,
    KinesisRemoveTagsFromStreamRequest,
    KinesisRemoveTagsFromStreamResponse,
    KinesisRestoreDeadLetterQueueRecordsRequest,
    KinesisRestoreDeadLetterQueueRecordsResponse,
    KinesisSplitShardRequest,
    KinesisSplitShardResponse,
    KinesisStartStreamEncryptionRequest,
    KinesisStartStreamEncryptionResponse,
    KinesisStopStreamEncryptionRequest,
    KinesisStopStreamEncryptionResponse,
    KinesisSubscribeToShardRequest,
    KinesisSubscribeToShardResponse,
    KinesisTagResourceRequest,
    KinesisTagResourceResponse,
    KinesisUntagResourceRequest,
    KinesisUntagResourceResponse,
    KinesisUpdateAccountSettingsRequest,
    KinesisUpdateAccountSettingsResponse,
    KinesisUpdateChannelRequest,
    KinesisUpdateChannelResponse,
    KinesisUpdateDeadLetterQueueRecordsVisibilityRequest,
    KinesisUpdateDeadLetterQueueRecordsVisibilityResponse,
    KinesisUpdateMaxRecordSizeRequest,
    KinesisUpdateMaxRecordSizeResponse,
    KinesisUpdateQueueRecordsVisibilityRequest,
    KinesisUpdateQueueRecordsVisibilityResponse,
    KinesisUpdateQueueRequest,
    KinesisUpdateQueueResponse,
    KinesisUpdateShardCountRequest,
    KinesisUpdateShardCountResponse,
    KinesisUpdateStreamModeRequest,
    KinesisUpdateStreamModeResponse,
    KinesisUpdateStreamRecordDistributionStrategyRequest,
    KinesisUpdateStreamRecordDistributionStrategyResponse,
    KinesisUpdateStreamWarmThroughputRequest,
    KinesisUpdateStreamWarmThroughputResponse,
)
from werkflow_aws.types.kinesis_client import KinesisClient
from .base import AWSBaseService


class AWSKinesis(AWSBaseService[KinesisClient]):
    service_name = 'kinesis'
    boto3_service_name = 'kinesis'

    def __init__(self) -> None:
        super().__init__(service_name='kinesis', boto3_service_name='kinesis')

    async def acknowledge_dead_letter_queue_records(
        self,
        request: KinesisAcknowledgeDeadLetterQueueRecordsRequest,
    ) -> KinesisAcknowledgeDeadLetterQueueRecordsResponse:
        client = self._require_client()
        return await self._execute(client.acknowledge_dead_letter_queue_records, request, KinesisAcknowledgeDeadLetterQueueRecordsResponse)

    async def acknowledge_queue_records(
        self,
        request: KinesisAcknowledgeQueueRecordsRequest,
    ) -> KinesisAcknowledgeQueueRecordsResponse:
        client = self._require_client()
        return await self._execute(client.acknowledge_queue_records, request, KinesisAcknowledgeQueueRecordsResponse)

    async def add_tags_to_stream(
        self,
        request: KinesisAddTagsToStreamRequest,
    ) -> KinesisAddTagsToStreamResponse:
        client = self._require_client()
        return await self._execute(client.add_tags_to_stream, request, KinesisAddTagsToStreamResponse)

    async def create_channel(
        self,
        request: KinesisCreateChannelRequest,
    ) -> KinesisCreateChannelResponse:
        client = self._require_client()
        return await self._execute(client.create_channel, request, KinesisCreateChannelResponse)

    async def create_queue(
        self,
        request: KinesisCreateQueueRequest,
    ) -> KinesisCreateQueueResponse:
        client = self._require_client()
        return await self._execute(client.create_queue, request, KinesisCreateQueueResponse)

    async def create_stream(
        self,
        request: KinesisCreateStreamRequest,
    ) -> KinesisCreateStreamResponse:
        client = self._require_client()
        return await self._execute(client.create_stream, request, KinesisCreateStreamResponse)

    async def decrease_stream_retention_period(
        self,
        request: KinesisDecreaseStreamRetentionPeriodRequest,
    ) -> KinesisDecreaseStreamRetentionPeriodResponse:
        client = self._require_client()
        return await self._execute(client.decrease_stream_retention_period, request, KinesisDecreaseStreamRetentionPeriodResponse)

    async def delete_channel(
        self,
        request: KinesisDeleteChannelRequest,
    ) -> KinesisDeleteChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_channel, request, KinesisDeleteChannelResponse)

    async def delete_queue(
        self,
        request: KinesisDeleteQueueRequest,
    ) -> KinesisDeleteQueueResponse:
        client = self._require_client()
        return await self._execute(client.delete_queue, request, KinesisDeleteQueueResponse)

    async def delete_resource_policy(
        self,
        request: KinesisDeleteResourcePolicyRequest,
    ) -> KinesisDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, KinesisDeleteResourcePolicyResponse)

    async def delete_stream(
        self,
        request: KinesisDeleteStreamRequest | None = None,
    ) -> KinesisDeleteStreamResponse:
        client = self._require_client()
        return await self._execute(client.delete_stream, request, KinesisDeleteStreamResponse)

    async def deregister_stream_consumer(
        self,
        request: KinesisDeregisterStreamConsumerRequest | None = None,
    ) -> KinesisDeregisterStreamConsumerResponse:
        client = self._require_client()
        return await self._execute(client.deregister_stream_consumer, request, KinesisDeregisterStreamConsumerResponse)

    async def describe_account_settings(
        self,
        request: KinesisDescribeAccountSettingsRequest | None = None,
    ) -> KinesisDescribeAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_settings, request, KinesisDescribeAccountSettingsResponse)

    async def describe_channel(
        self,
        request: KinesisDescribeChannelRequest,
    ) -> KinesisDescribeChannelResponse:
        client = self._require_client()
        return await self._execute(client.describe_channel, request, KinesisDescribeChannelResponse)

    async def describe_limits(
        self,
        request: KinesisDescribeLimitsRequest | None = None,
    ) -> KinesisDescribeLimitsResponse:
        client = self._require_client()
        return await self._execute(client.describe_limits, request, KinesisDescribeLimitsResponse)

    async def describe_queue(
        self,
        request: KinesisDescribeQueueRequest,
    ) -> KinesisDescribeQueueResponse:
        client = self._require_client()
        return await self._execute(client.describe_queue, request, KinesisDescribeQueueResponse)

    async def describe_stream(
        self,
        request: KinesisDescribeStreamRequest | None = None,
    ) -> KinesisDescribeStreamResponse:
        client = self._require_client()
        return await self._execute(client.describe_stream, request, KinesisDescribeStreamResponse)

    async def describe_stream_paginated(
        self,
        request: KinesisDescribeStreamRequest | None = None,
    ) -> list[KinesisDescribeStreamResponse]:
        return await self._paginate('describe_stream', request, KinesisDescribeStreamResponse)

    async def describe_stream_consumer(
        self,
        request: KinesisDescribeStreamConsumerRequest | None = None,
    ) -> KinesisDescribeStreamConsumerResponse:
        client = self._require_client()
        return await self._execute(client.describe_stream_consumer, request, KinesisDescribeStreamConsumerResponse)

    async def describe_stream_summary(
        self,
        request: KinesisDescribeStreamSummaryRequest | None = None,
    ) -> KinesisDescribeStreamSummaryResponse:
        client = self._require_client()
        return await self._execute(client.describe_stream_summary, request, KinesisDescribeStreamSummaryResponse)

    async def disable_enhanced_monitoring(
        self,
        request: KinesisDisableEnhancedMonitoringRequest,
    ) -> KinesisDisableEnhancedMonitoringResponse:
        client = self._require_client()
        return await self._execute(client.disable_enhanced_monitoring, request, KinesisDisableEnhancedMonitoringResponse)

    async def enable_enhanced_monitoring(
        self,
        request: KinesisEnableEnhancedMonitoringRequest,
    ) -> KinesisEnableEnhancedMonitoringResponse:
        client = self._require_client()
        return await self._execute(client.enable_enhanced_monitoring, request, KinesisEnableEnhancedMonitoringResponse)

    async def get_records(
        self,
        request: KinesisGetRecordsRequest,
    ) -> KinesisGetRecordsResponse:
        client = self._require_client()
        return await self._execute(client.get_records, request, KinesisGetRecordsResponse)

    async def get_resource_policy(
        self,
        request: KinesisGetResourcePolicyRequest,
    ) -> KinesisGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, KinesisGetResourcePolicyResponse)

    async def get_shard_iterator(
        self,
        request: KinesisGetShardIteratorRequest,
    ) -> KinesisGetShardIteratorResponse:
        client = self._require_client()
        return await self._execute(client.get_shard_iterator, request, KinesisGetShardIteratorResponse)

    async def increase_stream_retention_period(
        self,
        request: KinesisIncreaseStreamRetentionPeriodRequest,
    ) -> KinesisIncreaseStreamRetentionPeriodResponse:
        client = self._require_client()
        return await self._execute(client.increase_stream_retention_period, request, KinesisIncreaseStreamRetentionPeriodResponse)

    async def list_channels(
        self,
        request: KinesisListChannelsRequest | None = None,
    ) -> KinesisListChannelsResponse:
        client = self._require_client()
        return await self._execute(client.list_channels, request, KinesisListChannelsResponse)

    async def list_channels_paginated(
        self,
        request: KinesisListChannelsRequest | None = None,
    ) -> list[KinesisListChannelsResponse]:
        return await self._paginate('list_channels', request, KinesisListChannelsResponse)

    async def list_queues(
        self,
        request: KinesisListQueuesRequest | None = None,
    ) -> KinesisListQueuesResponse:
        client = self._require_client()
        return await self._execute(client.list_queues, request, KinesisListQueuesResponse)

    async def list_queues_paginated(
        self,
        request: KinesisListQueuesRequest | None = None,
    ) -> list[KinesisListQueuesResponse]:
        return await self._paginate('list_queues', request, KinesisListQueuesResponse)

    async def list_shards(
        self,
        request: KinesisListShardsRequest | None = None,
    ) -> KinesisListShardsResponse:
        client = self._require_client()
        return await self._execute(client.list_shards, request, KinesisListShardsResponse)

    async def list_shards_paginated(
        self,
        request: KinesisListShardsRequest | None = None,
    ) -> list[KinesisListShardsResponse]:
        return await self._paginate('list_shards', request, KinesisListShardsResponse)

    async def list_stream_consumers(
        self,
        request: KinesisListStreamConsumersRequest,
    ) -> KinesisListStreamConsumersResponse:
        client = self._require_client()
        return await self._execute(client.list_stream_consumers, request, KinesisListStreamConsumersResponse)

    async def list_stream_consumers_paginated(
        self,
        request: KinesisListStreamConsumersRequest,
    ) -> list[KinesisListStreamConsumersResponse]:
        return await self._paginate('list_stream_consumers', request, KinesisListStreamConsumersResponse)

    async def list_streams(
        self,
        request: KinesisListStreamsRequest | None = None,
    ) -> KinesisListStreamsResponse:
        client = self._require_client()
        return await self._execute(client.list_streams, request, KinesisListStreamsResponse)

    async def list_streams_paginated(
        self,
        request: KinesisListStreamsRequest | None = None,
    ) -> list[KinesisListStreamsResponse]:
        return await self._paginate('list_streams', request, KinesisListStreamsResponse)

    async def list_tags_for_resource(
        self,
        request: KinesisListTagsForResourceRequest,
    ) -> KinesisListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, KinesisListTagsForResourceResponse)

    async def list_tags_for_stream(
        self,
        request: KinesisListTagsForStreamRequest | None = None,
    ) -> KinesisListTagsForStreamResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_stream, request, KinesisListTagsForStreamResponse)

    async def merge_shards(
        self,
        request: KinesisMergeShardsRequest,
    ) -> KinesisMergeShardsResponse:
        client = self._require_client()
        return await self._execute(client.merge_shards, request, KinesisMergeShardsResponse)

    async def put_record(
        self,
        request: KinesisPutRecordRequest,
    ) -> KinesisPutRecordResponse:
        client = self._require_client()
        return await self._execute(client.put_record, request, KinesisPutRecordResponse)

    async def put_records(
        self,
        request: KinesisPutRecordsRequest,
    ) -> KinesisPutRecordsResponse:
        client = self._require_client()
        return await self._execute(client.put_records, request, KinesisPutRecordsResponse)

    async def put_resource_policy(
        self,
        request: KinesisPutResourcePolicyRequest,
    ) -> KinesisPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, KinesisPutResourcePolicyResponse)

    async def receive_dead_letter_queue_records(
        self,
        request: KinesisReceiveDeadLetterQueueRecordsRequest,
    ) -> KinesisReceiveDeadLetterQueueRecordsResponse:
        client = self._require_client()
        return await self._execute(client.receive_dead_letter_queue_records, request, KinesisReceiveDeadLetterQueueRecordsResponse)

    async def receive_queue_records(
        self,
        request: KinesisReceiveQueueRecordsRequest,
    ) -> KinesisReceiveQueueRecordsResponse:
        client = self._require_client()
        return await self._execute(client.receive_queue_records, request, KinesisReceiveQueueRecordsResponse)

    async def register_stream_consumer(
        self,
        request: KinesisRegisterStreamConsumerRequest,
    ) -> KinesisRegisterStreamConsumerResponse:
        client = self._require_client()
        return await self._execute(client.register_stream_consumer, request, KinesisRegisterStreamConsumerResponse)

    async def remove_tags_from_stream(
        self,
        request: KinesisRemoveTagsFromStreamRequest,
    ) -> KinesisRemoveTagsFromStreamResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags_from_stream, request, KinesisRemoveTagsFromStreamResponse)

    async def restore_dead_letter_queue_records(
        self,
        request: KinesisRestoreDeadLetterQueueRecordsRequest,
    ) -> KinesisRestoreDeadLetterQueueRecordsResponse:
        client = self._require_client()
        return await self._execute(client.restore_dead_letter_queue_records, request, KinesisRestoreDeadLetterQueueRecordsResponse)

    async def split_shard(
        self,
        request: KinesisSplitShardRequest,
    ) -> KinesisSplitShardResponse:
        client = self._require_client()
        return await self._execute(client.split_shard, request, KinesisSplitShardResponse)

    async def start_stream_encryption(
        self,
        request: KinesisStartStreamEncryptionRequest,
    ) -> KinesisStartStreamEncryptionResponse:
        client = self._require_client()
        return await self._execute(client.start_stream_encryption, request, KinesisStartStreamEncryptionResponse)

    async def stop_stream_encryption(
        self,
        request: KinesisStopStreamEncryptionRequest,
    ) -> KinesisStopStreamEncryptionResponse:
        client = self._require_client()
        return await self._execute(client.stop_stream_encryption, request, KinesisStopStreamEncryptionResponse)

    async def subscribe_to_shard(
        self,
        request: KinesisSubscribeToShardRequest,
    ) -> KinesisSubscribeToShardResponse:
        client = self._require_client()
        return await self._execute(client.subscribe_to_shard, request, KinesisSubscribeToShardResponse)

    async def tag_resource(
        self,
        request: KinesisTagResourceRequest,
    ) -> KinesisTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, KinesisTagResourceResponse)

    async def untag_resource(
        self,
        request: KinesisUntagResourceRequest,
    ) -> KinesisUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, KinesisUntagResourceResponse)

    async def update_account_settings(
        self,
        request: KinesisUpdateAccountSettingsRequest,
    ) -> KinesisUpdateAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_account_settings, request, KinesisUpdateAccountSettingsResponse)

    async def update_channel(
        self,
        request: KinesisUpdateChannelRequest,
    ) -> KinesisUpdateChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_channel, request, KinesisUpdateChannelResponse)

    async def update_dead_letter_queue_records_visibility(
        self,
        request: KinesisUpdateDeadLetterQueueRecordsVisibilityRequest,
    ) -> KinesisUpdateDeadLetterQueueRecordsVisibilityResponse:
        client = self._require_client()
        return await self._execute(client.update_dead_letter_queue_records_visibility, request, KinesisUpdateDeadLetterQueueRecordsVisibilityResponse)

    async def update_max_record_size(
        self,
        request: KinesisUpdateMaxRecordSizeRequest,
    ) -> KinesisUpdateMaxRecordSizeResponse:
        client = self._require_client()
        return await self._execute(client.update_max_record_size, request, KinesisUpdateMaxRecordSizeResponse)

    async def update_queue(
        self,
        request: KinesisUpdateQueueRequest,
    ) -> KinesisUpdateQueueResponse:
        client = self._require_client()
        return await self._execute(client.update_queue, request, KinesisUpdateQueueResponse)

    async def update_queue_records_visibility(
        self,
        request: KinesisUpdateQueueRecordsVisibilityRequest,
    ) -> KinesisUpdateQueueRecordsVisibilityResponse:
        client = self._require_client()
        return await self._execute(client.update_queue_records_visibility, request, KinesisUpdateQueueRecordsVisibilityResponse)

    async def update_shard_count(
        self,
        request: KinesisUpdateShardCountRequest,
    ) -> KinesisUpdateShardCountResponse:
        client = self._require_client()
        return await self._execute(client.update_shard_count, request, KinesisUpdateShardCountResponse)

    async def update_stream_mode(
        self,
        request: KinesisUpdateStreamModeRequest,
    ) -> KinesisUpdateStreamModeResponse:
        client = self._require_client()
        return await self._execute(client.update_stream_mode, request, KinesisUpdateStreamModeResponse)

    async def update_stream_record_distribution_strategy(
        self,
        request: KinesisUpdateStreamRecordDistributionStrategyRequest,
    ) -> KinesisUpdateStreamRecordDistributionStrategyResponse:
        client = self._require_client()
        return await self._execute(client.update_stream_record_distribution_strategy, request, KinesisUpdateStreamRecordDistributionStrategyResponse)

    async def update_stream_warm_throughput(
        self,
        request: KinesisUpdateStreamWarmThroughputRequest,
    ) -> KinesisUpdateStreamWarmThroughputResponse:
        client = self._require_client()
        return await self._execute(client.update_stream_warm_throughput, request, KinesisUpdateStreamWarmThroughputResponse)
