from werkflow_aws.models.firewall import (
    FMSAssociateAdminAccountRequest,
    FMSAssociateAdminAccountResponse,
    FMSAssociateThirdPartyFirewallRequest,
    FMSAssociateThirdPartyFirewallResponse,
    FMSBatchAssociateResourceRequest,
    FMSBatchAssociateResourceResponse,
    FMSBatchDisassociateResourceRequest,
    FMSBatchDisassociateResourceResponse,
    FMSDeleteAppsListRequest,
    FMSDeleteAppsListResponse,
    FMSDeleteNotificationChannelRequest,
    FMSDeleteNotificationChannelResponse,
    FMSDeletePolicyRequest,
    FMSDeletePolicyResponse,
    FMSDeleteProtocolsListRequest,
    FMSDeleteProtocolsListResponse,
    FMSDeleteResourceSetRequest,
    FMSDeleteResourceSetResponse,
    FMSDisassociateAdminAccountRequest,
    FMSDisassociateAdminAccountResponse,
    FMSDisassociateThirdPartyFirewallRequest,
    FMSDisassociateThirdPartyFirewallResponse,
    FMSGetAdminAccountRequest,
    FMSGetAdminAccountResponse,
    FMSGetAdminScopeRequest,
    FMSGetAdminScopeResponse,
    FMSGetAppsListRequest,
    FMSGetAppsListResponse,
    FMSGetComplianceDetailRequest,
    FMSGetComplianceDetailResponse,
    FMSGetNotificationChannelRequest,
    FMSGetNotificationChannelResponse,
    FMSGetPolicyRequest,
    FMSGetPolicyResponse,
    FMSGetProtectionStatusRequest,
    FMSGetProtectionStatusResponse,
    FMSGetProtocolsListRequest,
    FMSGetProtocolsListResponse,
    FMSGetResourceSetRequest,
    FMSGetResourceSetResponse,
    FMSGetThirdPartyFirewallAssociationStatusRequest,
    FMSGetThirdPartyFirewallAssociationStatusResponse,
    FMSGetViolationDetailsRequest,
    FMSGetViolationDetailsResponse,
    FMSListAdminAccountsForOrganizationRequest,
    FMSListAdminAccountsForOrganizationResponse,
    FMSListAdminsManagingAccountRequest,
    FMSListAdminsManagingAccountResponse,
    FMSListAppsListsRequest,
    FMSListAppsListsResponse,
    FMSListComplianceStatusRequest,
    FMSListComplianceStatusResponse,
    FMSListDiscoveredResourcesRequest,
    FMSListDiscoveredResourcesResponse,
    FMSListMemberAccountsRequest,
    FMSListMemberAccountsResponse,
    FMSListPoliciesRequest,
    FMSListPoliciesResponse,
    FMSListProtocolsListsRequest,
    FMSListProtocolsListsResponse,
    FMSListResourceSetResourcesRequest,
    FMSListResourceSetResourcesResponse,
    FMSListResourceSetsRequest,
    FMSListResourceSetsResponse,
    FMSListTagsForResourceRequest,
    FMSListTagsForResourceResponse,
    FMSListThirdPartyFirewallFirewallPoliciesRequest,
    FMSListThirdPartyFirewallFirewallPoliciesResponse,
    FMSPutAdminAccountRequest,
    FMSPutAdminAccountResponse,
    FMSPutAppsListRequest,
    FMSPutAppsListResponse,
    FMSPutNotificationChannelRequest,
    FMSPutNotificationChannelResponse,
    FMSPutPolicyRequest,
    FMSPutPolicyResponse,
    FMSPutProtocolsListRequest,
    FMSPutProtocolsListResponse,
    FMSPutResourceSetRequest,
    FMSPutResourceSetResponse,
    FMSTagResourceRequest,
    FMSTagResourceResponse,
    FMSUntagResourceRequest,
    FMSUntagResourceResponse,
)
from werkflow_aws.types.firewall_client import FMSClient
from .base import AWSBaseService


