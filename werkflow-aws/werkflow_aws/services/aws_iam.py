from werkflow_aws.models.iam import (
    IAMAddUserToGroupRequest,
    IAMAddUserToGroupResponse,
    IAMAttachRolePolicyRequest,
    IAMAttachRolePolicyResponse,
    IAMAttachUserPolicyRequest,
    IAMAttachUserPolicyResponse,
    IAMCreateAccessKeyRequest,
    IAMCreateAccessKeyResponse,
    IAMCreateGroupRequest,
    IAMCreateGroupResponse,
    IAMCreateInstanceProfileRequest,
    IAMCreateInstanceProfileResponse,
    IAMCreatePolicyRequest,
    IAMCreatePolicyResponse,
    IAMCreatePolicyVersionRequest,
    IAMCreatePolicyVersionResponse,
    IAMCreateRoleRequest,
    IAMCreateRoleResponse,
    IAMCreateUserRequest,
    IAMCreateUserResponse,
    IAMDeleteAccessKeyRequest,
    IAMDeleteAccessKeyResponse,
    IAMDeleteGroupRequest,
    IAMDeleteGroupResponse,
    IAMDeleteInstanceProfileRequest,
    IAMDeleteInstanceProfileResponse,
    IAMDeletePolicyRequest,
    IAMDeletePolicyResponse,
    IAMDeletePolicyVersionRequest,
    IAMDeletePolicyVersionResponse,
    IAMDeleteRolePolicyRequest,
    IAMDeleteRolePolicyResponse,
    IAMDeleteRoleRequest,
    IAMDeleteRoleResponse,
    IAMDeleteUserRequest,
    IAMDeleteUserResponse,
    IAMDetachRolePolicyRequest,
    IAMDetachRolePolicyResponse,
    IAMDetachUserPolicyRequest,
    IAMDetachUserPolicyResponse,
    IAMGetGroupRequest,
    IAMGetGroupResponse,
    IAMGetInstanceProfileRequest,
    IAMGetInstanceProfileResponse,
    IAMGetPolicyRequest,
    IAMGetPolicyResponse,
    IAMGetPolicyVersionRequest,
    IAMGetPolicyVersionResponse,
    IAMGetRolePolicyRequest,
    IAMGetRolePolicyResponse,
    IAMGetRoleRequest,
    IAMGetRoleResponse,
    IAMGetUserRequest,
    IAMGetUserResponse,
    IAMListAccessKeysRequest,
    IAMListAccessKeysResponse,
    IAMListAttachedRolePoliciesRequest,
    IAMListAttachedRolePoliciesResponse,
    IAMListAttachedUserPoliciesRequest,
    IAMListAttachedUserPoliciesResponse,
    IAMListGroupsRequest,
    IAMListGroupsResponse,
    IAMListInstanceProfilesRequest,
    IAMListInstanceProfilesResponse,
    IAMListPoliciesRequest,
    IAMListPoliciesResponse,
    IAMListPolicyVersionsRequest,
    IAMListPolicyVersionsResponse,
    IAMListRolePoliciesRequest,
    IAMListRolePoliciesResponse,
    IAMListRolesRequest,
    IAMListRolesResponse,
    IAMListUsersRequest,
    IAMListUsersResponse,
    IAMPutRolePolicyRequest,
    IAMPutRolePolicyResponse,
    IAMRemoveUserFromGroupRequest,
    IAMRemoveUserFromGroupResponse,
    IAMUpdateAssumeRolePolicyRequest,
    IAMUpdateAssumeRolePolicyResponse,
)
from werkflow_aws.types.iam_client import IAMClient
from .base import AWSBaseService
from werkflow_aws.models.iam import (
    IAMAcceptDelegationRequestRequest,
    IAMAcceptDelegationRequestResponse,
    IAMAcquireRoleRequest,
    IAMAcquireRoleResponse,
    IAMAddClientIDToOpenIDConnectProviderRequest,
    IAMAddClientIDToOpenIDConnectProviderResponse,
    IAMAddRoleToInstanceProfileRequest,
    IAMAddRoleToInstanceProfileResponse,
    IAMAssociateDelegationRequestRequest,
    IAMAssociateDelegationRequestResponse,
    IAMAttachGroupPolicyRequest,
    IAMAttachGroupPolicyResponse,
    IAMChangePasswordRequest,
    IAMChangePasswordResponse,
    IAMCreateAccountAliasRequest,
    IAMCreateAccountAliasResponse,
    IAMCreateDelegationRequestRequest,
    IAMCreateDelegationRequestResponse,
    IAMCreateLoginProfileRequest,
    IAMCreateLoginProfileResponse,
    IAMCreateOpenIDConnectProviderRequest,
    IAMCreateOpenIDConnectProviderResponse,
    IAMCreateSAMLProviderRequest,
    IAMCreateSAMLProviderResponse,
    IAMCreateServiceLinkedRoleRequest,
    IAMCreateServiceLinkedRoleResponse,
    IAMCreateServiceSpecificCredentialRequest,
    IAMCreateServiceSpecificCredentialResponse,
    IAMCreateVirtualMFADeviceRequest,
    IAMCreateVirtualMFADeviceResponse,
    IAMDeactivateMFADeviceRequest,
    IAMDeactivateMFADeviceResponse,
    IAMDeleteAccountAliasRequest,
    IAMDeleteAccountAliasResponse,
    IAMDeleteAccountPasswordPolicyRequest,
    IAMDeleteAccountPasswordPolicyResponse,
    IAMDeleteGroupPolicyRequest,
    IAMDeleteGroupPolicyResponse,
    IAMDeleteLoginProfileRequest,
    IAMDeleteLoginProfileResponse,
    IAMDeleteOpenIDConnectProviderRequest,
    IAMDeleteOpenIDConnectProviderResponse,
    IAMDeleteRolePermissionsBoundaryRequest,
    IAMDeleteRolePermissionsBoundaryResponse,
    IAMDeleteSAMLProviderRequest,
    IAMDeleteSAMLProviderResponse,
    IAMDeleteSSHPublicKeyRequest,
    IAMDeleteSSHPublicKeyResponse,
    IAMDeleteServerCertificateRequest,
    IAMDeleteServerCertificateResponse,
    IAMDeleteServiceLinkedRoleRequest,
    IAMDeleteServiceLinkedRoleResponse,
    IAMDeleteServiceSpecificCredentialRequest,
    IAMDeleteServiceSpecificCredentialResponse,
    IAMDeleteSigningCertificateRequest,
    IAMDeleteSigningCertificateResponse,
    IAMDeleteUserPermissionsBoundaryRequest,
    IAMDeleteUserPermissionsBoundaryResponse,
    IAMDeleteUserPolicyRequest,
    IAMDeleteUserPolicyResponse,
    IAMDeleteVirtualMFADeviceRequest,
    IAMDeleteVirtualMFADeviceResponse,
    IAMDetachGroupPolicyRequest,
    IAMDetachGroupPolicyResponse,
    IAMDisableOrganizationsRootCredentialsManagementRequest,
    IAMDisableOrganizationsRootCredentialsManagementResponse,
    IAMDisableOrganizationsRootSessionsRequest,
    IAMDisableOrganizationsRootSessionsResponse,
    IAMDisableOutboundWebIdentityFederationRequest,
    IAMDisableOutboundWebIdentityFederationResponse,
    IAMEnableMFADeviceRequest,
    IAMEnableMFADeviceResponse,
    IAMEnableOrganizationsRootCredentialsManagementRequest,
    IAMEnableOrganizationsRootCredentialsManagementResponse,
    IAMEnableOrganizationsRootSessionsRequest,
    IAMEnableOrganizationsRootSessionsResponse,
    IAMEnableOutboundWebIdentityFederationRequest,
    IAMEnableOutboundWebIdentityFederationResponse,
    IAMGenerateCredentialReportRequest,
    IAMGenerateCredentialReportResponse,
    IAMGenerateOrganizationsAccessReportRequest,
    IAMGenerateOrganizationsAccessReportResponse,
    IAMGenerateServiceLastAccessedDetailsRequest,
    IAMGenerateServiceLastAccessedDetailsResponse,
    IAMGetAccessKeyLastUsedRequest,
    IAMGetAccessKeyLastUsedResponse,
    IAMGetAccountAuthorizationDetailsRequest,
    IAMGetAccountAuthorizationDetailsResponse,
    IAMGetAccountPasswordPolicyRequest,
    IAMGetAccountPasswordPolicyResponse,
    IAMGetAccountPropertiesRequest,
    IAMGetAccountPropertiesResponse,
    IAMGetAccountSummaryRequest,
    IAMGetAccountSummaryResponse,
    IAMGetContextKeysForCustomPolicyRequest,
    IAMGetContextKeysForCustomPolicyResponse,
    IAMGetContextKeysForPrincipalPolicyRequest,
    IAMGetContextKeysForPrincipalPolicyResponse,
    IAMGetCredentialReportRequest,
    IAMGetCredentialReportResponse,
    IAMGetDelegationRequestRequest,
    IAMGetDelegationRequestResponse,
    IAMGetGroupPolicyRequest,
    IAMGetGroupPolicyResponse,
    IAMGetHumanReadableSummaryRequest,
    IAMGetHumanReadableSummaryResponse,
    IAMGetLoginProfileRequest,
    IAMGetLoginProfileResponse,
    IAMGetMFADeviceRequest,
    IAMGetMFADeviceResponse,
    IAMGetOpenIDConnectProviderRequest,
    IAMGetOpenIDConnectProviderResponse,
    IAMGetOrganizationsAccessReportRequest,
    IAMGetOrganizationsAccessReportResponse,
    IAMGetOutboundWebIdentityFederationInfoRequest,
    IAMGetOutboundWebIdentityFederationInfoResponse,
    IAMGetRoleTemplateVersionRequest,
    IAMGetRoleTemplateVersionResponse,
    IAMGetSAMLProviderRequest,
    IAMGetSAMLProviderResponse,
    IAMGetSSHPublicKeyRequest,
    IAMGetSSHPublicKeyResponse,
    IAMGetServerCertificateRequest,
    IAMGetServerCertificateResponse,
    IAMGetServiceLastAccessedDetailsRequest,
    IAMGetServiceLastAccessedDetailsResponse,
    IAMGetServiceLastAccessedDetailsWithEntitiesRequest,
    IAMGetServiceLastAccessedDetailsWithEntitiesResponse,
    IAMGetServiceLinkedRoleDeletionStatusRequest,
    IAMGetServiceLinkedRoleDeletionStatusResponse,
    IAMGetUserPolicyRequest,
    IAMGetUserPolicyResponse,
    IAMListAccountAliasesRequest,
    IAMListAccountAliasesResponse,
    IAMListAttachedGroupPoliciesRequest,
    IAMListAttachedGroupPoliciesResponse,
    IAMListDelegationRequestsRequest,
    IAMListDelegationRequestsResponse,
    IAMListEntitiesForPolicyRequest,
    IAMListEntitiesForPolicyResponse,
    IAMListGroupPoliciesRequest,
    IAMListGroupPoliciesResponse,
    IAMListGroupsForUserRequest,
    IAMListGroupsForUserResponse,
    IAMListInstanceProfileTagsRequest,
    IAMListInstanceProfileTagsResponse,
    IAMListInstanceProfilesForRoleRequest,
    IAMListInstanceProfilesForRoleResponse,
    IAMListMFADeviceTagsRequest,
    IAMListMFADeviceTagsResponse,
    IAMListMFADevicesRequest,
    IAMListMFADevicesResponse,
    IAMListOpenIDConnectProviderTagsRequest,
    IAMListOpenIDConnectProviderTagsResponse,
    IAMListOpenIDConnectProvidersRequest,
    IAMListOpenIDConnectProvidersResponse,
    IAMListOrganizationsFeaturesRequest,
    IAMListOrganizationsFeaturesResponse,
    IAMListPoliciesGrantingServiceAccessRequest,
    IAMListPoliciesGrantingServiceAccessResponse,
    IAMListPolicyTagsRequest,
    IAMListPolicyTagsResponse,
    IAMListRoleTagsRequest,
    IAMListRoleTagsResponse,
    IAMListSAMLProviderTagsRequest,
    IAMListSAMLProviderTagsResponse,
    IAMListSAMLProvidersRequest,
    IAMListSAMLProvidersResponse,
    IAMListSSHPublicKeysRequest,
    IAMListSSHPublicKeysResponse,
    IAMListServerCertificateTagsRequest,
    IAMListServerCertificateTagsResponse,
    IAMListServerCertificatesRequest,
    IAMListServerCertificatesResponse,
    IAMListServiceSpecificCredentialsRequest,
    IAMListServiceSpecificCredentialsResponse,
    IAMListSigningCertificatesRequest,
    IAMListSigningCertificatesResponse,
    IAMListUserPoliciesRequest,
    IAMListUserPoliciesResponse,
    IAMListUserTagsRequest,
    IAMListUserTagsResponse,
    IAMListVirtualMFADevicesRequest,
    IAMListVirtualMFADevicesResponse,
    IAMPutAccountPropertiesRequest,
    IAMPutAccountPropertiesResponse,
    IAMPutGroupPolicyRequest,
    IAMPutGroupPolicyResponse,
    IAMPutRolePermissionsBoundaryRequest,
    IAMPutRolePermissionsBoundaryResponse,
    IAMPutUserPermissionsBoundaryRequest,
    IAMPutUserPermissionsBoundaryResponse,
    IAMPutUserPolicyRequest,
    IAMPutUserPolicyResponse,
    IAMRejectDelegationRequestRequest,
    IAMRejectDelegationRequestResponse,
    IAMRemoveClientIDFromOpenIDConnectProviderRequest,
    IAMRemoveClientIDFromOpenIDConnectProviderResponse,
    IAMRemoveRoleFromInstanceProfileRequest,
    IAMRemoveRoleFromInstanceProfileResponse,
    IAMResetServiceSpecificCredentialRequest,
    IAMResetServiceSpecificCredentialResponse,
    IAMResyncMFADeviceRequest,
    IAMResyncMFADeviceResponse,
    IAMSendDelegationTokenRequest,
    IAMSendDelegationTokenResponse,
    IAMSetDefaultPolicyVersionRequest,
    IAMSetDefaultPolicyVersionResponse,
    IAMSetSecurityTokenServicePreferencesRequest,
    IAMSetSecurityTokenServicePreferencesResponse,
    IAMSimulateCustomPolicyRequest,
    IAMSimulateCustomPolicyResponse,
    IAMSimulatePrincipalPolicyRequest,
    IAMSimulatePrincipalPolicyResponse,
    IAMTagInstanceProfileRequest,
    IAMTagInstanceProfileResponse,
    IAMTagMFADeviceRequest,
    IAMTagMFADeviceResponse,
    IAMTagOpenIDConnectProviderRequest,
    IAMTagOpenIDConnectProviderResponse,
    IAMTagPolicyRequest,
    IAMTagPolicyResponse,
    IAMTagRoleRequest,
    IAMTagRoleResponse,
    IAMTagSAMLProviderRequest,
    IAMTagSAMLProviderResponse,
    IAMTagServerCertificateRequest,
    IAMTagServerCertificateResponse,
    IAMTagUserRequest,
    IAMTagUserResponse,
    IAMUntagInstanceProfileRequest,
    IAMUntagInstanceProfileResponse,
    IAMUntagMFADeviceRequest,
    IAMUntagMFADeviceResponse,
    IAMUntagOpenIDConnectProviderRequest,
    IAMUntagOpenIDConnectProviderResponse,
    IAMUntagPolicyRequest,
    IAMUntagPolicyResponse,
    IAMUntagRoleRequest,
    IAMUntagRoleResponse,
    IAMUntagSAMLProviderRequest,
    IAMUntagSAMLProviderResponse,
    IAMUntagServerCertificateRequest,
    IAMUntagServerCertificateResponse,
    IAMUntagUserRequest,
    IAMUntagUserResponse,
    IAMUpdateAccessKeyRequest,
    IAMUpdateAccessKeyResponse,
    IAMUpdateAccountPasswordPolicyRequest,
    IAMUpdateAccountPasswordPolicyResponse,
    IAMUpdateDelegationRequestRequest,
    IAMUpdateDelegationRequestResponse,
    IAMUpdateGroupRequest,
    IAMUpdateGroupResponse,
    IAMUpdateLoginProfileRequest,
    IAMUpdateLoginProfileResponse,
    IAMUpdateOpenIDConnectProviderRequest,
    IAMUpdateOpenIDConnectProviderResponse,
    IAMUpdateOpenIDConnectProviderThumbprintRequest,
    IAMUpdateOpenIDConnectProviderThumbprintResponse,
    IAMUpdateRoleDescriptionRequest,
    IAMUpdateRoleDescriptionResponse,
    IAMUpdateRoleRequest,
    IAMUpdateRoleResponse,
    IAMUpdateSAMLProviderRequest,
    IAMUpdateSAMLProviderResponse,
    IAMUpdateSSHPublicKeyRequest,
    IAMUpdateSSHPublicKeyResponse,
    IAMUpdateServerCertificateRequest,
    IAMUpdateServerCertificateResponse,
    IAMUpdateServiceSpecificCredentialRequest,
    IAMUpdateServiceSpecificCredentialResponse,
    IAMUpdateSigningCertificateRequest,
    IAMUpdateSigningCertificateResponse,
    IAMUpdateUserRequest,
    IAMUpdateUserResponse,
    IAMUploadSSHPublicKeyRequest,
    IAMUploadSSHPublicKeyResponse,
    IAMUploadServerCertificateRequest,
    IAMUploadServerCertificateResponse,
    IAMUploadSigningCertificateRequest,
    IAMUploadSigningCertificateResponse,
)


