from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class SecurityLakeClient(ABC):

    @abstractmethod
    def create_aws_log_source(
        self,
        *,
        sources: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_log_source(
        self,
        *,
        configuration: dict[str, Any],
        sourceName: str,
        eventClasses: list[str] | None = None,
        sourceVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_lake(
        self,
        *,
        configurations: list[dict[str, Any]],
        metaStoreManagerRoleArn: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_lake_exception_subscription(
        self,
        *,
        notificationEndpoint: str,
        subscriptionProtocol: str,
        exceptionTimeToLive: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_lake_organization_configuration(
        self,
        *,
        autoEnableNewAccount: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_subscriber(
        self,
        *,
        sources: list[dict[str, Any]],
        subscriberIdentity: dict[str, Any],
        subscriberName: str,
        accessTypes: list[str] | None = None,
        subscriberDescription: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_subscriber_notification(
        self,
        *,
        configuration: dict[str, Any],
        subscriberId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_aws_log_source(
        self,
        *,
        sources: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_log_source(
        self,
        *,
        sourceName: str,
        sourceVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_lake(
        self,
        *,
        regions: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_lake_exception_subscription(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_lake_organization_configuration(
        self,
        *,
        autoEnableNewAccount: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_subscriber(
        self,
        *,
        subscriberId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_subscriber_notification(
        self,
        *,
        subscriberId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_data_lake_delegated_administrator(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_lake_exception_subscription(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_lake_organization_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_lake_sources(
        self,
        *,
        accounts: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_subscriber(
        self,
        *,
        subscriberId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_lake_exceptions(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        regions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_lakes(
        self,
        *,
        regions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_log_sources(
        self,
        *,
        accounts: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        regions: list[str] | None = None,
        sources: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_subscribers(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_data_lake_delegated_administrator(
        self,
        *,
        accountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_lake(
        self,
        *,
        configurations: list[dict[str, Any]],
        metaStoreManagerRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_lake_exception_subscription(
        self,
        *,
        notificationEndpoint: str,
        subscriptionProtocol: str,
        exceptionTimeToLive: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_subscriber(
        self,
        *,
        subscriberId: str,
        sources: list[dict[str, Any]] | None = None,
        subscriberDescription: str | None = None,
        subscriberIdentity: dict[str, Any] | None = None,
        subscriberName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_subscriber_notification(
        self,
        *,
        configuration: dict[str, Any],
        subscriberId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
