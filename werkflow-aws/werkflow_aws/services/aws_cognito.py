from werkflow_aws.models.cognito import (
    CognitoIDPAddCustomAttributesRequest,
    CognitoIDPAddCustomAttributesResponse,
    CognitoIDPAddUserPoolClientSecretRequest,
    CognitoIDPAddUserPoolClientSecretResponse,
    CognitoIDPAdminAddUserToGroupRequest,
    CognitoIDPAdminAddUserToGroupResponse,
    CognitoIDPAdminConfirmSignUpRequest,
    CognitoIDPAdminConfirmSignUpResponse,
    CognitoIDPAdminCreateUserRequest,
    CognitoIDPAdminCreateUserResponse,
    CognitoIDPAdminDeleteSoftwareTokenRequest,
    CognitoIDPAdminDeleteSoftwareTokenResponse,
    CognitoIDPAdminDeleteUserAttributesRequest,
    CognitoIDPAdminDeleteUserAttributesResponse,
    CognitoIDPAdminDeleteUserRequest,
    CognitoIDPAdminDeleteUserResponse,
    CognitoIDPAdminDisableProviderForUserRequest,
    CognitoIDPAdminDisableProviderForUserResponse,
    CognitoIDPAdminDisableUserRequest,
    CognitoIDPAdminDisableUserResponse,
    CognitoIDPAdminEnableUserRequest,
    CognitoIDPAdminEnableUserResponse,
    CognitoIDPAdminForgetDeviceRequest,
    CognitoIDPAdminForgetDeviceResponse,
    CognitoIDPAdminGetDeviceRequest,
    CognitoIDPAdminGetDeviceResponse,
    CognitoIDPAdminGetUserAuthFactorsRequest,
    CognitoIDPAdminGetUserAuthFactorsResponse,
    CognitoIDPAdminGetUserRequest,
    CognitoIDPAdminGetUserResponse,
    CognitoIDPAdminInitiateAuthRequest,
    CognitoIDPAdminInitiateAuthResponse,
    CognitoIDPAdminLinkProviderForUserRequest,
    CognitoIDPAdminLinkProviderForUserResponse,
    CognitoIDPAdminListDevicesRequest,
    CognitoIDPAdminListDevicesResponse,
    CognitoIDPAdminListGroupsForUserRequest,
    CognitoIDPAdminListGroupsForUserResponse,
    CognitoIDPAdminListUserAuthEventsRequest,
    CognitoIDPAdminListUserAuthEventsResponse,
    CognitoIDPAdminListUserSessionsRequest,
    CognitoIDPAdminListUserSessionsResponse,
    CognitoIDPAdminRemoveUserFromGroupRequest,
    CognitoIDPAdminRemoveUserFromGroupResponse,
    CognitoIDPAdminResetUserPasswordRequest,
    CognitoIDPAdminResetUserPasswordResponse,
    CognitoIDPAdminRespondToAuthChallengeRequest,
    CognitoIDPAdminRespondToAuthChallengeResponse,
    CognitoIDPAdminRevokeUserSessionRequest,
    CognitoIDPAdminRevokeUserSessionResponse,
    CognitoIDPAdminSetUserMFAPreferenceRequest,
    CognitoIDPAdminSetUserMFAPreferenceResponse,
    CognitoIDPAdminSetUserPasswordRequest,
    CognitoIDPAdminSetUserPasswordResponse,
    CognitoIDPAdminSetUserSettingsRequest,
    CognitoIDPAdminSetUserSettingsResponse,
    CognitoIDPAdminUpdateAuthEventFeedbackRequest,
    CognitoIDPAdminUpdateAuthEventFeedbackResponse,
    CognitoIDPAdminUpdateDeviceStatusRequest,
    CognitoIDPAdminUpdateDeviceStatusResponse,
    CognitoIDPAdminUpdateUserAttributesRequest,
    CognitoIDPAdminUpdateUserAttributesResponse,
    CognitoIDPAdminUserGlobalSignOutRequest,
    CognitoIDPAdminUserGlobalSignOutResponse,
    CognitoIDPAssociateSoftwareTokenRequest,
    CognitoIDPAssociateSoftwareTokenResponse,
    CognitoIDPCancelPointInTimeRecoveryRequest,
    CognitoIDPCancelPointInTimeRecoveryResponse,
    CognitoIDPChangePasswordRequest,
    CognitoIDPChangePasswordResponse,
    CognitoIDPCompleteWebAuthnRegistrationRequest,
    CognitoIDPCompleteWebAuthnRegistrationResponse,
    CognitoIDPConfirmDeviceRequest,
    CognitoIDPConfirmDeviceResponse,
    CognitoIDPConfirmForgotPasswordRequest,
    CognitoIDPConfirmForgotPasswordResponse,
    CognitoIDPConfirmSignUpRequest,
    CognitoIDPConfirmSignUpResponse,
    CognitoIDPCreateCIMDPolicyRequest,
    CognitoIDPCreateCIMDPolicyResponse,
    CognitoIDPCreateGroupRequest,
    CognitoIDPCreateGroupResponse,
    CognitoIDPCreateIdentityProviderRequest,
    CognitoIDPCreateIdentityProviderResponse,
    CognitoIDPCreateManagedLoginBrandingRequest,
    CognitoIDPCreateManagedLoginBrandingResponse,
    CognitoIDPCreateResourceServerRequest,
    CognitoIDPCreateResourceServerResponse,
    CognitoIDPCreateTermsRequest,
    CognitoIDPCreateTermsResponse,
    CognitoIDPCreateUserImportJobRequest,
    CognitoIDPCreateUserImportJobResponse,
    CognitoIDPCreateUserPoolClientRequest,
    CognitoIDPCreateUserPoolClientResponse,
    CognitoIDPCreateUserPoolDomainRequest,
    CognitoIDPCreateUserPoolDomainResponse,
    CognitoIDPCreateUserPoolReplicaRequest,
    CognitoIDPCreateUserPoolReplicaResponse,
    CognitoIDPCreateUserPoolRequest,
    CognitoIDPCreateUserPoolResponse,
    CognitoIDPDeleteCIMDPolicyRequest,
    CognitoIDPDeleteCIMDPolicyResponse,
    CognitoIDPDeleteGroupRequest,
    CognitoIDPDeleteGroupResponse,
    CognitoIDPDeleteIdentityProviderRequest,
    CognitoIDPDeleteIdentityProviderResponse,
    CognitoIDPDeleteManagedLoginBrandingRequest,
    CognitoIDPDeleteManagedLoginBrandingResponse,
    CognitoIDPDeleteResourceServerRequest,
    CognitoIDPDeleteResourceServerResponse,
    CognitoIDPDeleteTermsRequest,
    CognitoIDPDeleteTermsResponse,
    CognitoIDPDeleteUserAttributesRequest,
    CognitoIDPDeleteUserAttributesResponse,
    CognitoIDPDeleteUserPoolClientRequest,
    CognitoIDPDeleteUserPoolClientResponse,
    CognitoIDPDeleteUserPoolClientSecretRequest,
    CognitoIDPDeleteUserPoolClientSecretResponse,
    CognitoIDPDeleteUserPoolDomainRequest,
    CognitoIDPDeleteUserPoolDomainResponse,
    CognitoIDPDeleteUserPoolReplicaRequest,
    CognitoIDPDeleteUserPoolReplicaResponse,
    CognitoIDPDeleteUserPoolRequest,
    CognitoIDPDeleteUserPoolResponse,
    CognitoIDPDeleteUserRequest,
    CognitoIDPDeleteUserResponse,
    CognitoIDPDeleteWebAuthnCredentialRequest,
    CognitoIDPDeleteWebAuthnCredentialResponse,
    CognitoIDPDescribeCIMDPolicyRequest,
    CognitoIDPDescribeCIMDPolicyResponse,
    CognitoIDPDescribeIdentityProviderRequest,
    CognitoIDPDescribeIdentityProviderResponse,
    CognitoIDPDescribeManagedLoginBrandingByClientRequest,
    CognitoIDPDescribeManagedLoginBrandingByClientResponse,
    CognitoIDPDescribeManagedLoginBrandingRequest,
    CognitoIDPDescribeManagedLoginBrandingResponse,
    CognitoIDPDescribePointInTimeRecoveryRequest,
    CognitoIDPDescribePointInTimeRecoveryResponse,
    CognitoIDPDescribeResourceServerRequest,
    CognitoIDPDescribeResourceServerResponse,
    CognitoIDPDescribeRiskConfigurationRequest,
    CognitoIDPDescribeRiskConfigurationResponse,
    CognitoIDPDescribeTermsByClientRequest,
    CognitoIDPDescribeTermsByClientResponse,
    CognitoIDPDescribeTermsRequest,
    CognitoIDPDescribeTermsResponse,
    CognitoIDPDescribeUserImportJobRequest,
    CognitoIDPDescribeUserImportJobResponse,
    CognitoIDPDescribeUserPoolClientRequest,
    CognitoIDPDescribeUserPoolClientResponse,
    CognitoIDPDescribeUserPoolDomainRequest,
    CognitoIDPDescribeUserPoolDomainResponse,
    CognitoIDPDescribeUserPoolRequest,
    CognitoIDPDescribeUserPoolResponse,
    CognitoIDPForgetDeviceRequest,
    CognitoIDPForgetDeviceResponse,
    CognitoIDPForgotPasswordRequest,
    CognitoIDPForgotPasswordResponse,
    CognitoIDPGetCSVHeaderRequest,
    CognitoIDPGetCSVHeaderResponse,
    CognitoIDPGetClientTokenRequest,
    CognitoIDPGetClientTokenResponse,
    CognitoIDPGetDerivedTokenRequest,
    CognitoIDPGetDerivedTokenResponse,
    CognitoIDPGetDeviceRequest,
    CognitoIDPGetDeviceResponse,
    CognitoIDPGetGroupRequest,
    CognitoIDPGetGroupResponse,
    CognitoIDPGetIdentityProviderByIdentifierRequest,
    CognitoIDPGetIdentityProviderByIdentifierResponse,
    CognitoIDPGetLogDeliveryConfigurationRequest,
    CognitoIDPGetLogDeliveryConfigurationResponse,
    CognitoIDPGetProvisionedLimitRequest,
    CognitoIDPGetProvisionedLimitResponse,
    CognitoIDPGetSigningCertificateRequest,
    CognitoIDPGetSigningCertificateResponse,
    CognitoIDPGetTokensFromRefreshTokenRequest,
    CognitoIDPGetTokensFromRefreshTokenResponse,
    CognitoIDPGetUICustomizationRequest,
    CognitoIDPGetUICustomizationResponse,
    CognitoIDPGetUserAttributeVerificationCodeRequest,
    CognitoIDPGetUserAttributeVerificationCodeResponse,
    CognitoIDPGetUserAuthFactorsRequest,
    CognitoIDPGetUserAuthFactorsResponse,
    CognitoIDPGetUserPoolClientSessionConfigurationRequest,
    CognitoIDPGetUserPoolClientSessionConfigurationResponse,
    CognitoIDPGetUserPoolMfaConfigRequest,
    CognitoIDPGetUserPoolMfaConfigResponse,
    CognitoIDPGetUserPoolSessionConfigurationRequest,
    CognitoIDPGetUserPoolSessionConfigurationResponse,
    CognitoIDPGetUserRequest,
    CognitoIDPGetUserResponse,
    CognitoIDPGlobalSignOutRequest,
    CognitoIDPGlobalSignOutResponse,
    CognitoIDPInitiateAuthRequest,
    CognitoIDPInitiateAuthResponse,
    CognitoIDPInitiatePointInTimeRecoveryRequest,
    CognitoIDPInitiatePointInTimeRecoveryResponse,
    CognitoIDPListCIMDPoliciesRequest,
    CognitoIDPListCIMDPoliciesResponse,
    CognitoIDPListClientMetadataURLsRequest,
    CognitoIDPListClientMetadataURLsResponse,
    CognitoIDPListDevicesRequest,
    CognitoIDPListDevicesResponse,
    CognitoIDPListGroupsRequest,
    CognitoIDPListGroupsResponse,
    CognitoIDPListIdentityProvidersRequest,
    CognitoIDPListIdentityProvidersResponse,
    CognitoIDPListPointInTimeRecoveriesRequest,
    CognitoIDPListPointInTimeRecoveriesResponse,
    CognitoIDPListResourceServersRequest,
    CognitoIDPListResourceServersResponse,
    CognitoIDPListTagsForResourceRequest,
    CognitoIDPListTagsForResourceResponse,
    CognitoIDPListTermsRequest,
    CognitoIDPListTermsResponse,
    CognitoIDPListUserImportJobsRequest,
    CognitoIDPListUserImportJobsResponse,
    CognitoIDPListUserPoolClientSecretsRequest,
    CognitoIDPListUserPoolClientSecretsResponse,
    CognitoIDPListUserPoolClientsRequest,
    CognitoIDPListUserPoolClientsResponse,
    CognitoIDPListUserPoolReplicasRequest,
    CognitoIDPListUserPoolReplicasResponse,
    CognitoIDPListUserPoolsRequest,
    CognitoIDPListUserPoolsResponse,
    CognitoIDPListUserSessionsRequest,
    CognitoIDPListUserSessionsResponse,
    CognitoIDPListUsersInGroupRequest,
    CognitoIDPListUsersInGroupResponse,
    CognitoIDPListUsersRequest,
    CognitoIDPListUsersResponse,
    CognitoIDPListWebAuthnCredentialsRequest,
    CognitoIDPListWebAuthnCredentialsResponse,
    CognitoIDPResendConfirmationCodeRequest,
    CognitoIDPResendConfirmationCodeResponse,
    CognitoIDPRespondToAuthChallengeRequest,
    CognitoIDPRespondToAuthChallengeResponse,
    CognitoIDPRevokeTokenRequest,
    CognitoIDPRevokeTokenResponse,
    CognitoIDPRevokeUserSessionRequest,
    CognitoIDPRevokeUserSessionResponse,
    CognitoIDPSetLogDeliveryConfigurationRequest,
    CognitoIDPSetLogDeliveryConfigurationResponse,
    CognitoIDPSetRiskConfigurationRequest,
    CognitoIDPSetRiskConfigurationResponse,
    CognitoIDPSetUICustomizationRequest,
    CognitoIDPSetUICustomizationResponse,
    CognitoIDPSetUserMFAPreferenceRequest,
    CognitoIDPSetUserMFAPreferenceResponse,
    CognitoIDPSetUserPoolClientSessionConfigurationRequest,
    CognitoIDPSetUserPoolClientSessionConfigurationResponse,
    CognitoIDPSetUserPoolMfaConfigRequest,
    CognitoIDPSetUserPoolMfaConfigResponse,
    CognitoIDPSetUserPoolSessionConfigurationRequest,
    CognitoIDPSetUserPoolSessionConfigurationResponse,
    CognitoIDPSetUserSettingsRequest,
    CognitoIDPSetUserSettingsResponse,
    CognitoIDPSignUpRequest,
    CognitoIDPSignUpResponse,
    CognitoIDPStartPointInTimeRecoveryRequest,
    CognitoIDPStartPointInTimeRecoveryResponse,
    CognitoIDPStartUserImportJobRequest,
    CognitoIDPStartUserImportJobResponse,
    CognitoIDPStartWebAuthnRegistrationRequest,
    CognitoIDPStartWebAuthnRegistrationResponse,
    CognitoIDPStopUserImportJobRequest,
    CognitoIDPStopUserImportJobResponse,
    CognitoIDPTagResourceRequest,
    CognitoIDPTagResourceResponse,
    CognitoIDPUntagResourceRequest,
    CognitoIDPUntagResourceResponse,
    CognitoIDPUpdateAuthEventFeedbackRequest,
    CognitoIDPUpdateAuthEventFeedbackResponse,
    CognitoIDPUpdateCIMDPolicyRequest,
    CognitoIDPUpdateCIMDPolicyResponse,
    CognitoIDPUpdateClientMetadataURLStateRequest,
    CognitoIDPUpdateClientMetadataURLStateResponse,
    CognitoIDPUpdateDeviceStatusRequest,
    CognitoIDPUpdateDeviceStatusResponse,
    CognitoIDPUpdateGroupRequest,
    CognitoIDPUpdateGroupResponse,
    CognitoIDPUpdateIdentityProviderRequest,
    CognitoIDPUpdateIdentityProviderResponse,
    CognitoIDPUpdateManagedLoginBrandingRequest,
    CognitoIDPUpdateManagedLoginBrandingResponse,
    CognitoIDPUpdateProvisionedLimitRequest,
    CognitoIDPUpdateProvisionedLimitResponse,
    CognitoIDPUpdateResourceServerRequest,
    CognitoIDPUpdateResourceServerResponse,
    CognitoIDPUpdateTermsRequest,
    CognitoIDPUpdateTermsResponse,
    CognitoIDPUpdateUserAttributesRequest,
    CognitoIDPUpdateUserAttributesResponse,
    CognitoIDPUpdateUserPoolClientRequest,
    CognitoIDPUpdateUserPoolClientResponse,
    CognitoIDPUpdateUserPoolDomainRequest,
    CognitoIDPUpdateUserPoolDomainResponse,
    CognitoIDPUpdateUserPoolReplicaRequest,
    CognitoIDPUpdateUserPoolReplicaResponse,
    CognitoIDPUpdateUserPoolRequest,
    CognitoIDPUpdateUserPoolResponse,
    CognitoIDPVerifySoftwareTokenRequest,
    CognitoIDPVerifySoftwareTokenResponse,
    CognitoIDPVerifyUserAttributeRequest,
    CognitoIDPVerifyUserAttributeResponse,
)
from werkflow_aws.types.cognito_client import CognitoIDPClient
from .base import AWSBaseService


