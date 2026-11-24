from werkflow_aws.models.organizations import (
    OrganizationsDescribeAccountRequest,
    OrganizationsDescribeAccountResponse,
    OrganizationsDescribeOrganizationRequest,
    OrganizationsDescribeOrganizationResponse,
    OrganizationsDescribePolicyRequest,
    OrganizationsDescribePolicyResponse,
    OrganizationsEmptyResponse,
    OrganizationsListAccountsForParentRequest,
    OrganizationsListAccountsForParentResponse,
    OrganizationsListAccountsRequest,
    OrganizationsListAccountsResponse,
    OrganizationsListOrganizationalUnitsForParentRequest,
    OrganizationsListOrganizationalUnitsForParentResponse,
    OrganizationsListPoliciesRequest,
    OrganizationsListPoliciesResponse,
    OrganizationsListRootsRequest,
    OrganizationsListRootsResponse,
    OrganizationsListTagsForResourceRequest,
    OrganizationsListTagsForResourceResponse,
    OrganizationsTagResourceRequest,
    OrganizationsUntagResourceRequest,
)
from werkflow_aws.types import OrganizationsClient
from .base import AWSBaseService
from werkflow_aws.models.organizations import (
    OrganizationsAcceptHandshakeRequest,
    OrganizationsAcceptHandshakeResponse,
    OrganizationsAttachPolicyRequest,
    OrganizationsAttachPolicyResponse,
    OrganizationsCancelHandshakeRequest,
    OrganizationsCancelHandshakeResponse,
    OrganizationsCloseAccountRequest,
    OrganizationsCloseAccountResponse,
    OrganizationsCreateAccountRequest,
    OrganizationsCreateAccountResponse,
    OrganizationsCreateGovCloudAccountRequest,
    OrganizationsCreateGovCloudAccountResponse,
    OrganizationsCreateOrganizationRequest,
    OrganizationsCreateOrganizationResponse,
    OrganizationsCreateOrganizationalUnitRequest,
    OrganizationsCreateOrganizationalUnitResponse,
    OrganizationsCreatePolicyRequest,
    OrganizationsCreatePolicyResponse,
    OrganizationsDeclineHandshakeRequest,
    OrganizationsDeclineHandshakeResponse,
    OrganizationsDeleteOrganizationRequest,
    OrganizationsDeleteOrganizationResponse,
    OrganizationsDeleteOrganizationalUnitRequest,
    OrganizationsDeleteOrganizationalUnitResponse,
    OrganizationsDeletePolicyRequest,
    OrganizationsDeletePolicyResponse,
    OrganizationsDeleteResourcePolicyRequest,
    OrganizationsDeleteResourcePolicyResponse,
    OrganizationsDeregisterDelegatedAdministratorRequest,
    OrganizationsDeregisterDelegatedAdministratorResponse,
    OrganizationsDescribeCreateAccountStatusRequest,
    OrganizationsDescribeCreateAccountStatusResponse,
    OrganizationsDescribeEffectivePolicyRequest,
    OrganizationsDescribeEffectivePolicyResponse,
    OrganizationsDescribeHandshakeRequest,
    OrganizationsDescribeHandshakeResponse,
    OrganizationsDescribeOrganizationalUnitRequest,
    OrganizationsDescribeOrganizationalUnitResponse,
    OrganizationsDescribeResourcePolicyRequest,
    OrganizationsDescribeResourcePolicyResponse,
    OrganizationsDescribeResponsibilityTransferRequest,
    OrganizationsDescribeResponsibilityTransferResponse,
    OrganizationsDetachPolicyRequest,
    OrganizationsDetachPolicyResponse,
    OrganizationsDisableAWSServiceAccessRequest,
    OrganizationsDisableAWSServiceAccessResponse,
    OrganizationsDisablePolicyTypeRequest,
    OrganizationsDisablePolicyTypeResponse,
    OrganizationsEnableAWSServiceAccessRequest,
    OrganizationsEnableAWSServiceAccessResponse,
    OrganizationsEnableAllFeaturesRequest,
    OrganizationsEnableAllFeaturesResponse,
    OrganizationsEnablePolicyTypeRequest,
    OrganizationsEnablePolicyTypeResponse,
    OrganizationsInviteAccountToOrganizationRequest,
    OrganizationsInviteAccountToOrganizationResponse,
    OrganizationsInviteOrganizationToTransferResponsibilityRequest,
    OrganizationsInviteOrganizationToTransferResponsibilityResponse,
    OrganizationsLeaveOrganizationRequest,
    OrganizationsLeaveOrganizationResponse,
    OrganizationsListAWSServiceAccessForOrganizationRequest,
    OrganizationsListAWSServiceAccessForOrganizationResponse,
    OrganizationsListAccountsWithInvalidEffectivePolicyRequest,
    OrganizationsListAccountsWithInvalidEffectivePolicyResponse,
    OrganizationsListChildrenRequest,
    OrganizationsListChildrenResponse,
    OrganizationsListCreateAccountStatusRequest,
    OrganizationsListCreateAccountStatusResponse,
    OrganizationsListDelegatedAdministratorsRequest,
    OrganizationsListDelegatedAdministratorsResponse,
    OrganizationsListDelegatedServicesForAccountRequest,
    OrganizationsListDelegatedServicesForAccountResponse,
    OrganizationsListEffectivePolicyValidationErrorsRequest,
    OrganizationsListEffectivePolicyValidationErrorsResponse,
    OrganizationsListHandshakesForAccountRequest,
    OrganizationsListHandshakesForAccountResponse,
    OrganizationsListHandshakesForOrganizationRequest,
    OrganizationsListHandshakesForOrganizationResponse,
    OrganizationsListInboundResponsibilityTransfersRequest,
    OrganizationsListInboundResponsibilityTransfersResponse,
    OrganizationsListOutboundResponsibilityTransfersRequest,
    OrganizationsListOutboundResponsibilityTransfersResponse,
    OrganizationsListParentsRequest,
    OrganizationsListParentsResponse,
    OrganizationsListPoliciesForTargetRequest,
    OrganizationsListPoliciesForTargetResponse,
    OrganizationsListTargetsForPolicyRequest,
    OrganizationsListTargetsForPolicyResponse,
    OrganizationsMoveAccountRequest,
    OrganizationsMoveAccountResponse,
    OrganizationsPutResourcePolicyRequest,
    OrganizationsPutResourcePolicyResponse,
    OrganizationsRegisterDelegatedAdministratorRequest,
    OrganizationsRegisterDelegatedAdministratorResponse,
    OrganizationsRemoveAccountFromOrganizationRequest,
    OrganizationsRemoveAccountFromOrganizationResponse,
    OrganizationsTerminateResponsibilityTransferRequest,
    OrganizationsTerminateResponsibilityTransferResponse,
    OrganizationsUpdateOrganizationalUnitRequest,
    OrganizationsUpdateOrganizationalUnitResponse,
    OrganizationsUpdatePolicyRequest,
    OrganizationsUpdatePolicyResponse,
    OrganizationsUpdateResponsibilityTransferRequest,
    OrganizationsUpdateResponsibilityTransferResponse,
)


