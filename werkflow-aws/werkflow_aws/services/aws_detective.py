from werkflow_aws.models.detective import (
    DetectiveAcceptInvitationRequest,
    DetectiveAcceptInvitationResponse,
    DetectiveBatchGetGraphMemberDatasourcesRequest,
    DetectiveBatchGetGraphMemberDatasourcesResponse,
    DetectiveBatchGetMembershipDatasourcesRequest,
    DetectiveBatchGetMembershipDatasourcesResponse,
    DetectiveCreateGraphRequest,
    DetectiveCreateGraphResponse,
    DetectiveCreateMembersRequest,
    DetectiveCreateMembersResponse,
    DetectiveDeleteGraphRequest,
    DetectiveDeleteGraphResponse,
    DetectiveDeleteMembersRequest,
    DetectiveDeleteMembersResponse,
    DetectiveDescribeOrganizationConfigurationRequest,
    DetectiveDescribeOrganizationConfigurationResponse,
    DetectiveDisableOrganizationAdminAccountRequest,
    DetectiveDisableOrganizationAdminAccountResponse,
    DetectiveDisassociateMembershipRequest,
    DetectiveDisassociateMembershipResponse,
    DetectiveEnableOrganizationAdminAccountRequest,
    DetectiveEnableOrganizationAdminAccountResponse,
    DetectiveGetInvestigationRequest,
    DetectiveGetInvestigationResponse,
    DetectiveGetMembersRequest,
    DetectiveGetMembersResponse,
    DetectiveListDatasourcePackagesRequest,
    DetectiveListDatasourcePackagesResponse,
    DetectiveListGraphsRequest,
    DetectiveListGraphsResponse,
    DetectiveListIndicatorsRequest,
    DetectiveListIndicatorsResponse,
    DetectiveListInvestigationsRequest,
    DetectiveListInvestigationsResponse,
    DetectiveListInvitationsRequest,
    DetectiveListInvitationsResponse,
    DetectiveListMembersRequest,
    DetectiveListMembersResponse,
    DetectiveListOrganizationAdminAccountsRequest,
    DetectiveListOrganizationAdminAccountsResponse,
    DetectiveListTagsForResourceRequest,
    DetectiveListTagsForResourceResponse,
    DetectiveRejectInvitationRequest,
    DetectiveRejectInvitationResponse,
    DetectiveStartInvestigationRequest,
    DetectiveStartInvestigationResponse,
    DetectiveStartMonitoringMemberRequest,
    DetectiveStartMonitoringMemberResponse,
    DetectiveTagResourceRequest,
    DetectiveTagResourceResponse,
    DetectiveUntagResourceRequest,
    DetectiveUntagResourceResponse,
    DetectiveUpdateDatasourcePackagesRequest,
    DetectiveUpdateDatasourcePackagesResponse,
    DetectiveUpdateInvestigationStateRequest,
    DetectiveUpdateInvestigationStateResponse,
    DetectiveUpdateOrganizationConfigurationRequest,
    DetectiveUpdateOrganizationConfigurationResponse,
)
from werkflow_aws.types.detective_client import DetectiveClient
from .base import AWSBaseService