class AWSCognitoIDP(AWSBaseService[CognitoIDPClient]):
    service_name = 'cognito'
    boto3_service_name = 'cognito-idp'

    def __init__(self) -> None:
        super().__init__(service_name='cognito', boto3_service_name='cognito-idp')

    async def add_custom_attributes(
        self,
        request: CognitoIDPAddCustomAttributesRequest,
    ) -> CognitoIDPAddCustomAttributesResponse:
        client = self._require_client()
        return await self._execute(client.add_custom_attributes, request, CognitoIDPAddCustomAttributesResponse)

    async def add_user_pool_client_secret(
        self,
        request: CognitoIDPAddUserPoolClientSecretRequest,
    ) -> CognitoIDPAddUserPoolClientSecretResponse:
        client = self._require_client()
        return await self._execute(client.add_user_pool_client_secret, request, CognitoIDPAddUserPoolClientSecretResponse)

    async def admin_add_user_to_group(
        self,
        request: CognitoIDPAdminAddUserToGroupRequest,
    ) -> CognitoIDPAdminAddUserToGroupResponse:
        client = self._require_client()
        return await self._execute(client.admin_add_user_to_group, request, CognitoIDPAdminAddUserToGroupResponse)

    async def admin_confirm_sign_up(
        self,
        request: CognitoIDPAdminConfirmSignUpRequest,
    ) -> CognitoIDPAdminConfirmSignUpResponse:
        client = self._require_client()
        return await self._execute(client.admin_confirm_sign_up, request, CognitoIDPAdminConfirmSignUpResponse)

    async def admin_create_user(
        self,
        request: CognitoIDPAdminCreateUserRequest,
    ) -> CognitoIDPAdminCreateUserResponse:
        client = self._require_client()
        return await self._execute(client.admin_create_user, request, CognitoIDPAdminCreateUserResponse)

    async def admin_delete_software_token(
        self,
        request: CognitoIDPAdminDeleteSoftwareTokenRequest,
    ) -> CognitoIDPAdminDeleteSoftwareTokenResponse:
        client = self._require_client()
        return await self._execute(client.admin_delete_software_token, request, CognitoIDPAdminDeleteSoftwareTokenResponse)

    async def admin_delete_user(
        self,
        request: CognitoIDPAdminDeleteUserRequest,
    ) -> CognitoIDPAdminDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.admin_delete_user, request, CognitoIDPAdminDeleteUserResponse)

    async def admin_delete_user_attributes(
        self,
        request: CognitoIDPAdminDeleteUserAttributesRequest,
    ) -> CognitoIDPAdminDeleteUserAttributesResponse:
        client = self._require_client()
        return await self._execute(client.admin_delete_user_attributes, request, CognitoIDPAdminDeleteUserAttributesResponse)

    async def admin_disable_provider_for_user(
        self,
        request: CognitoIDPAdminDisableProviderForUserRequest,
    ) -> CognitoIDPAdminDisableProviderForUserResponse:
        client = self._require_client()
        return await self._execute(client.admin_disable_provider_for_user, request, CognitoIDPAdminDisableProviderForUserResponse)

    async def admin_disable_user(
        self,
        request: CognitoIDPAdminDisableUserRequest,
    ) -> CognitoIDPAdminDisableUserResponse:
        client = self._require_client()
        return await self._execute(client.admin_disable_user, request, CognitoIDPAdminDisableUserResponse)

    async def admin_enable_user(
        self,
        request: CognitoIDPAdminEnableUserRequest,
    ) -> CognitoIDPAdminEnableUserResponse:
        client = self._require_client()
        return await self._execute(client.admin_enable_user, request, CognitoIDPAdminEnableUserResponse)

    async def admin_forget_device(
        self,
        request: CognitoIDPAdminForgetDeviceRequest,
    ) -> CognitoIDPAdminForgetDeviceResponse:
        client = self._require_client()
        return await self._execute(client.admin_forget_device, request, CognitoIDPAdminForgetDeviceResponse)

    async def admin_get_device(
        self,
        request: CognitoIDPAdminGetDeviceRequest,
    ) -> CognitoIDPAdminGetDeviceResponse:
        client = self._require_client()
        return await self._execute(client.admin_get_device, request, CognitoIDPAdminGetDeviceResponse)

    async def admin_get_user(
        self,
        request: CognitoIDPAdminGetUserRequest,
    ) -> CognitoIDPAdminGetUserResponse:
        client = self._require_client()
        return await self._execute(client.admin_get_user, request, CognitoIDPAdminGetUserResponse)

    async def admin_get_user_auth_factors(
        self,
        request: CognitoIDPAdminGetUserAuthFactorsRequest,
    ) -> CognitoIDPAdminGetUserAuthFactorsResponse:
        client = self._require_client()
        return await self._execute(client.admin_get_user_auth_factors, request, CognitoIDPAdminGetUserAuthFactorsResponse)

    async def admin_initiate_auth(
        self,
        request: CognitoIDPAdminInitiateAuthRequest,
    ) -> CognitoIDPAdminInitiateAuthResponse:
        client = self._require_client()
        return await self._execute(client.admin_initiate_auth, request, CognitoIDPAdminInitiateAuthResponse)

    async def admin_link_provider_for_user(
        self,
        request: CognitoIDPAdminLinkProviderForUserRequest,
    ) -> CognitoIDPAdminLinkProviderForUserResponse:
        client = self._require_client()
        return await self._execute(client.admin_link_provider_for_user, request, CognitoIDPAdminLinkProviderForUserResponse)

    async def admin_list_devices(
        self,
        request: CognitoIDPAdminListDevicesRequest,
    ) -> CognitoIDPAdminListDevicesResponse:
        client = self._require_client()
        return await self._execute(client.admin_list_devices, request, CognitoIDPAdminListDevicesResponse)

    async def admin_list_groups_for_user(
        self,
        request: CognitoIDPAdminListGroupsForUserRequest,
    ) -> CognitoIDPAdminListGroupsForUserResponse:
        client = self._require_client()
        return await self._execute(client.admin_list_groups_for_user, request, CognitoIDPAdminListGroupsForUserResponse)

    async def admin_list_groups_for_user_paginated(
        self,
        request: CognitoIDPAdminListGroupsForUserRequest,
    ) -> list[CognitoIDPAdminListGroupsForUserResponse]:
        return await self._paginate('admin_list_groups_for_user', request, CognitoIDPAdminListGroupsForUserResponse)

    async def admin_list_user_auth_events(
        self,
        request: CognitoIDPAdminListUserAuthEventsRequest,
    ) -> CognitoIDPAdminListUserAuthEventsResponse:
        client = self._require_client()
        return await self._execute(client.admin_list_user_auth_events, request, CognitoIDPAdminListUserAuthEventsResponse)

    async def admin_list_user_auth_events_paginated(
        self,
        request: CognitoIDPAdminListUserAuthEventsRequest,
    ) -> list[CognitoIDPAdminListUserAuthEventsResponse]:
        return await self._paginate('admin_list_user_auth_events', request, CognitoIDPAdminListUserAuthEventsResponse)

    async def admin_list_user_sessions(
        self,
        request: CognitoIDPAdminListUserSessionsRequest,
    ) -> CognitoIDPAdminListUserSessionsResponse:
        client = self._require_client()
        return await self._execute(client.admin_list_user_sessions, request, CognitoIDPAdminListUserSessionsResponse)

    async def admin_remove_user_from_group(
        self,
        request: CognitoIDPAdminRemoveUserFromGroupRequest,
    ) -> CognitoIDPAdminRemoveUserFromGroupResponse:
        client = self._require_client()
        return await self._execute(client.admin_remove_user_from_group, request, CognitoIDPAdminRemoveUserFromGroupResponse)

    async def admin_reset_user_password(
        self,
        request: CognitoIDPAdminResetUserPasswordRequest,
    ) -> CognitoIDPAdminResetUserPasswordResponse:
        client = self._require_client()
        return await self._execute(client.admin_reset_user_password, request, CognitoIDPAdminResetUserPasswordResponse)

    async def admin_respond_to_auth_challenge(
        self,
        request: CognitoIDPAdminRespondToAuthChallengeRequest,
    ) -> CognitoIDPAdminRespondToAuthChallengeResponse:
        client = self._require_client()
        return await self._execute(client.admin_respond_to_auth_challenge, request, CognitoIDPAdminRespondToAuthChallengeResponse)

    async def admin_revoke_user_session(
        self,
        request: CognitoIDPAdminRevokeUserSessionRequest,
    ) -> CognitoIDPAdminRevokeUserSessionResponse:
        client = self._require_client()
        return await self._execute(client.admin_revoke_user_session, request, CognitoIDPAdminRevokeUserSessionResponse)

    async def admin_set_user_mfa_preference(
        self,
        request: CognitoIDPAdminSetUserMFAPreferenceRequest,
    ) -> CognitoIDPAdminSetUserMFAPreferenceResponse:
        client = self._require_client()
        return await self._execute(client.admin_set_user_mfa_preference, request, CognitoIDPAdminSetUserMFAPreferenceResponse)

    async def admin_set_user_password(
        self,
        request: CognitoIDPAdminSetUserPasswordRequest,
    ) -> CognitoIDPAdminSetUserPasswordResponse:
        client = self._require_client()
        return await self._execute(client.admin_set_user_password, request, CognitoIDPAdminSetUserPasswordResponse)

    async def admin_set_user_settings(
        self,
        request: CognitoIDPAdminSetUserSettingsRequest,
    ) -> CognitoIDPAdminSetUserSettingsResponse:
        client = self._require_client()
        return await self._execute(client.admin_set_user_settings, request, CognitoIDPAdminSetUserSettingsResponse)

    async def admin_update_auth_event_feedback(
        self,
        request: CognitoIDPAdminUpdateAuthEventFeedbackRequest,
    ) -> CognitoIDPAdminUpdateAuthEventFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.admin_update_auth_event_feedback, request, CognitoIDPAdminUpdateAuthEventFeedbackResponse)

    async def admin_update_device_status(
        self,
        request: CognitoIDPAdminUpdateDeviceStatusRequest,
    ) -> CognitoIDPAdminUpdateDeviceStatusResponse:
        client = self._require_client()
        return await self._execute(client.admin_update_device_status, request, CognitoIDPAdminUpdateDeviceStatusResponse)

    async def admin_update_user_attributes(
        self,
        request: CognitoIDPAdminUpdateUserAttributesRequest,
    ) -> CognitoIDPAdminUpdateUserAttributesResponse:
        client = self._require_client()
        return await self._execute(client.admin_update_user_attributes, request, CognitoIDPAdminUpdateUserAttributesResponse)

    async def admin_user_global_sign_out(
        self,
        request: CognitoIDPAdminUserGlobalSignOutRequest,
    ) -> CognitoIDPAdminUserGlobalSignOutResponse:
        client = self._require_client()
        return await self._execute(client.admin_user_global_sign_out, request, CognitoIDPAdminUserGlobalSignOutResponse)

    async def associate_software_token(
        self,
        request: CognitoIDPAssociateSoftwareTokenRequest | None = None,
    ) -> CognitoIDPAssociateSoftwareTokenResponse:
        client = self._require_client()
        return await self._execute(client.associate_software_token, request, CognitoIDPAssociateSoftwareTokenResponse)

    async def cancel_point_in_time_recovery(
        self,
        request: CognitoIDPCancelPointInTimeRecoveryRequest,
    ) -> CognitoIDPCancelPointInTimeRecoveryResponse:
        client = self._require_client()
        return await self._execute(client.cancel_point_in_time_recovery, request, CognitoIDPCancelPointInTimeRecoveryResponse)

    async def change_password(
        self,
        request: CognitoIDPChangePasswordRequest,
    ) -> CognitoIDPChangePasswordResponse:
        client = self._require_client()
        return await self._execute(client.change_password, request, CognitoIDPChangePasswordResponse)

    async def complete_web_authn_registration(
        self,
        request: CognitoIDPCompleteWebAuthnRegistrationRequest,
    ) -> CognitoIDPCompleteWebAuthnRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.complete_web_authn_registration, request, CognitoIDPCompleteWebAuthnRegistrationResponse)

    async def confirm_device(
        self,
        request: CognitoIDPConfirmDeviceRequest,
    ) -> CognitoIDPConfirmDeviceResponse:
        client = self._require_client()
        return await self._execute(client.confirm_device, request, CognitoIDPConfirmDeviceResponse)

    async def confirm_forgot_password(
        self,
        request: CognitoIDPConfirmForgotPasswordRequest,
    ) -> CognitoIDPConfirmForgotPasswordResponse:
        client = self._require_client()
        return await self._execute(client.confirm_forgot_password, request, CognitoIDPConfirmForgotPasswordResponse)

    async def confirm_sign_up(
        self,
        request: CognitoIDPConfirmSignUpRequest,
    ) -> CognitoIDPConfirmSignUpResponse:
        client = self._require_client()
        return await self._execute(client.confirm_sign_up, request, CognitoIDPConfirmSignUpResponse)

    async def create_cimd_policy(
        self,
        request: CognitoIDPCreateCIMDPolicyRequest,
    ) -> CognitoIDPCreateCIMDPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_cimd_policy, request, CognitoIDPCreateCIMDPolicyResponse)

    async def create_group(
        self,
        request: CognitoIDPCreateGroupRequest,
    ) -> CognitoIDPCreateGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_group, request, CognitoIDPCreateGroupResponse)

    async def create_identity_provider(
        self,
        request: CognitoIDPCreateIdentityProviderRequest,
    ) -> CognitoIDPCreateIdentityProviderResponse:
        client = self._require_client()
        return await self._execute(client.create_identity_provider, request, CognitoIDPCreateIdentityProviderResponse)

    async def create_managed_login_branding(
        self,
        request: CognitoIDPCreateManagedLoginBrandingRequest,
    ) -> CognitoIDPCreateManagedLoginBrandingResponse:
        client = self._require_client()
        return await self._execute(client.create_managed_login_branding, request, CognitoIDPCreateManagedLoginBrandingResponse)

    async def create_resource_server(
        self,
        request: CognitoIDPCreateResourceServerRequest,
    ) -> CognitoIDPCreateResourceServerResponse:
        client = self._require_client()
        return await self._execute(client.create_resource_server, request, CognitoIDPCreateResourceServerResponse)

    async def create_terms(
        self,
        request: CognitoIDPCreateTermsRequest,
    ) -> CognitoIDPCreateTermsResponse:
        client = self._require_client()
        return await self._execute(client.create_terms, request, CognitoIDPCreateTermsResponse)

    async def create_user_import_job(
        self,
        request: CognitoIDPCreateUserImportJobRequest,
    ) -> CognitoIDPCreateUserImportJobResponse:
        client = self._require_client()
        return await self._execute(client.create_user_import_job, request, CognitoIDPCreateUserImportJobResponse)

    async def create_user_pool(
        self,
        request: CognitoIDPCreateUserPoolRequest,
    ) -> CognitoIDPCreateUserPoolResponse:
        client = self._require_client()
        return await self._execute(client.create_user_pool, request, CognitoIDPCreateUserPoolResponse)

    async def create_user_pool_client(
        self,
        request: CognitoIDPCreateUserPoolClientRequest,
    ) -> CognitoIDPCreateUserPoolClientResponse:
        client = self._require_client()
        return await self._execute(client.create_user_pool_client, request, CognitoIDPCreateUserPoolClientResponse)

    async def create_user_pool_domain(
        self,
        request: CognitoIDPCreateUserPoolDomainRequest,
    ) -> CognitoIDPCreateUserPoolDomainResponse:
        client = self._require_client()
        return await self._execute(client.create_user_pool_domain, request, CognitoIDPCreateUserPoolDomainResponse)

    async def create_user_pool_replica(
        self,
        request: CognitoIDPCreateUserPoolReplicaRequest,
    ) -> CognitoIDPCreateUserPoolReplicaResponse:
        client = self._require_client()
        return await self._execute(client.create_user_pool_replica, request, CognitoIDPCreateUserPoolReplicaResponse)

    async def delete_cimd_policy(
        self,
        request: CognitoIDPDeleteCIMDPolicyRequest,
    ) -> CognitoIDPDeleteCIMDPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_cimd_policy, request, CognitoIDPDeleteCIMDPolicyResponse)

    async def delete_group(
        self,
        request: CognitoIDPDeleteGroupRequest,
    ) -> CognitoIDPDeleteGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_group, request, CognitoIDPDeleteGroupResponse)

    async def delete_identity_provider(
        self,
        request: CognitoIDPDeleteIdentityProviderRequest,
    ) -> CognitoIDPDeleteIdentityProviderResponse:
        client = self._require_client()
        return await self._execute(client.delete_identity_provider, request, CognitoIDPDeleteIdentityProviderResponse)

    async def delete_managed_login_branding(
        self,
        request: CognitoIDPDeleteManagedLoginBrandingRequest,
    ) -> CognitoIDPDeleteManagedLoginBrandingResponse:
        client = self._require_client()
        return await self._execute(client.delete_managed_login_branding, request, CognitoIDPDeleteManagedLoginBrandingResponse)

    async def delete_resource_server(
        self,
        request: CognitoIDPDeleteResourceServerRequest,
    ) -> CognitoIDPDeleteResourceServerResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_server, request, CognitoIDPDeleteResourceServerResponse)

    async def delete_terms(
        self,
        request: CognitoIDPDeleteTermsRequest,
    ) -> CognitoIDPDeleteTermsResponse:
        client = self._require_client()
        return await self._execute(client.delete_terms, request, CognitoIDPDeleteTermsResponse)

    async def delete_user(
        self,
        request: CognitoIDPDeleteUserRequest,
    ) -> CognitoIDPDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.delete_user, request, CognitoIDPDeleteUserResponse)

    async def delete_user_attributes(
        self,
        request: CognitoIDPDeleteUserAttributesRequest,
    ) -> CognitoIDPDeleteUserAttributesResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_attributes, request, CognitoIDPDeleteUserAttributesResponse)

    async def delete_user_pool(
        self,
        request: CognitoIDPDeleteUserPoolRequest,
    ) -> CognitoIDPDeleteUserPoolResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_pool, request, CognitoIDPDeleteUserPoolResponse)

    async def delete_user_pool_client(
        self,
        request: CognitoIDPDeleteUserPoolClientRequest,
    ) -> CognitoIDPDeleteUserPoolClientResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_pool_client, request, CognitoIDPDeleteUserPoolClientResponse)

    async def delete_user_pool_client_secret(
        self,
        request: CognitoIDPDeleteUserPoolClientSecretRequest,
    ) -> CognitoIDPDeleteUserPoolClientSecretResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_pool_client_secret, request, CognitoIDPDeleteUserPoolClientSecretResponse)

    async def delete_user_pool_domain(
        self,
        request: CognitoIDPDeleteUserPoolDomainRequest,
    ) -> CognitoIDPDeleteUserPoolDomainResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_pool_domain, request, CognitoIDPDeleteUserPoolDomainResponse)

    async def delete_user_pool_replica(
        self,
        request: CognitoIDPDeleteUserPoolReplicaRequest,
    ) -> CognitoIDPDeleteUserPoolReplicaResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_pool_replica, request, CognitoIDPDeleteUserPoolReplicaResponse)

    async def delete_web_authn_credential(
        self,
        request: CognitoIDPDeleteWebAuthnCredentialRequest,
    ) -> CognitoIDPDeleteWebAuthnCredentialResponse:
        client = self._require_client()
        return await self._execute(client.delete_web_authn_credential, request, CognitoIDPDeleteWebAuthnCredentialResponse)

    async def describe_cimd_policy(
        self,
        request: CognitoIDPDescribeCIMDPolicyRequest,
    ) -> CognitoIDPDescribeCIMDPolicyResponse:
        client = self._require_client()
        return await self._execute(client.describe_cimd_policy, request, CognitoIDPDescribeCIMDPolicyResponse)

    async def describe_identity_provider(
        self,
        request: CognitoIDPDescribeIdentityProviderRequest,
    ) -> CognitoIDPDescribeIdentityProviderResponse:
        client = self._require_client()
        return await self._execute(client.describe_identity_provider, request, CognitoIDPDescribeIdentityProviderResponse)

    async def describe_managed_login_branding(
        self,
        request: CognitoIDPDescribeManagedLoginBrandingRequest,
    ) -> CognitoIDPDescribeManagedLoginBrandingResponse:
        client = self._require_client()
        return await self._execute(client.describe_managed_login_branding, request, CognitoIDPDescribeManagedLoginBrandingResponse)

    async def describe_managed_login_branding_by_client(
        self,
        request: CognitoIDPDescribeManagedLoginBrandingByClientRequest,
    ) -> CognitoIDPDescribeManagedLoginBrandingByClientResponse:
        client = self._require_client()
        return await self._execute(client.describe_managed_login_branding_by_client, request, CognitoIDPDescribeManagedLoginBrandingByClientResponse)

    async def describe_point_in_time_recovery(
        self,
        request: CognitoIDPDescribePointInTimeRecoveryRequest,
    ) -> CognitoIDPDescribePointInTimeRecoveryResponse:
        client = self._require_client()
        return await self._execute(client.describe_point_in_time_recovery, request, CognitoIDPDescribePointInTimeRecoveryResponse)

    async def describe_resource_server(
        self,
        request: CognitoIDPDescribeResourceServerRequest,
    ) -> CognitoIDPDescribeResourceServerResponse:
        client = self._require_client()
        return await self._execute(client.describe_resource_server, request, CognitoIDPDescribeResourceServerResponse)

    async def describe_risk_configuration(
        self,
        request: CognitoIDPDescribeRiskConfigurationRequest,
    ) -> CognitoIDPDescribeRiskConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_risk_configuration, request, CognitoIDPDescribeRiskConfigurationResponse)

    async def describe_terms(
        self,
        request: CognitoIDPDescribeTermsRequest,
    ) -> CognitoIDPDescribeTermsResponse:
        client = self._require_client()
        return await self._execute(client.describe_terms, request, CognitoIDPDescribeTermsResponse)

    async def describe_terms_by_client(
        self,
        request: CognitoIDPDescribeTermsByClientRequest,
    ) -> CognitoIDPDescribeTermsByClientResponse:
        client = self._require_client()
        return await self._execute(client.describe_terms_by_client, request, CognitoIDPDescribeTermsByClientResponse)

    async def describe_user_import_job(
        self,
        request: CognitoIDPDescribeUserImportJobRequest,
    ) -> CognitoIDPDescribeUserImportJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_user_import_job, request, CognitoIDPDescribeUserImportJobResponse)

    async def describe_user_pool(
        self,
        request: CognitoIDPDescribeUserPoolRequest,
    ) -> CognitoIDPDescribeUserPoolResponse:
        client = self._require_client()
        return await self._execute(client.describe_user_pool, request, CognitoIDPDescribeUserPoolResponse)

    async def describe_user_pool_client(
        self,
        request: CognitoIDPDescribeUserPoolClientRequest,
    ) -> CognitoIDPDescribeUserPoolClientResponse:
        client = self._require_client()
        return await self._execute(client.describe_user_pool_client, request, CognitoIDPDescribeUserPoolClientResponse)

    async def describe_user_pool_domain(
        self,
        request: CognitoIDPDescribeUserPoolDomainRequest,
    ) -> CognitoIDPDescribeUserPoolDomainResponse:
        client = self._require_client()
        return await self._execute(client.describe_user_pool_domain, request, CognitoIDPDescribeUserPoolDomainResponse)

    async def forget_device(
        self,
        request: CognitoIDPForgetDeviceRequest,
    ) -> CognitoIDPForgetDeviceResponse:
        client = self._require_client()
        return await self._execute(client.forget_device, request, CognitoIDPForgetDeviceResponse)

    async def forgot_password(
        self,
        request: CognitoIDPForgotPasswordRequest,
    ) -> CognitoIDPForgotPasswordResponse:
        client = self._require_client()
        return await self._execute(client.forgot_password, request, CognitoIDPForgotPasswordResponse)

    async def get_csv_header(
        self,
        request: CognitoIDPGetCSVHeaderRequest,
    ) -> CognitoIDPGetCSVHeaderResponse:
        client = self._require_client()
        return await self._execute(client.get_csv_header, request, CognitoIDPGetCSVHeaderResponse)

    async def get_client_token(
        self,
        request: CognitoIDPGetClientTokenRequest,
    ) -> CognitoIDPGetClientTokenResponse:
        client = self._require_client()
        return await self._execute(client.get_client_token, request, CognitoIDPGetClientTokenResponse)

    async def get_derived_token(
        self,
        request: CognitoIDPGetDerivedTokenRequest,
    ) -> CognitoIDPGetDerivedTokenResponse:
        client = self._require_client()
        return await self._execute(client.get_derived_token, request, CognitoIDPGetDerivedTokenResponse)

    async def get_device(
        self,
        request: CognitoIDPGetDeviceRequest,
    ) -> CognitoIDPGetDeviceResponse:
        client = self._require_client()
        return await self._execute(client.get_device, request, CognitoIDPGetDeviceResponse)

    async def get_group(
        self,
        request: CognitoIDPGetGroupRequest,
    ) -> CognitoIDPGetGroupResponse:
        client = self._require_client()
        return await self._execute(client.get_group, request, CognitoIDPGetGroupResponse)

    async def get_identity_provider_by_identifier(
        self,
        request: CognitoIDPGetIdentityProviderByIdentifierRequest,
    ) -> CognitoIDPGetIdentityProviderByIdentifierResponse:
        client = self._require_client()
        return await self._execute(client.get_identity_provider_by_identifier, request, CognitoIDPGetIdentityProviderByIdentifierResponse)

    async def get_log_delivery_configuration(
        self,
        request: CognitoIDPGetLogDeliveryConfigurationRequest,
    ) -> CognitoIDPGetLogDeliveryConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_log_delivery_configuration, request, CognitoIDPGetLogDeliveryConfigurationResponse)

    async def get_provisioned_limit(
        self,
        request: CognitoIDPGetProvisionedLimitRequest,
    ) -> CognitoIDPGetProvisionedLimitResponse:
        client = self._require_client()
        return await self._execute(client.get_provisioned_limit, request, CognitoIDPGetProvisionedLimitResponse)

    async def get_signing_certificate(
        self,
        request: CognitoIDPGetSigningCertificateRequest,
    ) -> CognitoIDPGetSigningCertificateResponse:
        client = self._require_client()
        return await self._execute(client.get_signing_certificate, request, CognitoIDPGetSigningCertificateResponse)

    async def get_tokens_from_refresh_token(
        self,
        request: CognitoIDPGetTokensFromRefreshTokenRequest,
    ) -> CognitoIDPGetTokensFromRefreshTokenResponse:
        client = self._require_client()
        return await self._execute(client.get_tokens_from_refresh_token, request, CognitoIDPGetTokensFromRefreshTokenResponse)

    async def get_ui_customization(
        self,
        request: CognitoIDPGetUICustomizationRequest,
    ) -> CognitoIDPGetUICustomizationResponse:
        client = self._require_client()
        return await self._execute(client.get_ui_customization, request, CognitoIDPGetUICustomizationResponse)

    async def get_user(
        self,
        request: CognitoIDPGetUserRequest,
    ) -> CognitoIDPGetUserResponse:
        client = self._require_client()
        return await self._execute(client.get_user, request, CognitoIDPGetUserResponse)

    async def get_user_attribute_verification_code(
        self,
        request: CognitoIDPGetUserAttributeVerificationCodeRequest,
    ) -> CognitoIDPGetUserAttributeVerificationCodeResponse:
        client = self._require_client()
        return await self._execute(client.get_user_attribute_verification_code, request, CognitoIDPGetUserAttributeVerificationCodeResponse)

    async def get_user_auth_factors(
        self,
        request: CognitoIDPGetUserAuthFactorsRequest,
    ) -> CognitoIDPGetUserAuthFactorsResponse:
        client = self._require_client()
        return await self._execute(client.get_user_auth_factors, request, CognitoIDPGetUserAuthFactorsResponse)

    async def get_user_pool_client_session_configuration(
        self,
        request: CognitoIDPGetUserPoolClientSessionConfigurationRequest,
    ) -> CognitoIDPGetUserPoolClientSessionConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_user_pool_client_session_configuration, request, CognitoIDPGetUserPoolClientSessionConfigurationResponse)

    async def get_user_pool_mfa_config(
        self,
        request: CognitoIDPGetUserPoolMfaConfigRequest,
    ) -> CognitoIDPGetUserPoolMfaConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_user_pool_mfa_config, request, CognitoIDPGetUserPoolMfaConfigResponse)

    async def get_user_pool_session_configuration(
        self,
        request: CognitoIDPGetUserPoolSessionConfigurationRequest,
    ) -> CognitoIDPGetUserPoolSessionConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_user_pool_session_configuration, request, CognitoIDPGetUserPoolSessionConfigurationResponse)

    async def global_sign_out(
        self,
        request: CognitoIDPGlobalSignOutRequest,
    ) -> CognitoIDPGlobalSignOutResponse:
        client = self._require_client()
        return await self._execute(client.global_sign_out, request, CognitoIDPGlobalSignOutResponse)

    async def initiate_auth(
        self,
        request: CognitoIDPInitiateAuthRequest,
    ) -> CognitoIDPInitiateAuthResponse:
        client = self._require_client()
        return await self._execute(client.initiate_auth, request, CognitoIDPInitiateAuthResponse)

    async def initiate_point_in_time_recovery(
        self,
        request: CognitoIDPInitiatePointInTimeRecoveryRequest,
    ) -> CognitoIDPInitiatePointInTimeRecoveryResponse:
        client = self._require_client()
        return await self._execute(client.initiate_point_in_time_recovery, request, CognitoIDPInitiatePointInTimeRecoveryResponse)

    async def list_cimd_policies(
        self,
        request: CognitoIDPListCIMDPoliciesRequest,
    ) -> CognitoIDPListCIMDPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_cimd_policies, request, CognitoIDPListCIMDPoliciesResponse)

    async def list_cimd_policies_paginated(
        self,
        request: CognitoIDPListCIMDPoliciesRequest,
    ) -> list[CognitoIDPListCIMDPoliciesResponse]:
        return await self._paginate('list_cimd_policies', request, CognitoIDPListCIMDPoliciesResponse)

    async def list_client_metadata_urls(
        self,
        request: CognitoIDPListClientMetadataURLsRequest,
    ) -> CognitoIDPListClientMetadataURLsResponse:
        client = self._require_client()
        return await self._execute(client.list_client_metadata_urls, request, CognitoIDPListClientMetadataURLsResponse)

    async def list_client_metadata_urls_paginated(
        self,
        request: CognitoIDPListClientMetadataURLsRequest,
    ) -> list[CognitoIDPListClientMetadataURLsResponse]:
        return await self._paginate('list_client_metadata_urls', request, CognitoIDPListClientMetadataURLsResponse)

    async def list_devices(
        self,
        request: CognitoIDPListDevicesRequest,
    ) -> CognitoIDPListDevicesResponse:
        client = self._require_client()
        return await self._execute(client.list_devices, request, CognitoIDPListDevicesResponse)

    async def list_groups(
        self,
        request: CognitoIDPListGroupsRequest,
    ) -> CognitoIDPListGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_groups, request, CognitoIDPListGroupsResponse)

    async def list_groups_paginated(
        self,
        request: CognitoIDPListGroupsRequest,
    ) -> list[CognitoIDPListGroupsResponse]:
        return await self._paginate('list_groups', request, CognitoIDPListGroupsResponse)

    async def list_identity_providers(
        self,
        request: CognitoIDPListIdentityProvidersRequest,
    ) -> CognitoIDPListIdentityProvidersResponse:
        client = self._require_client()
        return await self._execute(client.list_identity_providers, request, CognitoIDPListIdentityProvidersResponse)

    async def list_identity_providers_paginated(
        self,
        request: CognitoIDPListIdentityProvidersRequest,
    ) -> list[CognitoIDPListIdentityProvidersResponse]:
        return await self._paginate('list_identity_providers', request, CognitoIDPListIdentityProvidersResponse)

    async def list_point_in_time_recoveries(
        self,
        request: CognitoIDPListPointInTimeRecoveriesRequest,
    ) -> CognitoIDPListPointInTimeRecoveriesResponse:
        client = self._require_client()
        return await self._execute(client.list_point_in_time_recoveries, request, CognitoIDPListPointInTimeRecoveriesResponse)

    async def list_resource_servers(
        self,
        request: CognitoIDPListResourceServersRequest,
    ) -> CognitoIDPListResourceServersResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_servers, request, CognitoIDPListResourceServersResponse)

    async def list_resource_servers_paginated(
        self,
        request: CognitoIDPListResourceServersRequest,
    ) -> list[CognitoIDPListResourceServersResponse]:
        return await self._paginate('list_resource_servers', request, CognitoIDPListResourceServersResponse)

    async def list_tags_for_resource(
        self,
        request: CognitoIDPListTagsForResourceRequest,
    ) -> CognitoIDPListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, CognitoIDPListTagsForResourceResponse)

    async def list_terms(
        self,
        request: CognitoIDPListTermsRequest,
    ) -> CognitoIDPListTermsResponse:
        client = self._require_client()
        return await self._execute(client.list_terms, request, CognitoIDPListTermsResponse)

    async def list_user_import_jobs(
        self,
        request: CognitoIDPListUserImportJobsRequest,
    ) -> CognitoIDPListUserImportJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_user_import_jobs, request, CognitoIDPListUserImportJobsResponse)

    async def list_user_pool_client_secrets(
        self,
        request: CognitoIDPListUserPoolClientSecretsRequest,
    ) -> CognitoIDPListUserPoolClientSecretsResponse:
        client = self._require_client()
        return await self._execute(client.list_user_pool_client_secrets, request, CognitoIDPListUserPoolClientSecretsResponse)

    async def list_user_pool_clients(
        self,
        request: CognitoIDPListUserPoolClientsRequest,
    ) -> CognitoIDPListUserPoolClientsResponse:
        client = self._require_client()
        return await self._execute(client.list_user_pool_clients, request, CognitoIDPListUserPoolClientsResponse)

    async def list_user_pool_clients_paginated(
        self,
        request: CognitoIDPListUserPoolClientsRequest,
    ) -> list[CognitoIDPListUserPoolClientsResponse]:
        return await self._paginate('list_user_pool_clients', request, CognitoIDPListUserPoolClientsResponse)

    async def list_user_pool_replicas(
        self,
        request: CognitoIDPListUserPoolReplicasRequest,
    ) -> CognitoIDPListUserPoolReplicasResponse:
        client = self._require_client()
        return await self._execute(client.list_user_pool_replicas, request, CognitoIDPListUserPoolReplicasResponse)

    async def list_user_pools(
        self,
        request: CognitoIDPListUserPoolsRequest,
    ) -> CognitoIDPListUserPoolsResponse:
        client = self._require_client()
        return await self._execute(client.list_user_pools, request, CognitoIDPListUserPoolsResponse)

    async def list_user_pools_paginated(
        self,
        request: CognitoIDPListUserPoolsRequest,
    ) -> list[CognitoIDPListUserPoolsResponse]:
        return await self._paginate('list_user_pools', request, CognitoIDPListUserPoolsResponse)

    async def list_user_sessions(
        self,
        request: CognitoIDPListUserSessionsRequest,
    ) -> CognitoIDPListUserSessionsResponse:
        client = self._require_client()
        return await self._execute(client.list_user_sessions, request, CognitoIDPListUserSessionsResponse)

    async def list_users(
        self,
        request: CognitoIDPListUsersRequest,
    ) -> CognitoIDPListUsersResponse:
        client = self._require_client()
        return await self._execute(client.list_users, request, CognitoIDPListUsersResponse)

    async def list_users_paginated(
        self,
        request: CognitoIDPListUsersRequest,
    ) -> list[CognitoIDPListUsersResponse]:
        return await self._paginate('list_users', request, CognitoIDPListUsersResponse)

    async def list_users_in_group(
        self,
        request: CognitoIDPListUsersInGroupRequest,
    ) -> CognitoIDPListUsersInGroupResponse:
        client = self._require_client()
        return await self._execute(client.list_users_in_group, request, CognitoIDPListUsersInGroupResponse)

    async def list_users_in_group_paginated(
        self,
        request: CognitoIDPListUsersInGroupRequest,
    ) -> list[CognitoIDPListUsersInGroupResponse]:
        return await self._paginate('list_users_in_group', request, CognitoIDPListUsersInGroupResponse)

    async def list_web_authn_credentials(
        self,
        request: CognitoIDPListWebAuthnCredentialsRequest,
    ) -> CognitoIDPListWebAuthnCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.list_web_authn_credentials, request, CognitoIDPListWebAuthnCredentialsResponse)

    async def resend_confirmation_code(
        self,
        request: CognitoIDPResendConfirmationCodeRequest,
    ) -> CognitoIDPResendConfirmationCodeResponse:
        client = self._require_client()
        return await self._execute(client.resend_confirmation_code, request, CognitoIDPResendConfirmationCodeResponse)

    async def respond_to_auth_challenge(
        self,
        request: CognitoIDPRespondToAuthChallengeRequest,
    ) -> CognitoIDPRespondToAuthChallengeResponse:
        client = self._require_client()
        return await self._execute(client.respond_to_auth_challenge, request, CognitoIDPRespondToAuthChallengeResponse)

    async def revoke_token(
        self,
        request: CognitoIDPRevokeTokenRequest,
    ) -> CognitoIDPRevokeTokenResponse:
        client = self._require_client()
        return await self._execute(client.revoke_token, request, CognitoIDPRevokeTokenResponse)

    async def revoke_user_session(
        self,
        request: CognitoIDPRevokeUserSessionRequest,
    ) -> CognitoIDPRevokeUserSessionResponse:
        client = self._require_client()
        return await self._execute(client.revoke_user_session, request, CognitoIDPRevokeUserSessionResponse)

    async def set_log_delivery_configuration(
        self,
        request: CognitoIDPSetLogDeliveryConfigurationRequest,
    ) -> CognitoIDPSetLogDeliveryConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.set_log_delivery_configuration, request, CognitoIDPSetLogDeliveryConfigurationResponse)

    async def set_risk_configuration(
        self,
        request: CognitoIDPSetRiskConfigurationRequest,
    ) -> CognitoIDPSetRiskConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.set_risk_configuration, request, CognitoIDPSetRiskConfigurationResponse)

    async def set_ui_customization(
        self,
        request: CognitoIDPSetUICustomizationRequest,
    ) -> CognitoIDPSetUICustomizationResponse:
        client = self._require_client()
        return await self._execute(client.set_ui_customization, request, CognitoIDPSetUICustomizationResponse)

    async def set_user_mfa_preference(
        self,
        request: CognitoIDPSetUserMFAPreferenceRequest,
    ) -> CognitoIDPSetUserMFAPreferenceResponse:
        client = self._require_client()
        return await self._execute(client.set_user_mfa_preference, request, CognitoIDPSetUserMFAPreferenceResponse)

    async def set_user_pool_client_session_configuration(
        self,
        request: CognitoIDPSetUserPoolClientSessionConfigurationRequest,
    ) -> CognitoIDPSetUserPoolClientSessionConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.set_user_pool_client_session_configuration, request, CognitoIDPSetUserPoolClientSessionConfigurationResponse)

    async def set_user_pool_mfa_config(
        self,
        request: CognitoIDPSetUserPoolMfaConfigRequest,
    ) -> CognitoIDPSetUserPoolMfaConfigResponse:
        client = self._require_client()
        return await self._execute(client.set_user_pool_mfa_config, request, CognitoIDPSetUserPoolMfaConfigResponse)

    async def set_user_pool_session_configuration(
        self,
        request: CognitoIDPSetUserPoolSessionConfigurationRequest,
    ) -> CognitoIDPSetUserPoolSessionConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.set_user_pool_session_configuration, request, CognitoIDPSetUserPoolSessionConfigurationResponse)

    async def set_user_settings(
        self,
        request: CognitoIDPSetUserSettingsRequest,
    ) -> CognitoIDPSetUserSettingsResponse:
        client = self._require_client()
        return await self._execute(client.set_user_settings, request, CognitoIDPSetUserSettingsResponse)

    async def sign_up(
        self,
        request: CognitoIDPSignUpRequest,
    ) -> CognitoIDPSignUpResponse:
        client = self._require_client()
        return await self._execute(client.sign_up, request, CognitoIDPSignUpResponse)

    async def start_point_in_time_recovery(
        self,
        request: CognitoIDPStartPointInTimeRecoveryRequest,
    ) -> CognitoIDPStartPointInTimeRecoveryResponse:
        client = self._require_client()
        return await self._execute(client.start_point_in_time_recovery, request, CognitoIDPStartPointInTimeRecoveryResponse)

    async def start_user_import_job(
        self,
        request: CognitoIDPStartUserImportJobRequest,
    ) -> CognitoIDPStartUserImportJobResponse:
        client = self._require_client()
        return await self._execute(client.start_user_import_job, request, CognitoIDPStartUserImportJobResponse)

    async def start_web_authn_registration(
        self,
        request: CognitoIDPStartWebAuthnRegistrationRequest,
    ) -> CognitoIDPStartWebAuthnRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.start_web_authn_registration, request, CognitoIDPStartWebAuthnRegistrationResponse)

    async def stop_user_import_job(
        self,
        request: CognitoIDPStopUserImportJobRequest,
    ) -> CognitoIDPStopUserImportJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_user_import_job, request, CognitoIDPStopUserImportJobResponse)

    async def tag_resource(
        self,
        request: CognitoIDPTagResourceRequest,
    ) -> CognitoIDPTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, CognitoIDPTagResourceResponse)

    async def untag_resource(
        self,
        request: CognitoIDPUntagResourceRequest,
    ) -> CognitoIDPUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, CognitoIDPUntagResourceResponse)

    async def update_auth_event_feedback(
        self,
        request: CognitoIDPUpdateAuthEventFeedbackRequest,
    ) -> CognitoIDPUpdateAuthEventFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.update_auth_event_feedback, request, CognitoIDPUpdateAuthEventFeedbackResponse)

    async def update_cimd_policy(
        self,
        request: CognitoIDPUpdateCIMDPolicyRequest,
    ) -> CognitoIDPUpdateCIMDPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_cimd_policy, request, CognitoIDPUpdateCIMDPolicyResponse)

    async def update_client_metadata_url_state(
        self,
        request: CognitoIDPUpdateClientMetadataURLStateRequest,
    ) -> CognitoIDPUpdateClientMetadataURLStateResponse:
        client = self._require_client()
        return await self._execute(client.update_client_metadata_url_state, request, CognitoIDPUpdateClientMetadataURLStateResponse)

    async def update_device_status(
        self,
        request: CognitoIDPUpdateDeviceStatusRequest,
    ) -> CognitoIDPUpdateDeviceStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_device_status, request, CognitoIDPUpdateDeviceStatusResponse)

    async def update_group(
        self,
        request: CognitoIDPUpdateGroupRequest,
    ) -> CognitoIDPUpdateGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_group, request, CognitoIDPUpdateGroupResponse)

    async def update_identity_provider(
        self,
        request: CognitoIDPUpdateIdentityProviderRequest,
    ) -> CognitoIDPUpdateIdentityProviderResponse:
        client = self._require_client()
        return await self._execute(client.update_identity_provider, request, CognitoIDPUpdateIdentityProviderResponse)

    async def update_managed_login_branding(
        self,
        request: CognitoIDPUpdateManagedLoginBrandingRequest | None = None,
    ) -> CognitoIDPUpdateManagedLoginBrandingResponse:
        client = self._require_client()
        return await self._execute(client.update_managed_login_branding, request, CognitoIDPUpdateManagedLoginBrandingResponse)

    async def update_provisioned_limit(
        self,
        request: CognitoIDPUpdateProvisionedLimitRequest,
    ) -> CognitoIDPUpdateProvisionedLimitResponse:
        client = self._require_client()
        return await self._execute(client.update_provisioned_limit, request, CognitoIDPUpdateProvisionedLimitResponse)

    async def update_resource_server(
        self,
        request: CognitoIDPUpdateResourceServerRequest,
    ) -> CognitoIDPUpdateResourceServerResponse:
        client = self._require_client()
        return await self._execute(client.update_resource_server, request, CognitoIDPUpdateResourceServerResponse)

    async def update_terms(
        self,
        request: CognitoIDPUpdateTermsRequest,
    ) -> CognitoIDPUpdateTermsResponse:
        client = self._require_client()
        return await self._execute(client.update_terms, request, CognitoIDPUpdateTermsResponse)

    async def update_user_attributes(
        self,
        request: CognitoIDPUpdateUserAttributesRequest,
    ) -> CognitoIDPUpdateUserAttributesResponse:
        client = self._require_client()
        return await self._execute(client.update_user_attributes, request, CognitoIDPUpdateUserAttributesResponse)

    async def update_user_pool(
        self,
        request: CognitoIDPUpdateUserPoolRequest,
    ) -> CognitoIDPUpdateUserPoolResponse:
        client = self._require_client()
        return await self._execute(client.update_user_pool, request, CognitoIDPUpdateUserPoolResponse)

    async def update_user_pool_client(
        self,
        request: CognitoIDPUpdateUserPoolClientRequest,
    ) -> CognitoIDPUpdateUserPoolClientResponse:
        client = self._require_client()
        return await self._execute(client.update_user_pool_client, request, CognitoIDPUpdateUserPoolClientResponse)

    async def update_user_pool_domain(
        self,
        request: CognitoIDPUpdateUserPoolDomainRequest,
    ) -> CognitoIDPUpdateUserPoolDomainResponse:
        client = self._require_client()
        return await self._execute(client.update_user_pool_domain, request, CognitoIDPUpdateUserPoolDomainResponse)

    async def update_user_pool_replica(
        self,
        request: CognitoIDPUpdateUserPoolReplicaRequest,
    ) -> CognitoIDPUpdateUserPoolReplicaResponse:
        client = self._require_client()
        return await self._execute(client.update_user_pool_replica, request, CognitoIDPUpdateUserPoolReplicaResponse)

    async def verify_software_token(
        self,
        request: CognitoIDPVerifySoftwareTokenRequest,
    ) -> CognitoIDPVerifySoftwareTokenResponse:
        client = self._require_client()
        return await self._execute(client.verify_software_token, request, CognitoIDPVerifySoftwareTokenResponse)

    async def verify_user_attribute(
        self,
        request: CognitoIDPVerifyUserAttributeRequest,
    ) -> CognitoIDPVerifyUserAttributeResponse:
        client = self._require_client()
        return await self._execute(client.verify_user_attribute, request, CognitoIDPVerifyUserAttributeResponse)
