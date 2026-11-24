from werkflow_aws.models.kinesis_vs import (
    KinesisVideoCreateSignalingChannelRequest,
    KinesisVideoCreateSignalingChannelResponse,
    KinesisVideoCreateStreamRequest,
    KinesisVideoCreateStreamResponse,
    KinesisVideoDeleteEdgeConfigurationRequest,
    KinesisVideoDeleteEdgeConfigurationResponse,
    KinesisVideoDeleteSignalingChannelRequest,
    KinesisVideoDeleteSignalingChannelResponse,
    KinesisVideoDeleteStreamRequest,
    KinesisVideoDeleteStreamResponse,
    KinesisVideoDescribeEdgeConfigurationRequest,
    KinesisVideoDescribeEdgeConfigurationResponse,
    KinesisVideoDescribeImageGenerationConfigurationRequest,
    KinesisVideoDescribeImageGenerationConfigurationResponse,
    KinesisVideoDescribeMappedResourceConfigurationRequest,
    KinesisVideoDescribeMappedResourceConfigurationResponse,
    KinesisVideoDescribeMediaStorageConfigurationRequest,
    KinesisVideoDescribeMediaStorageConfigurationResponse,
    KinesisVideoDescribeNotificationConfigurationRequest,
    KinesisVideoDescribeNotificationConfigurationResponse,
    KinesisVideoDescribeSignalingChannelRequest,
    KinesisVideoDescribeSignalingChannelResponse,
    KinesisVideoDescribeStreamRequest,
    KinesisVideoDescribeStreamResponse,
    KinesisVideoDescribeStreamStorageConfigurationRequest,
    KinesisVideoDescribeStreamStorageConfigurationResponse,
    KinesisVideoGetDataEndpointRequest,
    KinesisVideoGetDataEndpointResponse,
    KinesisVideoGetSignalingChannelEndpointRequest,
    KinesisVideoGetSignalingChannelEndpointResponse,
    KinesisVideoListEdgeAgentConfigurationsRequest,
    KinesisVideoListEdgeAgentConfigurationsResponse,
    KinesisVideoListSignalingChannelsRequest,
    KinesisVideoListSignalingChannelsResponse,
    KinesisVideoListStreamsRequest,
    KinesisVideoListStreamsResponse,
    KinesisVideoListTagsForResourceRequest,
    KinesisVideoListTagsForResourceResponse,
    KinesisVideoListTagsForStreamRequest,
    KinesisVideoListTagsForStreamResponse,
    KinesisVideoStartEdgeConfigurationUpdateRequest,
    KinesisVideoStartEdgeConfigurationUpdateResponse,
    KinesisVideoTagResourceRequest,
    KinesisVideoTagResourceResponse,
    KinesisVideoTagStreamRequest,
    KinesisVideoTagStreamResponse,
    KinesisVideoUntagResourceRequest,
    KinesisVideoUntagResourceResponse,
    KinesisVideoUntagStreamRequest,
    KinesisVideoUntagStreamResponse,
    KinesisVideoUpdateDataRetentionRequest,
    KinesisVideoUpdateDataRetentionResponse,
    KinesisVideoUpdateImageGenerationConfigurationRequest,
    KinesisVideoUpdateImageGenerationConfigurationResponse,
    KinesisVideoUpdateMediaStorageConfigurationRequest,
    KinesisVideoUpdateMediaStorageConfigurationResponse,
    KinesisVideoUpdateNotificationConfigurationRequest,
    KinesisVideoUpdateNotificationConfigurationResponse,
    KinesisVideoUpdateSignalingChannelRequest,
    KinesisVideoUpdateSignalingChannelResponse,
    KinesisVideoUpdateStreamRequest,
    KinesisVideoUpdateStreamResponse,
    KinesisVideoUpdateStreamStorageConfigurationRequest,
    KinesisVideoUpdateStreamStorageConfigurationResponse,
)
from werkflow_aws.types.kinesis_vs_client import KinesisVideoClient
from .base import AWSBaseService