class AWSDetective(AWSBaseService[DetectiveClient]):
    service_name = 'detective'
    boto3_service_name = 'detective'

    def __init__(self) -> None:
        super().__init__(service_name='detective', boto3_service_name='detective')

    async def accept_invitation(
        self,
        request: DetectiveAcceptInvitationRequest,
    ) -> DetectiveAcceptInvitationResponse:
        client = self._require_client()
        return await self._execute(client.accept_invitation, request, DetectiveAcceptInvitationResponse)

    async def batch_get_graph_member_datasources(
        self,
        request: DetectiveBatchGetGraphMemberDatasourcesRequest,
    ) -> DetectiveBatchGetGraphMemberDatasourcesResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_graph_member_datasources, request, DetectiveBatchGetGraphMemberDatasourcesResponse)

    async def batch_get_membership_datasources(
        self,
        request: DetectiveBatchGetMembershipDatasourcesRequest,
    ) -> DetectiveBatchGetMembershipDatasourcesResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_membership_datasources, request, DetectiveBatchGetMembershipDatasourcesResponse)

    async def create_graph(
        self,
        request: DetectiveCreateGraphRequest | None = None,
    ) -> DetectiveCreateGraphResponse:
        client = self._require_client()
        return await self._execute(client.create_graph, request, DetectiveCreateGraphResponse)

    async def create_members(
        self,
        request: DetectiveCreateMembersRequest,
    ) -> DetectiveCreateMembersResponse:
        client = self._require_client()
        return await self._execute(client.create_members, request, DetectiveCreateMembersResponse)

    async def delete_graph(
        self,
        request: DetectiveDeleteGraphRequest,
    ) -> DetectiveDeleteGraphResponse:
        client = self._require_client()
        return await self._execute(client.delete_graph, request, DetectiveDeleteGraphResponse)

    async def delete_members(
        self,
        request: DetectiveDeleteMembersRequest,
    ) -> DetectiveDeleteMembersResponse:
        client = self._require_client()
        return await self._execute(client.delete_members, request, DetectiveDeleteMembersResponse)

    async def describe_organization_configuration(
        self,
        request: DetectiveDescribeOrganizationConfigurationRequest,
    ) -> DetectiveDescribeOrganizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_organization_configuration, request, DetectiveDescribeOrganizationConfigurationResponse)

    async def disable_organization_admin_account(
        self,
        request: DetectiveDisableOrganizationAdminAccountRequest | None = None,
    ) -> DetectiveDisableOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.disable_organization_admin_account, request, DetectiveDisableOrganizationAdminAccountResponse)

    async def disassociate_membership(
        self,
        request: DetectiveDisassociateMembershipRequest,
    ) -> DetectiveDisassociateMembershipResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_membership, request, DetectiveDisassociateMembershipResponse)

    async def enable_organization_admin_account(
        self,
        request: DetectiveEnableOrganizationAdminAccountRequest,
    ) -> DetectiveEnableOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.enable_organization_admin_account, request, DetectiveEnableOrganizationAdminAccountResponse)

    async def get_investigation(
        self,
        request: DetectiveGetInvestigationRequest,
    ) -> DetectiveGetInvestigationResponse:
        client = self._require_client()
        return await self._execute(client.get_investigation, request, DetectiveGetInvestigationResponse)

    async def get_members(
        self,
        request: DetectiveGetMembersRequest,
    ) -> DetectiveGetMembersResponse:
        client = self._require_client()
        return await self._execute(client.get_members, request, DetectiveGetMembersResponse)

    async def list_datasource_packages(
        self,
        request: DetectiveListDatasourcePackagesRequest,
    ) -> DetectiveListDatasourcePackagesResponse:
        client = self._require_client()
        return await self._execute(client.list_datasource_packages, request, DetectiveListDatasourcePackagesResponse)

    async def list_graphs(
        self,
        request: DetectiveListGraphsRequest | None = None,
    ) -> DetectiveListGraphsResponse:
        client = self._require_client()
        return await self._execute(client.list_graphs, request, DetectiveListGraphsResponse)

    async def list_indicators(
        self,
        request: DetectiveListIndicatorsRequest,
    ) -> DetectiveListIndicatorsResponse:
        client = self._require_client()
        return await self._execute(client.list_indicators, request, DetectiveListIndicatorsResponse)

    async def list_investigations(
        self,
        request: DetectiveListInvestigationsRequest,
    ) -> DetectiveListInvestigationsResponse:
        client = self._require_client()
        return await self._execute(client.list_investigations, request, DetectiveListInvestigationsResponse)

    async def list_invitations(
        self,
        request: DetectiveListInvitationsRequest | None = None,
    ) -> DetectiveListInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.list_invitations, request, DetectiveListInvitationsResponse)

    async def list_members(
        self,
        request: DetectiveListMembersRequest,
    ) -> DetectiveListMembersResponse:
        client = self._require_client()
        return await self._execute(client.list_members, request, DetectiveListMembersResponse)

    async def list_organization_admin_accounts(
        self,
        request: DetectiveListOrganizationAdminAccountsRequest | None = None,
    ) -> DetectiveListOrganizationAdminAccountsResponse:
        client = self._require_client()
        return await self._execute(client.list_organization_admin_accounts, request, DetectiveListOrganizationAdminAccountsResponse)

    async def list_tags_for_resource(
        self,
        request: DetectiveListTagsForResourceRequest,
    ) -> DetectiveListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, DetectiveListTagsForResourceResponse)

    async def reject_invitation(
        self,
        request: DetectiveRejectInvitationRequest,
    ) -> DetectiveRejectInvitationResponse:
        client = self._require_client()
        return await self._execute(client.reject_invitation, request, DetectiveRejectInvitationResponse)

    async def start_investigation(
        self,
        request: DetectiveStartInvestigationRequest,
    ) -> DetectiveStartInvestigationResponse:
        client = self._require_client()
        return await self._execute(client.start_investigation, request, DetectiveStartInvestigationResponse)

    async def start_monitoring_member(
        self,
        request: DetectiveStartMonitoringMemberRequest,
    ) -> DetectiveStartMonitoringMemberResponse:
        client = self._require_client()
        return await self._execute(client.start_monitoring_member, request, DetectiveStartMonitoringMemberResponse)

    async def tag_resource(
        self,
        request: DetectiveTagResourceRequest,
    ) -> DetectiveTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, DetectiveTagResourceResponse)

    async def untag_resource(
        self,
        request: DetectiveUntagResourceRequest,
    ) -> DetectiveUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, DetectiveUntagResourceResponse)

    async def update_datasource_packages(
        self,
        request: DetectiveUpdateDatasourcePackagesRequest,
    ) -> DetectiveUpdateDatasourcePackagesResponse:
        client = self._require_client()
        return await self._execute(client.update_datasource_packages, request, DetectiveUpdateDatasourcePackagesResponse)

    async def update_investigation_state(
        self,
        request: DetectiveUpdateInvestigationStateRequest,
    ) -> DetectiveUpdateInvestigationStateResponse:
        client = self._require_client()
        return await self._execute(client.update_investigation_state, request, DetectiveUpdateInvestigationStateResponse)

    async def update_organization_configuration(
        self,
        request: DetectiveUpdateOrganizationConfigurationRequest,
    ) -> DetectiveUpdateOrganizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_organization_configuration, request, DetectiveUpdateOrganizationConfigurationResponse)
