from werkflow_aws.models.managed_grafana import (
    ManagedGrafanaAssociateLicenseRequest,
    ManagedGrafanaAssociateLicenseResponse,
    ManagedGrafanaCreateWorkspaceApiKeyRequest,
    ManagedGrafanaCreateWorkspaceApiKeyResponse,
    ManagedGrafanaCreateWorkspaceRequest,
    ManagedGrafanaCreateWorkspaceResponse,
    ManagedGrafanaCreateWorkspaceServiceAccountRequest,
    ManagedGrafanaCreateWorkspaceServiceAccountResponse,
    ManagedGrafanaCreateWorkspaceServiceAccountTokenRequest,
    ManagedGrafanaCreateWorkspaceServiceAccountTokenResponse,
    ManagedGrafanaDeleteWorkspaceApiKeyRequest,
    ManagedGrafanaDeleteWorkspaceApiKeyResponse,
    ManagedGrafanaDeleteWorkspaceRequest,
    ManagedGrafanaDeleteWorkspaceResponse,
    ManagedGrafanaDeleteWorkspaceServiceAccountRequest,
    ManagedGrafanaDeleteWorkspaceServiceAccountResponse,
    ManagedGrafanaDeleteWorkspaceServiceAccountTokenRequest,
    ManagedGrafanaDeleteWorkspaceServiceAccountTokenResponse,
    ManagedGrafanaDescribeWorkspaceAuthenticationRequest,
    ManagedGrafanaDescribeWorkspaceAuthenticationResponse,
    ManagedGrafanaDescribeWorkspaceConfigurationRequest,
    ManagedGrafanaDescribeWorkspaceConfigurationResponse,
    ManagedGrafanaDescribeWorkspaceRequest,
    ManagedGrafanaDescribeWorkspaceResponse,
    ManagedGrafanaDisassociateLicenseRequest,
    ManagedGrafanaDisassociateLicenseResponse,
    ManagedGrafanaListPermissionsRequest,
    ManagedGrafanaListPermissionsResponse,
    ManagedGrafanaListTagsForResourceRequest,
    ManagedGrafanaListTagsForResourceResponse,
    ManagedGrafanaListVersionsRequest,
    ManagedGrafanaListVersionsResponse,
    ManagedGrafanaListWorkspaceServiceAccountTokensRequest,
    ManagedGrafanaListWorkspaceServiceAccountTokensResponse,
    ManagedGrafanaListWorkspaceServiceAccountsRequest,
    ManagedGrafanaListWorkspaceServiceAccountsResponse,
    ManagedGrafanaListWorkspacesRequest,
    ManagedGrafanaListWorkspacesResponse,
    ManagedGrafanaTagResourceRequest,
    ManagedGrafanaTagResourceResponse,
    ManagedGrafanaUntagResourceRequest,
    ManagedGrafanaUntagResourceResponse,
    ManagedGrafanaUpdatePermissionsRequest,
    ManagedGrafanaUpdatePermissionsResponse,
    ManagedGrafanaUpdateWorkspaceAuthenticationRequest,
    ManagedGrafanaUpdateWorkspaceAuthenticationResponse,
    ManagedGrafanaUpdateWorkspaceConfigurationRequest,
    ManagedGrafanaUpdateWorkspaceConfigurationResponse,
    ManagedGrafanaUpdateWorkspaceRequest,
    ManagedGrafanaUpdateWorkspaceResponse,
)
from werkflow_aws.types.managed_grafana_client import ManagedGrafanaClient
from .base import AWSBaseService


