from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class ECRClient(ABC):

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
    def batch_get_image(
        self,
        *,
        repositoryName: str,
        imageIds: list[dict[str, Any]],
        registryId: str | None = None,
        acceptedMediaTypes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_repository_scanning_configuration(
        self,
        *,
        repositoryNames: list[str],
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
    def create_pull_through_cache_rule(
        self,
        *,
        ecrRepositoryPrefix: str,
        upstreamRegistryUrl: str,
        registryId: str | None = None,
        upstreamRegistry: str | None = None,
        credentialArn: str | None = None,
        customRoleArn: str | None = None,
        upstreamRepositoryPrefix: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_repository(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        imageTagMutability: str | None = None,
        imageTagMutabilityExclusionFilters: list[dict[str, Any]] | None = None,
        imageScanningConfiguration: dict[str, Any] | None = None,
        encryptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_repository_creation_template(
        self,
        *,
        prefix: str,
        appliedFor: list[str],
        description: str | None = None,
        encryptionConfiguration: dict[str, Any] | None = None,
        resourceTags: list[dict[str, Any]] | None = None,
        imageTagMutability: str | None = None,
        imageTagMutabilityExclusionFilters: list[dict[str, Any]] | None = None,
        repositoryPolicy: str | None = None,
        lifecyclePolicy: str | None = None,
        customRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lifecycle_policy(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_pull_through_cache_rule(
        self,
        *,
        ecrRepositoryPrefix: str,
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_registry_policy(self) -> dict[str, Any]:
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
    def delete_repository_creation_template(
        self,
        *,
        prefix: str,
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
    def delete_signing_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_pull_time_update_exclusion(
        self,
        *,
        principalArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_replication_status(
        self,
        *,
        repositoryName: str,
        imageId: dict[str, Any],
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_scan_findings(
        self,
        *,
        repositoryName: str,
        imageId: dict[str, Any],
        registryId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_signing_status(
        self,
        *,
        repositoryName: str,
        imageId: dict[str, Any],
        registryId: str | None = None,
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
        filter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pull_through_cache_rules(
        self,
        *,
        registryId: str | None = None,
        ecrRepositoryPrefixes: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_registry(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replication_backfill_results(
        self,
        *,
        replicationBackfillId: str,
        registryId: str | None = None,
        resultStatusFilter: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
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
    def describe_repository_creation_templates(
        self,
        *,
        prefixes: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_setting(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_authorization_token(
        self,
        *,
        registryIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_download_url_for_layer(
        self,
        *,
        repositoryName: str,
        layerDigest: str,
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lifecycle_policy(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lifecycle_policy_preview(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
        imageIds: list[dict[str, Any]] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_registry_policy(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_registry_scanning_configuration(self) -> dict[str, Any]:
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
    def get_signing_configuration(self) -> dict[str, Any]:
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
    def list_image_referrers(
        self,
        *,
        repositoryName: str,
        subjectId: dict[str, Any],
        registryId: str | None = None,
        filter: dict[str, Any] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_images(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pull_time_update_exclusions(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_replication_backfills(
        self,
        *,
        registryId: str | None = None,
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
    def put_account_setting(
        self,
        *,
        name: str,
        value: str,
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
    def put_image_scanning_configuration(
        self,
        *,
        repositoryName: str,
        imageScanningConfiguration: dict[str, Any],
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_image_tag_mutability(
        self,
        *,
        repositoryName: str,
        imageTagMutability: str,
        registryId: str | None = None,
        imageTagMutabilityExclusionFilters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_lifecycle_policy(
        self,
        *,
        repositoryName: str,
        lifecyclePolicyText: str,
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_registry_policy(
        self,
        *,
        policyText: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_registry_scanning_configuration(
        self,
        *,
        scanType: str | None = None,
        rules: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_replication_configuration(
        self,
        *,
        replicationConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_signing_configuration(
        self,
        *,
        signingConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_pull_time_update_exclusion(
        self,
        *,
        principalArn: str,
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
    def start_image_scan(
        self,
        *,
        repositoryName: str,
        imageId: dict[str, Any],
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_lifecycle_policy_preview(
        self,
        *,
        repositoryName: str,
        registryId: str | None = None,
        lifecyclePolicyText: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_replication_backfill(
        self,
        *,
        destination: dict[str, Any],
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_replication_backfill(
        self,
        *,
        replicationBackfillId: str,
        registryId: str | None = None,
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
    def update_image_storage_class(
        self,
        *,
        repositoryName: str,
        imageId: dict[str, Any],
        targetStorageClass: str,
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pull_through_cache_rule(
        self,
        *,
        ecrRepositoryPrefix: str,
        registryId: str | None = None,
        credentialArn: str | None = None,
        customRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_repository_creation_template(
        self,
        *,
        prefix: str,
        description: str | None = None,
        encryptionConfiguration: dict[str, Any] | None = None,
        resourceTags: list[dict[str, Any]] | None = None,
        imageTagMutability: str | None = None,
        imageTagMutabilityExclusionFilters: list[dict[str, Any]] | None = None,
        repositoryPolicy: str | None = None,
        lifecyclePolicy: str | None = None,
        appliedFor: list[str] | None = None,
        customRoleArn: str | None = None,
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
    def validate_pull_through_cache_rule(
        self,
        *,
        ecrRepositoryPrefix: str,
        registryId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
