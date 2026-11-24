from werkflow_aws.models.macie import (
    MacieAcceptInvitationRequest,
    MacieAcceptInvitationResponse,
    MacieBatchGetCustomDataIdentifiersRequest,
    MacieBatchGetCustomDataIdentifiersResponse,
    MacieBatchUpdateAutomatedDiscoveryAccountsRequest,
    MacieBatchUpdateAutomatedDiscoveryAccountsResponse,
    MacieCreateAllowListRequest,
    MacieCreateAllowListResponse,
    MacieCreateClassificationJobRequest,
    MacieCreateClassificationJobResponse,
    MacieCreateCustomDataIdentifierRequest,
    MacieCreateCustomDataIdentifierResponse,
    MacieCreateFindingsFilterRequest,
    MacieCreateFindingsFilterResponse,
    MacieCreateInvitationsRequest,
    MacieCreateInvitationsResponse,
    MacieCreateMemberRequest,
    MacieCreateMemberResponse,
    MacieCreateSampleFindingsRequest,
    MacieCreateSampleFindingsResponse,
    MacieDeclineInvitationsRequest,
    MacieDeclineInvitationsResponse,
    MacieDeleteAllowListRequest,
    MacieDeleteAllowListResponse,
    MacieDeleteCustomDataIdentifierRequest,
    MacieDeleteCustomDataIdentifierResponse,
    MacieDeleteFindingsFilterRequest,
    MacieDeleteFindingsFilterResponse,
    MacieDeleteInvitationsRequest,
    MacieDeleteInvitationsResponse,
    MacieDeleteMemberRequest,
    MacieDeleteMemberResponse,
    MacieDescribeBucketsRequest,
    MacieDescribeBucketsResponse,
    MacieDescribeClassificationJobRequest,
    MacieDescribeClassificationJobResponse,
    MacieDescribeOrganizationConfigurationRequest,
    MacieDescribeOrganizationConfigurationResponse,
    MacieDisableMacieRequest,
    MacieDisableMacieResponse,
    MacieDisableOrganizationAdminAccountRequest,
    MacieDisableOrganizationAdminAccountResponse,
    MacieDisassociateFromAdministratorAccountRequest,
    MacieDisassociateFromAdministratorAccountResponse,
    MacieDisassociateFromMasterAccountRequest,
    MacieDisassociateFromMasterAccountResponse,
    MacieDisassociateMemberRequest,
    MacieDisassociateMemberResponse,
    MacieEnableMacieRequest,
    MacieEnableMacieResponse,
    MacieEnableOrganizationAdminAccountRequest,
    MacieEnableOrganizationAdminAccountResponse,
    MacieGetAdministratorAccountRequest,
    MacieGetAdministratorAccountResponse,
    MacieGetAllowListRequest,
    MacieGetAllowListResponse,
    MacieGetAutomatedDiscoveryConfigurationRequest,
    MacieGetAutomatedDiscoveryConfigurationResponse,
    MacieGetBucketStatisticsRequest,
    MacieGetBucketStatisticsResponse,
    MacieGetClassificationExportConfigurationRequest,
    MacieGetClassificationExportConfigurationResponse,
    MacieGetClassificationScopeRequest,
    MacieGetClassificationScopeResponse,
    MacieGetCustomDataIdentifierRequest,
    MacieGetCustomDataIdentifierResponse,
    MacieGetFindingStatisticsRequest,
    MacieGetFindingStatisticsResponse,
    MacieGetFindingsFilterRequest,
    MacieGetFindingsFilterResponse,
    MacieGetFindingsPublicationConfigurationRequest,
    MacieGetFindingsPublicationConfigurationResponse,
    MacieGetFindingsRequest,
    MacieGetFindingsResponse,
    MacieGetInvitationsCountRequest,
    MacieGetInvitationsCountResponse,
    MacieGetMacieSessionRequest,
    MacieGetMacieSessionResponse,
    MacieGetMasterAccountRequest,
    MacieGetMasterAccountResponse,
    MacieGetMemberRequest,
    MacieGetMemberResponse,
    MacieGetResourceProfileRequest,
    MacieGetResourceProfileResponse,
    MacieGetRevealConfigurationRequest,
    MacieGetRevealConfigurationResponse,
    MacieGetSensitiveDataOccurrencesAvailabilityRequest,
    MacieGetSensitiveDataOccurrencesAvailabilityResponse,
    MacieGetSensitiveDataOccurrencesRequest,
    MacieGetSensitiveDataOccurrencesResponse,
    MacieGetSensitivityInspectionTemplateRequest,
    MacieGetSensitivityInspectionTemplateResponse,
    MacieGetUsageStatisticsRequest,
    MacieGetUsageStatisticsResponse,
    MacieGetUsageTotalsRequest,
    MacieGetUsageTotalsResponse,
    MacieListAllowListsRequest,
    MacieListAllowListsResponse,
    MacieListAutomatedDiscoveryAccountsRequest,
    MacieListAutomatedDiscoveryAccountsResponse,
    MacieListClassificationJobsRequest,
    MacieListClassificationJobsResponse,
    MacieListClassificationScopesRequest,
    MacieListClassificationScopesResponse,
    MacieListCustomDataIdentifiersRequest,
    MacieListCustomDataIdentifiersResponse,
    MacieListFindingsFiltersRequest,
    MacieListFindingsFiltersResponse,
    MacieListFindingsRequest,
    MacieListFindingsResponse,
    MacieListInvitationsRequest,
    MacieListInvitationsResponse,
    MacieListManagedDataIdentifiersRequest,
    MacieListManagedDataIdentifiersResponse,
    MacieListMembersRequest,
    MacieListMembersResponse,
    MacieListOrganizationAdminAccountsRequest,
    MacieListOrganizationAdminAccountsResponse,
    MacieListResourceProfileArtifactsRequest,
    MacieListResourceProfileArtifactsResponse,
    MacieListResourceProfileDetectionsRequest,
    MacieListResourceProfileDetectionsResponse,
    MacieListSensitivityInspectionTemplatesRequest,
    MacieListSensitivityInspectionTemplatesResponse,
    MacieListTagsForResourceRequest,
    MacieListTagsForResourceResponse,
    MaciePutClassificationExportConfigurationRequest,
    MaciePutClassificationExportConfigurationResponse,
    MaciePutFindingsPublicationConfigurationRequest,
    MaciePutFindingsPublicationConfigurationResponse,
    MacieSearchResourcesRequest,
    MacieSearchResourcesResponse,
    MacieTagResourceRequest,
    MacieTagResourceResponse,
    MacieTestCustomDataIdentifierRequest,
    MacieTestCustomDataIdentifierResponse,
    MacieUntagResourceRequest,
    MacieUntagResourceResponse,
    MacieUpdateAllowListRequest,
    MacieUpdateAllowListResponse,
    MacieUpdateAutomatedDiscoveryConfigurationRequest,
    MacieUpdateAutomatedDiscoveryConfigurationResponse,
    MacieUpdateClassificationJobRequest,
    MacieUpdateClassificationJobResponse,
    MacieUpdateClassificationScopeRequest,
    MacieUpdateClassificationScopeResponse,
    MacieUpdateFindingsFilterRequest,
    MacieUpdateFindingsFilterResponse,
    MacieUpdateMacieSessionRequest,
    MacieUpdateMacieSessionResponse,
    MacieUpdateMemberSessionRequest,
    MacieUpdateMemberSessionResponse,
    MacieUpdateOrganizationConfigurationRequest,
    MacieUpdateOrganizationConfigurationResponse,
    MacieUpdateResourceProfileDetectionsRequest,
    MacieUpdateResourceProfileDetectionsResponse,
    MacieUpdateResourceProfileRequest,
    MacieUpdateResourceProfileResponse,
    MacieUpdateRevealConfigurationRequest,
    MacieUpdateRevealConfigurationResponse,
    MacieUpdateSensitivityInspectionTemplateRequest,
    MacieUpdateSensitivityInspectionTemplateResponse,
)
from werkflow_aws.types.macie_client import MacieClient
from .base import AWSBaseService