class AWSManagedGrafana(AWSBaseService[ManagedGrafanaClient]):
    service_name = 'managed-grafana'
    boto3_service_name = 'grafana'

    def __init__(self) -> None:
        super().__init__(service_name='managed-grafana', boto3_service_name='grafana')

    async def associate_license(
        self,
        request: ManagedGrafanaAssociateLicenseRequest,
    ) -> ManagedGrafanaAssociateLicenseResponse:
        client = self._require_client()
        return await self._execute(client.associate_license, request, ManagedGrafanaAssociateLicenseResponse)

    async def create_workspace(
        self,
        request: ManagedGrafanaCreateWorkspaceRequest,
    ) -> ManagedGrafanaCreateWorkspaceResponse:
        client = self._require_client()
        return await self._execute(client.create_workspace, request, ManagedGrafanaCreateWorkspaceResponse)

    async def create_workspace_api_key(
        self,
        request: ManagedGrafanaCreateWorkspaceApiKeyRequest,
    ) -> ManagedGrafanaCreateWorkspaceApiKeyResponse:
        client = self._require_client()
        return await self._execute(client.create_workspace_api_key, request, ManagedGrafanaCreateWorkspaceApiKeyResponse)

    async def create_workspace_service_account(
        self,
        request: ManagedGrafanaCreateWorkspaceServiceAccountRequest,
    ) -> ManagedGrafanaCreateWorkspaceServiceAccountResponse:
        client = self._require_client()
        return await self._execute(client.create_workspace_service_account, request, ManagedGrafanaCreateWorkspaceServiceAccountResponse)

    async def create_workspace_service_account_token(
        self,
        request: ManagedGrafanaCreateWorkspaceServiceAccountTokenRequest,
    ) -> ManagedGrafanaCreateWorkspaceServiceAccountTokenResponse:
        client = self._require_client()
        return await self._execute(client.create_workspace_service_account_token, request, ManagedGrafanaCreateWorkspaceServiceAccountTokenResponse)

    async def delete_workspace(
        self,
        request: ManagedGrafanaDeleteWorkspaceRequest,
    ) -> ManagedGrafanaDeleteWorkspaceResponse:
        client = self._require_client()
        return await self._execute(client.delete_workspace, request, ManagedGrafanaDeleteWorkspaceResponse)

    async def delete_workspace_api_key(
        self,
        request: ManagedGrafanaDeleteWorkspaceApiKeyRequest,
    ) -> ManagedGrafanaDeleteWorkspaceApiKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_workspace_api_key, request, ManagedGrafanaDeleteWorkspaceApiKeyResponse)

    async def delete_workspace_service_account(
        self,
        request: ManagedGrafanaDeleteWorkspaceServiceAccountRequest,
    ) -> ManagedGrafanaDeleteWorkspaceServiceAccountResponse:
        client = self._require_client()
        return await self._execute(client.delete_workspace_service_account, request, ManagedGrafanaDeleteWorkspaceServiceAccountResponse)

    async def delete_workspace_service_account_token(
        self,
        request: ManagedGrafanaDeleteWorkspaceServiceAccountTokenRequest,
    ) -> ManagedGrafanaDeleteWorkspaceServiceAccountTokenResponse:
        client = self._require_client()
        return await self._execute(client.delete_workspace_service_account_token, request, ManagedGrafanaDeleteWorkspaceServiceAccountTokenResponse)

    async def describe_workspace(
        self,
        request: ManagedGrafanaDescribeWorkspaceRequest,
    ) -> ManagedGrafanaDescribeWorkspaceResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspace, request, ManagedGrafanaDescribeWorkspaceResponse)

    async def describe_workspace_authentication(
        self,
        request: ManagedGrafanaDescribeWorkspaceAuthenticationRequest,
    ) -> ManagedGrafanaDescribeWorkspaceAuthenticationResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspace_authentication, request, ManagedGrafanaDescribeWorkspaceAuthenticationResponse)

    async def describe_workspace_configuration(
        self,
        request: ManagedGrafanaDescribeWorkspaceConfigurationRequest,
    ) -> ManagedGrafanaDescribeWorkspaceConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspace_configuration, request, ManagedGrafanaDescribeWorkspaceConfigurationResponse)

    async def disassociate_license(
        self,
        request: ManagedGrafanaDisassociateLicenseRequest,
    ) -> ManagedGrafanaDisassociateLicenseResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_license, request, ManagedGrafanaDisassociateLicenseResponse)

    async def list_permissions(
        self,
        request: ManagedGrafanaListPermissionsRequest,
    ) -> ManagedGrafanaListPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.list_permissions, request, ManagedGrafanaListPermissionsResponse)

    async def list_permissions_paginated(
        self,
        request: ManagedGrafanaListPermissionsRequest,
    ) -> list[ManagedGrafanaListPermissionsResponse]:
        return await self._paginate('list_permissions', request, ManagedGrafanaListPermissionsResponse)

    async def list_tags_for_resource(
        self,
        request: ManagedGrafanaListTagsForResourceRequest,
    ) -> ManagedGrafanaListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, ManagedGrafanaListTagsForResourceResponse)

    async def list_versions(
        self,
        request: ManagedGrafanaListVersionsRequest | None = None,
    ) -> ManagedGrafanaListVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_versions, request, ManagedGrafanaListVersionsResponse)

    async def list_versions_paginated(
        self,
        request: ManagedGrafanaListVersionsRequest | None = None,
    ) -> list[ManagedGrafanaListVersionsResponse]:
        return await self._paginate('list_versions', request, ManagedGrafanaListVersionsResponse)

    async def list_workspace_service_account_tokens(
        self,
        request: ManagedGrafanaListWorkspaceServiceAccountTokensRequest,
    ) -> ManagedGrafanaListWorkspaceServiceAccountTokensResponse:
        client = self._require_client()
        return await self._execute(client.list_workspace_service_account_tokens, request, ManagedGrafanaListWorkspaceServiceAccountTokensResponse)

    async def list_workspace_service_account_tokens_paginated(
        self,
        request: ManagedGrafanaListWorkspaceServiceAccountTokensRequest,
    ) -> list[ManagedGrafanaListWorkspaceServiceAccountTokensResponse]:
        return await self._paginate('list_workspace_service_account_tokens', request, ManagedGrafanaListWorkspaceServiceAccountTokensResponse)

    async def list_workspace_service_accounts(
        self,
        request: ManagedGrafanaListWorkspaceServiceAccountsRequest,
    ) -> ManagedGrafanaListWorkspaceServiceAccountsResponse:
        client = self._require_client()
        return await self._execute(client.list_workspace_service_accounts, request, ManagedGrafanaListWorkspaceServiceAccountsResponse)

    async def list_workspace_service_accounts_paginated(
        self,
        request: ManagedGrafanaListWorkspaceServiceAccountsRequest,
    ) -> list[ManagedGrafanaListWorkspaceServiceAccountsResponse]:
        return await self._paginate('list_workspace_service_accounts', request, ManagedGrafanaListWorkspaceServiceAccountsResponse)

    async def list_workspaces(
        self,
        request: ManagedGrafanaListWorkspacesRequest | None = None,
    ) -> ManagedGrafanaListWorkspacesResponse:
        client = self._require_client()
        return await self._execute(client.list_workspaces, request, ManagedGrafanaListWorkspacesResponse)

    async def list_workspaces_paginated(
        self,
        request: ManagedGrafanaListWorkspacesRequest | None = None,
    ) -> list[ManagedGrafanaListWorkspacesResponse]:
        return await self._paginate('list_workspaces', request, ManagedGrafanaListWorkspacesResponse)

    async def tag_resource(
        self,
        request: ManagedGrafanaTagResourceRequest,
    ) -> ManagedGrafanaTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, ManagedGrafanaTagResourceResponse)

    async def untag_resource(
        self,
        request: ManagedGrafanaUntagResourceRequest,
    ) -> ManagedGrafanaUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, ManagedGrafanaUntagResourceResponse)

    async def update_permissions(
        self,
        request: ManagedGrafanaUpdatePermissionsRequest,
    ) -> ManagedGrafanaUpdatePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_permissions, request, ManagedGrafanaUpdatePermissionsResponse)

    async def update_workspace(
        self,
        request: ManagedGrafanaUpdateWorkspaceRequest,
    ) -> ManagedGrafanaUpdateWorkspaceResponse:
        client = self._require_client()
        return await self._execute(client.update_workspace, request, ManagedGrafanaUpdateWorkspaceResponse)

    async def update_workspace_authentication(
        self,
        request: ManagedGrafanaUpdateWorkspaceAuthenticationRequest,
    ) -> ManagedGrafanaUpdateWorkspaceAuthenticationResponse:
        client = self._require_client()
        return await self._execute(client.update_workspace_authentication, request, ManagedGrafanaUpdateWorkspaceAuthenticationResponse)

    async def update_workspace_configuration(
        self,
        request: ManagedGrafanaUpdateWorkspaceConfigurationRequest,
    ) -> ManagedGrafanaUpdateWorkspaceConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_workspace_configuration, request, ManagedGrafanaUpdateWorkspaceConfigurationResponse)
