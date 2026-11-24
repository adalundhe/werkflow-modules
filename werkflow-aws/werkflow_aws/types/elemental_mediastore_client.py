from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class MediaStoreClient(ABC):

    @abstractmethod
    def create_container(
        self,
        *,
        ContainerName: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_container(
        self,
        *,
        ContainerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_container_policy(
        self,
        *,
        ContainerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cors_policy(
        self,
        *,
        ContainerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lifecycle_policy(
        self,
        *,
        ContainerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_metric_policy(
        self,
        *,
        ContainerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_container(
        self,
        *,
        ContainerName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_container_policy(
        self,
        *,
        ContainerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cors_policy(
        self,
        *,
        ContainerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lifecycle_policy(
        self,
        *,
        ContainerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_metric_policy(
        self,
        *,
        ContainerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_containers(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        Resource: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_container_policy(
        self,
        *,
        ContainerName: str,
        Policy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_cors_policy(
        self,
        *,
        ContainerName: str,
        CorsPolicy: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_lifecycle_policy(
        self,
        *,
        ContainerName: str,
        LifecyclePolicy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_metric_policy(
        self,
        *,
        ContainerName: str,
        MetricPolicy: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_access_logging(
        self,
        *,
        ContainerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_access_logging(
        self,
        *,
        ContainerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        Resource: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        Resource: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