class AWSFMS(AWSBaseService[FMSClient]):
    service_name = 'firewall'
    boto3_service_name = 'fms'

    def __init__(self) -> None:
        super().__init__(service_name='firewall', boto3_service_name='fms')

    async def associate_admin_account(
        self,
        request: FMSAssociateAdminAccountRequest,
    ) -> FMSAssociateAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.associate_admin_account, request, FMSAssociateAdminAccountResponse)

    async def associate_third_party_firewall(
        self,
        request: FMSAssociateThirdPartyFirewallRequest,
    ) -> FMSAssociateThirdPartyFirewallResponse:
        client = self._require_client()
        return await self._execute(client.associate_third_party_firewall, request, FMSAssociateThirdPartyFirewallResponse)

    async def batch_associate_resource(
        self,
        request: FMSBatchAssociateResourceRequest,
    ) -> FMSBatchAssociateResourceResponse:
        client = self._require_client()
        return await self._execute(client.batch_associate_resource, request, FMSBatchAssociateResourceResponse)

    async def batch_disassociate_resource(
        self,
        request: FMSBatchDisassociateResourceRequest,
    ) -> FMSBatchDisassociateResourceResponse:
        client = self._require_client()
        return await self._execute(client.batch_disassociate_resource, request, FMSBatchDisassociateResourceResponse)

    async def delete_apps_list(
        self,
        request: FMSDeleteAppsListRequest,
    ) -> FMSDeleteAppsListResponse:
        client = self._require_client()
        return await self._execute(client.delete_apps_list, request, FMSDeleteAppsListResponse)

    async def delete_notification_channel(
        self,
        request: FMSDeleteNotificationChannelRequest | None = None,
    ) -> FMSDeleteNotificationChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_notification_channel, request, FMSDeleteNotificationChannelResponse)

    async def delete_policy(
        self,
        request: FMSDeletePolicyRequest,
    ) -> FMSDeletePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_policy, request, FMSDeletePolicyResponse)

    async def delete_protocols_list(
        self,
        request: FMSDeleteProtocolsListRequest,
    ) -> FMSDeleteProtocolsListResponse:
        client = self._require_client()
        return await self._execute(client.delete_protocols_list, request, FMSDeleteProtocolsListResponse)

    async def delete_resource_set(
        self,
        request: FMSDeleteResourceSetRequest,
    ) -> FMSDeleteResourceSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_set, request, FMSDeleteResourceSetResponse)

    async def disassociate_admin_account(
        self,
        request: FMSDisassociateAdminAccountRequest | None = None,
    ) -> FMSDisassociateAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_admin_account, request, FMSDisassociateAdminAccountResponse)

    async def disassociate_third_party_firewall(
        self,
        request: FMSDisassociateThirdPartyFirewallRequest,
    ) -> FMSDisassociateThirdPartyFirewallResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_third_party_firewall, request, FMSDisassociateThirdPartyFirewallResponse)

    async def get_admin_account(
        self,
        request: FMSGetAdminAccountRequest | None = None,
    ) -> FMSGetAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.get_admin_account, request, FMSGetAdminAccountResponse)

    async def get_admin_scope(
        self,
        request: FMSGetAdminScopeRequest,
    ) -> FMSGetAdminScopeResponse:
        client = self._require_client()
        return await self._execute(client.get_admin_scope, request, FMSGetAdminScopeResponse)

    async def get_apps_list(
        self,
        request: FMSGetAppsListRequest,
    ) -> FMSGetAppsListResponse:
        client = self._require_client()
        return await self._execute(client.get_apps_list, request, FMSGetAppsListResponse)

    async def get_compliance_detail(
        self,
        request: FMSGetComplianceDetailRequest,
    ) -> FMSGetComplianceDetailResponse:
        client = self._require_client()
        return await self._execute(client.get_compliance_detail, request, FMSGetComplianceDetailResponse)

    async def get_notification_channel(
        self,
        request: FMSGetNotificationChannelRequest | None = None,
    ) -> FMSGetNotificationChannelResponse:
        client = self._require_client()
        return await self._execute(client.get_notification_channel, request, FMSGetNotificationChannelResponse)

    async def get_policy(
        self,
        request: FMSGetPolicyRequest,
    ) -> FMSGetPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_policy, request, FMSGetPolicyResponse)

    async def get_protection_status(
        self,
        request: FMSGetProtectionStatusRequest,
    ) -> FMSGetProtectionStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_protection_status, request, FMSGetProtectionStatusResponse)

    async def get_protocols_list(
        self,
        request: FMSGetProtocolsListRequest,
    ) -> FMSGetProtocolsListResponse:
        client = self._require_client()
        return await self._execute(client.get_protocols_list, request, FMSGetProtocolsListResponse)

    async def get_resource_set(
        self,
        request: FMSGetResourceSetRequest,
    ) -> FMSGetResourceSetResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_set, request, FMSGetResourceSetResponse)

    async def get_third_party_firewall_association_status(
        self,
        request: FMSGetThirdPartyFirewallAssociationStatusRequest,
    ) -> FMSGetThirdPartyFirewallAssociationStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_third_party_firewall_association_status, request, FMSGetThirdPartyFirewallAssociationStatusResponse)

    async def get_violation_details(
        self,
        request: FMSGetViolationDetailsRequest,
    ) -> FMSGetViolationDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_violation_details, request, FMSGetViolationDetailsResponse)

    async def list_admin_accounts_for_organization(
        self,
        request: FMSListAdminAccountsForOrganizationRequest | None = None,
    ) -> FMSListAdminAccountsForOrganizationResponse:
        client = self._require_client()
        return await self._execute(client.list_admin_accounts_for_organization, request, FMSListAdminAccountsForOrganizationResponse)

    async def list_admin_accounts_for_organization_paginated(
        self,
        request: FMSListAdminAccountsForOrganizationRequest | None = None,
    ) -> list[FMSListAdminAccountsForOrganizationResponse]:
        return await self._paginate('list_admin_accounts_for_organization', request, FMSListAdminAccountsForOrganizationResponse)

    async def list_admins_managing_account(
        self,
        request: FMSListAdminsManagingAccountRequest | None = None,
    ) -> FMSListAdminsManagingAccountResponse:
        client = self._require_client()
        return await self._execute(client.list_admins_managing_account, request, FMSListAdminsManagingAccountResponse)

    async def list_admins_managing_account_paginated(
        self,
        request: FMSListAdminsManagingAccountRequest | None = None,
    ) -> list[FMSListAdminsManagingAccountResponse]:
        return await self._paginate('list_admins_managing_account', request, FMSListAdminsManagingAccountResponse)

    async def list_apps_lists(
        self,
        request: FMSListAppsListsRequest,
    ) -> FMSListAppsListsResponse:
        client = self._require_client()
        return await self._execute(client.list_apps_lists, request, FMSListAppsListsResponse)

    async def list_apps_lists_paginated(
        self,
        request: FMSListAppsListsRequest,
    ) -> list[FMSListAppsListsResponse]:
        return await self._paginate('list_apps_lists', request, FMSListAppsListsResponse)

    async def list_compliance_status(
        self,
        request: FMSListComplianceStatusRequest,
    ) -> FMSListComplianceStatusResponse:
        client = self._require_client()
        return await self._execute(client.list_compliance_status, request, FMSListComplianceStatusResponse)

    async def list_compliance_status_paginated(
        self,
        request: FMSListComplianceStatusRequest,
    ) -> list[FMSListComplianceStatusResponse]:
        return await self._paginate('list_compliance_status', request, FMSListComplianceStatusResponse)

    async def list_discovered_resources(
        self,
        request: FMSListDiscoveredResourcesRequest,
    ) -> FMSListDiscoveredResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_discovered_resources, request, FMSListDiscoveredResourcesResponse)

    async def list_member_accounts(
        self,
        request: FMSListMemberAccountsRequest | None = None,
    ) -> FMSListMemberAccountsResponse:
        client = self._require_client()
        return await self._execute(client.list_member_accounts, request, FMSListMemberAccountsResponse)

    async def list_member_accounts_paginated(
        self,
        request: FMSListMemberAccountsRequest | None = None,
    ) -> list[FMSListMemberAccountsResponse]:
        return await self._paginate('list_member_accounts', request, FMSListMemberAccountsResponse)

    async def list_policies(
        self,
        request: FMSListPoliciesRequest | None = None,
    ) -> FMSListPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_policies, request, FMSListPoliciesResponse)

    async def list_policies_paginated(
        self,
        request: FMSListPoliciesRequest | None = None,
    ) -> list[FMSListPoliciesResponse]:
        return await self._paginate('list_policies', request, FMSListPoliciesResponse)

    async def list_protocols_lists(
        self,
        request: FMSListProtocolsListsRequest,
    ) -> FMSListProtocolsListsResponse:
        client = self._require_client()
        return await self._execute(client.list_protocols_lists, request, FMSListProtocolsListsResponse)

    async def list_protocols_lists_paginated(
        self,
        request: FMSListProtocolsListsRequest,
    ) -> list[FMSListProtocolsListsResponse]:
        return await self._paginate('list_protocols_lists', request, FMSListProtocolsListsResponse)

    async def list_resource_set_resources(
        self,
        request: FMSListResourceSetResourcesRequest,
    ) -> FMSListResourceSetResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_set_resources, request, FMSListResourceSetResourcesResponse)

    async def list_resource_sets(
        self,
        request: FMSListResourceSetsRequest | None = None,
    ) -> FMSListResourceSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_sets, request, FMSListResourceSetsResponse)

    async def list_tags_for_resource(
        self,
        request: FMSListTagsForResourceRequest,
    ) -> FMSListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, FMSListTagsForResourceResponse)

    async def list_third_party_firewall_firewall_policies(
        self,
        request: FMSListThirdPartyFirewallFirewallPoliciesRequest,
    ) -> FMSListThirdPartyFirewallFirewallPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_third_party_firewall_firewall_policies, request, FMSListThirdPartyFirewallFirewallPoliciesResponse)

    async def list_third_party_firewall_firewall_policies_paginated(
        self,
        request: FMSListThirdPartyFirewallFirewallPoliciesRequest,
    ) -> list[FMSListThirdPartyFirewallFirewallPoliciesResponse]:
        return await self._paginate('list_third_party_firewall_firewall_policies', request, FMSListThirdPartyFirewallFirewallPoliciesResponse)

    async def put_admin_account(
        self,
        request: FMSPutAdminAccountRequest,
    ) -> FMSPutAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.put_admin_account, request, FMSPutAdminAccountResponse)

    async def put_apps_list(
        self,
        request: FMSPutAppsListRequest,
    ) -> FMSPutAppsListResponse:
        client = self._require_client()
        return await self._execute(client.put_apps_list, request, FMSPutAppsListResponse)

    async def put_notification_channel(
        self,
        request: FMSPutNotificationChannelRequest,
    ) -> FMSPutNotificationChannelResponse:
        client = self._require_client()
        return await self._execute(client.put_notification_channel, request, FMSPutNotificationChannelResponse)

    async def put_policy(
        self,
        request: FMSPutPolicyRequest,
    ) -> FMSPutPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_policy, request, FMSPutPolicyResponse)

    async def put_protocols_list(
        self,
        request: FMSPutProtocolsListRequest,
    ) -> FMSPutProtocolsListResponse:
        client = self._require_client()
        return await self._execute(client.put_protocols_list, request, FMSPutProtocolsListResponse)

    async def put_resource_set(
        self,
        request: FMSPutResourceSetRequest,
    ) -> FMSPutResourceSetResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_set, request, FMSPutResourceSetResponse)

    async def tag_resource(
        self,
        request: FMSTagResourceRequest,
    ) -> FMSTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, FMSTagResourceResponse)

    async def untag_resource(
        self,
        request: FMSUntagResourceRequest,
    ) -> FMSUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, FMSUntagResourceResponse)
