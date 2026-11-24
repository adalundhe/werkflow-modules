from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class FirehoseClient(ABC):

    @abstractmethod
    def create_delivery_stream(
        self,
        *,
        DeliveryStreamName: str,
        DeliveryStreamType: str | None = None,
        DirectPutSourceConfiguration: dict[str, Any] | None = None,
        KinesisStreamSourceConfiguration: dict[str, Any] | None = None,
        DeliveryStreamEncryptionConfigurationInput: dict[str, Any] | None = None,
        S3DestinationConfiguration: dict[str, Any] | None = None,
        ExtendedS3DestinationConfiguration: dict[str, Any] | None = None,
        RedshiftDestinationConfiguration: dict[str, Any] | None = None,
        ElasticsearchDestinationConfiguration: dict[str, Any] | None = None,
        AmazonopensearchserviceDestinationConfiguration: dict[str, Any] | None = None,
        SplunkDestinationConfiguration: dict[str, Any] | None = None,
        HttpEndpointDestinationConfiguration: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        AmazonOpenSearchServerlessDestinationConfiguration: dict[str, Any] | None = None,
        MSKSourceConfiguration: dict[str, Any] | None = None,
        SnowflakeDestinationConfiguration: dict[str, Any] | None = None,
        IcebergDestinationConfiguration: dict[str, Any] | None = None,
        DatabaseSourceConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_delivery_stream(
        self,
        *,
        DeliveryStreamName: str,
        AllowForceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_delivery_stream(
        self,
        *,
        DeliveryStreamName: str,
        Limit: int | None = None,
        ExclusiveStartDestinationId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_delivery_streams(
        self,
        *,
        Limit: int | None = None,
        DeliveryStreamType: str | None = None,
        ExclusiveStartDeliveryStreamName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_delivery_stream(
        self,
        *,
        DeliveryStreamName: str,
        ExclusiveStartTagKey: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_record(
        self,
        *,
        DeliveryStreamName: str,
        Record: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_record_batch(
        self,
        *,
        DeliveryStreamName: str,
        Records: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_delivery_stream_encryption(
        self,
        *,
        DeliveryStreamName: str,
        DeliveryStreamEncryptionConfigurationInput: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_delivery_stream_encryption(
        self,
        *,
        DeliveryStreamName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_delivery_stream(
        self,
        *,
        DeliveryStreamName: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_delivery_stream(
        self,
        *,
        DeliveryStreamName: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_destination(
        self,
        *,
        DeliveryStreamName: str,
        CurrentDeliveryStreamVersionId: str,
        DestinationId: str,
        S3DestinationUpdate: dict[str, Any] | None = None,
        ExtendedS3DestinationUpdate: dict[str, Any] | None = None,
        RedshiftDestinationUpdate: dict[str, Any] | None = None,
        ElasticsearchDestinationUpdate: dict[str, Any] | None = None,
        AmazonopensearchserviceDestinationUpdate: dict[str, Any] | None = None,
        SplunkDestinationUpdate: dict[str, Any] | None = None,
        HttpEndpointDestinationUpdate: dict[str, Any] | None = None,
        AmazonOpenSearchServerlessDestinationUpdate: dict[str, Any] | None = None,
        SnowflakeDestinationUpdate: dict[str, Any] | None = None,
        IcebergDestinationUpdate: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
