from werkflow_aws.models.transfer_family import (
    TransferCreateAccessRequest,
    TransferCreateAccessResponse,
    TransferCreateAgreementRequest,
    TransferCreateAgreementResponse,
    TransferCreateConnectorRequest,
    TransferCreateConnectorResponse,
    TransferCreateProfileRequest,
    TransferCreateProfileResponse,
    TransferCreateServerRequest,
    TransferCreateServerResponse,
    TransferCreateUserRequest,
    TransferCreateUserResponse,
    TransferCreateWebAppRequest,
    TransferCreateWebAppResponse,
    TransferCreateWorkflowRequest,
    TransferCreateWorkflowResponse,
    TransferDeleteAccessRequest,
    TransferDeleteAccessResponse,
    TransferDeleteAgreementRequest,
    TransferDeleteAgreementResponse,
    TransferDeleteCertificateRequest,
    TransferDeleteCertificateResponse,
    TransferDeleteConnectorRequest,
    TransferDeleteConnectorResponse,
    TransferDeleteHostKeyRequest,
    TransferDeleteHostKeyResponse,
    TransferDeleteProfileRequest,
    TransferDeleteProfileResponse,
    TransferDeleteServerRequest,
    TransferDeleteServerResponse,
    TransferDeleteSshPublicKeyRequest,
    TransferDeleteSshPublicKeyResponse,
    TransferDeleteUserRequest,
    TransferDeleteUserResponse,
    TransferDeleteWebAppCustomizationRequest,
    TransferDeleteWebAppCustomizationResponse,
    TransferDeleteWebAppRequest,
    TransferDeleteWebAppResponse,
    TransferDeleteWorkflowRequest,
    TransferDeleteWorkflowResponse,
    TransferDescribeAccessRequest,
    TransferDescribeAccessResponse,
    TransferDescribeAgreementRequest,
    TransferDescribeAgreementResponse,
    TransferDescribeCertificateRequest,
    TransferDescribeCertificateResponse,
    TransferDescribeConnectorRequest,
    TransferDescribeConnectorResponse,
    TransferDescribeExecutionRequest,
    TransferDescribeExecutionResponse,
    TransferDescribeHostKeyRequest,
    TransferDescribeHostKeyResponse,
    TransferDescribeProfileRequest,
    TransferDescribeProfileResponse,
    TransferDescribeSecurityPolicyRequest,
    TransferDescribeSecurityPolicyResponse,
    TransferDescribeServerRequest,
    TransferDescribeServerResponse,
    TransferDescribeUserRequest,
    TransferDescribeUserResponse,
    TransferDescribeWebAppCustomizationRequest,
    TransferDescribeWebAppCustomizationResponse,
    TransferDescribeWebAppRequest,
    TransferDescribeWebAppResponse,
    TransferDescribeWorkflowRequest,
    TransferDescribeWorkflowResponse,
    TransferImportCertificateRequest,
    TransferImportCertificateResponse,
    TransferImportHostKeyRequest,
    TransferImportHostKeyResponse,
    TransferImportSshPublicKeyRequest,
    TransferImportSshPublicKeyResponse,
    TransferListAccessesRequest,
    TransferListAccessesResponse,
    TransferListAgreementsRequest,
    TransferListAgreementsResponse,
    TransferListCertificatesRequest,
    TransferListCertificatesResponse,
    TransferListConnectorsRequest,
    TransferListConnectorsResponse,
    TransferListExecutionsRequest,
    TransferListExecutionsResponse,
    TransferListFileTransferResultsRequest,
    TransferListFileTransferResultsResponse,
    TransferListHostKeysRequest,
    TransferListHostKeysResponse,
    TransferListProfilesRequest,
    TransferListProfilesResponse,
    TransferListSecurityPoliciesRequest,
    TransferListSecurityPoliciesResponse,
    TransferListServersRequest,
    TransferListServersResponse,
    TransferListTagsForResourceRequest,
    TransferListTagsForResourceResponse,
    TransferListUsersRequest,
    TransferListUsersResponse,
    TransferListWebAppsRequest,
    TransferListWebAppsResponse,
    TransferListWorkflowsRequest,
    TransferListWorkflowsResponse,
    TransferSendWorkflowStepStateRequest,
    TransferSendWorkflowStepStateResponse,
    TransferStartDirectoryListingRequest,
    TransferStartDirectoryListingResponse,
    TransferStartFileTransferRequest,
    TransferStartFileTransferResponse,
    TransferStartRemoteDeleteRequest,
    TransferStartRemoteDeleteResponse,
    TransferStartRemoteMoveRequest,
    TransferStartRemoteMoveResponse,
    TransferStartServerRequest,
    TransferStartServerResponse,
    TransferStopServerRequest,
    TransferStopServerResponse,
    TransferTagResourceRequest,
    TransferTagResourceResponse,
    TransferTestConnectionRequest,
    TransferTestConnectionResponse,
    TransferTestIdentityProviderRequest,
    TransferTestIdentityProviderResponse,
    TransferUntagResourceRequest,
    TransferUntagResourceResponse,
    TransferUpdateAccessRequest,
    TransferUpdateAccessResponse,
    TransferUpdateAgreementRequest,
    TransferUpdateAgreementResponse,
    TransferUpdateCertificateRequest,
    TransferUpdateCertificateResponse,
    TransferUpdateConnectorRequest,
    TransferUpdateConnectorResponse,
    TransferUpdateHostKeyRequest,
    TransferUpdateHostKeyResponse,
    TransferUpdateProfileRequest,
    TransferUpdateProfileResponse,
    TransferUpdateServerRequest,
    TransferUpdateServerResponse,
    TransferUpdateUserRequest,
    TransferUpdateUserResponse,
    TransferUpdateWebAppCustomizationRequest,
    TransferUpdateWebAppCustomizationResponse,
    TransferUpdateWebAppRequest,
    TransferUpdateWebAppResponse,
)
from werkflow_aws.types.transfer_family_client import TransferClient
from .base import AWSBaseService


