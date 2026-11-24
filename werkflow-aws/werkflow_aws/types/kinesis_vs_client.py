from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class KinesisVideoClient(ABC):

    @abstractmethod
    def create_signaling_channel(
        self,
        *,
        ChannelName: str,
        ChannelType: str | None = None,
        SingleMasterConfiguration: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stream(
        self,
        *,
        StreamName: str,
        DeviceName: str | None = None,
        MediaType: str | None = None,
        KmsKeyId: str | None = None,
        DataRetentionInHours: int | None = None,
        Tags: dict[str, str] | None = None,
        StreamStorageConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_edge_configuration(
        self,
        *,
        StreamName: str | None = None,
        StreamARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_signaling_channel(
        self,
        *,
        ChannelARN: str,
        CurrentVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_stream(
        self,
        *,
        StreamARN: str,
        CurrentVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_edge_configuration(
        self,
        *,
        StreamName: str | None = None,
        StreamARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_generation_configuration(
        self,
        *,
        StreamName: str | None = None,
        StreamARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_mapped_resource_configuration(
        self,
        *,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_media_storage_configuration(
        self,
        *,
        ChannelName: str | None = None,
        ChannelARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_notification_configuration(
        self,
        *,
        StreamName: str | None = None,
        StreamARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_signaling_channel(
        self,
        *,
        ChannelName: str | None = None,
        ChannelARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stream(
        self,
        *,
        StreamName: str | None = None,
        StreamARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stream_storage_configuration(
        self,
        *,
        StreamName: str | None = None,
        StreamARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_endpoint(
        self,
        *,
        APIName: str,
        StreamName: str | None = None,
        StreamARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_signaling_channel_endpoint(
        self,
        *,
        ChannelARN: str,
        SingleMasterChannelEndpointConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_edge_agent_configurations(
        self,
        *,
        HubDeviceArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_signaling_channels(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        ChannelNameCondition: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_streams(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        StreamNameCondition: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_stream(
        self,
        *,
        NextToken: str | None = None,
        StreamARN: str | None = None,
        StreamName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_edge_configuration_update(
        self,
        *,
        EdgeConfig: dict[str, Any],
        StreamName: str | None = None,
        StreamARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceARN: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_stream(
        self,
        *,
        Tags: dict[str, str],
        StreamARN: str | None = None,
        StreamName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceARN: str,
        TagKeyList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_stream(
        self,
        *,
        TagKeyList: list[str],
        StreamARN: str | None = None,
        StreamName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_retention(
        self,
        *,
        CurrentVersion: str,
        Operation: str,
        DataRetentionChangeInHours: int,
        StreamName: str | None = None,
        StreamARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_image_generation_configuration(
        self,
        *,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        ImageGenerationConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_media_storage_configuration(
        self,
        *,
        ChannelARN: str,
        MediaStorageConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_notification_configuration(
        self,
        *,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        NotificationConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_signaling_channel(
        self,
        *,
        ChannelARN: str,
        CurrentVersion: str,
        SingleMasterConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stream(
        self,
        *,
        CurrentVersion: str,
        StreamName: str | None = None,
        StreamARN: str | None = None,
        DeviceName: str | None = None,
        MediaType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stream_storage_configuration(
        self,
        *,
        CurrentVersion: str,
        StreamStorageConfiguration: dict[str, Any],
        StreamName: str | None = None,
        StreamARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
