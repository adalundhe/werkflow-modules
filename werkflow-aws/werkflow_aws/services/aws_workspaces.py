from werkflow_aws.models.workspaces import (
    WorkSpacesAcceptAccountLinkInvitationRequest,
    WorkSpacesAcceptAccountLinkInvitationResponse,
    WorkSpacesAssociateConnectionAliasRequest,
    WorkSpacesAssociateConnectionAliasResponse,
    WorkSpacesAssociateIpGroupsRequest,
    WorkSpacesAssociateIpGroupsResponse,
    WorkSpacesAssociateWorkspaceApplicationRequest,
    WorkSpacesAssociateWorkspaceApplicationResponse,
    WorkSpacesAuthorizeIpRulesRequest,
    WorkSpacesAuthorizeIpRulesResponse,
    WorkSpacesCopyWorkspaceImageRequest,
    WorkSpacesCopyWorkspaceImageResponse,
    WorkSpacesCreateAccountLinkInvitationRequest,
    WorkSpacesCreateAccountLinkInvitationResponse,
    WorkSpacesCreateConnectClientAddInRequest,
    WorkSpacesCreateConnectClientAddInResponse,
    WorkSpacesCreateConnectionAliasRequest,
    WorkSpacesCreateConnectionAliasResponse,
    WorkSpacesCreateIpGroupRequest,
    WorkSpacesCreateIpGroupResponse,
    WorkSpacesCreateStandbyWorkspacesRequest,
    WorkSpacesCreateStandbyWorkspacesResponse,
    WorkSpacesCreateTagsRequest,
    WorkSpacesCreateTagsResponse,
    WorkSpacesCreateUpdatedWorkspaceImageRequest,
    WorkSpacesCreateUpdatedWorkspaceImageResponse,
    WorkSpacesCreateWorkspaceBundleRequest,
    WorkSpacesCreateWorkspaceBundleResponse,
    WorkSpacesCreateWorkspaceImageRequest,
    WorkSpacesCreateWorkspaceImageResponse,
    WorkSpacesCreateWorkspacesPoolRequest,
    WorkSpacesCreateWorkspacesPoolResponse,
    WorkSpacesCreateWorkspacesRequest,
    WorkSpacesCreateWorkspacesResponse,
    WorkSpacesDeleteAccountLinkInvitationRequest,
    WorkSpacesDeleteAccountLinkInvitationResponse,
    WorkSpacesDeleteClientBrandingRequest,
    WorkSpacesDeleteClientBrandingResponse,
    WorkSpacesDeleteConnectClientAddInRequest,
    WorkSpacesDeleteConnectClientAddInResponse,
    WorkSpacesDeleteConnectionAliasRequest,
    WorkSpacesDeleteConnectionAliasResponse,
    WorkSpacesDeleteIpGroupRequest,
    WorkSpacesDeleteIpGroupResponse,
    WorkSpacesDeleteTagsRequest,
    WorkSpacesDeleteTagsResponse,
    WorkSpacesDeleteWorkspaceBundleRequest,
    WorkSpacesDeleteWorkspaceBundleResponse,
    WorkSpacesDeleteWorkspaceImageRequest,
    WorkSpacesDeleteWorkspaceImageResponse,
    WorkSpacesDeployWorkspaceApplicationsRequest,
    WorkSpacesDeployWorkspaceApplicationsResponse,
    WorkSpacesDeregisterWorkspaceDirectoryRequest,
    WorkSpacesDeregisterWorkspaceDirectoryResponse,
    WorkSpacesDescribeAccountModificationsRequest,
    WorkSpacesDescribeAccountModificationsResponse,
    WorkSpacesDescribeAccountRequest,
    WorkSpacesDescribeAccountResponse,
    WorkSpacesDescribeApplicationAssociationsRequest,
    WorkSpacesDescribeApplicationAssociationsResponse,
    WorkSpacesDescribeApplicationsRequest,
    WorkSpacesDescribeApplicationsResponse,
    WorkSpacesDescribeBundleAssociationsRequest,
    WorkSpacesDescribeBundleAssociationsResponse,
    WorkSpacesDescribeClientBrandingRequest,
    WorkSpacesDescribeClientBrandingResponse,
    WorkSpacesDescribeClientPropertiesRequest,
    WorkSpacesDescribeClientPropertiesResponse,
    WorkSpacesDescribeConnectClientAddInsRequest,
    WorkSpacesDescribeConnectClientAddInsResponse,
    WorkSpacesDescribeConnectionAliasPermissionsRequest,
    WorkSpacesDescribeConnectionAliasPermissionsResponse,
    WorkSpacesDescribeConnectionAliasesRequest,
    WorkSpacesDescribeConnectionAliasesResponse,
    WorkSpacesDescribeCustomWorkspaceImageImportRequest,
    WorkSpacesDescribeCustomWorkspaceImageImportResponse,
    WorkSpacesDescribeImageAssociationsRequest,
    WorkSpacesDescribeImageAssociationsResponse,
    WorkSpacesDescribeIpGroupsRequest,
    WorkSpacesDescribeIpGroupsResponse,
    WorkSpacesDescribeTagsRequest,
    WorkSpacesDescribeTagsResponse,
    WorkSpacesDescribeWorkspaceAssociationsRequest,
    WorkSpacesDescribeWorkspaceAssociationsResponse,
    WorkSpacesDescribeWorkspaceBundlesRequest,
    WorkSpacesDescribeWorkspaceBundlesResponse,
    WorkSpacesDescribeWorkspaceDirectoriesRequest,
    WorkSpacesDescribeWorkspaceDirectoriesResponse,
    WorkSpacesDescribeWorkspaceImagePermissionsRequest,
    WorkSpacesDescribeWorkspaceImagePermissionsResponse,
    WorkSpacesDescribeWorkspaceImagesRequest,
    WorkSpacesDescribeWorkspaceImagesResponse,
    WorkSpacesDescribeWorkspaceSnapshotsRequest,
    WorkSpacesDescribeWorkspaceSnapshotsResponse,
    WorkSpacesDescribeWorkspacesConnectionStatusRequest,
    WorkSpacesDescribeWorkspacesConnectionStatusResponse,
    WorkSpacesDescribeWorkspacesPoolSessionsRequest,
    WorkSpacesDescribeWorkspacesPoolSessionsResponse,
    WorkSpacesDescribeWorkspacesPoolsRequest,
    WorkSpacesDescribeWorkspacesPoolsResponse,
    WorkSpacesDescribeWorkspacesRequest,
    WorkSpacesDescribeWorkspacesResponse,
    WorkSpacesDisassociateConnectionAliasRequest,
    WorkSpacesDisassociateConnectionAliasResponse,
    WorkSpacesDisassociateIpGroupsRequest,
    WorkSpacesDisassociateIpGroupsResponse,
    WorkSpacesDisassociateWorkspaceApplicationRequest,
    WorkSpacesDisassociateWorkspaceApplicationResponse,
    WorkSpacesGetAccountLinkRequest,
    WorkSpacesGetAccountLinkResponse,
    WorkSpacesImportClientBrandingRequest,
    WorkSpacesImportClientBrandingResponse,
    WorkSpacesImportCustomWorkspaceImageRequest,
    WorkSpacesImportCustomWorkspaceImageResponse,
    WorkSpacesImportWorkspaceImageRequest,
    WorkSpacesImportWorkspaceImageResponse,
    WorkSpacesListAccountLinksRequest,
    WorkSpacesListAccountLinksResponse,
    WorkSpacesListAvailableManagementCidrRangesRequest,
    WorkSpacesListAvailableManagementCidrRangesResponse,
    WorkSpacesMigrateWorkspaceRequest,
    WorkSpacesMigrateWorkspaceResponse,
    WorkSpacesModifyAccountRequest,
    WorkSpacesModifyAccountResponse,
    WorkSpacesModifyCertificateBasedAuthPropertiesRequest,
    WorkSpacesModifyCertificateBasedAuthPropertiesResponse,
    WorkSpacesModifyClientPropertiesRequest,
    WorkSpacesModifyClientPropertiesResponse,
    WorkSpacesModifyEndpointEncryptionModeRequest,
    WorkSpacesModifyEndpointEncryptionModeResponse,
    WorkSpacesModifySamlPropertiesRequest,
    WorkSpacesModifySamlPropertiesResponse,
    WorkSpacesModifySelfservicePermissionsRequest,
    WorkSpacesModifySelfservicePermissionsResponse,
    WorkSpacesModifyStreamingPropertiesRequest,
    WorkSpacesModifyStreamingPropertiesResponse,
    WorkSpacesModifyWorkspaceAccessPropertiesRequest,
    WorkSpacesModifyWorkspaceAccessPropertiesResponse,
    WorkSpacesModifyWorkspaceCreationPropertiesRequest,
    WorkSpacesModifyWorkspaceCreationPropertiesResponse,
    WorkSpacesModifyWorkspacePropertiesRequest,
    WorkSpacesModifyWorkspacePropertiesResponse,
    WorkSpacesModifyWorkspaceStateRequest,
    WorkSpacesModifyWorkspaceStateResponse,
    WorkSpacesRebootWorkspacesRequest,
    WorkSpacesRebootWorkspacesResponse,
    WorkSpacesRebuildWorkspacesRequest,
    WorkSpacesRebuildWorkspacesResponse,
    WorkSpacesRegisterWorkspaceDirectoryRequest,
    WorkSpacesRegisterWorkspaceDirectoryResponse,
    WorkSpacesRejectAccountLinkInvitationRequest,
    WorkSpacesRejectAccountLinkInvitationResponse,
    WorkSpacesRestoreWorkspaceRequest,
    WorkSpacesRestoreWorkspaceResponse,
    WorkSpacesRevokeIpRulesRequest,
    WorkSpacesRevokeIpRulesResponse,
    WorkSpacesStartWorkspacesPoolRequest,
    WorkSpacesStartWorkspacesPoolResponse,
    WorkSpacesStartWorkspacesRequest,
    WorkSpacesStartWorkspacesResponse,
    WorkSpacesStopWorkspacesPoolRequest,
    WorkSpacesStopWorkspacesPoolResponse,
    WorkSpacesStopWorkspacesRequest,
    WorkSpacesStopWorkspacesResponse,
    WorkSpacesTerminateWorkspacesPoolRequest,
    WorkSpacesTerminateWorkspacesPoolResponse,
    WorkSpacesTerminateWorkspacesPoolSessionRequest,
    WorkSpacesTerminateWorkspacesPoolSessionResponse,
    WorkSpacesTerminateWorkspacesRequest,
    WorkSpacesTerminateWorkspacesResponse,
    WorkSpacesUpdateConnectClientAddInRequest,
    WorkSpacesUpdateConnectClientAddInResponse,
    WorkSpacesUpdateConnectionAliasPermissionRequest,
    WorkSpacesUpdateConnectionAliasPermissionResponse,
    WorkSpacesUpdateRulesOfIpGroupRequest,
    WorkSpacesUpdateRulesOfIpGroupResponse,
    WorkSpacesUpdateWorkspaceBundleRequest,
    WorkSpacesUpdateWorkspaceBundleResponse,
    WorkSpacesUpdateWorkspaceImagePermissionRequest,
    WorkSpacesUpdateWorkspaceImagePermissionResponse,
    WorkSpacesUpdateWorkspacesPoolRequest,
    WorkSpacesUpdateWorkspacesPoolResponse,
)
from werkflow_aws.types.workspaces_client import WorkSpacesClient
from .base import AWSBaseService