class AWSTransfer(AWSBaseService[TransferClient]):
    service_name = 'transfer-family'
    boto3_service_name = 'transfer'

    def __init__(self) -> None:
        super().__init__(service_name='transfer-family', boto3_service_name='transfer')

    async def create_access(
        self,
        request: TransferCreateAccessRequest,
    ) -> TransferCreateAccessResponse:
        client = self._require_client()
        return await self._execute(client.create_access, request, TransferCreateAccessResponse)

    async def create_agreement(
        self,
        request: TransferCreateAgreementRequest,
    ) -> TransferCreateAgreementResponse:
        client = self._require_client()
        return await self._execute(client.create_agreement, request, TransferCreateAgreementResponse)

    async def create_connector(
        self,
        request: TransferCreateConnectorRequest,
    ) -> TransferCreateConnectorResponse:
        client = self._require_client()
        return await self._execute(client.create_connector, request, TransferCreateConnectorResponse)

    async def create_profile(
        self,
        request: TransferCreateProfileRequest,
    ) -> TransferCreateProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_profile, request, TransferCreateProfileResponse)

    async def create_server(
        self,
        request: TransferCreateServerRequest | None = None,
    ) -> TransferCreateServerResponse:
        client = self._require_client()
        return await self._execute(client.create_server, request, TransferCreateServerResponse)

    async def create_user(
        self,
        request: TransferCreateUserRequest,
    ) -> TransferCreateUserResponse:
        client = self._require_client()
        return await self._execute(client.create_user, request, TransferCreateUserResponse)

    async def create_web_app(
        self,
        request: TransferCreateWebAppRequest,
    ) -> TransferCreateWebAppResponse:
        client = self._require_client()
        return await self._execute(client.create_web_app, request, TransferCreateWebAppResponse)

    async def create_workflow(
        self,
        request: TransferCreateWorkflowRequest,
    ) -> TransferCreateWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.create_workflow, request, TransferCreateWorkflowResponse)

    async def delete_access(
        self,
        request: TransferDeleteAccessRequest,
    ) -> TransferDeleteAccessResponse:
        client = self._require_client()
        return await self._execute(client.delete_access, request, TransferDeleteAccessResponse)

    async def delete_agreement(
        self,
        request: TransferDeleteAgreementRequest,
    ) -> TransferDeleteAgreementResponse:
        client = self._require_client()
        return await self._execute(client.delete_agreement, request, TransferDeleteAgreementResponse)

    async def delete_certificate(
        self,
        request: TransferDeleteCertificateRequest,
    ) -> TransferDeleteCertificateResponse:
        client = self._require_client()
        return await self._execute(client.delete_certificate, request, TransferDeleteCertificateResponse)

    async def delete_connector(
        self,
        request: TransferDeleteConnectorRequest,
    ) -> TransferDeleteConnectorResponse:
        client = self._require_client()
        return await self._execute(client.delete_connector, request, TransferDeleteConnectorResponse)

    async def delete_host_key(
        self,
        request: TransferDeleteHostKeyRequest,
    ) -> TransferDeleteHostKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_host_key, request, TransferDeleteHostKeyResponse)

    async def delete_profile(
        self,
        request: TransferDeleteProfileRequest,
    ) -> TransferDeleteProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_profile, request, TransferDeleteProfileResponse)

    async def delete_server(
        self,
        request: TransferDeleteServerRequest,
    ) -> TransferDeleteServerResponse:
        client = self._require_client()
        return await self._execute(client.delete_server, request, TransferDeleteServerResponse)

    async def delete_ssh_public_key(
        self,
        request: TransferDeleteSshPublicKeyRequest,
    ) -> TransferDeleteSshPublicKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_ssh_public_key, request, TransferDeleteSshPublicKeyResponse)

    async def delete_user(
        self,
        request: TransferDeleteUserRequest,
    ) -> TransferDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.delete_user, request, TransferDeleteUserResponse)

    async def delete_web_app(
        self,
        request: TransferDeleteWebAppRequest,
    ) -> TransferDeleteWebAppResponse:
        client = self._require_client()
        return await self._execute(client.delete_web_app, request, TransferDeleteWebAppResponse)

    async def delete_web_app_customization(
        self,
        request: TransferDeleteWebAppCustomizationRequest,
    ) -> TransferDeleteWebAppCustomizationResponse:
        client = self._require_client()
        return await self._execute(client.delete_web_app_customization, request, TransferDeleteWebAppCustomizationResponse)

    async def delete_workflow(
        self,
        request: TransferDeleteWorkflowRequest,
    ) -> TransferDeleteWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.delete_workflow, request, TransferDeleteWorkflowResponse)

    async def describe_access(
        self,
        request: TransferDescribeAccessRequest,
    ) -> TransferDescribeAccessResponse:
        client = self._require_client()
        return await self._execute(client.describe_access, request, TransferDescribeAccessResponse)

    async def describe_agreement(
        self,
        request: TransferDescribeAgreementRequest,
    ) -> TransferDescribeAgreementResponse:
        client = self._require_client()
        return await self._execute(client.describe_agreement, request, TransferDescribeAgreementResponse)

    async def describe_certificate(
        self,
        request: TransferDescribeCertificateRequest,
    ) -> TransferDescribeCertificateResponse:
        client = self._require_client()
        return await self._execute(client.describe_certificate, request, TransferDescribeCertificateResponse)

    async def describe_connector(
        self,
        request: TransferDescribeConnectorRequest,
    ) -> TransferDescribeConnectorResponse:
        client = self._require_client()
        return await self._execute(client.describe_connector, request, TransferDescribeConnectorResponse)

    async def describe_execution(
        self,
        request: TransferDescribeExecutionRequest,
    ) -> TransferDescribeExecutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_execution, request, TransferDescribeExecutionResponse)

    async def describe_host_key(
        self,
        request: TransferDescribeHostKeyRequest,
    ) -> TransferDescribeHostKeyResponse:
        client = self._require_client()
        return await self._execute(client.describe_host_key, request, TransferDescribeHostKeyResponse)

    async def describe_profile(
        self,
        request: TransferDescribeProfileRequest,
    ) -> TransferDescribeProfileResponse:
        client = self._require_client()
        return await self._execute(client.describe_profile, request, TransferDescribeProfileResponse)

    async def describe_security_policy(
        self,
        request: TransferDescribeSecurityPolicyRequest,
    ) -> TransferDescribeSecurityPolicyResponse:
        client = self._require_client()
        return await self._execute(client.describe_security_policy, request, TransferDescribeSecurityPolicyResponse)

    async def describe_server(
        self,
        request: TransferDescribeServerRequest,
    ) -> TransferDescribeServerResponse:
        client = self._require_client()
        return await self._execute(client.describe_server, request, TransferDescribeServerResponse)

    async def describe_user(
        self,
        request: TransferDescribeUserRequest,
    ) -> TransferDescribeUserResponse:
        client = self._require_client()
        return await self._execute(client.describe_user, request, TransferDescribeUserResponse)

    async def describe_web_app(
        self,
        request: TransferDescribeWebAppRequest,
    ) -> TransferDescribeWebAppResponse:
        client = self._require_client()
        return await self._execute(client.describe_web_app, request, TransferDescribeWebAppResponse)

    async def describe_web_app_customization(
        self,
        request: TransferDescribeWebAppCustomizationRequest,
    ) -> TransferDescribeWebAppCustomizationResponse:
        client = self._require_client()
        return await self._execute(client.describe_web_app_customization, request, TransferDescribeWebAppCustomizationResponse)

    async def describe_workflow(
        self,
        request: TransferDescribeWorkflowRequest,
    ) -> TransferDescribeWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.describe_workflow, request, TransferDescribeWorkflowResponse)

    async def import_certificate(
        self,
        request: TransferImportCertificateRequest,
    ) -> TransferImportCertificateResponse:
        client = self._require_client()
        return await self._execute(client.import_certificate, request, TransferImportCertificateResponse)

    async def import_host_key(
        self,
        request: TransferImportHostKeyRequest,
    ) -> TransferImportHostKeyResponse:
        client = self._require_client()
        return await self._execute(client.import_host_key, request, TransferImportHostKeyResponse)

    async def import_ssh_public_key(
        self,
        request: TransferImportSshPublicKeyRequest,
    ) -> TransferImportSshPublicKeyResponse:
        client = self._require_client()
        return await self._execute(client.import_ssh_public_key, request, TransferImportSshPublicKeyResponse)

    async def list_accesses(
        self,
        request: TransferListAccessesRequest,
    ) -> TransferListAccessesResponse:
        client = self._require_client()
        return await self._execute(client.list_accesses, request, TransferListAccessesResponse)

    async def list_accesses_paginated(
        self,
        request: TransferListAccessesRequest,
    ) -> list[TransferListAccessesResponse]:
        return await self._paginate('list_accesses', request, TransferListAccessesResponse)

    async def list_agreements(
        self,
        request: TransferListAgreementsRequest,
    ) -> TransferListAgreementsResponse:
        client = self._require_client()
        return await self._execute(client.list_agreements, request, TransferListAgreementsResponse)

    async def list_agreements_paginated(
        self,
        request: TransferListAgreementsRequest,
    ) -> list[TransferListAgreementsResponse]:
        return await self._paginate('list_agreements', request, TransferListAgreementsResponse)

    async def list_certificates(
        self,
        request: TransferListCertificatesRequest | None = None,
    ) -> TransferListCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.list_certificates, request, TransferListCertificatesResponse)

    async def list_certificates_paginated(
        self,
        request: TransferListCertificatesRequest | None = None,
    ) -> list[TransferListCertificatesResponse]:
        return await self._paginate('list_certificates', request, TransferListCertificatesResponse)

    async def list_connectors(
        self,
        request: TransferListConnectorsRequest | None = None,
    ) -> TransferListConnectorsResponse:
        client = self._require_client()
        return await self._execute(client.list_connectors, request, TransferListConnectorsResponse)

    async def list_connectors_paginated(
        self,
        request: TransferListConnectorsRequest | None = None,
    ) -> list[TransferListConnectorsResponse]:
        return await self._paginate('list_connectors', request, TransferListConnectorsResponse)

    async def list_executions(
        self,
        request: TransferListExecutionsRequest,
    ) -> TransferListExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_executions, request, TransferListExecutionsResponse)

    async def list_executions_paginated(
        self,
        request: TransferListExecutionsRequest,
    ) -> list[TransferListExecutionsResponse]:
        return await self._paginate('list_executions', request, TransferListExecutionsResponse)

    async def list_file_transfer_results(
        self,
        request: TransferListFileTransferResultsRequest,
    ) -> TransferListFileTransferResultsResponse:
        client = self._require_client()
        return await self._execute(client.list_file_transfer_results, request, TransferListFileTransferResultsResponse)

    async def list_file_transfer_results_paginated(
        self,
        request: TransferListFileTransferResultsRequest,
    ) -> list[TransferListFileTransferResultsResponse]:
        return await self._paginate('list_file_transfer_results', request, TransferListFileTransferResultsResponse)

    async def list_host_keys(
        self,
        request: TransferListHostKeysRequest,
    ) -> TransferListHostKeysResponse:
        client = self._require_client()
        return await self._execute(client.list_host_keys, request, TransferListHostKeysResponse)

    async def list_profiles(
        self,
        request: TransferListProfilesRequest | None = None,
    ) -> TransferListProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_profiles, request, TransferListProfilesResponse)

    async def list_profiles_paginated(
        self,
        request: TransferListProfilesRequest | None = None,
    ) -> list[TransferListProfilesResponse]:
        return await self._paginate('list_profiles', request, TransferListProfilesResponse)

    async def list_security_policies(
        self,
        request: TransferListSecurityPoliciesRequest | None = None,
    ) -> TransferListSecurityPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_security_policies, request, TransferListSecurityPoliciesResponse)

    async def list_security_policies_paginated(
        self,
        request: TransferListSecurityPoliciesRequest | None = None,
    ) -> list[TransferListSecurityPoliciesResponse]:
        return await self._paginate('list_security_policies', request, TransferListSecurityPoliciesResponse)

    async def list_servers(
        self,
        request: TransferListServersRequest | None = None,
    ) -> TransferListServersResponse:
        client = self._require_client()
        return await self._execute(client.list_servers, request, TransferListServersResponse)

    async def list_servers_paginated(
        self,
        request: TransferListServersRequest | None = None,
    ) -> list[TransferListServersResponse]:
        return await self._paginate('list_servers', request, TransferListServersResponse)

    async def list_tags_for_resource(
        self,
        request: TransferListTagsForResourceRequest,
    ) -> TransferListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, TransferListTagsForResourceResponse)

    async def list_tags_for_resource_paginated(
        self,
        request: TransferListTagsForResourceRequest,
    ) -> list[TransferListTagsForResourceResponse]:
        return await self._paginate('list_tags_for_resource', request, TransferListTagsForResourceResponse)

    async def list_users(
        self,
        request: TransferListUsersRequest,
    ) -> TransferListUsersResponse:
        client = self._require_client()
        return await self._execute(client.list_users, request, TransferListUsersResponse)

    async def list_users_paginated(
        self,
        request: TransferListUsersRequest,
    ) -> list[TransferListUsersResponse]:
        return await self._paginate('list_users', request, TransferListUsersResponse)

    async def list_web_apps(
        self,
        request: TransferListWebAppsRequest | None = None,
    ) -> TransferListWebAppsResponse:
        client = self._require_client()
        return await self._execute(client.list_web_apps, request, TransferListWebAppsResponse)

    async def list_web_apps_paginated(
        self,
        request: TransferListWebAppsRequest | None = None,
    ) -> list[TransferListWebAppsResponse]:
        return await self._paginate('list_web_apps', request, TransferListWebAppsResponse)

    async def list_workflows(
        self,
        request: TransferListWorkflowsRequest | None = None,
    ) -> TransferListWorkflowsResponse:
        client = self._require_client()
        return await self._execute(client.list_workflows, request, TransferListWorkflowsResponse)

    async def list_workflows_paginated(
        self,
        request: TransferListWorkflowsRequest | None = None,
    ) -> list[TransferListWorkflowsResponse]:
        return await self._paginate('list_workflows', request, TransferListWorkflowsResponse)

    async def send_workflow_step_state(
        self,
        request: TransferSendWorkflowStepStateRequest,
    ) -> TransferSendWorkflowStepStateResponse:
        client = self._require_client()
        return await self._execute(client.send_workflow_step_state, request, TransferSendWorkflowStepStateResponse)

    async def start_directory_listing(
        self,
        request: TransferStartDirectoryListingRequest,
    ) -> TransferStartDirectoryListingResponse:
        client = self._require_client()
        return await self._execute(client.start_directory_listing, request, TransferStartDirectoryListingResponse)

    async def start_file_transfer(
        self,
        request: TransferStartFileTransferRequest,
    ) -> TransferStartFileTransferResponse:
        client = self._require_client()
        return await self._execute(client.start_file_transfer, request, TransferStartFileTransferResponse)

    async def start_remote_delete(
        self,
        request: TransferStartRemoteDeleteRequest,
    ) -> TransferStartRemoteDeleteResponse:
        client = self._require_client()
        return await self._execute(client.start_remote_delete, request, TransferStartRemoteDeleteResponse)

    async def start_remote_move(
        self,
        request: TransferStartRemoteMoveRequest,
    ) -> TransferStartRemoteMoveResponse:
        client = self._require_client()
        return await self._execute(client.start_remote_move, request, TransferStartRemoteMoveResponse)

    async def start_server(
        self,
        request: TransferStartServerRequest,
    ) -> TransferStartServerResponse:
        client = self._require_client()
        return await self._execute(client.start_server, request, TransferStartServerResponse)

    async def stop_server(
        self,
        request: TransferStopServerRequest,
    ) -> TransferStopServerResponse:
        client = self._require_client()
        return await self._execute(client.stop_server, request, TransferStopServerResponse)

    async def tag_resource(
        self,
        request: TransferTagResourceRequest,
    ) -> TransferTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, TransferTagResourceResponse)

    async def test_connection(
        self,
        request: TransferTestConnectionRequest,
    ) -> TransferTestConnectionResponse:
        client = self._require_client()
        return await self._execute(client.test_connection, request, TransferTestConnectionResponse)

    async def test_identity_provider(
        self,
        request: TransferTestIdentityProviderRequest,
    ) -> TransferTestIdentityProviderResponse:
        client = self._require_client()
        return await self._execute(client.test_identity_provider, request, TransferTestIdentityProviderResponse)

    async def untag_resource(
        self,
        request: TransferUntagResourceRequest,
    ) -> TransferUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, TransferUntagResourceResponse)

    async def update_access(
        self,
        request: TransferUpdateAccessRequest,
    ) -> TransferUpdateAccessResponse:
        client = self._require_client()
        return await self._execute(client.update_access, request, TransferUpdateAccessResponse)

    async def update_agreement(
        self,
        request: TransferUpdateAgreementRequest,
    ) -> TransferUpdateAgreementResponse:
        client = self._require_client()
        return await self._execute(client.update_agreement, request, TransferUpdateAgreementResponse)

    async def update_certificate(
        self,
        request: TransferUpdateCertificateRequest,
    ) -> TransferUpdateCertificateResponse:
        client = self._require_client()
        return await self._execute(client.update_certificate, request, TransferUpdateCertificateResponse)

    async def update_connector(
        self,
        request: TransferUpdateConnectorRequest,
    ) -> TransferUpdateConnectorResponse:
        client = self._require_client()
        return await self._execute(client.update_connector, request, TransferUpdateConnectorResponse)

    async def update_host_key(
        self,
        request: TransferUpdateHostKeyRequest,
    ) -> TransferUpdateHostKeyResponse:
        client = self._require_client()
        return await self._execute(client.update_host_key, request, TransferUpdateHostKeyResponse)

    async def update_profile(
        self,
        request: TransferUpdateProfileRequest,
    ) -> TransferUpdateProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_profile, request, TransferUpdateProfileResponse)

    async def update_server(
        self,
        request: TransferUpdateServerRequest,
    ) -> TransferUpdateServerResponse:
        client = self._require_client()
        return await self._execute(client.update_server, request, TransferUpdateServerResponse)

    async def update_user(
        self,
        request: TransferUpdateUserRequest,
    ) -> TransferUpdateUserResponse:
        client = self._require_client()
        return await self._execute(client.update_user, request, TransferUpdateUserResponse)

    async def update_web_app(
        self,
        request: TransferUpdateWebAppRequest,
    ) -> TransferUpdateWebAppResponse:
        client = self._require_client()
        return await self._execute(client.update_web_app, request, TransferUpdateWebAppResponse)

    async def update_web_app_customization(
        self,
        request: TransferUpdateWebAppCustomizationRequest,
    ) -> TransferUpdateWebAppCustomizationResponse:
        client = self._require_client()
        return await self._execute(client.update_web_app_customization, request, TransferUpdateWebAppCustomizationResponse)
