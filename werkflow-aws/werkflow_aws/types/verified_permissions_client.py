from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class VerifiedPermissionsClient(ABC):

    @abstractmethod
    def batch_get_policy(
        self,
        *,
        requests: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_is_authorized(
        self,
        *,
        policyStoreId: str,
        requests: list[dict[str, Any]],
        entities: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_is_authorized_with_token(
        self,
        *,
        policyStoreId: str,
        requests: list[dict[str, Any]],
        identityToken: str | None = None,
        accessToken: str | None = None,
        entities: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_identity_source(
        self,
        *,
        policyStoreId: str,
        configuration: dict[str, Any],
        clientToken: str | None = None,
        principalEntityType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_policy(
        self,
        *,
        policyStoreId: str,
        definition: dict[str, Any],
        clientToken: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_policy_store(
        self,
        *,
        validationSettings: dict[str, Any],
        clientToken: str | None = None,
        description: str | None = None,
        deletionProtection: str | None = None,
        encryptionSettings: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_policy_store_alias(
        self,
        *,
        aliasName: str,
        policyStoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_policy_template(
        self,
        *,
        policyStoreId: str,
        statement: str,
        clientToken: str | None = None,
        description: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_identity_source(
        self,
        *,
        policyStoreId: str,
        identitySourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy(
        self,
        *,
        policyStoreId: str,
        policyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy_store(
        self,
        *,
        policyStoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy_store_alias(
        self,
        *,
        aliasName: str,
        deletionMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy_template(
        self,
        *,
        policyStoreId: str,
        policyTemplateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_identity_source(
        self,
        *,
        policyStoreId: str,
        identitySourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy(
        self,
        *,
        policyStoreId: str,
        policyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy_store(
        self,
        *,
        policyStoreId: str,
        tags: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy_store_alias(
        self,
        *,
        aliasName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy_template(
        self,
        *,
        policyStoreId: str,
        policyTemplateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_schema(
        self,
        *,
        policyStoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def is_authorized(
        self,
        *,
        policyStoreId: str,
        principal: dict[str, Any] | None = None,
        action: dict[str, Any] | None = None,
        resource: dict[str, Any] | None = None,
        context: dict[str, Any] | None = None,
        entities: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def is_authorized_with_token(
        self,
        *,
        policyStoreId: str,
        identityToken: str | None = None,
        accessToken: str | None = None,
        action: dict[str, Any] | None = None,
        resource: dict[str, Any] | None = None,
        context: dict[str, Any] | None = None,
        entities: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_identity_sources(
        self,
        *,
        policyStoreId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policies(
        self,
        *,
        policyStoreId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policy_store_aliases(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
        filter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policy_stores(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policy_templates(
        self,
        *,
        policyStoreId: str,
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
    def put_schema(
        self,
        *,
        policyStoreId: str,
        definition: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: dict[str, str],
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
    def update_identity_source(
        self,
        *,
        policyStoreId: str,
        identitySourceId: str,
        updateConfiguration: dict[str, Any],
        principalEntityType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_policy(
        self,
        *,
        policyStoreId: str,
        policyId: str,
        definition: dict[str, Any] | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_policy_store(
        self,
        *,
        policyStoreId: str,
        validationSettings: dict[str, Any],
        deletionProtection: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_policy_template(
        self,
        *,
        policyStoreId: str,
        policyTemplateId: str,
        statement: str,
        description: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
