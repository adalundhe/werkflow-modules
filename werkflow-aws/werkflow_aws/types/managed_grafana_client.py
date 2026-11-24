from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class ManagedGrafanaClient(ABC):

    @abstractmethod
    def associate_license(
        self,
        *,
        workspaceId: str,
        licenseType: str,
        grafanaToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workspace(
        self,
        *,
        accountAccessType: str,
        permissionType: str,
        authenticationProviders: list[str],
        clientToken: str | None = None,
        organizationRoleName: str | None = None,
        stackSetName: str | None = None,
        workspaceDataSources: list[str] | None = None,
        workspaceDescription: str | None = None,
        workspaceName: str | None = None,
        workspaceNotificationDestinations: list[str] | None = None,
        workspaceOrganizationalUnits: list[str] | None = None,
        workspaceRoleArn: str | None = None,
        tags: dict[str, str] | None = None,
        vpcConfiguration: dict[str, Any] | None = None,
        configuration: str | None = None,
        networkAccessControl: dict[str, Any] | None = None,
        grafanaVersion: str | None = None,
        ipAddressType: str | None = None,
        kmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workspace_api_key(
        self,
        *,
        keyName: str,
        keyRole: str,
        secondsToLive: int,
        workspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workspace_service_account(
        self,
        *,
        name: str,
        grafanaRole: str,
        workspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workspace_service_account_token(
        self,
        *,
        name: str,
        secondsToLive: int,
        serviceAccountId: str,
        workspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workspace(
        self,
        *,
        workspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workspace_api_key(
        self,
        *,
        keyName: str,
        workspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workspace_service_account(
        self,
        *,
        serviceAccountId: str,
        workspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workspace_service_account_token(
        self,
        *,
        tokenId: str,
        serviceAccountId: str,
        workspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspace(
        self,
        *,
        workspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspace_authentication(
        self,
        *,
        workspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspace_configuration(
        self,
        *,
        workspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_license(
        self,
        *,
        workspaceId: str,
        licenseType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_permissions(
        self,
        *,
        workspaceId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
        userType: str | None = None,
        userId: str | None = None,
        groupId: str | None = None,
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
    def list_versions(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        workspaceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workspace_service_account_tokens(
        self,
        *,
        serviceAccountId: str,
        workspaceId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workspace_service_accounts(
        self,
        *,
        workspaceId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workspaces(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
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
    def update_permissions(
        self,
        *,
        updateInstructionBatch: list[dict[str, Any]],
        workspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workspace(
        self,
        *,
        workspaceId: str,
        accountAccessType: str | None = None,
        organizationRoleName: str | None = None,
        permissionType: str | None = None,
        stackSetName: str | None = None,
        workspaceDataSources: list[str] | None = None,
        workspaceDescription: str | None = None,
        workspaceName: str | None = None,
        workspaceNotificationDestinations: list[str] | None = None,
        workspaceOrganizationalUnits: list[str] | None = None,
        workspaceRoleArn: str | None = None,
        vpcConfiguration: dict[str, Any] | None = None,
        removeVpcConfiguration: bool | None = None,
        networkAccessControl: dict[str, Any] | None = None,
        removeNetworkAccessConfiguration: bool | None = None,
        ipAddressType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workspace_authentication(
        self,
        *,
        workspaceId: str,
        authenticationProviders: list[str],
        samlConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workspace_configuration(
        self,
        *,
        configuration: str,
        workspaceId: str,
        grafanaVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
