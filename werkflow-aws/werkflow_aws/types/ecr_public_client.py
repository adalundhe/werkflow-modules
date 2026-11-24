from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class ECRPublicClient(ABC):

    @abstractmethod
    def batch_check_layer_availability(
        self,
        *,
        repositoryName: str,
        layerDigests: list[str],
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_image(
        self,
        *,
        repositoryName: str,
        imageIds: list[dict[str, Any]],
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def complete_layer_upload(
        self,
        *,
        repositoryName: str,
        uploadId: str,
        layerDigests: list[str],
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_repository(
        self,
        *,
        repositoryName: str,
        catalogData: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_repository(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
        force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_repository_policy(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_tags(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_images(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
        imageIds: list[dict[str, Any]] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_registries(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_repositories(
        self,
        *,
        registryId: str | None = None,
        repositoryNames: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_authorization_token(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_registry_catalog_data(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_repository_catalog_data(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_repository_policy(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def initiate_layer_upload(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
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
    def put_image(
        self,
        *,
        repositoryName: str,
        imageManifest: str,
        registryId: str | None = None,
        imageManifestMediaType: str | None = None,
        imageTag: str | None = None,
        imageDigest: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_registry_catalog_data(
        self,
        *,
        displayName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_repository_catalog_data(
        self,
        *,
        repositoryName: str,
        catalogData: dict[str, Any],
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_repository_policy(
        self,
        *,
        repositoryName: str,
        policyText: str,
        registryId: str | None = None,
        force: bool | None = None,
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
    def upload_layer_part(
        self,
        *,
        repositoryName: str,
        uploadId: str,
        partFirstByte: int,
        partLastByte: int,
        layerPartBlob: bytes | BinaryIO | str,
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
