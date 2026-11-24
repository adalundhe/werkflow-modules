from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class OpenSearchServerlessClient(ABC):

    @abstractmethod
    def batch_get_collection(
        self,
        *,
        ids: list[str] | None = None,
        names: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_collection_group(
        self,
        *,
        ids: list[str] | None = None,
        names: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_effective_lifecycle_policy(
        self,
        *,
        resourceIdentifiers: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_lifecycle_policy(
        self,
        *,
        identifiers: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_vpc_endpoint(
        self,
        *,
        ids: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_ingestion_job(
        self,
        *,
        collectionId: str,
        ingestionJobId: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_access_policy(
        self,
        *,
        type: str,
        name: str,
        policy: str,
        description: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_collection(
        self,
        *,
        name: str,
        type: str | None = None,
        description: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        standbyReplicas: str | None = None,
        vectorOptions: dict[str, Any] | None = None,
        collectionGroupName: str | None = None,
        encryptionConfig: dict[str, Any] | None = None,
        deletionProtection: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_collection_group(
        self,
        *,
        name: str,
        standbyReplicas: str,
        description: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        capacityLimits: dict[str, Any] | None = None,
        generation: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_index(
        self,
        *,
        id: str,
        indexName: str,
        indexSchema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ingestion_job(
        self,
        *,
        collectionId: str,
        ingestionJobName: str,
        indexName: str,
        source: dict[str, Any],
        failureIndexName: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ingestion_stream(
        self,
        *,
        collectionId: str,
        ingestionStreamName: str,
        indexName: str,
        source: dict[str, Any],
        roleArn: str,
        failureIndexName: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_lifecycle_policy(
        self,
        *,
        type: str,
        name: str,
        policy: str,
        description: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_security_config(
        self,
        *,
        type: str,
        name: str,
        description: str | None = None,
        samlOptions: dict[str, Any] | None = None,
        iamIdentityCenterOptions: dict[str, Any] | None = None,
        iamFederationOptions: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_security_policy(
        self,
        *,
        type: str,
        name: str,
        policy: str,
        description: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_endpoint(
        self,
        *,
        name: str,
        vpcId: str,
        subnetIds: list[str],
        securityGroupIds: list[str] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_access_policy(
        self,
        *,
        type: str,
        name: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_collection(
        self,
        *,
        id: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_collection_group(
        self,
        *,
        id: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_index(
        self,
        *,
        id: str,
        indexName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ingestion_stream(
        self,
        *,
        collectionId: str,
        ingestionStreamId: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lifecycle_policy(
        self,
        *,
        type: str,
        name: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_security_config(
        self,
        *,
        id: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_security_policy(
        self,
        *,
        type: str,
        name: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_endpoint(
        self,
        *,
        id: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_access_policy(
        self,
        *,
        type: str,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_settings(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_index(
        self,
        *,
        id: str,
        indexName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ingestion_job(
        self,
        *,
        collectionId: str,
        ingestionJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ingestion_stream(
        self,
        *,
        collectionId: str,
        ingestionStreamId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policies_stats(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_security_config(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_security_policy(
        self,
        *,
        type: str,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_access_policies(
        self,
        *,
        type: str,
        resource: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_collection_groups(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_collections(
        self,
        *,
        collectionFilters: dict[str, Any] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ingestion_jobs(
        self,
        *,
        collectionId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ingestion_streams(
        self,
        *,
        collectionId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_lifecycle_policies(
        self,
        *,
        type: str,
        resources: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_configs(
        self,
        *,
        type: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_policies(
        self,
        *,
        type: str,
        resource: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
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
    def list_vpc_endpoints(
        self,
        *,
        vpcEndpointFilters: dict[str, Any] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
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
    def update_access_policy(
        self,
        *,
        type: str,
        name: str,
        policyVersion: str,
        description: str | None = None,
        policy: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_account_settings(
        self,
        *,
        capacityLimits: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_collection(
        self,
        *,
        id: str,
        description: str | None = None,
        vectorOptions: dict[str, Any] | None = None,
        deletionProtection: str | None = None,
        encryptionConfig: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_collection_group(
        self,
        *,
        id: str,
        description: str | None = None,
        capacityLimits: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_index(
        self,
        *,
        id: str,
        indexName: str,
        indexSchema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_lifecycle_policy(
        self,
        *,
        type: str,
        name: str,
        policyVersion: str,
        description: str | None = None,
        policy: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_security_config(
        self,
        *,
        id: str,
        configVersion: str,
        description: str | None = None,
        samlOptions: dict[str, Any] | None = None,
        iamIdentityCenterOptionsUpdates: dict[str, Any] | None = None,
        iamFederationOptions: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_security_policy(
        self,
        *,
        type: str,
        name: str,
        policyVersion: str,
        description: str | None = None,
        policy: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vpc_endpoint(
        self,
        *,
        id: str,
        addSubnetIds: list[str] | None = None,
        removeSubnetIds: list[str] | None = None,
        addSecurityGroupIds: list[str] | None = None,
        removeSecurityGroupIds: list[str] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