class AWSKinesisVideo(AWSBaseService[KinesisVideoClient]):
    service_name = 'kinesis-vs'
    boto3_service_name = 'kinesisvideo'

    def __init__(self) -> None:
        super().__init__(service_name='kinesis-vs', boto3_service_name='kinesisvideo')

    async def create_signaling_channel(
        self,
        request: KinesisVideoCreateSignalingChannelRequest,
    ) -> KinesisVideoCreateSignalingChannelResponse:
        client = self._require_client()
        return await self._execute(client.create_signaling_channel, request, KinesisVideoCreateSignalingChannelResponse)

    async def create_stream(
        self,
        request: KinesisVideoCreateStreamRequest,
    ) -> KinesisVideoCreateStreamResponse:
        client = self._require_client()
        return await self._execute(client.create_stream, request, KinesisVideoCreateStreamResponse)

    async def delete_edge_configuration(
        self,
        request: KinesisVideoDeleteEdgeConfigurationRequest | None = None,
    ) -> KinesisVideoDeleteEdgeConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_edge_configuration, request, KinesisVideoDeleteEdgeConfigurationResponse)

    async def delete_signaling_channel(
        self,
        request: KinesisVideoDeleteSignalingChannelRequest,
    ) -> KinesisVideoDeleteSignalingChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_signaling_channel, request, KinesisVideoDeleteSignalingChannelResponse)

    async def delete_stream(
        self,
        request: KinesisVideoDeleteStreamRequest,
    ) -> KinesisVideoDeleteStreamResponse:
        client = self._require_client()
        return await self._execute(client.delete_stream, request, KinesisVideoDeleteStreamResponse)

    async def describe_edge_configuration(
        self,
        request: KinesisVideoDescribeEdgeConfigurationRequest | None = None,
    ) -> KinesisVideoDescribeEdgeConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_edge_configuration, request, KinesisVideoDescribeEdgeConfigurationResponse)

    async def describe_image_generation_configuration(
        self,
        request: KinesisVideoDescribeImageGenerationConfigurationRequest | None = None,
    ) -> KinesisVideoDescribeImageGenerationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_generation_configuration, request, KinesisVideoDescribeImageGenerationConfigurationResponse)

    async def describe_mapped_resource_configuration(
        self,
        request: KinesisVideoDescribeMappedResourceConfigurationRequest | None = None,
    ) -> KinesisVideoDescribeMappedResourceConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_mapped_resource_configuration, request, KinesisVideoDescribeMappedResourceConfigurationResponse)

    async def describe_mapped_resource_configuration_paginated(
        self,
        request: KinesisVideoDescribeMappedResourceConfigurationRequest | None = None,
    ) -> list[KinesisVideoDescribeMappedResourceConfigurationResponse]:
        return await self._paginate('describe_mapped_resource_configuration', request, KinesisVideoDescribeMappedResourceConfigurationResponse)

    async def describe_media_storage_configuration(
        self,
        request: KinesisVideoDescribeMediaStorageConfigurationRequest | None = None,
    ) -> KinesisVideoDescribeMediaStorageConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_media_storage_configuration, request, KinesisVideoDescribeMediaStorageConfigurationResponse)

    async def describe_notification_configuration(
        self,
        request: KinesisVideoDescribeNotificationConfigurationRequest | None = None,
    ) -> KinesisVideoDescribeNotificationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_notification_configuration, request, KinesisVideoDescribeNotificationConfigurationResponse)

    async def describe_signaling_channel(
        self,
        request: KinesisVideoDescribeSignalingChannelRequest | None = None,
    ) -> KinesisVideoDescribeSignalingChannelResponse:
        client = self._require_client()
        return await self._execute(client.describe_signaling_channel, request, KinesisVideoDescribeSignalingChannelResponse)

    async def describe_stream(
        self,
        request: KinesisVideoDescribeStreamRequest | None = None,
    ) -> KinesisVideoDescribeStreamResponse:
        client = self._require_client()
        return await self._execute(client.describe_stream, request, KinesisVideoDescribeStreamResponse)

    async def describe_stream_storage_configuration(
        self,
        request: KinesisVideoDescribeStreamStorageConfigurationRequest | None = None,
    ) -> KinesisVideoDescribeStreamStorageConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_stream_storage_configuration, request, KinesisVideoDescribeStreamStorageConfigurationResponse)

    async def get_data_endpoint(
        self,
        request: KinesisVideoGetDataEndpointRequest,
    ) -> KinesisVideoGetDataEndpointResponse:
        client = self._require_client()
        return await self._execute(client.get_data_endpoint, request, KinesisVideoGetDataEndpointResponse)

    async def get_signaling_channel_endpoint(
        self,
        request: KinesisVideoGetSignalingChannelEndpointRequest,
    ) -> KinesisVideoGetSignalingChannelEndpointResponse:
        client = self._require_client()
        return await self._execute(client.get_signaling_channel_endpoint, request, KinesisVideoGetSignalingChannelEndpointResponse)

    async def list_edge_agent_configurations(
        self,
        request: KinesisVideoListEdgeAgentConfigurationsRequest,
    ) -> KinesisVideoListEdgeAgentConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_edge_agent_configurations, request, KinesisVideoListEdgeAgentConfigurationsResponse)

    async def list_edge_agent_configurations_paginated(
        self,
        request: KinesisVideoListEdgeAgentConfigurationsRequest,
    ) -> list[KinesisVideoListEdgeAgentConfigurationsResponse]:
        return await self._paginate('list_edge_agent_configurations', request, KinesisVideoListEdgeAgentConfigurationsResponse)

    async def list_signaling_channels(
        self,
        request: KinesisVideoListSignalingChannelsRequest | None = None,
    ) -> KinesisVideoListSignalingChannelsResponse:
        client = self._require_client()
        return await self._execute(client.list_signaling_channels, request, KinesisVideoListSignalingChannelsResponse)

    async def list_signaling_channels_paginated(
        self,
        request: KinesisVideoListSignalingChannelsRequest | None = None,
    ) -> list[KinesisVideoListSignalingChannelsResponse]:
        return await self._paginate('list_signaling_channels', request, KinesisVideoListSignalingChannelsResponse)

    async def list_streams(
        self,
        request: KinesisVideoListStreamsRequest | None = None,
    ) -> KinesisVideoListStreamsResponse:
        client = self._require_client()
        return await self._execute(client.list_streams, request, KinesisVideoListStreamsResponse)

    async def list_streams_paginated(
        self,
        request: KinesisVideoListStreamsRequest | None = None,
    ) -> list[KinesisVideoListStreamsResponse]:
        return await self._paginate('list_streams', request, KinesisVideoListStreamsResponse)

    async def list_tags_for_resource(
        self,
        request: KinesisVideoListTagsForResourceRequest,
    ) -> KinesisVideoListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, KinesisVideoListTagsForResourceResponse)

    async def list_tags_for_stream(
        self,
        request: KinesisVideoListTagsForStreamRequest | None = None,
    ) -> KinesisVideoListTagsForStreamResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_stream, request, KinesisVideoListTagsForStreamResponse)

    async def start_edge_configuration_update(
        self,
        request: KinesisVideoStartEdgeConfigurationUpdateRequest,
    ) -> KinesisVideoStartEdgeConfigurationUpdateResponse:
        client = self._require_client()
        return await self._execute(client.start_edge_configuration_update, request, KinesisVideoStartEdgeConfigurationUpdateResponse)

    async def tag_resource(
        self,
        request: KinesisVideoTagResourceRequest,
    ) -> KinesisVideoTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, KinesisVideoTagResourceResponse)

    async def tag_stream(
        self,
        request: KinesisVideoTagStreamRequest,
    ) -> KinesisVideoTagStreamResponse:
        client = self._require_client()
        return await self._execute(client.tag_stream, request, KinesisVideoTagStreamResponse)

    async def untag_resource(
        self,
        request: KinesisVideoUntagResourceRequest,
    ) -> KinesisVideoUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, KinesisVideoUntagResourceResponse)

    async def untag_stream(
        self,
        request: KinesisVideoUntagStreamRequest,
    ) -> KinesisVideoUntagStreamResponse:
        client = self._require_client()
        return await self._execute(client.untag_stream, request, KinesisVideoUntagStreamResponse)

    async def update_data_retention(
        self,
        request: KinesisVideoUpdateDataRetentionRequest,
    ) -> KinesisVideoUpdateDataRetentionResponse:
        client = self._require_client()
        return await self._execute(client.update_data_retention, request, KinesisVideoUpdateDataRetentionResponse)

    async def update_image_generation_configuration(
        self,
        request: KinesisVideoUpdateImageGenerationConfigurationRequest | None = None,
    ) -> KinesisVideoUpdateImageGenerationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_image_generation_configuration, request, KinesisVideoUpdateImageGenerationConfigurationResponse)

    async def update_media_storage_configuration(
        self,
        request: KinesisVideoUpdateMediaStorageConfigurationRequest,
    ) -> KinesisVideoUpdateMediaStorageConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_media_storage_configuration, request, KinesisVideoUpdateMediaStorageConfigurationResponse)

    async def update_notification_configuration(
        self,
        request: KinesisVideoUpdateNotificationConfigurationRequest | None = None,
    ) -> KinesisVideoUpdateNotificationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_notification_configuration, request, KinesisVideoUpdateNotificationConfigurationResponse)

    async def update_signaling_channel(
        self,
        request: KinesisVideoUpdateSignalingChannelRequest,
    ) -> KinesisVideoUpdateSignalingChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_signaling_channel, request, KinesisVideoUpdateSignalingChannelResponse)

    async def update_stream(
        self,
        request: KinesisVideoUpdateStreamRequest,
    ) -> KinesisVideoUpdateStreamResponse:
        client = self._require_client()
        return await self._execute(client.update_stream, request, KinesisVideoUpdateStreamResponse)

    async def update_stream_storage_configuration(
        self,
        request: KinesisVideoUpdateStreamStorageConfigurationRequest,
    ) -> KinesisVideoUpdateStreamStorageConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_stream_storage_configuration, request, KinesisVideoUpdateStreamStorageConfigurationResponse)