class AWSIAM(AWSBaseService[IAMClient]):
    service_name = 'IAM'
    boto3_service_name = 'iam'

    def __init__(self) -> None:
        super().__init__(
            service_name='IAM',
            boto3_service_name='iam',
        )

    async def list_users(
        self,
        request: IAMListUsersRequest | None = None,
    ) -> IAMListUsersResponse:
        client = self._require_client()
        return await self._execute(
            client.list_users,
            request or IAMListUsersRequest(),
            IAMListUsersResponse,
        )

    async def list_users_paginated(
        self,
        request: IAMListUsersRequest | None = None,
    ) -> list[IAMListUsersResponse]:
        return await self._paginate(
            'list_users',
            request or IAMListUsersRequest(),
            IAMListUsersResponse,
        )

    async def get_user(
        self,
        request: IAMGetUserRequest | None = None,
    ) -> IAMGetUserResponse:
        client = self._require_client()
        return await self._execute(
            client.get_user,
            request or IAMGetUserRequest(),
            IAMGetUserResponse,
        )

    async def create_user(
        self,
        request: IAMCreateUserRequest,
    ) -> IAMCreateUserResponse:
        client = self._require_client()
        return await self._execute(
            client.create_user,
            request,
            IAMCreateUserResponse,
        )

    async def delete_user(
        self,
        request: IAMDeleteUserRequest,
    ) -> IAMDeleteUserResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_user,
            request,
            IAMDeleteUserResponse,
        )

    async def list_access_keys(
        self,
        request: IAMListAccessKeysRequest | None = None,
    ) -> IAMListAccessKeysResponse:
        client = self._require_client()
        return await self._execute(
            client.list_access_keys,
            request or IAMListAccessKeysRequest(),
            IAMListAccessKeysResponse,
        )

    async def list_access_keys_paginated(
        self,
        request: IAMListAccessKeysRequest | None = None,
    ) -> list[IAMListAccessKeysResponse]:
        return await self._paginate(
            'list_access_keys',
            request or IAMListAccessKeysRequest(),
            IAMListAccessKeysResponse,
        )

    async def create_access_key(
        self,
        request: IAMCreateAccessKeyRequest | None = None,
    ) -> IAMCreateAccessKeyResponse:
        client = self._require_client()
        return await self._execute(
            client.create_access_key,
            request or IAMCreateAccessKeyRequest(),
            IAMCreateAccessKeyResponse,
        )

    async def delete_access_key(
        self,
        request: IAMDeleteAccessKeyRequest,
    ) -> IAMDeleteAccessKeyResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_access_key,
            request,
            IAMDeleteAccessKeyResponse,
        )

    async def list_roles(
        self,
        request: IAMListRolesRequest | None = None,
    ) -> IAMListRolesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_roles,
            request or IAMListRolesRequest(),
            IAMListRolesResponse,
        )

    async def list_roles_paginated(
        self,
        request: IAMListRolesRequest | None = None,
    ) -> list[IAMListRolesResponse]:
        return await self._paginate(
            'list_roles',
            request or IAMListRolesRequest(),
            IAMListRolesResponse,
        )

    async def get_role(
        self,
        request: IAMGetRoleRequest,
    ) -> IAMGetRoleResponse:
        client = self._require_client()
        return await self._execute(
            client.get_role,
            request,
            IAMGetRoleResponse,
        )

    async def create_role(
        self,
        request: IAMCreateRoleRequest,
    ) -> IAMCreateRoleResponse:
        client = self._require_client()
        return await self._execute(
            client.create_role,
            request,
            IAMCreateRoleResponse,
        )

    async def delete_role(
        self,
        request: IAMDeleteRoleRequest,
    ) -> IAMDeleteRoleResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_role,
            request,
            IAMDeleteRoleResponse,
        )

    async def update_assume_role_policy(
        self,
        request: IAMUpdateAssumeRolePolicyRequest,
    ) -> IAMUpdateAssumeRolePolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.update_assume_role_policy,
            request,
            IAMUpdateAssumeRolePolicyResponse,
        )

    async def attach_role_policy(
        self,
        request: IAMAttachRolePolicyRequest,
    ) -> IAMAttachRolePolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.attach_role_policy,
            request,
            IAMAttachRolePolicyResponse,
        )

    async def detach_role_policy(
        self,
        request: IAMDetachRolePolicyRequest,
    ) -> IAMDetachRolePolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.detach_role_policy,
            request,
            IAMDetachRolePolicyResponse,
        )

    async def list_attached_role_policies(
        self,
        request: IAMListAttachedRolePoliciesRequest,
    ) -> IAMListAttachedRolePoliciesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_attached_role_policies,
            request,
            IAMListAttachedRolePoliciesResponse,
        )

    async def list_attached_role_policies_paginated(
        self,
        request: IAMListAttachedRolePoliciesRequest,
    ) -> list[IAMListAttachedRolePoliciesResponse]:
        return await self._paginate(
            'list_attached_role_policies',
            request,
            IAMListAttachedRolePoliciesResponse,
        )

    async def put_role_policy(
        self,
        request: IAMPutRolePolicyRequest,
    ) -> IAMPutRolePolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.put_role_policy,
            request,
            IAMPutRolePolicyResponse,
        )

    async def get_role_policy(
        self,
        request: IAMGetRolePolicyRequest,
    ) -> IAMGetRolePolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.get_role_policy,
            request,
            IAMGetRolePolicyResponse,
        )

    async def delete_role_policy(
        self,
        request: IAMDeleteRolePolicyRequest,
    ) -> IAMDeleteRolePolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_role_policy,
            request,
            IAMDeleteRolePolicyResponse,
        )

    async def list_role_policies(
        self,
        request: IAMListRolePoliciesRequest,
    ) -> IAMListRolePoliciesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_role_policies,
            request,
            IAMListRolePoliciesResponse,
        )

    async def list_role_policies_paginated(
        self,
        request: IAMListRolePoliciesRequest,
    ) -> list[IAMListRolePoliciesResponse]:
        return await self._paginate(
            'list_role_policies',
            request,
            IAMListRolePoliciesResponse,
        )

    async def list_policies(
        self,
        request: IAMListPoliciesRequest | None = None,
    ) -> IAMListPoliciesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_policies,
            request or IAMListPoliciesRequest(),
            IAMListPoliciesResponse,
        )

    async def list_policies_paginated(
        self,
        request: IAMListPoliciesRequest | None = None,
    ) -> list[IAMListPoliciesResponse]:
        return await self._paginate(
            'list_policies',
            request or IAMListPoliciesRequest(),
            IAMListPoliciesResponse,
        )

    async def get_policy(
        self,
        request: IAMGetPolicyRequest,
    ) -> IAMGetPolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.get_policy,
            request,
            IAMGetPolicyResponse,
        )

    async def get_policy_version(
        self,
        request: IAMGetPolicyVersionRequest,
    ) -> IAMGetPolicyVersionResponse:
        client = self._require_client()
        return await self._execute(
            client.get_policy_version,
            request,
            IAMGetPolicyVersionResponse,
        )

    async def create_policy(
        self,
        request: IAMCreatePolicyRequest,
    ) -> IAMCreatePolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.create_policy,
            request,
            IAMCreatePolicyResponse,
        )

    async def delete_policy(
        self,
        request: IAMDeletePolicyRequest,
    ) -> IAMDeletePolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_policy,
            request,
            IAMDeletePolicyResponse,
        )

    async def list_policy_versions(
        self,
        request: IAMListPolicyVersionsRequest,
    ) -> IAMListPolicyVersionsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_policy_versions,
            request,
            IAMListPolicyVersionsResponse,
        )

    async def list_policy_versions_paginated(
        self,
        request: IAMListPolicyVersionsRequest,
    ) -> list[IAMListPolicyVersionsResponse]:
        return await self._paginate(
            'list_policy_versions',
            request,
            IAMListPolicyVersionsResponse,
        )

    async def create_policy_version(
        self,
        request: IAMCreatePolicyVersionRequest,
    ) -> IAMCreatePolicyVersionResponse:
        client = self._require_client()
        return await self._execute(
            client.create_policy_version,
            request,
            IAMCreatePolicyVersionResponse,
        )

    async def delete_policy_version(
        self,
        request: IAMDeletePolicyVersionRequest,
    ) -> IAMDeletePolicyVersionResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_policy_version,
            request,
            IAMDeletePolicyVersionResponse,
        )

    async def list_groups(
        self,
        request: IAMListGroupsRequest | None = None,
    ) -> IAMListGroupsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_groups,
            request or IAMListGroupsRequest(),
            IAMListGroupsResponse,
        )

    async def list_groups_paginated(
        self,
        request: IAMListGroupsRequest | None = None,
    ) -> list[IAMListGroupsResponse]:
        return await self._paginate(
            'list_groups',
            request or IAMListGroupsRequest(),
            IAMListGroupsResponse,
        )

    async def get_group(
        self,
        request: IAMGetGroupRequest,
    ) -> IAMGetGroupResponse:
        client = self._require_client()
        return await self._execute(
            client.get_group,
            request,
            IAMGetGroupResponse,
        )

    async def get_group_paginated(
        self,
        request: IAMGetGroupRequest,
    ) -> list[IAMGetGroupResponse]:
        return await self._paginate(
            'get_group',
            request,
            IAMGetGroupResponse,
        )

    async def create_group(
        self,
        request: IAMCreateGroupRequest,
    ) -> IAMCreateGroupResponse:
        client = self._require_client()
        return await self._execute(
            client.create_group,
            request,
            IAMCreateGroupResponse,
        )

    async def delete_group(
        self,
        request: IAMDeleteGroupRequest,
    ) -> IAMDeleteGroupResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_group,
            request,
            IAMDeleteGroupResponse,
        )

    async def add_user_to_group(
        self,
        request: IAMAddUserToGroupRequest,
    ) -> IAMAddUserToGroupResponse:
        client = self._require_client()
        return await self._execute(
            client.add_user_to_group,
            request,
            IAMAddUserToGroupResponse,
        )

    async def remove_user_from_group(
        self,
        request: IAMRemoveUserFromGroupRequest,
    ) -> IAMRemoveUserFromGroupResponse:
        client = self._require_client()
        return await self._execute(
            client.remove_user_from_group,
            request,
            IAMRemoveUserFromGroupResponse,
        )

    async def attach_user_policy(
        self,
        request: IAMAttachUserPolicyRequest,
    ) -> IAMAttachUserPolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.attach_user_policy,
            request,
            IAMAttachUserPolicyResponse,
        )

    async def detach_user_policy(
        self,
        request: IAMDetachUserPolicyRequest,
    ) -> IAMDetachUserPolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.detach_user_policy,
            request,
            IAMDetachUserPolicyResponse,
        )

    async def list_attached_user_policies(
        self,
        request: IAMListAttachedUserPoliciesRequest,
    ) -> IAMListAttachedUserPoliciesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_attached_user_policies,
            request,
            IAMListAttachedUserPoliciesResponse,
        )

    async def list_attached_user_policies_paginated(
        self,
        request: IAMListAttachedUserPoliciesRequest,
    ) -> list[IAMListAttachedUserPoliciesResponse]:
        return await self._paginate(
            'list_attached_user_policies',
            request,
            IAMListAttachedUserPoliciesResponse,
        )

    async def list_instance_profiles(
        self,
        request: IAMListInstanceProfilesRequest | None = None,
    ) -> IAMListInstanceProfilesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_instance_profiles,
            request or IAMListInstanceProfilesRequest(),
            IAMListInstanceProfilesResponse,
        )

    async def list_instance_profiles_paginated(
        self,
        request: IAMListInstanceProfilesRequest | None = None,
    ) -> list[IAMListInstanceProfilesResponse]:
        return await self._paginate(
            'list_instance_profiles',
            request or IAMListInstanceProfilesRequest(),
            IAMListInstanceProfilesResponse,
        )

    async def get_instance_profile(
        self,
        request: IAMGetInstanceProfileRequest,
    ) -> IAMGetInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(
            client.get_instance_profile,
            request,
            IAMGetInstanceProfileResponse,
        )

    async def create_instance_profile(
        self,
        request: IAMCreateInstanceProfileRequest,
    ) -> IAMCreateInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(
            client.create_instance_profile,
            request,
            IAMCreateInstanceProfileResponse,
        )

    async def delete_instance_profile(
        self,
        request: IAMDeleteInstanceProfileRequest,
    ) -> IAMDeleteInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_instance_profile,
            request,
            IAMDeleteInstanceProfileResponse,
        )

    async def accept_delegation_request(
        self,
        request: IAMAcceptDelegationRequestRequest,
    ) -> IAMAcceptDelegationRequestResponse:
        client = self._require_client()
        return await self._execute(client.accept_delegation_request, request, IAMAcceptDelegationRequestResponse)

    async def acquire_role(
        self,
        request: IAMAcquireRoleRequest,
    ) -> IAMAcquireRoleResponse:
        client = self._require_client()
        return await self._execute(client.acquire_role, request, IAMAcquireRoleResponse)

    async def add_client_id_to_open_id_connect_provider(
        self,
        request: IAMAddClientIDToOpenIDConnectProviderRequest,
    ) -> IAMAddClientIDToOpenIDConnectProviderResponse:
        client = self._require_client()
        return await self._execute(client.add_client_id_to_open_id_connect_provider, request, IAMAddClientIDToOpenIDConnectProviderResponse)

    async def add_role_to_instance_profile(
        self,
        request: IAMAddRoleToInstanceProfileRequest,
    ) -> IAMAddRoleToInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.add_role_to_instance_profile, request, IAMAddRoleToInstanceProfileResponse)

    async def associate_delegation_request(
        self,
        request: IAMAssociateDelegationRequestRequest,
    ) -> IAMAssociateDelegationRequestResponse:
        client = self._require_client()
        return await self._execute(client.associate_delegation_request, request, IAMAssociateDelegationRequestResponse)

    async def attach_group_policy(
        self,
        request: IAMAttachGroupPolicyRequest,
    ) -> IAMAttachGroupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.attach_group_policy, request, IAMAttachGroupPolicyResponse)

    async def change_password(
        self,
        request: IAMChangePasswordRequest,
    ) -> IAMChangePasswordResponse:
        client = self._require_client()
        return await self._execute(client.change_password, request, IAMChangePasswordResponse)

    async def create_account_alias(
        self,
        request: IAMCreateAccountAliasRequest,
    ) -> IAMCreateAccountAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_account_alias, request, IAMCreateAccountAliasResponse)

    async def create_delegation_request(
        self,
        request: IAMCreateDelegationRequestRequest,
    ) -> IAMCreateDelegationRequestResponse:
        client = self._require_client()
        return await self._execute(client.create_delegation_request, request, IAMCreateDelegationRequestResponse)

    async def create_login_profile(
        self,
        request: IAMCreateLoginProfileRequest | None = None,
    ) -> IAMCreateLoginProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_login_profile, request, IAMCreateLoginProfileResponse)

    async def create_open_id_connect_provider(
        self,
        request: IAMCreateOpenIDConnectProviderRequest,
    ) -> IAMCreateOpenIDConnectProviderResponse:
        client = self._require_client()
        return await self._execute(client.create_open_id_connect_provider, request, IAMCreateOpenIDConnectProviderResponse)

    async def create_saml_provider(
        self,
        request: IAMCreateSAMLProviderRequest,
    ) -> IAMCreateSAMLProviderResponse:
        client = self._require_client()
        return await self._execute(client.create_saml_provider, request, IAMCreateSAMLProviderResponse)

    async def create_service_linked_role(
        self,
        request: IAMCreateServiceLinkedRoleRequest,
    ) -> IAMCreateServiceLinkedRoleResponse:
        client = self._require_client()
        return await self._execute(client.create_service_linked_role, request, IAMCreateServiceLinkedRoleResponse)

    async def create_service_specific_credential(
        self,
        request: IAMCreateServiceSpecificCredentialRequest,
    ) -> IAMCreateServiceSpecificCredentialResponse:
        client = self._require_client()
        return await self._execute(client.create_service_specific_credential, request, IAMCreateServiceSpecificCredentialResponse)

    async def create_virtual_mfa_device(
        self,
        request: IAMCreateVirtualMFADeviceRequest,
    ) -> IAMCreateVirtualMFADeviceResponse:
        client = self._require_client()
        return await self._execute(client.create_virtual_mfa_device, request, IAMCreateVirtualMFADeviceResponse)

    async def deactivate_mfa_device(
        self,
        request: IAMDeactivateMFADeviceRequest,
    ) -> IAMDeactivateMFADeviceResponse:
        client = self._require_client()
        return await self._execute(client.deactivate_mfa_device, request, IAMDeactivateMFADeviceResponse)

    async def delete_account_alias(
        self,
        request: IAMDeleteAccountAliasRequest,
    ) -> IAMDeleteAccountAliasResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_alias, request, IAMDeleteAccountAliasResponse)

    async def delete_account_password_policy(
        self,
        request: IAMDeleteAccountPasswordPolicyRequest | None = None,
    ) -> IAMDeleteAccountPasswordPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_password_policy, request, IAMDeleteAccountPasswordPolicyResponse)

    async def delete_group_policy(
        self,
        request: IAMDeleteGroupPolicyRequest,
    ) -> IAMDeleteGroupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_group_policy, request, IAMDeleteGroupPolicyResponse)

    async def delete_login_profile(
        self,
        request: IAMDeleteLoginProfileRequest | None = None,
    ) -> IAMDeleteLoginProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_login_profile, request, IAMDeleteLoginProfileResponse)

    async def delete_open_id_connect_provider(
        self,
        request: IAMDeleteOpenIDConnectProviderRequest,
    ) -> IAMDeleteOpenIDConnectProviderResponse:
        client = self._require_client()
        return await self._execute(client.delete_open_id_connect_provider, request, IAMDeleteOpenIDConnectProviderResponse)

    async def delete_role_permissions_boundary(
        self,
        request: IAMDeleteRolePermissionsBoundaryRequest,
    ) -> IAMDeleteRolePermissionsBoundaryResponse:
        client = self._require_client()
        return await self._execute(client.delete_role_permissions_boundary, request, IAMDeleteRolePermissionsBoundaryResponse)

    async def delete_saml_provider(
        self,
        request: IAMDeleteSAMLProviderRequest,
    ) -> IAMDeleteSAMLProviderResponse:
        client = self._require_client()
        return await self._execute(client.delete_saml_provider, request, IAMDeleteSAMLProviderResponse)

    async def delete_ssh_public_key(
        self,
        request: IAMDeleteSSHPublicKeyRequest,
    ) -> IAMDeleteSSHPublicKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_ssh_public_key, request, IAMDeleteSSHPublicKeyResponse)

    async def delete_server_certificate(
        self,
        request: IAMDeleteServerCertificateRequest,
    ) -> IAMDeleteServerCertificateResponse:
        client = self._require_client()
        return await self._execute(client.delete_server_certificate, request, IAMDeleteServerCertificateResponse)

    async def delete_service_linked_role(
        self,
        request: IAMDeleteServiceLinkedRoleRequest,
    ) -> IAMDeleteServiceLinkedRoleResponse:
        client = self._require_client()
        return await self._execute(client.delete_service_linked_role, request, IAMDeleteServiceLinkedRoleResponse)

    async def delete_service_specific_credential(
        self,
        request: IAMDeleteServiceSpecificCredentialRequest,
    ) -> IAMDeleteServiceSpecificCredentialResponse:
        client = self._require_client()
        return await self._execute(client.delete_service_specific_credential, request, IAMDeleteServiceSpecificCredentialResponse)

    async def delete_signing_certificate(
        self,
        request: IAMDeleteSigningCertificateRequest,
    ) -> IAMDeleteSigningCertificateResponse:
        client = self._require_client()
        return await self._execute(client.delete_signing_certificate, request, IAMDeleteSigningCertificateResponse)

    async def delete_user_permissions_boundary(
        self,
        request: IAMDeleteUserPermissionsBoundaryRequest,
    ) -> IAMDeleteUserPermissionsBoundaryResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_permissions_boundary, request, IAMDeleteUserPermissionsBoundaryResponse)

    async def delete_user_policy(
        self,
        request: IAMDeleteUserPolicyRequest,
    ) -> IAMDeleteUserPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_policy, request, IAMDeleteUserPolicyResponse)

    async def delete_virtual_mfa_device(
        self,
        request: IAMDeleteVirtualMFADeviceRequest,
    ) -> IAMDeleteVirtualMFADeviceResponse:
        client = self._require_client()
        return await self._execute(client.delete_virtual_mfa_device, request, IAMDeleteVirtualMFADeviceResponse)

    async def detach_group_policy(
        self,
        request: IAMDetachGroupPolicyRequest,
    ) -> IAMDetachGroupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.detach_group_policy, request, IAMDetachGroupPolicyResponse)

    async def disable_organizations_root_credentials_management(
        self,
        request: IAMDisableOrganizationsRootCredentialsManagementRequest | None = None,
    ) -> IAMDisableOrganizationsRootCredentialsManagementResponse:
        client = self._require_client()
        return await self._execute(client.disable_organizations_root_credentials_management, request, IAMDisableOrganizationsRootCredentialsManagementResponse)

    async def disable_organizations_root_sessions(
        self,
        request: IAMDisableOrganizationsRootSessionsRequest | None = None,
    ) -> IAMDisableOrganizationsRootSessionsResponse:
        client = self._require_client()
        return await self._execute(client.disable_organizations_root_sessions, request, IAMDisableOrganizationsRootSessionsResponse)

    async def disable_outbound_web_identity_federation(
        self,
        request: IAMDisableOutboundWebIdentityFederationRequest | None = None,
    ) -> IAMDisableOutboundWebIdentityFederationResponse:
        client = self._require_client()
        return await self._execute(client.disable_outbound_web_identity_federation, request, IAMDisableOutboundWebIdentityFederationResponse)

    async def enable_mfa_device(
        self,
        request: IAMEnableMFADeviceRequest,
    ) -> IAMEnableMFADeviceResponse:
        client = self._require_client()
        return await self._execute(client.enable_mfa_device, request, IAMEnableMFADeviceResponse)

    async def enable_organizations_root_credentials_management(
        self,
        request: IAMEnableOrganizationsRootCredentialsManagementRequest | None = None,
    ) -> IAMEnableOrganizationsRootCredentialsManagementResponse:
        client = self._require_client()
        return await self._execute(client.enable_organizations_root_credentials_management, request, IAMEnableOrganizationsRootCredentialsManagementResponse)

    async def enable_organizations_root_sessions(
        self,
        request: IAMEnableOrganizationsRootSessionsRequest | None = None,
    ) -> IAMEnableOrganizationsRootSessionsResponse:
        client = self._require_client()
        return await self._execute(client.enable_organizations_root_sessions, request, IAMEnableOrganizationsRootSessionsResponse)

    async def enable_outbound_web_identity_federation(
        self,
        request: IAMEnableOutboundWebIdentityFederationRequest | None = None,
    ) -> IAMEnableOutboundWebIdentityFederationResponse:
        client = self._require_client()
        return await self._execute(client.enable_outbound_web_identity_federation, request, IAMEnableOutboundWebIdentityFederationResponse)

    async def generate_credential_report(
        self,
        request: IAMGenerateCredentialReportRequest | None = None,
    ) -> IAMGenerateCredentialReportResponse:
        client = self._require_client()
        return await self._execute(client.generate_credential_report, request, IAMGenerateCredentialReportResponse)

    async def generate_organizations_access_report(
        self,
        request: IAMGenerateOrganizationsAccessReportRequest,
    ) -> IAMGenerateOrganizationsAccessReportResponse:
        client = self._require_client()
        return await self._execute(client.generate_organizations_access_report, request, IAMGenerateOrganizationsAccessReportResponse)

    async def generate_service_last_accessed_details(
        self,
        request: IAMGenerateServiceLastAccessedDetailsRequest,
    ) -> IAMGenerateServiceLastAccessedDetailsResponse:
        client = self._require_client()
        return await self._execute(client.generate_service_last_accessed_details, request, IAMGenerateServiceLastAccessedDetailsResponse)

    async def get_access_key_last_used(
        self,
        request: IAMGetAccessKeyLastUsedRequest,
    ) -> IAMGetAccessKeyLastUsedResponse:
        client = self._require_client()
        return await self._execute(client.get_access_key_last_used, request, IAMGetAccessKeyLastUsedResponse)

    async def get_account_authorization_details(
        self,
        request: IAMGetAccountAuthorizationDetailsRequest | None = None,
    ) -> IAMGetAccountAuthorizationDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_account_authorization_details, request, IAMGetAccountAuthorizationDetailsResponse)

    async def get_account_authorization_details_paginated(
        self,
        request: IAMGetAccountAuthorizationDetailsRequest | None = None,
    ) -> list[IAMGetAccountAuthorizationDetailsResponse]:
        return await self._paginate('get_account_authorization_details', request, IAMGetAccountAuthorizationDetailsResponse)

    async def get_account_password_policy(
        self,
        request: IAMGetAccountPasswordPolicyRequest | None = None,
    ) -> IAMGetAccountPasswordPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_account_password_policy, request, IAMGetAccountPasswordPolicyResponse)

    async def get_account_properties(
        self,
        request: IAMGetAccountPropertiesRequest | None = None,
    ) -> IAMGetAccountPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.get_account_properties, request, IAMGetAccountPropertiesResponse)

    async def get_account_summary(
        self,
        request: IAMGetAccountSummaryRequest | None = None,
    ) -> IAMGetAccountSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_account_summary, request, IAMGetAccountSummaryResponse)

    async def get_context_keys_for_custom_policy(
        self,
        request: IAMGetContextKeysForCustomPolicyRequest,
    ) -> IAMGetContextKeysForCustomPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_context_keys_for_custom_policy, request, IAMGetContextKeysForCustomPolicyResponse)

    async def get_context_keys_for_principal_policy(
        self,
        request: IAMGetContextKeysForPrincipalPolicyRequest,
    ) -> IAMGetContextKeysForPrincipalPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_context_keys_for_principal_policy, request, IAMGetContextKeysForPrincipalPolicyResponse)

    async def get_credential_report(
        self,
        request: IAMGetCredentialReportRequest | None = None,
    ) -> IAMGetCredentialReportResponse:
        client = self._require_client()
        return await self._execute(client.get_credential_report, request, IAMGetCredentialReportResponse)

    async def get_delegation_request(
        self,
        request: IAMGetDelegationRequestRequest,
    ) -> IAMGetDelegationRequestResponse:
        client = self._require_client()
        return await self._execute(client.get_delegation_request, request, IAMGetDelegationRequestResponse)

    async def get_group_policy(
        self,
        request: IAMGetGroupPolicyRequest,
    ) -> IAMGetGroupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_group_policy, request, IAMGetGroupPolicyResponse)

    async def get_human_readable_summary(
        self,
        request: IAMGetHumanReadableSummaryRequest,
    ) -> IAMGetHumanReadableSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_human_readable_summary, request, IAMGetHumanReadableSummaryResponse)

    async def get_login_profile(
        self,
        request: IAMGetLoginProfileRequest | None = None,
    ) -> IAMGetLoginProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_login_profile, request, IAMGetLoginProfileResponse)

    async def get_mfa_device(
        self,
        request: IAMGetMFADeviceRequest,
    ) -> IAMGetMFADeviceResponse:
        client = self._require_client()
        return await self._execute(client.get_mfa_device, request, IAMGetMFADeviceResponse)

    async def get_open_id_connect_provider(
        self,
        request: IAMGetOpenIDConnectProviderRequest,
    ) -> IAMGetOpenIDConnectProviderResponse:
        client = self._require_client()
        return await self._execute(client.get_open_id_connect_provider, request, IAMGetOpenIDConnectProviderResponse)

    async def get_organizations_access_report(
        self,
        request: IAMGetOrganizationsAccessReportRequest,
    ) -> IAMGetOrganizationsAccessReportResponse:
        client = self._require_client()
        return await self._execute(client.get_organizations_access_report, request, IAMGetOrganizationsAccessReportResponse)

    async def get_outbound_web_identity_federation_info(
        self,
        request: IAMGetOutboundWebIdentityFederationInfoRequest | None = None,
    ) -> IAMGetOutboundWebIdentityFederationInfoResponse:
        client = self._require_client()
        return await self._execute(client.get_outbound_web_identity_federation_info, request, IAMGetOutboundWebIdentityFederationInfoResponse)

    async def get_role_template_version(
        self,
        request: IAMGetRoleTemplateVersionRequest,
    ) -> IAMGetRoleTemplateVersionResponse:
        client = self._require_client()
        return await self._execute(client.get_role_template_version, request, IAMGetRoleTemplateVersionResponse)

    async def get_saml_provider(
        self,
        request: IAMGetSAMLProviderRequest,
    ) -> IAMGetSAMLProviderResponse:
        client = self._require_client()
        return await self._execute(client.get_saml_provider, request, IAMGetSAMLProviderResponse)

    async def get_ssh_public_key(
        self,
        request: IAMGetSSHPublicKeyRequest,
    ) -> IAMGetSSHPublicKeyResponse:
        client = self._require_client()
        return await self._execute(client.get_ssh_public_key, request, IAMGetSSHPublicKeyResponse)

    async def get_server_certificate(
        self,
        request: IAMGetServerCertificateRequest,
    ) -> IAMGetServerCertificateResponse:
        client = self._require_client()
        return await self._execute(client.get_server_certificate, request, IAMGetServerCertificateResponse)

    async def get_service_last_accessed_details(
        self,
        request: IAMGetServiceLastAccessedDetailsRequest,
    ) -> IAMGetServiceLastAccessedDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_service_last_accessed_details, request, IAMGetServiceLastAccessedDetailsResponse)

    async def get_service_last_accessed_details_with_entities(
        self,
        request: IAMGetServiceLastAccessedDetailsWithEntitiesRequest,
    ) -> IAMGetServiceLastAccessedDetailsWithEntitiesResponse:
        client = self._require_client()
        return await self._execute(client.get_service_last_accessed_details_with_entities, request, IAMGetServiceLastAccessedDetailsWithEntitiesResponse)

    async def get_service_linked_role_deletion_status(
        self,
        request: IAMGetServiceLinkedRoleDeletionStatusRequest,
    ) -> IAMGetServiceLinkedRoleDeletionStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_service_linked_role_deletion_status, request, IAMGetServiceLinkedRoleDeletionStatusResponse)

    async def get_user_policy(
        self,
        request: IAMGetUserPolicyRequest,
    ) -> IAMGetUserPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_user_policy, request, IAMGetUserPolicyResponse)

    async def list_account_aliases(
        self,
        request: IAMListAccountAliasesRequest | None = None,
    ) -> IAMListAccountAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_account_aliases, request, IAMListAccountAliasesResponse)

    async def list_account_aliases_paginated(
        self,
        request: IAMListAccountAliasesRequest | None = None,
    ) -> list[IAMListAccountAliasesResponse]:
        return await self._paginate('list_account_aliases', request, IAMListAccountAliasesResponse)

    async def list_attached_group_policies(
        self,
        request: IAMListAttachedGroupPoliciesRequest,
    ) -> IAMListAttachedGroupPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_attached_group_policies, request, IAMListAttachedGroupPoliciesResponse)

    async def list_attached_group_policies_paginated(
        self,
        request: IAMListAttachedGroupPoliciesRequest,
    ) -> list[IAMListAttachedGroupPoliciesResponse]:
        return await self._paginate('list_attached_group_policies', request, IAMListAttachedGroupPoliciesResponse)

    async def list_delegation_requests(
        self,
        request: IAMListDelegationRequestsRequest | None = None,
    ) -> IAMListDelegationRequestsResponse:
        client = self._require_client()
        return await self._execute(client.list_delegation_requests, request, IAMListDelegationRequestsResponse)

    async def list_entities_for_policy(
        self,
        request: IAMListEntitiesForPolicyRequest,
    ) -> IAMListEntitiesForPolicyResponse:
        client = self._require_client()
        return await self._execute(client.list_entities_for_policy, request, IAMListEntitiesForPolicyResponse)

    async def list_entities_for_policy_paginated(
        self,
        request: IAMListEntitiesForPolicyRequest,
    ) -> list[IAMListEntitiesForPolicyResponse]:
        return await self._paginate('list_entities_for_policy', request, IAMListEntitiesForPolicyResponse)

    async def list_group_policies(
        self,
        request: IAMListGroupPoliciesRequest,
    ) -> IAMListGroupPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_group_policies, request, IAMListGroupPoliciesResponse)

    async def list_group_policies_paginated(
        self,
        request: IAMListGroupPoliciesRequest,
    ) -> list[IAMListGroupPoliciesResponse]:
        return await self._paginate('list_group_policies', request, IAMListGroupPoliciesResponse)

    async def list_groups_for_user(
        self,
        request: IAMListGroupsForUserRequest,
    ) -> IAMListGroupsForUserResponse:
        client = self._require_client()
        return await self._execute(client.list_groups_for_user, request, IAMListGroupsForUserResponse)

    async def list_groups_for_user_paginated(
        self,
        request: IAMListGroupsForUserRequest,
    ) -> list[IAMListGroupsForUserResponse]:
        return await self._paginate('list_groups_for_user', request, IAMListGroupsForUserResponse)

    async def list_instance_profile_tags(
        self,
        request: IAMListInstanceProfileTagsRequest,
    ) -> IAMListInstanceProfileTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_instance_profile_tags, request, IAMListInstanceProfileTagsResponse)

    async def list_instance_profile_tags_paginated(
        self,
        request: IAMListInstanceProfileTagsRequest,
    ) -> list[IAMListInstanceProfileTagsResponse]:
        return await self._paginate('list_instance_profile_tags', request, IAMListInstanceProfileTagsResponse)

    async def list_instance_profiles_for_role(
        self,
        request: IAMListInstanceProfilesForRoleRequest,
    ) -> IAMListInstanceProfilesForRoleResponse:
        client = self._require_client()
        return await self._execute(client.list_instance_profiles_for_role, request, IAMListInstanceProfilesForRoleResponse)

    async def list_instance_profiles_for_role_paginated(
        self,
        request: IAMListInstanceProfilesForRoleRequest,
    ) -> list[IAMListInstanceProfilesForRoleResponse]:
        return await self._paginate('list_instance_profiles_for_role', request, IAMListInstanceProfilesForRoleResponse)

    async def list_mfa_device_tags(
        self,
        request: IAMListMFADeviceTagsRequest,
    ) -> IAMListMFADeviceTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_mfa_device_tags, request, IAMListMFADeviceTagsResponse)

    async def list_mfa_device_tags_paginated(
        self,
        request: IAMListMFADeviceTagsRequest,
    ) -> list[IAMListMFADeviceTagsResponse]:
        return await self._paginate('list_mfa_device_tags', request, IAMListMFADeviceTagsResponse)

    async def list_mfa_devices(
        self,
        request: IAMListMFADevicesRequest | None = None,
    ) -> IAMListMFADevicesResponse:
        client = self._require_client()
        return await self._execute(client.list_mfa_devices, request, IAMListMFADevicesResponse)

    async def list_mfa_devices_paginated(
        self,
        request: IAMListMFADevicesRequest | None = None,
    ) -> list[IAMListMFADevicesResponse]:
        return await self._paginate('list_mfa_devices', request, IAMListMFADevicesResponse)

    async def list_open_id_connect_provider_tags(
        self,
        request: IAMListOpenIDConnectProviderTagsRequest,
    ) -> IAMListOpenIDConnectProviderTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_open_id_connect_provider_tags, request, IAMListOpenIDConnectProviderTagsResponse)

    async def list_open_id_connect_provider_tags_paginated(
        self,
        request: IAMListOpenIDConnectProviderTagsRequest,
    ) -> list[IAMListOpenIDConnectProviderTagsResponse]:
        return await self._paginate('list_open_id_connect_provider_tags', request, IAMListOpenIDConnectProviderTagsResponse)

    async def list_open_id_connect_providers(
        self,
        request: IAMListOpenIDConnectProvidersRequest | None = None,
    ) -> IAMListOpenIDConnectProvidersResponse:
        client = self._require_client()
        return await self._execute(client.list_open_id_connect_providers, request, IAMListOpenIDConnectProvidersResponse)

    async def list_organizations_features(
        self,
        request: IAMListOrganizationsFeaturesRequest | None = None,
    ) -> IAMListOrganizationsFeaturesResponse:
        client = self._require_client()
        return await self._execute(client.list_organizations_features, request, IAMListOrganizationsFeaturesResponse)

    async def list_policies_granting_service_access(
        self,
        request: IAMListPoliciesGrantingServiceAccessRequest,
    ) -> IAMListPoliciesGrantingServiceAccessResponse:
        client = self._require_client()
        return await self._execute(client.list_policies_granting_service_access, request, IAMListPoliciesGrantingServiceAccessResponse)

    async def list_policy_tags(
        self,
        request: IAMListPolicyTagsRequest,
    ) -> IAMListPolicyTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_policy_tags, request, IAMListPolicyTagsResponse)

    async def list_policy_tags_paginated(
        self,
        request: IAMListPolicyTagsRequest,
    ) -> list[IAMListPolicyTagsResponse]:
        return await self._paginate('list_policy_tags', request, IAMListPolicyTagsResponse)

    async def list_role_tags(
        self,
        request: IAMListRoleTagsRequest,
    ) -> IAMListRoleTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_role_tags, request, IAMListRoleTagsResponse)

    async def list_role_tags_paginated(
        self,
        request: IAMListRoleTagsRequest,
    ) -> list[IAMListRoleTagsResponse]:
        return await self._paginate('list_role_tags', request, IAMListRoleTagsResponse)

    async def list_saml_provider_tags(
        self,
        request: IAMListSAMLProviderTagsRequest,
    ) -> IAMListSAMLProviderTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_saml_provider_tags, request, IAMListSAMLProviderTagsResponse)

    async def list_saml_provider_tags_paginated(
        self,
        request: IAMListSAMLProviderTagsRequest,
    ) -> list[IAMListSAMLProviderTagsResponse]:
        return await self._paginate('list_saml_provider_tags', request, IAMListSAMLProviderTagsResponse)

    async def list_saml_providers(
        self,
        request: IAMListSAMLProvidersRequest | None = None,
    ) -> IAMListSAMLProvidersResponse:
        client = self._require_client()
        return await self._execute(client.list_saml_providers, request, IAMListSAMLProvidersResponse)

    async def list_ssh_public_keys(
        self,
        request: IAMListSSHPublicKeysRequest | None = None,
    ) -> IAMListSSHPublicKeysResponse:
        client = self._require_client()
        return await self._execute(client.list_ssh_public_keys, request, IAMListSSHPublicKeysResponse)

    async def list_ssh_public_keys_paginated(
        self,
        request: IAMListSSHPublicKeysRequest | None = None,
    ) -> list[IAMListSSHPublicKeysResponse]:
        return await self._paginate('list_ssh_public_keys', request, IAMListSSHPublicKeysResponse)

    async def list_server_certificate_tags(
        self,
        request: IAMListServerCertificateTagsRequest,
    ) -> IAMListServerCertificateTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_server_certificate_tags, request, IAMListServerCertificateTagsResponse)

    async def list_server_certificate_tags_paginated(
        self,
        request: IAMListServerCertificateTagsRequest,
    ) -> list[IAMListServerCertificateTagsResponse]:
        return await self._paginate('list_server_certificate_tags', request, IAMListServerCertificateTagsResponse)

    async def list_server_certificates(
        self,
        request: IAMListServerCertificatesRequest | None = None,
    ) -> IAMListServerCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.list_server_certificates, request, IAMListServerCertificatesResponse)

    async def list_server_certificates_paginated(
        self,
        request: IAMListServerCertificatesRequest | None = None,
    ) -> list[IAMListServerCertificatesResponse]:
        return await self._paginate('list_server_certificates', request, IAMListServerCertificatesResponse)

    async def list_service_specific_credentials(
        self,
        request: IAMListServiceSpecificCredentialsRequest | None = None,
    ) -> IAMListServiceSpecificCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.list_service_specific_credentials, request, IAMListServiceSpecificCredentialsResponse)

    async def list_signing_certificates(
        self,
        request: IAMListSigningCertificatesRequest | None = None,
    ) -> IAMListSigningCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.list_signing_certificates, request, IAMListSigningCertificatesResponse)

    async def list_signing_certificates_paginated(
        self,
        request: IAMListSigningCertificatesRequest | None = None,
    ) -> list[IAMListSigningCertificatesResponse]:
        return await self._paginate('list_signing_certificates', request, IAMListSigningCertificatesResponse)

    async def list_user_policies(
        self,
        request: IAMListUserPoliciesRequest,
    ) -> IAMListUserPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_user_policies, request, IAMListUserPoliciesResponse)

    async def list_user_policies_paginated(
        self,
        request: IAMListUserPoliciesRequest,
    ) -> list[IAMListUserPoliciesResponse]:
        return await self._paginate('list_user_policies', request, IAMListUserPoliciesResponse)

    async def list_user_tags(
        self,
        request: IAMListUserTagsRequest,
    ) -> IAMListUserTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_user_tags, request, IAMListUserTagsResponse)

    async def list_user_tags_paginated(
        self,
        request: IAMListUserTagsRequest,
    ) -> list[IAMListUserTagsResponse]:
        return await self._paginate('list_user_tags', request, IAMListUserTagsResponse)

    async def list_virtual_mfa_devices(
        self,
        request: IAMListVirtualMFADevicesRequest | None = None,
    ) -> IAMListVirtualMFADevicesResponse:
        client = self._require_client()
        return await self._execute(client.list_virtual_mfa_devices, request, IAMListVirtualMFADevicesResponse)

    async def list_virtual_mfa_devices_paginated(
        self,
        request: IAMListVirtualMFADevicesRequest | None = None,
    ) -> list[IAMListVirtualMFADevicesResponse]:
        return await self._paginate('list_virtual_mfa_devices', request, IAMListVirtualMFADevicesResponse)

    async def put_account_properties(
        self,
        request: IAMPutAccountPropertiesRequest,
    ) -> IAMPutAccountPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.put_account_properties, request, IAMPutAccountPropertiesResponse)

    async def put_group_policy(
        self,
        request: IAMPutGroupPolicyRequest,
    ) -> IAMPutGroupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_group_policy, request, IAMPutGroupPolicyResponse)

    async def put_role_permissions_boundary(
        self,
        request: IAMPutRolePermissionsBoundaryRequest,
    ) -> IAMPutRolePermissionsBoundaryResponse:
        client = self._require_client()
        return await self._execute(client.put_role_permissions_boundary, request, IAMPutRolePermissionsBoundaryResponse)

    async def put_user_permissions_boundary(
        self,
        request: IAMPutUserPermissionsBoundaryRequest,
    ) -> IAMPutUserPermissionsBoundaryResponse:
        client = self._require_client()
        return await self._execute(client.put_user_permissions_boundary, request, IAMPutUserPermissionsBoundaryResponse)

    async def put_user_policy(
        self,
        request: IAMPutUserPolicyRequest,
    ) -> IAMPutUserPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_user_policy, request, IAMPutUserPolicyResponse)

    async def reject_delegation_request(
        self,
        request: IAMRejectDelegationRequestRequest,
    ) -> IAMRejectDelegationRequestResponse:
        client = self._require_client()
        return await self._execute(client.reject_delegation_request, request, IAMRejectDelegationRequestResponse)

    async def remove_client_id_from_open_id_connect_provider(
        self,
        request: IAMRemoveClientIDFromOpenIDConnectProviderRequest,
    ) -> IAMRemoveClientIDFromOpenIDConnectProviderResponse:
        client = self._require_client()
        return await self._execute(client.remove_client_id_from_open_id_connect_provider, request, IAMRemoveClientIDFromOpenIDConnectProviderResponse)

    async def remove_role_from_instance_profile(
        self,
        request: IAMRemoveRoleFromInstanceProfileRequest,
    ) -> IAMRemoveRoleFromInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.remove_role_from_instance_profile, request, IAMRemoveRoleFromInstanceProfileResponse)

    async def reset_service_specific_credential(
        self,
        request: IAMResetServiceSpecificCredentialRequest,
    ) -> IAMResetServiceSpecificCredentialResponse:
        client = self._require_client()
        return await self._execute(client.reset_service_specific_credential, request, IAMResetServiceSpecificCredentialResponse)

    async def resync_mfa_device(
        self,
        request: IAMResyncMFADeviceRequest,
    ) -> IAMResyncMFADeviceResponse:
        client = self._require_client()
        return await self._execute(client.resync_mfa_device, request, IAMResyncMFADeviceResponse)

    async def send_delegation_token(
        self,
        request: IAMSendDelegationTokenRequest,
    ) -> IAMSendDelegationTokenResponse:
        client = self._require_client()
        return await self._execute(client.send_delegation_token, request, IAMSendDelegationTokenResponse)

    async def set_default_policy_version(
        self,
        request: IAMSetDefaultPolicyVersionRequest,
    ) -> IAMSetDefaultPolicyVersionResponse:
        client = self._require_client()
        return await self._execute(client.set_default_policy_version, request, IAMSetDefaultPolicyVersionResponse)

    async def set_security_token_service_preferences(
        self,
        request: IAMSetSecurityTokenServicePreferencesRequest,
    ) -> IAMSetSecurityTokenServicePreferencesResponse:
        client = self._require_client()
        return await self._execute(client.set_security_token_service_preferences, request, IAMSetSecurityTokenServicePreferencesResponse)

    async def simulate_custom_policy(
        self,
        request: IAMSimulateCustomPolicyRequest,
    ) -> IAMSimulateCustomPolicyResponse:
        client = self._require_client()
        return await self._execute(client.simulate_custom_policy, request, IAMSimulateCustomPolicyResponse)

    async def simulate_custom_policy_paginated(
        self,
        request: IAMSimulateCustomPolicyRequest,
    ) -> list[IAMSimulateCustomPolicyResponse]:
        return await self._paginate('simulate_custom_policy', request, IAMSimulateCustomPolicyResponse)

    async def simulate_principal_policy(
        self,
        request: IAMSimulatePrincipalPolicyRequest,
    ) -> IAMSimulatePrincipalPolicyResponse:
        client = self._require_client()
        return await self._execute(client.simulate_principal_policy, request, IAMSimulatePrincipalPolicyResponse)

    async def simulate_principal_policy_paginated(
        self,
        request: IAMSimulatePrincipalPolicyRequest,
    ) -> list[IAMSimulatePrincipalPolicyResponse]:
        return await self._paginate('simulate_principal_policy', request, IAMSimulatePrincipalPolicyResponse)

    async def tag_instance_profile(
        self,
        request: IAMTagInstanceProfileRequest,
    ) -> IAMTagInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.tag_instance_profile, request, IAMTagInstanceProfileResponse)

    async def tag_mfa_device(
        self,
        request: IAMTagMFADeviceRequest,
    ) -> IAMTagMFADeviceResponse:
        client = self._require_client()
        return await self._execute(client.tag_mfa_device, request, IAMTagMFADeviceResponse)

    async def tag_open_id_connect_provider(
        self,
        request: IAMTagOpenIDConnectProviderRequest,
    ) -> IAMTagOpenIDConnectProviderResponse:
        client = self._require_client()
        return await self._execute(client.tag_open_id_connect_provider, request, IAMTagOpenIDConnectProviderResponse)

    async def tag_policy(
        self,
        request: IAMTagPolicyRequest,
    ) -> IAMTagPolicyResponse:
        client = self._require_client()
        return await self._execute(client.tag_policy, request, IAMTagPolicyResponse)

    async def tag_role(
        self,
        request: IAMTagRoleRequest,
    ) -> IAMTagRoleResponse:
        client = self._require_client()
        return await self._execute(client.tag_role, request, IAMTagRoleResponse)

    async def tag_saml_provider(
        self,
        request: IAMTagSAMLProviderRequest,
    ) -> IAMTagSAMLProviderResponse:
        client = self._require_client()
        return await self._execute(client.tag_saml_provider, request, IAMTagSAMLProviderResponse)

    async def tag_server_certificate(
        self,
        request: IAMTagServerCertificateRequest,
    ) -> IAMTagServerCertificateResponse:
        client = self._require_client()
        return await self._execute(client.tag_server_certificate, request, IAMTagServerCertificateResponse)

    async def tag_user(
        self,
        request: IAMTagUserRequest,
    ) -> IAMTagUserResponse:
        client = self._require_client()
        return await self._execute(client.tag_user, request, IAMTagUserResponse)

    async def untag_instance_profile(
        self,
        request: IAMUntagInstanceProfileRequest,
    ) -> IAMUntagInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.untag_instance_profile, request, IAMUntagInstanceProfileResponse)

    async def untag_mfa_device(
        self,
        request: IAMUntagMFADeviceRequest,
    ) -> IAMUntagMFADeviceResponse:
        client = self._require_client()
        return await self._execute(client.untag_mfa_device, request, IAMUntagMFADeviceResponse)

    async def untag_open_id_connect_provider(
        self,
        request: IAMUntagOpenIDConnectProviderRequest,
    ) -> IAMUntagOpenIDConnectProviderResponse:
        client = self._require_client()
        return await self._execute(client.untag_open_id_connect_provider, request, IAMUntagOpenIDConnectProviderResponse)

    async def untag_policy(
        self,
        request: IAMUntagPolicyRequest,
    ) -> IAMUntagPolicyResponse:
        client = self._require_client()
        return await self._execute(client.untag_policy, request, IAMUntagPolicyResponse)

    async def untag_role(
        self,
        request: IAMUntagRoleRequest,
    ) -> IAMUntagRoleResponse:
        client = self._require_client()
        return await self._execute(client.untag_role, request, IAMUntagRoleResponse)

    async def untag_saml_provider(
        self,
        request: IAMUntagSAMLProviderRequest,
    ) -> IAMUntagSAMLProviderResponse:
        client = self._require_client()
        return await self._execute(client.untag_saml_provider, request, IAMUntagSAMLProviderResponse)

    async def untag_server_certificate(
        self,
        request: IAMUntagServerCertificateRequest,
    ) -> IAMUntagServerCertificateResponse:
        client = self._require_client()
        return await self._execute(client.untag_server_certificate, request, IAMUntagServerCertificateResponse)

    async def untag_user(
        self,
        request: IAMUntagUserRequest,
    ) -> IAMUntagUserResponse:
        client = self._require_client()
        return await self._execute(client.untag_user, request, IAMUntagUserResponse)

    async def update_access_key(
        self,
        request: IAMUpdateAccessKeyRequest,
    ) -> IAMUpdateAccessKeyResponse:
        client = self._require_client()
        return await self._execute(client.update_access_key, request, IAMUpdateAccessKeyResponse)

    async def update_account_password_policy(
        self,
        request: IAMUpdateAccountPasswordPolicyRequest | None = None,
    ) -> IAMUpdateAccountPasswordPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_account_password_policy, request, IAMUpdateAccountPasswordPolicyResponse)

    async def update_delegation_request(
        self,
        request: IAMUpdateDelegationRequestRequest,
    ) -> IAMUpdateDelegationRequestResponse:
        client = self._require_client()
        return await self._execute(client.update_delegation_request, request, IAMUpdateDelegationRequestResponse)

    async def update_group(
        self,
        request: IAMUpdateGroupRequest,
    ) -> IAMUpdateGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_group, request, IAMUpdateGroupResponse)

    async def update_login_profile(
        self,
        request: IAMUpdateLoginProfileRequest,
    ) -> IAMUpdateLoginProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_login_profile, request, IAMUpdateLoginProfileResponse)

    async def update_open_id_connect_provider(
        self,
        request: IAMUpdateOpenIDConnectProviderRequest,
    ) -> IAMUpdateOpenIDConnectProviderResponse:
        client = self._require_client()
        return await self._execute(client.update_open_id_connect_provider, request, IAMUpdateOpenIDConnectProviderResponse)

    async def update_open_id_connect_provider_thumbprint(
        self,
        request: IAMUpdateOpenIDConnectProviderThumbprintRequest,
    ) -> IAMUpdateOpenIDConnectProviderThumbprintResponse:
        client = self._require_client()
        return await self._execute(client.update_open_id_connect_provider_thumbprint, request, IAMUpdateOpenIDConnectProviderThumbprintResponse)

    async def update_role(
        self,
        request: IAMUpdateRoleRequest,
    ) -> IAMUpdateRoleResponse:
        client = self._require_client()
        return await self._execute(client.update_role, request, IAMUpdateRoleResponse)

    async def update_role_description(
        self,
        request: IAMUpdateRoleDescriptionRequest,
    ) -> IAMUpdateRoleDescriptionResponse:
        client = self._require_client()
        return await self._execute(client.update_role_description, request, IAMUpdateRoleDescriptionResponse)

    async def update_saml_provider(
        self,
        request: IAMUpdateSAMLProviderRequest,
    ) -> IAMUpdateSAMLProviderResponse:
        client = self._require_client()
        return await self._execute(client.update_saml_provider, request, IAMUpdateSAMLProviderResponse)

    async def update_ssh_public_key(
        self,
        request: IAMUpdateSSHPublicKeyRequest,
    ) -> IAMUpdateSSHPublicKeyResponse:
        client = self._require_client()
        return await self._execute(client.update_ssh_public_key, request, IAMUpdateSSHPublicKeyResponse)

    async def update_server_certificate(
        self,
        request: IAMUpdateServerCertificateRequest,
    ) -> IAMUpdateServerCertificateResponse:
        client = self._require_client()
        return await self._execute(client.update_server_certificate, request, IAMUpdateServerCertificateResponse)

    async def update_service_specific_credential(
        self,
        request: IAMUpdateServiceSpecificCredentialRequest,
    ) -> IAMUpdateServiceSpecificCredentialResponse:
        client = self._require_client()
        return await self._execute(client.update_service_specific_credential, request, IAMUpdateServiceSpecificCredentialResponse)

    async def update_signing_certificate(
        self,
        request: IAMUpdateSigningCertificateRequest,
    ) -> IAMUpdateSigningCertificateResponse:
        client = self._require_client()
        return await self._execute(client.update_signing_certificate, request, IAMUpdateSigningCertificateResponse)

    async def update_user(
        self,
        request: IAMUpdateUserRequest,
    ) -> IAMUpdateUserResponse:
        client = self._require_client()
        return await self._execute(client.update_user, request, IAMUpdateUserResponse)

    async def upload_ssh_public_key(
        self,
        request: IAMUploadSSHPublicKeyRequest,
    ) -> IAMUploadSSHPublicKeyResponse:
        client = self._require_client()
        return await self._execute(client.upload_ssh_public_key, request, IAMUploadSSHPublicKeyResponse)

    async def upload_server_certificate(
        self,
        request: IAMUploadServerCertificateRequest,
    ) -> IAMUploadServerCertificateResponse:
        client = self._require_client()
        return await self._execute(client.upload_server_certificate, request, IAMUploadServerCertificateResponse)

    async def upload_signing_certificate(
        self,
        request: IAMUploadSigningCertificateRequest,
    ) -> IAMUploadSigningCertificateResponse:
        client = self._require_client()
        return await self._execute(client.upload_signing_certificate, request, IAMUploadSigningCertificateResponse)