class AWSMacie(AWSBaseService[MacieClient]):
    service_name = 'macie'
    boto3_service_name = 'macie2'

    def __init__(self) -> None:
        super().__init__(service_name='macie', boto3_service_name='macie2')

    async def accept_invitation(
        self,
        request: MacieAcceptInvitationRequest,
    ) -> MacieAcceptInvitationResponse:
        client = self._require_client()
        return await self._execute(client.accept_invitation, request, MacieAcceptInvitationResponse)

    async def batch_get_custom_data_identifiers(
        self,
        request: MacieBatchGetCustomDataIdentifiersRequest | None = None,
    ) -> MacieBatchGetCustomDataIdentifiersResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_custom_data_identifiers, request, MacieBatchGetCustomDataIdentifiersResponse)

    async def batch_update_automated_discovery_accounts(
        self,
        request: MacieBatchUpdateAutomatedDiscoveryAccountsRequest | None = None,
    ) -> MacieBatchUpdateAutomatedDiscoveryAccountsResponse:
        client = self._require_client()
        return await self._execute(client.batch_update_automated_discovery_accounts, request, MacieBatchUpdateAutomatedDiscoveryAccountsResponse)

    async def create_allow_list(
        self,
        request: MacieCreateAllowListRequest,
    ) -> MacieCreateAllowListResponse:
        client = self._require_client()
        return await self._execute(client.create_allow_list, request, MacieCreateAllowListResponse)

    async def create_classification_job(
        self,
        request: MacieCreateClassificationJobRequest,
    ) -> MacieCreateClassificationJobResponse:
        client = self._require_client()
        return await self._execute(client.create_classification_job, request, MacieCreateClassificationJobResponse)

    async def create_custom_data_identifier(
        self,
        request: MacieCreateCustomDataIdentifierRequest,
    ) -> MacieCreateCustomDataIdentifierResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_data_identifier, request, MacieCreateCustomDataIdentifierResponse)

    async def create_findings_filter(
        self,
        request: MacieCreateFindingsFilterRequest,
    ) -> MacieCreateFindingsFilterResponse:
        client = self._require_client()
        return await self._execute(client.create_findings_filter, request, MacieCreateFindingsFilterResponse)

    async def create_invitations(
        self,
        request: MacieCreateInvitationsRequest,
    ) -> MacieCreateInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.create_invitations, request, MacieCreateInvitationsResponse)

    async def create_member(
        self,
        request: MacieCreateMemberRequest,
    ) -> MacieCreateMemberResponse:
        client = self._require_client()
        return await self._execute(client.create_member, request, MacieCreateMemberResponse)

    async def create_sample_findings(
        self,
        request: MacieCreateSampleFindingsRequest | None = None,
    ) -> MacieCreateSampleFindingsResponse:
        client = self._require_client()
        return await self._execute(client.create_sample_findings, request, MacieCreateSampleFindingsResponse)

    async def decline_invitations(
        self,
        request: MacieDeclineInvitationsRequest,
    ) -> MacieDeclineInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.decline_invitations, request, MacieDeclineInvitationsResponse)

    async def delete_allow_list(
        self,
        request: MacieDeleteAllowListRequest,
    ) -> MacieDeleteAllowListResponse:
        client = self._require_client()
        return await self._execute(client.delete_allow_list, request, MacieDeleteAllowListResponse)

    async def delete_custom_data_identifier(
        self,
        request: MacieDeleteCustomDataIdentifierRequest,
    ) -> MacieDeleteCustomDataIdentifierResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_data_identifier, request, MacieDeleteCustomDataIdentifierResponse)

    async def delete_findings_filter(
        self,
        request: MacieDeleteFindingsFilterRequest,
    ) -> MacieDeleteFindingsFilterResponse:
        client = self._require_client()
        return await self._execute(client.delete_findings_filter, request, MacieDeleteFindingsFilterResponse)

    async def delete_invitations(
        self,
        request: MacieDeleteInvitationsRequest,
    ) -> MacieDeleteInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.delete_invitations, request, MacieDeleteInvitationsResponse)

    async def delete_member(
        self,
        request: MacieDeleteMemberRequest,
    ) -> MacieDeleteMemberResponse:
        client = self._require_client()
        return await self._execute(client.delete_member, request, MacieDeleteMemberResponse)

    async def describe_buckets(
        self,
        request: MacieDescribeBucketsRequest | None = None,
    ) -> MacieDescribeBucketsResponse:
        client = self._require_client()
        return await self._execute(client.describe_buckets, request, MacieDescribeBucketsResponse)

    async def describe_buckets_paginated(
        self,
        request: MacieDescribeBucketsRequest | None = None,
    ) -> list[MacieDescribeBucketsResponse]:
        return await self._paginate('describe_buckets', request, MacieDescribeBucketsResponse)

    async def describe_classification_job(
        self,
        request: MacieDescribeClassificationJobRequest,
    ) -> MacieDescribeClassificationJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_classification_job, request, MacieDescribeClassificationJobResponse)

    async def describe_organization_configuration(
        self,
        request: MacieDescribeOrganizationConfigurationRequest | None = None,
    ) -> MacieDescribeOrganizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_organization_configuration, request, MacieDescribeOrganizationConfigurationResponse)

    async def disable_macie(
        self,
        request: MacieDisableMacieRequest | None = None,
    ) -> MacieDisableMacieResponse:
        client = self._require_client()
        return await self._execute(client.disable_macie, request, MacieDisableMacieResponse)

    async def disable_organization_admin_account(
        self,
        request: MacieDisableOrganizationAdminAccountRequest,
    ) -> MacieDisableOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.disable_organization_admin_account, request, MacieDisableOrganizationAdminAccountResponse)

    async def disassociate_from_administrator_account(
        self,
        request: MacieDisassociateFromAdministratorAccountRequest | None = None,
    ) -> MacieDisassociateFromAdministratorAccountResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_from_administrator_account, request, MacieDisassociateFromAdministratorAccountResponse)

    async def disassociate_from_master_account(
        self,
        request: MacieDisassociateFromMasterAccountRequest | None = None,
    ) -> MacieDisassociateFromMasterAccountResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_from_master_account, request, MacieDisassociateFromMasterAccountResponse)

    async def disassociate_member(
        self,
        request: MacieDisassociateMemberRequest,
    ) -> MacieDisassociateMemberResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_member, request, MacieDisassociateMemberResponse)

    async def enable_macie(
        self,
        request: MacieEnableMacieRequest | None = None,
    ) -> MacieEnableMacieResponse:
        client = self._require_client()
        return await self._execute(client.enable_macie, request, MacieEnableMacieResponse)

    async def enable_organization_admin_account(
        self,
        request: MacieEnableOrganizationAdminAccountRequest,
    ) -> MacieEnableOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.enable_organization_admin_account, request, MacieEnableOrganizationAdminAccountResponse)

    async def get_administrator_account(
        self,
        request: MacieGetAdministratorAccountRequest | None = None,
    ) -> MacieGetAdministratorAccountResponse:
        client = self._require_client()
        return await self._execute(client.get_administrator_account, request, MacieGetAdministratorAccountResponse)

    async def get_allow_list(
        self,
        request: MacieGetAllowListRequest,
    ) -> MacieGetAllowListResponse:
        client = self._require_client()
        return await self._execute(client.get_allow_list, request, MacieGetAllowListResponse)

    async def get_automated_discovery_configuration(
        self,
        request: MacieGetAutomatedDiscoveryConfigurationRequest | None = None,
    ) -> MacieGetAutomatedDiscoveryConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_automated_discovery_configuration, request, MacieGetAutomatedDiscoveryConfigurationResponse)

    async def get_bucket_statistics(
        self,
        request: MacieGetBucketStatisticsRequest | None = None,
    ) -> MacieGetBucketStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_statistics, request, MacieGetBucketStatisticsResponse)

    async def get_classification_export_configuration(
        self,
        request: MacieGetClassificationExportConfigurationRequest | None = None,
    ) -> MacieGetClassificationExportConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_classification_export_configuration, request, MacieGetClassificationExportConfigurationResponse)

    async def get_classification_scope(
        self,
        request: MacieGetClassificationScopeRequest,
    ) -> MacieGetClassificationScopeResponse:
        client = self._require_client()
        return await self._execute(client.get_classification_scope, request, MacieGetClassificationScopeResponse)

    async def get_custom_data_identifier(
        self,
        request: MacieGetCustomDataIdentifierRequest,
    ) -> MacieGetCustomDataIdentifierResponse:
        client = self._require_client()
        return await self._execute(client.get_custom_data_identifier, request, MacieGetCustomDataIdentifierResponse)

    async def get_finding_statistics(
        self,
        request: MacieGetFindingStatisticsRequest,
    ) -> MacieGetFindingStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_finding_statistics, request, MacieGetFindingStatisticsResponse)

    async def get_findings(
        self,
        request: MacieGetFindingsRequest,
    ) -> MacieGetFindingsResponse:
        client = self._require_client()
        return await self._execute(client.get_findings, request, MacieGetFindingsResponse)

    async def get_findings_filter(
        self,
        request: MacieGetFindingsFilterRequest,
    ) -> MacieGetFindingsFilterResponse:
        client = self._require_client()
        return await self._execute(client.get_findings_filter, request, MacieGetFindingsFilterResponse)

    async def get_findings_publication_configuration(
        self,
        request: MacieGetFindingsPublicationConfigurationRequest | None = None,
    ) -> MacieGetFindingsPublicationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_findings_publication_configuration, request, MacieGetFindingsPublicationConfigurationResponse)

    async def get_invitations_count(
        self,
        request: MacieGetInvitationsCountRequest | None = None,
    ) -> MacieGetInvitationsCountResponse:
        client = self._require_client()
        return await self._execute(client.get_invitations_count, request, MacieGetInvitationsCountResponse)

    async def get_macie_session(
        self,
        request: MacieGetMacieSessionRequest | None = None,
    ) -> MacieGetMacieSessionResponse:
        client = self._require_client()
        return await self._execute(client.get_macie_session, request, MacieGetMacieSessionResponse)

    async def get_master_account(
        self,
        request: MacieGetMasterAccountRequest | None = None,
    ) -> MacieGetMasterAccountResponse:
        client = self._require_client()
        return await self._execute(client.get_master_account, request, MacieGetMasterAccountResponse)

    async def get_member(
        self,
        request: MacieGetMemberRequest,
    ) -> MacieGetMemberResponse:
        client = self._require_client()
        return await self._execute(client.get_member, request, MacieGetMemberResponse)

    async def get_resource_profile(
        self,
        request: MacieGetResourceProfileRequest,
    ) -> MacieGetResourceProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_profile, request, MacieGetResourceProfileResponse)

    async def get_reveal_configuration(
        self,
        request: MacieGetRevealConfigurationRequest | None = None,
    ) -> MacieGetRevealConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_reveal_configuration, request, MacieGetRevealConfigurationResponse)

    async def get_sensitive_data_occurrences(
        self,
        request: MacieGetSensitiveDataOccurrencesRequest,
    ) -> MacieGetSensitiveDataOccurrencesResponse:
        client = self._require_client()
        return await self._execute(client.get_sensitive_data_occurrences, request, MacieGetSensitiveDataOccurrencesResponse)

    async def get_sensitive_data_occurrences_availability(
        self,
        request: MacieGetSensitiveDataOccurrencesAvailabilityRequest,
    ) -> MacieGetSensitiveDataOccurrencesAvailabilityResponse:
        client = self._require_client()
        return await self._execute(client.get_sensitive_data_occurrences_availability, request, MacieGetSensitiveDataOccurrencesAvailabilityResponse)

    async def get_sensitivity_inspection_template(
        self,
        request: MacieGetSensitivityInspectionTemplateRequest,
    ) -> MacieGetSensitivityInspectionTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_sensitivity_inspection_template, request, MacieGetSensitivityInspectionTemplateResponse)

    async def get_usage_statistics(
        self,
        request: MacieGetUsageStatisticsRequest | None = None,
    ) -> MacieGetUsageStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_usage_statistics, request, MacieGetUsageStatisticsResponse)

    async def get_usage_statistics_paginated(
        self,
        request: MacieGetUsageStatisticsRequest | None = None,
    ) -> list[MacieGetUsageStatisticsResponse]:
        return await self._paginate('get_usage_statistics', request, MacieGetUsageStatisticsResponse)

    async def get_usage_totals(
        self,
        request: MacieGetUsageTotalsRequest | None = None,
    ) -> MacieGetUsageTotalsResponse:
        client = self._require_client()
        return await self._execute(client.get_usage_totals, request, MacieGetUsageTotalsResponse)

    async def list_allow_lists(
        self,
        request: MacieListAllowListsRequest | None = None,
    ) -> MacieListAllowListsResponse:
        client = self._require_client()
        return await self._execute(client.list_allow_lists, request, MacieListAllowListsResponse)

    async def list_allow_lists_paginated(
        self,
        request: MacieListAllowListsRequest | None = None,
    ) -> list[MacieListAllowListsResponse]:
        return await self._paginate('list_allow_lists', request, MacieListAllowListsResponse)

    async def list_automated_discovery_accounts(
        self,
        request: MacieListAutomatedDiscoveryAccountsRequest | None = None,
    ) -> MacieListAutomatedDiscoveryAccountsResponse:
        client = self._require_client()
        return await self._execute(client.list_automated_discovery_accounts, request, MacieListAutomatedDiscoveryAccountsResponse)

    async def list_automated_discovery_accounts_paginated(
        self,
        request: MacieListAutomatedDiscoveryAccountsRequest | None = None,
    ) -> list[MacieListAutomatedDiscoveryAccountsResponse]:
        return await self._paginate('list_automated_discovery_accounts', request, MacieListAutomatedDiscoveryAccountsResponse)

    async def list_classification_jobs(
        self,
        request: MacieListClassificationJobsRequest | None = None,
    ) -> MacieListClassificationJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_classification_jobs, request, MacieListClassificationJobsResponse)

    async def list_classification_jobs_paginated(
        self,
        request: MacieListClassificationJobsRequest | None = None,
    ) -> list[MacieListClassificationJobsResponse]:
        return await self._paginate('list_classification_jobs', request, MacieListClassificationJobsResponse)

    async def list_classification_scopes(
        self,
        request: MacieListClassificationScopesRequest | None = None,
    ) -> MacieListClassificationScopesResponse:
        client = self._require_client()
        return await self._execute(client.list_classification_scopes, request, MacieListClassificationScopesResponse)

    async def list_classification_scopes_paginated(
        self,
        request: MacieListClassificationScopesRequest | None = None,
    ) -> list[MacieListClassificationScopesResponse]:
        return await self._paginate('list_classification_scopes', request, MacieListClassificationScopesResponse)

    async def list_custom_data_identifiers(
        self,
        request: MacieListCustomDataIdentifiersRequest | None = None,
    ) -> MacieListCustomDataIdentifiersResponse:
        client = self._require_client()
        return await self._execute(client.list_custom_data_identifiers, request, MacieListCustomDataIdentifiersResponse)

    async def list_custom_data_identifiers_paginated(
        self,
        request: MacieListCustomDataIdentifiersRequest | None = None,
    ) -> list[MacieListCustomDataIdentifiersResponse]:
        return await self._paginate('list_custom_data_identifiers', request, MacieListCustomDataIdentifiersResponse)

    async def list_findings(
        self,
        request: MacieListFindingsRequest | None = None,
    ) -> MacieListFindingsResponse:
        client = self._require_client()
        return await self._execute(client.list_findings, request, MacieListFindingsResponse)

    async def list_findings_paginated(
        self,
        request: MacieListFindingsRequest | None = None,
    ) -> list[MacieListFindingsResponse]:
        return await self._paginate('list_findings', request, MacieListFindingsResponse)

    async def list_findings_filters(
        self,
        request: MacieListFindingsFiltersRequest | None = None,
    ) -> MacieListFindingsFiltersResponse:
        client = self._require_client()
        return await self._execute(client.list_findings_filters, request, MacieListFindingsFiltersResponse)

    async def list_findings_filters_paginated(
        self,
        request: MacieListFindingsFiltersRequest | None = None,
    ) -> list[MacieListFindingsFiltersResponse]:
        return await self._paginate('list_findings_filters', request, MacieListFindingsFiltersResponse)

    async def list_invitations(
        self,
        request: MacieListInvitationsRequest | None = None,
    ) -> MacieListInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.list_invitations, request, MacieListInvitationsResponse)

    async def list_invitations_paginated(
        self,
        request: MacieListInvitationsRequest | None = None,
    ) -> list[MacieListInvitationsResponse]:
        return await self._paginate('list_invitations', request, MacieListInvitationsResponse)

    async def list_managed_data_identifiers(
        self,
        request: MacieListManagedDataIdentifiersRequest | None = None,
    ) -> MacieListManagedDataIdentifiersResponse:
        client = self._require_client()
        return await self._execute(client.list_managed_data_identifiers, request, MacieListManagedDataIdentifiersResponse)

    async def list_managed_data_identifiers_paginated(
        self,
        request: MacieListManagedDataIdentifiersRequest | None = None,
    ) -> list[MacieListManagedDataIdentifiersResponse]:
        return await self._paginate('list_managed_data_identifiers', request, MacieListManagedDataIdentifiersResponse)

    async def list_members(
        self,
        request: MacieListMembersRequest | None = None,
    ) -> MacieListMembersResponse:
        client = self._require_client()
        return await self._execute(client.list_members, request, MacieListMembersResponse)

    async def list_members_paginated(
        self,
        request: MacieListMembersRequest | None = None,
    ) -> list[MacieListMembersResponse]:
        return await self._paginate('list_members', request, MacieListMembersResponse)

    async def list_organization_admin_accounts(
        self,
        request: MacieListOrganizationAdminAccountsRequest | None = None,
    ) -> MacieListOrganizationAdminAccountsResponse:
        client = self._require_client()
        return await self._execute(client.list_organization_admin_accounts, request, MacieListOrganizationAdminAccountsResponse)

    async def list_organization_admin_accounts_paginated(
        self,
        request: MacieListOrganizationAdminAccountsRequest | None = None,
    ) -> list[MacieListOrganizationAdminAccountsResponse]:
        return await self._paginate('list_organization_admin_accounts', request, MacieListOrganizationAdminAccountsResponse)

    async def list_resource_profile_artifacts(
        self,
        request: MacieListResourceProfileArtifactsRequest,
    ) -> MacieListResourceProfileArtifactsResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_profile_artifacts, request, MacieListResourceProfileArtifactsResponse)

    async def list_resource_profile_artifacts_paginated(
        self,
        request: MacieListResourceProfileArtifactsRequest,
    ) -> list[MacieListResourceProfileArtifactsResponse]:
        return await self._paginate('list_resource_profile_artifacts', request, MacieListResourceProfileArtifactsResponse)

    async def list_resource_profile_detections(
        self,
        request: MacieListResourceProfileDetectionsRequest,
    ) -> MacieListResourceProfileDetectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_profile_detections, request, MacieListResourceProfileDetectionsResponse)

    async def list_resource_profile_detections_paginated(
        self,
        request: MacieListResourceProfileDetectionsRequest,
    ) -> list[MacieListResourceProfileDetectionsResponse]:
        return await self._paginate('list_resource_profile_detections', request, MacieListResourceProfileDetectionsResponse)

    async def list_sensitivity_inspection_templates(
        self,
        request: MacieListSensitivityInspectionTemplatesRequest | None = None,
    ) -> MacieListSensitivityInspectionTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_sensitivity_inspection_templates, request, MacieListSensitivityInspectionTemplatesResponse)

    async def list_sensitivity_inspection_templates_paginated(
        self,
        request: MacieListSensitivityInspectionTemplatesRequest | None = None,
    ) -> list[MacieListSensitivityInspectionTemplatesResponse]:
        return await self._paginate('list_sensitivity_inspection_templates', request, MacieListSensitivityInspectionTemplatesResponse)

    async def list_tags_for_resource(
        self,
        request: MacieListTagsForResourceRequest,
    ) -> MacieListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, MacieListTagsForResourceResponse)

    async def put_classification_export_configuration(
        self,
        request: MaciePutClassificationExportConfigurationRequest,
    ) -> MaciePutClassificationExportConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_classification_export_configuration, request, MaciePutClassificationExportConfigurationResponse)

    async def put_findings_publication_configuration(
        self,
        request: MaciePutFindingsPublicationConfigurationRequest | None = None,
    ) -> MaciePutFindingsPublicationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_findings_publication_configuration, request, MaciePutFindingsPublicationConfigurationResponse)

    async def search_resources(
        self,
        request: MacieSearchResourcesRequest | None = None,
    ) -> MacieSearchResourcesResponse:
        client = self._require_client()
        return await self._execute(client.search_resources, request, MacieSearchResourcesResponse)

    async def search_resources_paginated(
        self,
        request: MacieSearchResourcesRequest | None = None,
    ) -> list[MacieSearchResourcesResponse]:
        return await self._paginate('search_resources', request, MacieSearchResourcesResponse)

    async def tag_resource(
        self,
        request: MacieTagResourceRequest,
    ) -> MacieTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, MacieTagResourceResponse)

    async def test_custom_data_identifier(
        self,
        request: MacieTestCustomDataIdentifierRequest,
    ) -> MacieTestCustomDataIdentifierResponse:
        client = self._require_client()
        return await self._execute(client.test_custom_data_identifier, request, MacieTestCustomDataIdentifierResponse)

    async def untag_resource(
        self,
        request: MacieUntagResourceRequest,
    ) -> MacieUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, MacieUntagResourceResponse)

    async def update_allow_list(
        self,
        request: MacieUpdateAllowListRequest,
    ) -> MacieUpdateAllowListResponse:
        client = self._require_client()
        return await self._execute(client.update_allow_list, request, MacieUpdateAllowListResponse)

    async def update_automated_discovery_configuration(
        self,
        request: MacieUpdateAutomatedDiscoveryConfigurationRequest,
    ) -> MacieUpdateAutomatedDiscoveryConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_automated_discovery_configuration, request, MacieUpdateAutomatedDiscoveryConfigurationResponse)

    async def update_classification_job(
        self,
        request: MacieUpdateClassificationJobRequest,
    ) -> MacieUpdateClassificationJobResponse:
        client = self._require_client()
        return await self._execute(client.update_classification_job, request, MacieUpdateClassificationJobResponse)

    async def update_classification_scope(
        self,
        request: MacieUpdateClassificationScopeRequest,
    ) -> MacieUpdateClassificationScopeResponse:
        client = self._require_client()
        return await self._execute(client.update_classification_scope, request, MacieUpdateClassificationScopeResponse)

    async def update_findings_filter(
        self,
        request: MacieUpdateFindingsFilterRequest,
    ) -> MacieUpdateFindingsFilterResponse:
        client = self._require_client()
        return await self._execute(client.update_findings_filter, request, MacieUpdateFindingsFilterResponse)

    async def update_macie_session(
        self,
        request: MacieUpdateMacieSessionRequest | None = None,
    ) -> MacieUpdateMacieSessionResponse:
        client = self._require_client()
        return await self._execute(client.update_macie_session, request, MacieUpdateMacieSessionResponse)

    async def update_member_session(
        self,
        request: MacieUpdateMemberSessionRequest,
    ) -> MacieUpdateMemberSessionResponse:
        client = self._require_client()
        return await self._execute(client.update_member_session, request, MacieUpdateMemberSessionResponse)

    async def update_organization_configuration(
        self,
        request: MacieUpdateOrganizationConfigurationRequest,
    ) -> MacieUpdateOrganizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_organization_configuration, request, MacieUpdateOrganizationConfigurationResponse)

    async def update_resource_profile(
        self,
        request: MacieUpdateResourceProfileRequest,
    ) -> MacieUpdateResourceProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_resource_profile, request, MacieUpdateResourceProfileResponse)

    async def update_resource_profile_detections(
        self,
        request: MacieUpdateResourceProfileDetectionsRequest,
    ) -> MacieUpdateResourceProfileDetectionsResponse:
        client = self._require_client()
        return await self._execute(client.update_resource_profile_detections, request, MacieUpdateResourceProfileDetectionsResponse)

    async def update_reveal_configuration(
        self,
        request: MacieUpdateRevealConfigurationRequest,
    ) -> MacieUpdateRevealConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_reveal_configuration, request, MacieUpdateRevealConfigurationResponse)

    async def update_sensitivity_inspection_template(
        self,
        request: MacieUpdateSensitivityInspectionTemplateRequest,
    ) -> MacieUpdateSensitivityInspectionTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_sensitivity_inspection_template, request, MacieUpdateSensitivityInspectionTemplateResponse)
