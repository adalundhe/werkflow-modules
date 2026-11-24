from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class CodeArtifactClient(ABC):

    @abstractmethod
    def get_authorization_token(
        self,
        *,
        domain: str,
        domainOwner: str | None = None,
        durationSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_repository_endpoint(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        domainOwner: str | None = None,
        endpointType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domains(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain(
        self,
        *,
        domain: str,
        domainOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain(
        self,
        *,
        domain: str,
        encryptionKey: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain(
        self,
        *,
        domain: str,
        domainOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_repositories(
        self,
        *,
        repositoryPrefix: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_repository(
        self,
        *,
        domain: str,
        repository: str,
        domainOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_repository(
        self,
        *,
        domain: str,
        repository: str,
        domainOwner: str | None = None,
        description: str | None = None,
        upstreams: list[dict[str, Any]] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_repository(
        self,
        *,
        domain: str,
        repository: str,
        domainOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_packages(
        self,
        *,
        domain: str,
        repository: str,
        domainOwner: str | None = None,
        format: str | None = None,
        namespace: str | None = None,
        packagePrefix: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        publish: str | None = None,
        upstream: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_package_versions(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
        status: str | None = None,
        sortBy: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        originType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_package_versions(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        versions: list[str],
        domainOwner: str | None = None,
        namespace: str | None = None,
        expectedStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_external_connection(
        self,
        *,
        domain: str,
        repository: str,
        externalConnection: str,
        domainOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_package_versions(
        self,
        *,
        domain: str,
        sourceRepository: str,
        destinationRepository: str,
        format: str,
        package: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
        versions: list[str] | None = None,
        versionRevisions: dict[str, str] | None = None,
        allowOverwrite: bool | None = None,
        includeFromUpstream: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_package_group(
        self,
        *,
        domain: str,
        packageGroup: str,
        domainOwner: str | None = None,
        contactInfo: str | None = None,
        description: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain_permissions_policy(
        self,
        *,
        domain: str,
        domainOwner: str | None = None,
        policyRevision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_package(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_package_group(
        self,
        *,
        domain: str,
        packageGroup: str,
        domainOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_repository_permissions_policy(
        self,
        *,
        domain: str,
        repository: str,
        domainOwner: str | None = None,
        policyRevision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_package(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_package_group(
        self,
        *,
        domain: str,
        packageGroup: str,
        domainOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_package_version(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        packageVersion: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_external_connection(
        self,
        *,
        domain: str,
        repository: str,
        externalConnection: str,
        domainOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def dispose_package_versions(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        versions: list[str],
        domainOwner: str | None = None,
        namespace: str | None = None,
        versionRevisions: dict[str, str] | None = None,
        expectedStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_associated_package_group(
        self,
        *,
        domain: str,
        format: str,
        package: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_permissions_policy(
        self,
        *,
        domain: str,
        domainOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_package_version_asset(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        packageVersion: str,
        asset: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
        packageVersionRevision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_package_version_readme(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        packageVersion: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_repository_permissions_policy(
        self,
        *,
        domain: str,
        repository: str,
        domainOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_allowed_repositories_for_group(
        self,
        *,
        domain: str,
        packageGroup: str,
        originRestrictionType: str,
        domainOwner: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_associated_packages(
        self,
        *,
        domain: str,
        packageGroup: str,
        domainOwner: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        preview: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_package_groups(
        self,
        *,
        domain: str,
        domainOwner: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        prefix: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_package_version_assets(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        packageVersion: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_package_version_dependencies(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        packageVersion: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_repositories_in_domain(
        self,
        *,
        domain: str,
        domainOwner: str | None = None,
        administratorAccount: str | None = None,
        repositoryPrefix: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sub_package_groups(
        self,
        *,
        domain: str,
        packageGroup: str,
        domainOwner: str | None = None,
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
    def publish_package_version(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        packageVersion: str,
        assetContent: bytes | BinaryIO | str,
        assetName: str,
        assetSHA256: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
        unfinished: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_domain_permissions_policy(
        self,
        *,
        domain: str,
        policyDocument: str,
        domainOwner: str | None = None,
        policyRevision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_package_origin_configuration(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        restrictions: dict[str, Any],
        domainOwner: str | None = None,
        namespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_repository_permissions_policy(
        self,
        *,
        domain: str,
        repository: str,
        policyDocument: str,
        domainOwner: str | None = None,
        policyRevision: str | None = None,
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
    def update_package_group(
        self,
        *,
        domain: str,
        packageGroup: str,
        domainOwner: str | None = None,
        contactInfo: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_package_group_origin_configuration(
        self,
        *,
        domain: str,
        packageGroup: str,
        domainOwner: str | None = None,
        restrictions: dict[str, str] | None = None,
        addAllowedRepositories: list[dict[str, Any]] | None = None,
        removeAllowedRepositories: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_package_versions_status(
        self,
        *,
        domain: str,
        repository: str,
        format: str,
        package: str,
        versions: list[str],
        targetStatus: str,
        domainOwner: str | None = None,
        namespace: str | None = None,
        versionRevisions: dict[str, str] | None = None,
        expectedStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_repository(
        self,
        *,
        domain: str,
        repository: str,
        domainOwner: str | None = None,
        description: str | None = None,
        upstreams: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