class AWSWorkSpaces(AWSBaseService[WorkSpacesClient]):
    service_name = 'workspaces'
    boto3_service_name = 'workspaces'

    def __init__(self) -> None:
        super().__init__(service_name='workspaces', boto3_service_name='workspaces')

    async def accept_account_link_invitation(
        self,
        request: WorkSpacesAcceptAccountLinkInvitationRequest,
    ) -> WorkSpacesAcceptAccountLinkInvitationResponse:
        client = self._require_client()
        return await self._execute(client.accept_account_link_invitation, request, WorkSpacesAcceptAccountLinkInvitationResponse)

    async def associate_connection_alias(
        self,
        request: WorkSpacesAssociateConnectionAliasRequest,
    ) -> WorkSpacesAssociateConnectionAliasResponse:
        client = self._require_client()
        return await self._execute(client.associate_connection_alias, request, WorkSpacesAssociateConnectionAliasResponse)

    async def associate_ip_groups(
        self,
        request: WorkSpacesAssociateIpGroupsRequest,
    ) -> WorkSpacesAssociateIpGroupsResponse:
        client = self._require_client()
        return await self._execute(client.associate_ip_groups, request, WorkSpacesAssociateIpGroupsResponse)

    async def associate_workspace_application(
        self,
        request: WorkSpacesAssociateWorkspaceApplicationRequest,
    ) -> WorkSpacesAssociateWorkspaceApplicationResponse:
        client = self._require_client()
        return await self._execute(client.associate_workspace_application, request, WorkSpacesAssociateWorkspaceApplicationResponse)

    async def authorize_ip_rules(
        self,
        request: WorkSpacesAuthorizeIpRulesRequest,
    ) -> WorkSpacesAuthorizeIpRulesResponse:
        client = self._require_client()
        return await self._execute(client.authorize_ip_rules, request, WorkSpacesAuthorizeIpRulesResponse)

    async def copy_workspace_image(
        self,
        request: WorkSpacesCopyWorkspaceImageRequest,
    ) -> WorkSpacesCopyWorkspaceImageResponse:
        client = self._require_client()
        return await self._execute(client.copy_workspace_image, request, WorkSpacesCopyWorkspaceImageResponse)

    async def create_account_link_invitation(
        self,
        request: WorkSpacesCreateAccountLinkInvitationRequest,
    ) -> WorkSpacesCreateAccountLinkInvitationResponse:
        client = self._require_client()
        return await self._execute(client.create_account_link_invitation, request, WorkSpacesCreateAccountLinkInvitationResponse)

    async def create_connect_client_add_in(
        self,
        request: WorkSpacesCreateConnectClientAddInRequest,
    ) -> WorkSpacesCreateConnectClientAddInResponse:
        client = self._require_client()
        return await self._execute(client.create_connect_client_add_in, request, WorkSpacesCreateConnectClientAddInResponse)

    async def create_connection_alias(
        self,
        request: WorkSpacesCreateConnectionAliasRequest,
    ) -> WorkSpacesCreateConnectionAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_connection_alias, request, WorkSpacesCreateConnectionAliasResponse)

    async def create_ip_group(
        self,
        request: WorkSpacesCreateIpGroupRequest,
    ) -> WorkSpacesCreateIpGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_ip_group, request, WorkSpacesCreateIpGroupResponse)

    async def create_standby_workspaces(
        self,
        request: WorkSpacesCreateStandbyWorkspacesRequest,
    ) -> WorkSpacesCreateStandbyWorkspacesResponse:
        client = self._require_client()
        return await self._execute(client.create_standby_workspaces, request, WorkSpacesCreateStandbyWorkspacesResponse)

    async def create_tags(
        self,
        request: WorkSpacesCreateTagsRequest,
    ) -> WorkSpacesCreateTagsResponse:
        client = self._require_client()
        return await self._execute(client.create_tags, request, WorkSpacesCreateTagsResponse)

    async def create_updated_workspace_image(
        self,
        request: WorkSpacesCreateUpdatedWorkspaceImageRequest,
    ) -> WorkSpacesCreateUpdatedWorkspaceImageResponse:
        client = self._require_client()
        return await self._execute(client.create_updated_workspace_image, request, WorkSpacesCreateUpdatedWorkspaceImageResponse)

    async def create_workspace_bundle(
        self,
        request: WorkSpacesCreateWorkspaceBundleRequest,
    ) -> WorkSpacesCreateWorkspaceBundleResponse:
        client = self._require_client()
        return await self._execute(client.create_workspace_bundle, request, WorkSpacesCreateWorkspaceBundleResponse)

    async def create_workspace_image(
        self,
        request: WorkSpacesCreateWorkspaceImageRequest,
    ) -> WorkSpacesCreateWorkspaceImageResponse:
        client = self._require_client()
        return await self._execute(client.create_workspace_image, request, WorkSpacesCreateWorkspaceImageResponse)

    async def create_workspaces(
        self,
        request: WorkSpacesCreateWorkspacesRequest,
    ) -> WorkSpacesCreateWorkspacesResponse:
        client = self._require_client()
        return await self._execute(client.create_workspaces, request, WorkSpacesCreateWorkspacesResponse)

    async def create_workspaces_pool(
        self,
        request: WorkSpacesCreateWorkspacesPoolRequest,
    ) -> WorkSpacesCreateWorkspacesPoolResponse:
        client = self._require_client()
        return await self._execute(client.create_workspaces_pool, request, WorkSpacesCreateWorkspacesPoolResponse)

    async def delete_account_link_invitation(
        self,
        request: WorkSpacesDeleteAccountLinkInvitationRequest,
    ) -> WorkSpacesDeleteAccountLinkInvitationResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_link_invitation, request, WorkSpacesDeleteAccountLinkInvitationResponse)

    async def delete_client_branding(
        self,
        request: WorkSpacesDeleteClientBrandingRequest,
    ) -> WorkSpacesDeleteClientBrandingResponse:
        client = self._require_client()
        return await self._execute(client.delete_client_branding, request, WorkSpacesDeleteClientBrandingResponse)

    async def delete_connect_client_add_in(
        self,
        request: WorkSpacesDeleteConnectClientAddInRequest,
    ) -> WorkSpacesDeleteConnectClientAddInResponse:
        client = self._require_client()
        return await self._execute(client.delete_connect_client_add_in, request, WorkSpacesDeleteConnectClientAddInResponse)

    async def delete_connection_alias(
        self,
        request: WorkSpacesDeleteConnectionAliasRequest,
    ) -> WorkSpacesDeleteConnectionAliasResponse:
        client = self._require_client()
        return await self._execute(client.delete_connection_alias, request, WorkSpacesDeleteConnectionAliasResponse)

    async def delete_ip_group(
        self,
        request: WorkSpacesDeleteIpGroupRequest,
    ) -> WorkSpacesDeleteIpGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_ip_group, request, WorkSpacesDeleteIpGroupResponse)

    async def delete_tags(
        self,
        request: WorkSpacesDeleteTagsRequest,
    ) -> WorkSpacesDeleteTagsResponse:
        client = self._require_client()
        return await self._execute(client.delete_tags, request, WorkSpacesDeleteTagsResponse)

    async def delete_workspace_bundle(
        self,
        request: WorkSpacesDeleteWorkspaceBundleRequest | None = None,
    ) -> WorkSpacesDeleteWorkspaceBundleResponse:
        client = self._require_client()
        return await self._execute(client.delete_workspace_bundle, request, WorkSpacesDeleteWorkspaceBundleResponse)

    async def delete_workspace_image(
        self,
        request: WorkSpacesDeleteWorkspaceImageRequest,
    ) -> WorkSpacesDeleteWorkspaceImageResponse:
        client = self._require_client()
        return await self._execute(client.delete_workspace_image, request, WorkSpacesDeleteWorkspaceImageResponse)

    async def deploy_workspace_applications(
        self,
        request: WorkSpacesDeployWorkspaceApplicationsRequest,
    ) -> WorkSpacesDeployWorkspaceApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.deploy_workspace_applications, request, WorkSpacesDeployWorkspaceApplicationsResponse)

    async def deregister_workspace_directory(
        self,
        request: WorkSpacesDeregisterWorkspaceDirectoryRequest,
    ) -> WorkSpacesDeregisterWorkspaceDirectoryResponse:
        client = self._require_client()
        return await self._execute(client.deregister_workspace_directory, request, WorkSpacesDeregisterWorkspaceDirectoryResponse)

    async def describe_account(
        self,
        request: WorkSpacesDescribeAccountRequest | None = None,
    ) -> WorkSpacesDescribeAccountResponse:
        client = self._require_client()
        return await self._execute(client.describe_account, request, WorkSpacesDescribeAccountResponse)

    async def describe_account_modifications(
        self,
        request: WorkSpacesDescribeAccountModificationsRequest | None = None,
    ) -> WorkSpacesDescribeAccountModificationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_modifications, request, WorkSpacesDescribeAccountModificationsResponse)

    async def describe_account_modifications_paginated(
        self,
        request: WorkSpacesDescribeAccountModificationsRequest | None = None,
    ) -> list[WorkSpacesDescribeAccountModificationsResponse]:
        return await self._paginate('describe_account_modifications', request, WorkSpacesDescribeAccountModificationsResponse)

    async def describe_application_associations(
        self,
        request: WorkSpacesDescribeApplicationAssociationsRequest,
    ) -> WorkSpacesDescribeApplicationAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_application_associations, request, WorkSpacesDescribeApplicationAssociationsResponse)

    async def describe_applications(
        self,
        request: WorkSpacesDescribeApplicationsRequest | None = None,
    ) -> WorkSpacesDescribeApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_applications, request, WorkSpacesDescribeApplicationsResponse)

    async def describe_bundle_associations(
        self,
        request: WorkSpacesDescribeBundleAssociationsRequest,
    ) -> WorkSpacesDescribeBundleAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_bundle_associations, request, WorkSpacesDescribeBundleAssociationsResponse)

    async def describe_client_branding(
        self,
        request: WorkSpacesDescribeClientBrandingRequest,
    ) -> WorkSpacesDescribeClientBrandingResponse:
        client = self._require_client()
        return await self._execute(client.describe_client_branding, request, WorkSpacesDescribeClientBrandingResponse)

    async def describe_client_properties(
        self,
        request: WorkSpacesDescribeClientPropertiesRequest,
    ) -> WorkSpacesDescribeClientPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.describe_client_properties, request, WorkSpacesDescribeClientPropertiesResponse)

    async def describe_connect_client_add_ins(
        self,
        request: WorkSpacesDescribeConnectClientAddInsRequest,
    ) -> WorkSpacesDescribeConnectClientAddInsResponse:
        client = self._require_client()
        return await self._execute(client.describe_connect_client_add_ins, request, WorkSpacesDescribeConnectClientAddInsResponse)

    async def describe_connection_alias_permissions(
        self,
        request: WorkSpacesDescribeConnectionAliasPermissionsRequest,
    ) -> WorkSpacesDescribeConnectionAliasPermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_connection_alias_permissions, request, WorkSpacesDescribeConnectionAliasPermissionsResponse)

    async def describe_connection_aliases(
        self,
        request: WorkSpacesDescribeConnectionAliasesRequest | None = None,
    ) -> WorkSpacesDescribeConnectionAliasesResponse:
        client = self._require_client()
        return await self._execute(client.describe_connection_aliases, request, WorkSpacesDescribeConnectionAliasesResponse)

    async def describe_custom_workspace_image_import(
        self,
        request: WorkSpacesDescribeCustomWorkspaceImageImportRequest,
    ) -> WorkSpacesDescribeCustomWorkspaceImageImportResponse:
        client = self._require_client()
        return await self._execute(client.describe_custom_workspace_image_import, request, WorkSpacesDescribeCustomWorkspaceImageImportResponse)

    async def describe_image_associations(
        self,
        request: WorkSpacesDescribeImageAssociationsRequest,
    ) -> WorkSpacesDescribeImageAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_associations, request, WorkSpacesDescribeImageAssociationsResponse)

    async def describe_ip_groups(
        self,
        request: WorkSpacesDescribeIpGroupsRequest | None = None,
    ) -> WorkSpacesDescribeIpGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_ip_groups, request, WorkSpacesDescribeIpGroupsResponse)

    async def describe_ip_groups_paginated(
        self,
        request: WorkSpacesDescribeIpGroupsRequest | None = None,
    ) -> list[WorkSpacesDescribeIpGroupsResponse]:
        return await self._paginate('describe_ip_groups', request, WorkSpacesDescribeIpGroupsResponse)

    async def describe_tags(
        self,
        request: WorkSpacesDescribeTagsRequest,
    ) -> WorkSpacesDescribeTagsResponse:
        client = self._require_client()
        return await self._execute(client.describe_tags, request, WorkSpacesDescribeTagsResponse)

    async def describe_workspace_associations(
        self,
        request: WorkSpacesDescribeWorkspaceAssociationsRequest,
    ) -> WorkSpacesDescribeWorkspaceAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspace_associations, request, WorkSpacesDescribeWorkspaceAssociationsResponse)

    async def describe_workspace_bundles(
        self,
        request: WorkSpacesDescribeWorkspaceBundlesRequest | None = None,
    ) -> WorkSpacesDescribeWorkspaceBundlesResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspace_bundles, request, WorkSpacesDescribeWorkspaceBundlesResponse)

    async def describe_workspace_bundles_paginated(
        self,
        request: WorkSpacesDescribeWorkspaceBundlesRequest | None = None,
    ) -> list[WorkSpacesDescribeWorkspaceBundlesResponse]:
        return await self._paginate('describe_workspace_bundles', request, WorkSpacesDescribeWorkspaceBundlesResponse)

    async def describe_workspace_directories(
        self,
        request: WorkSpacesDescribeWorkspaceDirectoriesRequest | None = None,
    ) -> WorkSpacesDescribeWorkspaceDirectoriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspace_directories, request, WorkSpacesDescribeWorkspaceDirectoriesResponse)

    async def describe_workspace_directories_paginated(
        self,
        request: WorkSpacesDescribeWorkspaceDirectoriesRequest | None = None,
    ) -> list[WorkSpacesDescribeWorkspaceDirectoriesResponse]:
        return await self._paginate('describe_workspace_directories', request, WorkSpacesDescribeWorkspaceDirectoriesResponse)

    async def describe_workspace_image_permissions(
        self,
        request: WorkSpacesDescribeWorkspaceImagePermissionsRequest,
    ) -> WorkSpacesDescribeWorkspaceImagePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspace_image_permissions, request, WorkSpacesDescribeWorkspaceImagePermissionsResponse)

    async def describe_workspace_images(
        self,
        request: WorkSpacesDescribeWorkspaceImagesRequest | None = None,
    ) -> WorkSpacesDescribeWorkspaceImagesResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspace_images, request, WorkSpacesDescribeWorkspaceImagesResponse)

    async def describe_workspace_images_paginated(
        self,
        request: WorkSpacesDescribeWorkspaceImagesRequest | None = None,
    ) -> list[WorkSpacesDescribeWorkspaceImagesResponse]:
        return await self._paginate('describe_workspace_images', request, WorkSpacesDescribeWorkspaceImagesResponse)

    async def describe_workspace_snapshots(
        self,
        request: WorkSpacesDescribeWorkspaceSnapshotsRequest,
    ) -> WorkSpacesDescribeWorkspaceSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspace_snapshots, request, WorkSpacesDescribeWorkspaceSnapshotsResponse)

    async def describe_workspaces(
        self,
        request: WorkSpacesDescribeWorkspacesRequest | None = None,
    ) -> WorkSpacesDescribeWorkspacesResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspaces, request, WorkSpacesDescribeWorkspacesResponse)

    async def describe_workspaces_paginated(
        self,
        request: WorkSpacesDescribeWorkspacesRequest | None = None,
    ) -> list[WorkSpacesDescribeWorkspacesResponse]:
        return await self._paginate('describe_workspaces', request, WorkSpacesDescribeWorkspacesResponse)

    async def describe_workspaces_connection_status(
        self,
        request: WorkSpacesDescribeWorkspacesConnectionStatusRequest | None = None,
    ) -> WorkSpacesDescribeWorkspacesConnectionStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspaces_connection_status, request, WorkSpacesDescribeWorkspacesConnectionStatusResponse)

    async def describe_workspaces_connection_status_paginated(
        self,
        request: WorkSpacesDescribeWorkspacesConnectionStatusRequest | None = None,
    ) -> list[WorkSpacesDescribeWorkspacesConnectionStatusResponse]:
        return await self._paginate('describe_workspaces_connection_status', request, WorkSpacesDescribeWorkspacesConnectionStatusResponse)

    async def describe_workspaces_pool_sessions(
        self,
        request: WorkSpacesDescribeWorkspacesPoolSessionsRequest,
    ) -> WorkSpacesDescribeWorkspacesPoolSessionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspaces_pool_sessions, request, WorkSpacesDescribeWorkspacesPoolSessionsResponse)

    async def describe_workspaces_pools(
        self,
        request: WorkSpacesDescribeWorkspacesPoolsRequest | None = None,
    ) -> WorkSpacesDescribeWorkspacesPoolsResponse:
        client = self._require_client()
        return await self._execute(client.describe_workspaces_pools, request, WorkSpacesDescribeWorkspacesPoolsResponse)

    async def disassociate_connection_alias(
        self,
        request: WorkSpacesDisassociateConnectionAliasRequest,
    ) -> WorkSpacesDisassociateConnectionAliasResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_connection_alias, request, WorkSpacesDisassociateConnectionAliasResponse)

    async def disassociate_ip_groups(
        self,
        request: WorkSpacesDisassociateIpGroupsRequest,
    ) -> WorkSpacesDisassociateIpGroupsResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_ip_groups, request, WorkSpacesDisassociateIpGroupsResponse)

    async def disassociate_workspace_application(
        self,
        request: WorkSpacesDisassociateWorkspaceApplicationRequest,
    ) -> WorkSpacesDisassociateWorkspaceApplicationResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_workspace_application, request, WorkSpacesDisassociateWorkspaceApplicationResponse)

    async def get_account_link(
        self,
        request: WorkSpacesGetAccountLinkRequest | None = None,
    ) -> WorkSpacesGetAccountLinkResponse:
        client = self._require_client()
        return await self._execute(client.get_account_link, request, WorkSpacesGetAccountLinkResponse)

    async def import_client_branding(
        self,
        request: WorkSpacesImportClientBrandingRequest,
    ) -> WorkSpacesImportClientBrandingResponse:
        client = self._require_client()
        return await self._execute(client.import_client_branding, request, WorkSpacesImportClientBrandingResponse)

    async def import_custom_workspace_image(
        self,
        request: WorkSpacesImportCustomWorkspaceImageRequest,
    ) -> WorkSpacesImportCustomWorkspaceImageResponse:
        client = self._require_client()
        return await self._execute(client.import_custom_workspace_image, request, WorkSpacesImportCustomWorkspaceImageResponse)

    async def import_workspace_image(
        self,
        request: WorkSpacesImportWorkspaceImageRequest,
    ) -> WorkSpacesImportWorkspaceImageResponse:
        client = self._require_client()
        return await self._execute(client.import_workspace_image, request, WorkSpacesImportWorkspaceImageResponse)

    async def list_account_links(
        self,
        request: WorkSpacesListAccountLinksRequest | None = None,
    ) -> WorkSpacesListAccountLinksResponse:
        client = self._require_client()
        return await self._execute(client.list_account_links, request, WorkSpacesListAccountLinksResponse)

    async def list_account_links_paginated(
        self,
        request: WorkSpacesListAccountLinksRequest | None = None,
    ) -> list[WorkSpacesListAccountLinksResponse]:
        return await self._paginate('list_account_links', request, WorkSpacesListAccountLinksResponse)

    async def list_available_management_cidr_ranges(
        self,
        request: WorkSpacesListAvailableManagementCidrRangesRequest,
    ) -> WorkSpacesListAvailableManagementCidrRangesResponse:
        client = self._require_client()
        return await self._execute(client.list_available_management_cidr_ranges, request, WorkSpacesListAvailableManagementCidrRangesResponse)

    async def list_available_management_cidr_ranges_paginated(
        self,
        request: WorkSpacesListAvailableManagementCidrRangesRequest,
    ) -> list[WorkSpacesListAvailableManagementCidrRangesResponse]:
        return await self._paginate('list_available_management_cidr_ranges', request, WorkSpacesListAvailableManagementCidrRangesResponse)

    async def migrate_workspace(
        self,
        request: WorkSpacesMigrateWorkspaceRequest,
    ) -> WorkSpacesMigrateWorkspaceResponse:
        client = self._require_client()
        return await self._execute(client.migrate_workspace, request, WorkSpacesMigrateWorkspaceResponse)

    async def modify_account(
        self,
        request: WorkSpacesModifyAccountRequest | None = None,
    ) -> WorkSpacesModifyAccountResponse:
        client = self._require_client()
        return await self._execute(client.modify_account, request, WorkSpacesModifyAccountResponse)

    async def modify_certificate_based_auth_properties(
        self,
        request: WorkSpacesModifyCertificateBasedAuthPropertiesRequest,
    ) -> WorkSpacesModifyCertificateBasedAuthPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.modify_certificate_based_auth_properties, request, WorkSpacesModifyCertificateBasedAuthPropertiesResponse)

    async def modify_client_properties(
        self,
        request: WorkSpacesModifyClientPropertiesRequest,
    ) -> WorkSpacesModifyClientPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.modify_client_properties, request, WorkSpacesModifyClientPropertiesResponse)

    async def modify_endpoint_encryption_mode(
        self,
        request: WorkSpacesModifyEndpointEncryptionModeRequest,
    ) -> WorkSpacesModifyEndpointEncryptionModeResponse:
        client = self._require_client()
        return await self._execute(client.modify_endpoint_encryption_mode, request, WorkSpacesModifyEndpointEncryptionModeResponse)

    async def modify_saml_properties(
        self,
        request: WorkSpacesModifySamlPropertiesRequest,
    ) -> WorkSpacesModifySamlPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.modify_saml_properties, request, WorkSpacesModifySamlPropertiesResponse)

    async def modify_selfservice_permissions(
        self,
        request: WorkSpacesModifySelfservicePermissionsRequest,
    ) -> WorkSpacesModifySelfservicePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.modify_selfservice_permissions, request, WorkSpacesModifySelfservicePermissionsResponse)

    async def modify_streaming_properties(
        self,
        request: WorkSpacesModifyStreamingPropertiesRequest,
    ) -> WorkSpacesModifyStreamingPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.modify_streaming_properties, request, WorkSpacesModifyStreamingPropertiesResponse)

    async def modify_workspace_access_properties(
        self,
        request: WorkSpacesModifyWorkspaceAccessPropertiesRequest,
    ) -> WorkSpacesModifyWorkspaceAccessPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.modify_workspace_access_properties, request, WorkSpacesModifyWorkspaceAccessPropertiesResponse)

    async def modify_workspace_creation_properties(
        self,
        request: WorkSpacesModifyWorkspaceCreationPropertiesRequest,
    ) -> WorkSpacesModifyWorkspaceCreationPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.modify_workspace_creation_properties, request, WorkSpacesModifyWorkspaceCreationPropertiesResponse)

    async def modify_workspace_properties(
        self,
        request: WorkSpacesModifyWorkspacePropertiesRequest,
    ) -> WorkSpacesModifyWorkspacePropertiesResponse:
        client = self._require_client()
        return await self._execute(client.modify_workspace_properties, request, WorkSpacesModifyWorkspacePropertiesResponse)

    async def modify_workspace_state(
        self,
        request: WorkSpacesModifyWorkspaceStateRequest,
    ) -> WorkSpacesModifyWorkspaceStateResponse:
        client = self._require_client()
        return await self._execute(client.modify_workspace_state, request, WorkSpacesModifyWorkspaceStateResponse)

    async def reboot_workspaces(
        self,
        request: WorkSpacesRebootWorkspacesRequest,
    ) -> WorkSpacesRebootWorkspacesResponse:
        client = self._require_client()
        return await self._execute(client.reboot_workspaces, request, WorkSpacesRebootWorkspacesResponse)

    async def rebuild_workspaces(
        self,
        request: WorkSpacesRebuildWorkspacesRequest,
    ) -> WorkSpacesRebuildWorkspacesResponse:
        client = self._require_client()
        return await self._execute(client.rebuild_workspaces, request, WorkSpacesRebuildWorkspacesResponse)

    async def register_workspace_directory(
        self,
        request: WorkSpacesRegisterWorkspaceDirectoryRequest | None = None,
    ) -> WorkSpacesRegisterWorkspaceDirectoryResponse:
        client = self._require_client()
        return await self._execute(client.register_workspace_directory, request, WorkSpacesRegisterWorkspaceDirectoryResponse)

    async def reject_account_link_invitation(
        self,
        request: WorkSpacesRejectAccountLinkInvitationRequest,
    ) -> WorkSpacesRejectAccountLinkInvitationResponse:
        client = self._require_client()
        return await self._execute(client.reject_account_link_invitation, request, WorkSpacesRejectAccountLinkInvitationResponse)

    async def restore_workspace(
        self,
        request: WorkSpacesRestoreWorkspaceRequest,
    ) -> WorkSpacesRestoreWorkspaceResponse:
        client = self._require_client()
        return await self._execute(client.restore_workspace, request, WorkSpacesRestoreWorkspaceResponse)

    async def revoke_ip_rules(
        self,
        request: WorkSpacesRevokeIpRulesRequest,
    ) -> WorkSpacesRevokeIpRulesResponse:
        client = self._require_client()
        return await self._execute(client.revoke_ip_rules, request, WorkSpacesRevokeIpRulesResponse)

    async def start_workspaces(
        self,
        request: WorkSpacesStartWorkspacesRequest,
    ) -> WorkSpacesStartWorkspacesResponse:
        client = self._require_client()
        return await self._execute(client.start_workspaces, request, WorkSpacesStartWorkspacesResponse)

    async def start_workspaces_pool(
        self,
        request: WorkSpacesStartWorkspacesPoolRequest,
    ) -> WorkSpacesStartWorkspacesPoolResponse:
        client = self._require_client()
        return await self._execute(client.start_workspaces_pool, request, WorkSpacesStartWorkspacesPoolResponse)

    async def stop_workspaces(
        self,
        request: WorkSpacesStopWorkspacesRequest,
    ) -> WorkSpacesStopWorkspacesResponse:
        client = self._require_client()
        return await self._execute(client.stop_workspaces, request, WorkSpacesStopWorkspacesResponse)

    async def stop_workspaces_pool(
        self,
        request: WorkSpacesStopWorkspacesPoolRequest,
    ) -> WorkSpacesStopWorkspacesPoolResponse:
        client = self._require_client()
        return await self._execute(client.stop_workspaces_pool, request, WorkSpacesStopWorkspacesPoolResponse)

    async def terminate_workspaces(
        self,
        request: WorkSpacesTerminateWorkspacesRequest,
    ) -> WorkSpacesTerminateWorkspacesResponse:
        client = self._require_client()
        return await self._execute(client.terminate_workspaces, request, WorkSpacesTerminateWorkspacesResponse)

    async def terminate_workspaces_pool(
        self,
        request: WorkSpacesTerminateWorkspacesPoolRequest,
    ) -> WorkSpacesTerminateWorkspacesPoolResponse:
        client = self._require_client()
        return await self._execute(client.terminate_workspaces_pool, request, WorkSpacesTerminateWorkspacesPoolResponse)

    async def terminate_workspaces_pool_session(
        self,
        request: WorkSpacesTerminateWorkspacesPoolSessionRequest,
    ) -> WorkSpacesTerminateWorkspacesPoolSessionResponse:
        client = self._require_client()
        return await self._execute(client.terminate_workspaces_pool_session, request, WorkSpacesTerminateWorkspacesPoolSessionResponse)

    async def update_connect_client_add_in(
        self,
        request: WorkSpacesUpdateConnectClientAddInRequest,
    ) -> WorkSpacesUpdateConnectClientAddInResponse:
        client = self._require_client()
        return await self._execute(client.update_connect_client_add_in, request, WorkSpacesUpdateConnectClientAddInResponse)

    async def update_connection_alias_permission(
        self,
        request: WorkSpacesUpdateConnectionAliasPermissionRequest,
    ) -> WorkSpacesUpdateConnectionAliasPermissionResponse:
        client = self._require_client()
        return await self._execute(client.update_connection_alias_permission, request, WorkSpacesUpdateConnectionAliasPermissionResponse)

    async def update_rules_of_ip_group(
        self,
        request: WorkSpacesUpdateRulesOfIpGroupRequest,
    ) -> WorkSpacesUpdateRulesOfIpGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_rules_of_ip_group, request, WorkSpacesUpdateRulesOfIpGroupResponse)

    async def update_workspace_bundle(
        self,
        request: WorkSpacesUpdateWorkspaceBundleRequest | None = None,
    ) -> WorkSpacesUpdateWorkspaceBundleResponse:
        client = self._require_client()
        return await self._execute(client.update_workspace_bundle, request, WorkSpacesUpdateWorkspaceBundleResponse)

    async def update_workspace_image_permission(
        self,
        request: WorkSpacesUpdateWorkspaceImagePermissionRequest,
    ) -> WorkSpacesUpdateWorkspaceImagePermissionResponse:
        client = self._require_client()
        return await self._execute(client.update_workspace_image_permission, request, WorkSpacesUpdateWorkspaceImagePermissionResponse)

    async def update_workspaces_pool(
        self,
        request: WorkSpacesUpdateWorkspacesPoolRequest,
    ) -> WorkSpacesUpdateWorkspacesPoolResponse:
        client = self._require_client()
        return await self._execute(client.update_workspaces_pool, request, WorkSpacesUpdateWorkspacesPoolResponse)