class AWSOrganizations(AWSBaseService[OrganizationsClient]):
    service_name = 'Organizations'
    boto3_service_name = 'organizations'

    def __init__(self) -> None:
        super().__init__(
            service_name='Organizations',
            boto3_service_name='organizations',
        )

    async def list_accounts(
        self,
        request: OrganizationsListAccountsRequest | None = None,
    ) -> OrganizationsListAccountsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_accounts,
            request or OrganizationsListAccountsRequest(),
            OrganizationsListAccountsResponse,
        )

    async def list_accounts_paginated(
        self,
        request: OrganizationsListAccountsRequest | None = None,
    ) -> list[OrganizationsListAccountsResponse]:
        return await self._paginate(
            'list_accounts',
            request or OrganizationsListAccountsRequest(),
            OrganizationsListAccountsResponse,
        )

    async def describe_organization(
        self,
        request: OrganizationsDescribeOrganizationRequest | None = None,
    ) -> OrganizationsDescribeOrganizationResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_organization,
            request,
            OrganizationsDescribeOrganizationResponse,
        )

    async def describe_account(
        self,
        request: OrganizationsDescribeAccountRequest,
    ) -> OrganizationsDescribeAccountResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_account,
            request,
            OrganizationsDescribeAccountResponse,
        )

    async def list_roots(
        self,
        request: OrganizationsListRootsRequest | None = None,
    ) -> OrganizationsListRootsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_roots,
            request or OrganizationsListRootsRequest(),
            OrganizationsListRootsResponse,
        )

    async def list_roots_paginated(
        self,
        request: OrganizationsListRootsRequest | None = None,
    ) -> list[OrganizationsListRootsResponse]:
        return await self._paginate(
            'list_roots',
            request or OrganizationsListRootsRequest(),
            OrganizationsListRootsResponse,
        )

    async def list_organizational_units_for_parent(
        self,
        request: OrganizationsListOrganizationalUnitsForParentRequest,
    ) -> OrganizationsListOrganizationalUnitsForParentResponse:
        client = self._require_client()
        return await self._execute(
            client.list_organizational_units_for_parent,
            request,
            OrganizationsListOrganizationalUnitsForParentResponse,
        )

    async def list_organizational_units_for_parent_paginated(
        self,
        request: OrganizationsListOrganizationalUnitsForParentRequest,
    ) -> list[OrganizationsListOrganizationalUnitsForParentResponse]:
        return await self._paginate(
            'list_organizational_units_for_parent',
            request,
            OrganizationsListOrganizationalUnitsForParentResponse,
        )

    async def list_accounts_for_parent(
        self,
        request: OrganizationsListAccountsForParentRequest,
    ) -> OrganizationsListAccountsForParentResponse:
        client = self._require_client()
        return await self._execute(
            client.list_accounts_for_parent,
            request,
            OrganizationsListAccountsForParentResponse,
        )

    async def list_accounts_for_parent_paginated(
        self,
        request: OrganizationsListAccountsForParentRequest,
    ) -> list[OrganizationsListAccountsForParentResponse]:
        return await self._paginate(
            'list_accounts_for_parent',
            request,
            OrganizationsListAccountsForParentResponse,
        )

    async def list_policies(
        self,
        request: OrganizationsListPoliciesRequest,
    ) -> OrganizationsListPoliciesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_policies,
            request,
            OrganizationsListPoliciesResponse,
        )

    async def list_policies_paginated(
        self,
        request: OrganizationsListPoliciesRequest,
    ) -> list[OrganizationsListPoliciesResponse]:
        return await self._paginate(
            'list_policies',
            request,
            OrganizationsListPoliciesResponse,
        )

    async def describe_policy(
        self,
        request: OrganizationsDescribePolicyRequest,
    ) -> OrganizationsDescribePolicyResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_policy,
            request,
            OrganizationsDescribePolicyResponse,
        )

    async def list_tags_for_resource(
        self,
        request: OrganizationsListTagsForResourceRequest,
    ) -> OrganizationsListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.list_tags_for_resource,
            request,
            OrganizationsListTagsForResourceResponse,
        )

    async def list_tags_for_resource_paginated(
        self,
        request: OrganizationsListTagsForResourceRequest,
    ) -> list[OrganizationsListTagsForResourceResponse]:
        return await self._paginate(
            'list_tags_for_resource',
            request,
            OrganizationsListTagsForResourceResponse,
        )

    async def tag_resource(
        self,
        request: OrganizationsTagResourceRequest,
    ) -> OrganizationsEmptyResponse:
        client = self._require_client()
        return await self._execute(
            client.tag_resource,
            request,
            OrganizationsEmptyResponse,
        )

    async def untag_resource(
        self,
        request: OrganizationsUntagResourceRequest,
    ) -> OrganizationsEmptyResponse:
        client = self._require_client()
        return await self._execute(
            client.untag_resource,
            request,
            OrganizationsEmptyResponse,
        )

    async def accept_handshake(
        self,
        request: OrganizationsAcceptHandshakeRequest,
    ) -> OrganizationsAcceptHandshakeResponse:
        client = self._require_client()
        return await self._execute(client.accept_handshake, request, OrganizationsAcceptHandshakeResponse)

    async def attach_policy(
        self,
        request: OrganizationsAttachPolicyRequest,
    ) -> OrganizationsAttachPolicyResponse:
        client = self._require_client()
        return await self._execute(client.attach_policy, request, OrganizationsAttachPolicyResponse)

    async def cancel_handshake(
        self,
        request: OrganizationsCancelHandshakeRequest,
    ) -> OrganizationsCancelHandshakeResponse:
        client = self._require_client()
        return await self._execute(client.cancel_handshake, request, OrganizationsCancelHandshakeResponse)

    async def close_account(
        self,
        request: OrganizationsCloseAccountRequest,
    ) -> OrganizationsCloseAccountResponse:
        client = self._require_client()
        return await self._execute(client.close_account, request, OrganizationsCloseAccountResponse)

    async def create_account(
        self,
        request: OrganizationsCreateAccountRequest,
    ) -> OrganizationsCreateAccountResponse:
        client = self._require_client()
        return await self._execute(client.create_account, request, OrganizationsCreateAccountResponse)

    async def create_gov_cloud_account(
        self,
        request: OrganizationsCreateGovCloudAccountRequest,
    ) -> OrganizationsCreateGovCloudAccountResponse:
        client = self._require_client()
        return await self._execute(client.create_gov_cloud_account, request, OrganizationsCreateGovCloudAccountResponse)

    async def create_organization(
        self,
        request: OrganizationsCreateOrganizationRequest | None = None,
    ) -> OrganizationsCreateOrganizationResponse:
        client = self._require_client()
        return await self._execute(client.create_organization, request, OrganizationsCreateOrganizationResponse)

    async def create_organizational_unit(
        self,
        request: OrganizationsCreateOrganizationalUnitRequest,
    ) -> OrganizationsCreateOrganizationalUnitResponse:
        client = self._require_client()
        return await self._execute(client.create_organizational_unit, request, OrganizationsCreateOrganizationalUnitResponse)

    async def create_policy(
        self,
        request: OrganizationsCreatePolicyRequest,
    ) -> OrganizationsCreatePolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_policy, request, OrganizationsCreatePolicyResponse)

    async def decline_handshake(
        self,
        request: OrganizationsDeclineHandshakeRequest,
    ) -> OrganizationsDeclineHandshakeResponse:
        client = self._require_client()
        return await self._execute(client.decline_handshake, request, OrganizationsDeclineHandshakeResponse)

    async def delete_organization(
        self,
        request: OrganizationsDeleteOrganizationRequest | None = None,
    ) -> OrganizationsDeleteOrganizationResponse:
        client = self._require_client()
        return await self._execute(client.delete_organization, request, OrganizationsDeleteOrganizationResponse)

    async def delete_organizational_unit(
        self,
        request: OrganizationsDeleteOrganizationalUnitRequest,
    ) -> OrganizationsDeleteOrganizationalUnitResponse:
        client = self._require_client()
        return await self._execute(client.delete_organizational_unit, request, OrganizationsDeleteOrganizationalUnitResponse)

    async def delete_policy(
        self,
        request: OrganizationsDeletePolicyRequest,
    ) -> OrganizationsDeletePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_policy, request, OrganizationsDeletePolicyResponse)

    async def delete_resource_policy(
        self,
        request: OrganizationsDeleteResourcePolicyRequest | None = None,
    ) -> OrganizationsDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, OrganizationsDeleteResourcePolicyResponse)

    async def deregister_delegated_administrator(
        self,
        request: OrganizationsDeregisterDelegatedAdministratorRequest,
    ) -> OrganizationsDeregisterDelegatedAdministratorResponse:
        client = self._require_client()
        return await self._execute(client.deregister_delegated_administrator, request, OrganizationsDeregisterDelegatedAdministratorResponse)

    async def describe_create_account_status(
        self,
        request: OrganizationsDescribeCreateAccountStatusRequest,
    ) -> OrganizationsDescribeCreateAccountStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_create_account_status, request, OrganizationsDescribeCreateAccountStatusResponse)

    async def describe_effective_policy(
        self,
        request: OrganizationsDescribeEffectivePolicyRequest,
    ) -> OrganizationsDescribeEffectivePolicyResponse:
        client = self._require_client()
        return await self._execute(client.describe_effective_policy, request, OrganizationsDescribeEffectivePolicyResponse)

    async def describe_handshake(
        self,
        request: OrganizationsDescribeHandshakeRequest,
    ) -> OrganizationsDescribeHandshakeResponse:
        client = self._require_client()
        return await self._execute(client.describe_handshake, request, OrganizationsDescribeHandshakeResponse)

    async def describe_organizational_unit(
        self,
        request: OrganizationsDescribeOrganizationalUnitRequest,
    ) -> OrganizationsDescribeOrganizationalUnitResponse:
        client = self._require_client()
        return await self._execute(client.describe_organizational_unit, request, OrganizationsDescribeOrganizationalUnitResponse)

    async def describe_resource_policy(
        self,
        request: OrganizationsDescribeResourcePolicyRequest | None = None,
    ) -> OrganizationsDescribeResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.describe_resource_policy, request, OrganizationsDescribeResourcePolicyResponse)

    async def describe_responsibility_transfer(
        self,
        request: OrganizationsDescribeResponsibilityTransferRequest,
    ) -> OrganizationsDescribeResponsibilityTransferResponse:
        client = self._require_client()
        return await self._execute(client.describe_responsibility_transfer, request, OrganizationsDescribeResponsibilityTransferResponse)

    async def detach_policy(
        self,
        request: OrganizationsDetachPolicyRequest,
    ) -> OrganizationsDetachPolicyResponse:
        client = self._require_client()
        return await self._execute(client.detach_policy, request, OrganizationsDetachPolicyResponse)

    async def disable_aws_service_access(
        self,
        request: OrganizationsDisableAWSServiceAccessRequest,
    ) -> OrganizationsDisableAWSServiceAccessResponse:
        client = self._require_client()
        return await self._execute(client.disable_aws_service_access, request, OrganizationsDisableAWSServiceAccessResponse)

    async def disable_policy_type(
        self,
        request: OrganizationsDisablePolicyTypeRequest,
    ) -> OrganizationsDisablePolicyTypeResponse:
        client = self._require_client()
        return await self._execute(client.disable_policy_type, request, OrganizationsDisablePolicyTypeResponse)

    async def enable_aws_service_access(
        self,
        request: OrganizationsEnableAWSServiceAccessRequest,
    ) -> OrganizationsEnableAWSServiceAccessResponse:
        client = self._require_client()
        return await self._execute(client.enable_aws_service_access, request, OrganizationsEnableAWSServiceAccessResponse)

    async def enable_all_features(
        self,
        request: OrganizationsEnableAllFeaturesRequest | None = None,
    ) -> OrganizationsEnableAllFeaturesResponse:
        client = self._require_client()
        return await self._execute(client.enable_all_features, request, OrganizationsEnableAllFeaturesResponse)

    async def enable_policy_type(
        self,
        request: OrganizationsEnablePolicyTypeRequest,
    ) -> OrganizationsEnablePolicyTypeResponse:
        client = self._require_client()
        return await self._execute(client.enable_policy_type, request, OrganizationsEnablePolicyTypeResponse)

    async def invite_account_to_organization(
        self,
        request: OrganizationsInviteAccountToOrganizationRequest,
    ) -> OrganizationsInviteAccountToOrganizationResponse:
        client = self._require_client()
        return await self._execute(client.invite_account_to_organization, request, OrganizationsInviteAccountToOrganizationResponse)

    async def invite_organization_to_transfer_responsibility(
        self,
        request: OrganizationsInviteOrganizationToTransferResponsibilityRequest,
    ) -> OrganizationsInviteOrganizationToTransferResponsibilityResponse:
        client = self._require_client()
        return await self._execute(client.invite_organization_to_transfer_responsibility, request, OrganizationsInviteOrganizationToTransferResponsibilityResponse)

    async def leave_organization(
        self,
        request: OrganizationsLeaveOrganizationRequest | None = None,
    ) -> OrganizationsLeaveOrganizationResponse:
        client = self._require_client()
        return await self._execute(client.leave_organization, request, OrganizationsLeaveOrganizationResponse)

    async def list_aws_service_access_for_organization(
        self,
        request: OrganizationsListAWSServiceAccessForOrganizationRequest | None = None,
    ) -> OrganizationsListAWSServiceAccessForOrganizationResponse:
        client = self._require_client()
        return await self._execute(client.list_aws_service_access_for_organization, request, OrganizationsListAWSServiceAccessForOrganizationResponse)

    async def list_aws_service_access_for_organization_paginated(
        self,
        request: OrganizationsListAWSServiceAccessForOrganizationRequest | None = None,
    ) -> list[OrganizationsListAWSServiceAccessForOrganizationResponse]:
        return await self._paginate('list_aws_service_access_for_organization', request, OrganizationsListAWSServiceAccessForOrganizationResponse)

    async def list_accounts_with_invalid_effective_policy(
        self,
        request: OrganizationsListAccountsWithInvalidEffectivePolicyRequest,
    ) -> OrganizationsListAccountsWithInvalidEffectivePolicyResponse:
        client = self._require_client()
        return await self._execute(client.list_accounts_with_invalid_effective_policy, request, OrganizationsListAccountsWithInvalidEffectivePolicyResponse)

    async def list_accounts_with_invalid_effective_policy_paginated(
        self,
        request: OrganizationsListAccountsWithInvalidEffectivePolicyRequest,
    ) -> list[OrganizationsListAccountsWithInvalidEffectivePolicyResponse]:
        return await self._paginate('list_accounts_with_invalid_effective_policy', request, OrganizationsListAccountsWithInvalidEffectivePolicyResponse)

    async def list_children(
        self,
        request: OrganizationsListChildrenRequest,
    ) -> OrganizationsListChildrenResponse:
        client = self._require_client()
        return await self._execute(client.list_children, request, OrganizationsListChildrenResponse)

    async def list_children_paginated(
        self,
        request: OrganizationsListChildrenRequest,
    ) -> list[OrganizationsListChildrenResponse]:
        return await self._paginate('list_children', request, OrganizationsListChildrenResponse)

    async def list_create_account_status(
        self,
        request: OrganizationsListCreateAccountStatusRequest | None = None,
    ) -> OrganizationsListCreateAccountStatusResponse:
        client = self._require_client()
        return await self._execute(client.list_create_account_status, request, OrganizationsListCreateAccountStatusResponse)

    async def list_create_account_status_paginated(
        self,
        request: OrganizationsListCreateAccountStatusRequest | None = None,
    ) -> list[OrganizationsListCreateAccountStatusResponse]:
        return await self._paginate('list_create_account_status', request, OrganizationsListCreateAccountStatusResponse)

    async def list_delegated_administrators(
        self,
        request: OrganizationsListDelegatedAdministratorsRequest | None = None,
    ) -> OrganizationsListDelegatedAdministratorsResponse:
        client = self._require_client()
        return await self._execute(client.list_delegated_administrators, request, OrganizationsListDelegatedAdministratorsResponse)

    async def list_delegated_administrators_paginated(
        self,
        request: OrganizationsListDelegatedAdministratorsRequest | None = None,
    ) -> list[OrganizationsListDelegatedAdministratorsResponse]:
        return await self._paginate('list_delegated_administrators', request, OrganizationsListDelegatedAdministratorsResponse)

    async def list_delegated_services_for_account(
        self,
        request: OrganizationsListDelegatedServicesForAccountRequest,
    ) -> OrganizationsListDelegatedServicesForAccountResponse:
        client = self._require_client()
        return await self._execute(client.list_delegated_services_for_account, request, OrganizationsListDelegatedServicesForAccountResponse)

    async def list_delegated_services_for_account_paginated(
        self,
        request: OrganizationsListDelegatedServicesForAccountRequest,
    ) -> list[OrganizationsListDelegatedServicesForAccountResponse]:
        return await self._paginate('list_delegated_services_for_account', request, OrganizationsListDelegatedServicesForAccountResponse)

    async def list_effective_policy_validation_errors(
        self,
        request: OrganizationsListEffectivePolicyValidationErrorsRequest,
    ) -> OrganizationsListEffectivePolicyValidationErrorsResponse:
        client = self._require_client()
        return await self._execute(client.list_effective_policy_validation_errors, request, OrganizationsListEffectivePolicyValidationErrorsResponse)

    async def list_effective_policy_validation_errors_paginated(
        self,
        request: OrganizationsListEffectivePolicyValidationErrorsRequest,
    ) -> list[OrganizationsListEffectivePolicyValidationErrorsResponse]:
        return await self._paginate('list_effective_policy_validation_errors', request, OrganizationsListEffectivePolicyValidationErrorsResponse)

    async def list_handshakes_for_account(
        self,
        request: OrganizationsListHandshakesForAccountRequest | None = None,
    ) -> OrganizationsListHandshakesForAccountResponse:
        client = self._require_client()
        return await self._execute(client.list_handshakes_for_account, request, OrganizationsListHandshakesForAccountResponse)

    async def list_handshakes_for_account_paginated(
        self,
        request: OrganizationsListHandshakesForAccountRequest | None = None,
    ) -> list[OrganizationsListHandshakesForAccountResponse]:
        return await self._paginate('list_handshakes_for_account', request, OrganizationsListHandshakesForAccountResponse)

    async def list_handshakes_for_organization(
        self,
        request: OrganizationsListHandshakesForOrganizationRequest | None = None,
    ) -> OrganizationsListHandshakesForOrganizationResponse:
        client = self._require_client()
        return await self._execute(client.list_handshakes_for_organization, request, OrganizationsListHandshakesForOrganizationResponse)

    async def list_handshakes_for_organization_paginated(
        self,
        request: OrganizationsListHandshakesForOrganizationRequest | None = None,
    ) -> list[OrganizationsListHandshakesForOrganizationResponse]:
        return await self._paginate('list_handshakes_for_organization', request, OrganizationsListHandshakesForOrganizationResponse)

    async def list_inbound_responsibility_transfers(
        self,
        request: OrganizationsListInboundResponsibilityTransfersRequest,
    ) -> OrganizationsListInboundResponsibilityTransfersResponse:
        client = self._require_client()
        return await self._execute(client.list_inbound_responsibility_transfers, request, OrganizationsListInboundResponsibilityTransfersResponse)

    async def list_outbound_responsibility_transfers(
        self,
        request: OrganizationsListOutboundResponsibilityTransfersRequest,
    ) -> OrganizationsListOutboundResponsibilityTransfersResponse:
        client = self._require_client()
        return await self._execute(client.list_outbound_responsibility_transfers, request, OrganizationsListOutboundResponsibilityTransfersResponse)

    async def list_parents(
        self,
        request: OrganizationsListParentsRequest,
    ) -> OrganizationsListParentsResponse:
        client = self._require_client()
        return await self._execute(client.list_parents, request, OrganizationsListParentsResponse)

    async def list_parents_paginated(
        self,
        request: OrganizationsListParentsRequest,
    ) -> list[OrganizationsListParentsResponse]:
        return await self._paginate('list_parents', request, OrganizationsListParentsResponse)

    async def list_policies_for_target(
        self,
        request: OrganizationsListPoliciesForTargetRequest,
    ) -> OrganizationsListPoliciesForTargetResponse:
        client = self._require_client()
        return await self._execute(client.list_policies_for_target, request, OrganizationsListPoliciesForTargetResponse)

    async def list_policies_for_target_paginated(
        self,
        request: OrganizationsListPoliciesForTargetRequest,
    ) -> list[OrganizationsListPoliciesForTargetResponse]:
        return await self._paginate('list_policies_for_target', request, OrganizationsListPoliciesForTargetResponse)

    async def list_targets_for_policy(
        self,
        request: OrganizationsListTargetsForPolicyRequest,
    ) -> OrganizationsListTargetsForPolicyResponse:
        client = self._require_client()
        return await self._execute(client.list_targets_for_policy, request, OrganizationsListTargetsForPolicyResponse)

    async def list_targets_for_policy_paginated(
        self,
        request: OrganizationsListTargetsForPolicyRequest,
    ) -> list[OrganizationsListTargetsForPolicyResponse]:
        return await self._paginate('list_targets_for_policy', request, OrganizationsListTargetsForPolicyResponse)

    async def move_account(
        self,
        request: OrganizationsMoveAccountRequest,
    ) -> OrganizationsMoveAccountResponse:
        client = self._require_client()
        return await self._execute(client.move_account, request, OrganizationsMoveAccountResponse)

    async def put_resource_policy(
        self,
        request: OrganizationsPutResourcePolicyRequest,
    ) -> OrganizationsPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, OrganizationsPutResourcePolicyResponse)

    async def register_delegated_administrator(
        self,
        request: OrganizationsRegisterDelegatedAdministratorRequest,
    ) -> OrganizationsRegisterDelegatedAdministratorResponse:
        client = self._require_client()
        return await self._execute(client.register_delegated_administrator, request, OrganizationsRegisterDelegatedAdministratorResponse)

    async def remove_account_from_organization(
        self,
        request: OrganizationsRemoveAccountFromOrganizationRequest,
    ) -> OrganizationsRemoveAccountFromOrganizationResponse:
        client = self._require_client()
        return await self._execute(client.remove_account_from_organization, request, OrganizationsRemoveAccountFromOrganizationResponse)

    async def terminate_responsibility_transfer(
        self,
        request: OrganizationsTerminateResponsibilityTransferRequest,
    ) -> OrganizationsTerminateResponsibilityTransferResponse:
        client = self._require_client()
        return await self._execute(client.terminate_responsibility_transfer, request, OrganizationsTerminateResponsibilityTransferResponse)

    async def update_organizational_unit(
        self,
        request: OrganizationsUpdateOrganizationalUnitRequest,
    ) -> OrganizationsUpdateOrganizationalUnitResponse:
        client = self._require_client()
        return await self._execute(client.update_organizational_unit, request, OrganizationsUpdateOrganizationalUnitResponse)

    async def update_policy(
        self,
        request: OrganizationsUpdatePolicyRequest,
    ) -> OrganizationsUpdatePolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_policy, request, OrganizationsUpdatePolicyResponse)

    async def update_responsibility_transfer(
        self,
        request: OrganizationsUpdateResponsibilityTransferRequest,
    ) -> OrganizationsUpdateResponsibilityTransferResponse:
        client = self._require_client()
        return await self._execute(client.update_responsibility_transfer, request, OrganizationsUpdateResponsibilityTransferResponse)

