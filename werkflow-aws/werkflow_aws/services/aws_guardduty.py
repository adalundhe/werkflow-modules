from werkflow_aws.models.guardduty import (
    GuardDutyAcceptAdministratorInvitationRequest,
    GuardDutyAcceptAdministratorInvitationResponse,
    GuardDutyAcceptInvitationRequest,
    GuardDutyAcceptInvitationResponse,
    GuardDutyArchiveFindingsRequest,
    GuardDutyArchiveFindingsResponse,
    GuardDutyCreateCustomDetectionRuleAssociationRequest,
    GuardDutyCreateCustomDetectionRuleAssociationResponse,
    GuardDutyCreateCustomDetectionRuleOrgConfigurationRequest,
    GuardDutyCreateCustomDetectionRuleOrgConfigurationResponse,
    GuardDutyCreateDetectorRequest,
    GuardDutyCreateDetectorResponse,
    GuardDutyCreateFilterRequest,
    GuardDutyCreateFilterResponse,
    GuardDutyCreateIPSetRequest,
    GuardDutyCreateIPSetResponse,
    GuardDutyCreateInvestigationRequest,
    GuardDutyCreateInvestigationResponse,
    GuardDutyCreateMalwareProtectionPlanRequest,
    GuardDutyCreateMalwareProtectionPlanResponse,
    GuardDutyCreateMembersRequest,
    GuardDutyCreateMembersResponse,
    GuardDutyCreatePublishingDestinationRequest,
    GuardDutyCreatePublishingDestinationResponse,
    GuardDutyCreateSampleFindingsRequest,
    GuardDutyCreateSampleFindingsResponse,
    GuardDutyCreateThreatEntitySetRequest,
    GuardDutyCreateThreatEntitySetResponse,
    GuardDutyCreateThreatIntelSetRequest,
    GuardDutyCreateThreatIntelSetResponse,
    GuardDutyCreateTrustedEntitySetRequest,
    GuardDutyCreateTrustedEntitySetResponse,
    GuardDutyDeclineInvitationsRequest,
    GuardDutyDeclineInvitationsResponse,
    GuardDutyDeleteCustomDetectionRuleAssociationRequest,
    GuardDutyDeleteCustomDetectionRuleAssociationResponse,
    GuardDutyDeleteCustomDetectionRuleOrgConfigurationRequest,
    GuardDutyDeleteCustomDetectionRuleOrgConfigurationResponse,
    GuardDutyDeleteDetectorRequest,
    GuardDutyDeleteDetectorResponse,
    GuardDutyDeleteFilterRequest,
    GuardDutyDeleteFilterResponse,
    GuardDutyDeleteIPSetRequest,
    GuardDutyDeleteIPSetResponse,
    GuardDutyDeleteInvitationsRequest,
    GuardDutyDeleteInvitationsResponse,
    GuardDutyDeleteMalwareProtectionPlanRequest,
    GuardDutyDeleteMalwareProtectionPlanResponse,
    GuardDutyDeleteMembersRequest,
    GuardDutyDeleteMembersResponse,
    GuardDutyDeletePublishingDestinationRequest,
    GuardDutyDeletePublishingDestinationResponse,
    GuardDutyDeleteThreatEntitySetRequest,
    GuardDutyDeleteThreatEntitySetResponse,
    GuardDutyDeleteThreatIntelSetRequest,
    GuardDutyDeleteThreatIntelSetResponse,
    GuardDutyDeleteTrustedEntitySetRequest,
    GuardDutyDeleteTrustedEntitySetResponse,
    GuardDutyDescribeMalwareScansRequest,
    GuardDutyDescribeMalwareScansResponse,
    GuardDutyDescribeOrganizationConfigurationRequest,
    GuardDutyDescribeOrganizationConfigurationResponse,
    GuardDutyDescribePublishingDestinationRequest,
    GuardDutyDescribePublishingDestinationResponse,
    GuardDutyDisableOrganizationAdminAccountRequest,
    GuardDutyDisableOrganizationAdminAccountResponse,
    GuardDutyDisassociateFromAdministratorAccountRequest,
    GuardDutyDisassociateFromAdministratorAccountResponse,
    GuardDutyDisassociateFromMasterAccountRequest,
    GuardDutyDisassociateFromMasterAccountResponse,
    GuardDutyDisassociateMembersRequest,
    GuardDutyDisassociateMembersResponse,
    GuardDutyEnableOrganizationAdminAccountRequest,
    GuardDutyEnableOrganizationAdminAccountResponse,
    GuardDutyGetAdministratorAccountRequest,
    GuardDutyGetAdministratorAccountResponse,
    GuardDutyGetCoverageStatisticsRequest,
    GuardDutyGetCoverageStatisticsResponse,
    GuardDutyGetCustomDetectionRuleAssociationRequest,
    GuardDutyGetCustomDetectionRuleAssociationResponse,
    GuardDutyGetCustomDetectionRuleOrgConfigurationRequest,
    GuardDutyGetCustomDetectionRuleOrgConfigurationResponse,
    GuardDutyGetCustomDetectionRuleRequest,
    GuardDutyGetCustomDetectionRuleResponse,
    GuardDutyGetDetectorRequest,
    GuardDutyGetDetectorResponse,
    GuardDutyGetFilterRequest,
    GuardDutyGetFilterResponse,
    GuardDutyGetFindingsRequest,
    GuardDutyGetFindingsResponse,
    GuardDutyGetFindingsStatisticsRequest,
    GuardDutyGetFindingsStatisticsResponse,
    GuardDutyGetIPSetRequest,
    GuardDutyGetIPSetResponse,
    GuardDutyGetInvestigationRequest,
    GuardDutyGetInvestigationResponse,
    GuardDutyGetInvitationsCountRequest,
    GuardDutyGetInvitationsCountResponse,
    GuardDutyGetMalwareProtectionPlanRequest,
    GuardDutyGetMalwareProtectionPlanResponse,
    GuardDutyGetMalwareScanRequest,
    GuardDutyGetMalwareScanResponse,
    GuardDutyGetMalwareScanSettingsRequest,
    GuardDutyGetMalwareScanSettingsResponse,
    GuardDutyGetMasterAccountRequest,
    GuardDutyGetMasterAccountResponse,
    GuardDutyGetMemberDetectorsRequest,
    GuardDutyGetMemberDetectorsResponse,
    GuardDutyGetMembersRequest,
    GuardDutyGetMembersResponse,
    GuardDutyGetOrganizationStatisticsRequest,
    GuardDutyGetOrganizationStatisticsResponse,
    GuardDutyGetRemainingFreeTrialDaysRequest,
    GuardDutyGetRemainingFreeTrialDaysResponse,
    GuardDutyGetThreatEntitySetRequest,
    GuardDutyGetThreatEntitySetResponse,
    GuardDutyGetThreatIntelSetRequest,
    GuardDutyGetThreatIntelSetResponse,
    GuardDutyGetTrustedEntitySetRequest,
    GuardDutyGetTrustedEntitySetResponse,
    GuardDutyGetUsageStatisticsRequest,
    GuardDutyGetUsageStatisticsResponse,
    GuardDutyInviteMembersRequest,
    GuardDutyInviteMembersResponse,
    GuardDutyListCoverageRequest,
    GuardDutyListCoverageResponse,
    GuardDutyListCustomDetectionRuleAssociationsRequest,
    GuardDutyListCustomDetectionRuleAssociationsResponse,
    GuardDutyListCustomDetectionRuleOrgConfigurationsRequest,
    GuardDutyListCustomDetectionRuleOrgConfigurationsResponse,
    GuardDutyListCustomDetectionRulesRequest,
    GuardDutyListCustomDetectionRulesResponse,
    GuardDutyListDetectorsRequest,
    GuardDutyListDetectorsResponse,
    GuardDutyListFiltersRequest,
    GuardDutyListFiltersResponse,
    GuardDutyListFindingsRequest,
    GuardDutyListFindingsResponse,
    GuardDutyListIPSetsRequest,
    GuardDutyListIPSetsResponse,
    GuardDutyListInvestigationRecordsRequest,
    GuardDutyListInvestigationRecordsResponse,
    GuardDutyListInvestigationsRequest,
    GuardDutyListInvestigationsResponse,
    GuardDutyListInvitationsRequest,
    GuardDutyListInvitationsResponse,
    GuardDutyListMalwareProtectionPlansRequest,
    GuardDutyListMalwareProtectionPlansResponse,
    GuardDutyListMalwareScansRequest,
    GuardDutyListMalwareScansResponse,
    GuardDutyListMembersRequest,
    GuardDutyListMembersResponse,
    GuardDutyListOrganizationAdminAccountsRequest,
    GuardDutyListOrganizationAdminAccountsResponse,
    GuardDutyListPublishingDestinationsRequest,
    GuardDutyListPublishingDestinationsResponse,
    GuardDutyListTagsForResourceRequest,
    GuardDutyListTagsForResourceResponse,
    GuardDutyListThreatEntitySetsRequest,
    GuardDutyListThreatEntitySetsResponse,
    GuardDutyListThreatIntelSetsRequest,
    GuardDutyListThreatIntelSetsResponse,
    GuardDutyListTrustedEntitySetsRequest,
    GuardDutyListTrustedEntitySetsResponse,
    GuardDutySendObjectMalwareScanRequest,
    GuardDutySendObjectMalwareScanResponse,
    GuardDutyStartMalwareScanRequest,
    GuardDutyStartMalwareScanResponse,
    GuardDutyStartMonitoringMembersRequest,
    GuardDutyStartMonitoringMembersResponse,
    GuardDutyStopMonitoringMembersRequest,
    GuardDutyStopMonitoringMembersResponse,
    GuardDutyTagResourceRequest,
    GuardDutyTagResourceResponse,
    GuardDutyUnarchiveFindingsRequest,
    GuardDutyUnarchiveFindingsResponse,
    GuardDutyUntagResourceRequest,
    GuardDutyUntagResourceResponse,
    GuardDutyUpdateCustomDetectionRuleAssociationRequest,
    GuardDutyUpdateCustomDetectionRuleAssociationResponse,
    GuardDutyUpdateCustomDetectionRuleOrgConfigurationRequest,
    GuardDutyUpdateCustomDetectionRuleOrgConfigurationResponse,
    GuardDutyUpdateDetectorRequest,
    GuardDutyUpdateDetectorResponse,
    GuardDutyUpdateFilterRequest,
    GuardDutyUpdateFilterResponse,
    GuardDutyUpdateFindingsFeedbackRequest,
    GuardDutyUpdateFindingsFeedbackResponse,
    GuardDutyUpdateIPSetRequest,
    GuardDutyUpdateIPSetResponse,
    GuardDutyUpdateMalwareProtectionPlanRequest,
    GuardDutyUpdateMalwareProtectionPlanResponse,
    GuardDutyUpdateMalwareScanSettingsRequest,
    GuardDutyUpdateMalwareScanSettingsResponse,
    GuardDutyUpdateMemberDetectorsRequest,
    GuardDutyUpdateMemberDetectorsResponse,
    GuardDutyUpdateOrganizationConfigurationRequest,
    GuardDutyUpdateOrganizationConfigurationResponse,
    GuardDutyUpdatePublishingDestinationRequest,
    GuardDutyUpdatePublishingDestinationResponse,
    GuardDutyUpdateThreatEntitySetRequest,
    GuardDutyUpdateThreatEntitySetResponse,
    GuardDutyUpdateThreatIntelSetRequest,
    GuardDutyUpdateThreatIntelSetResponse,
    GuardDutyUpdateTrustedEntitySetRequest,
    GuardDutyUpdateTrustedEntitySetResponse,
)
from werkflow_aws.types.guardduty_client import GuardDutyClient
from .base import AWSBaseService


class AWSGuardDuty(AWSBaseService[GuardDutyClient]):
    service_name = 'guardduty'
    boto3_service_name = 'guardduty'

    def __init__(self) -> None:
        super().__init__(service_name='guardduty', boto3_service_name='guardduty')

    async def accept_administrator_invitation(
        self,
        request: GuardDutyAcceptAdministratorInvitationRequest,
    ) -> GuardDutyAcceptAdministratorInvitationResponse:
        client = self._require_client()
        return await self._execute(client.accept_administrator_invitation, request, GuardDutyAcceptAdministratorInvitationResponse)

    async def accept_invitation(
        self,
        request: GuardDutyAcceptInvitationRequest,
    ) -> GuardDutyAcceptInvitationResponse:
        client = self._require_client()
        return await self._execute(client.accept_invitation, request, GuardDutyAcceptInvitationResponse)

    async def archive_findings(
        self,
        request: GuardDutyArchiveFindingsRequest,
    ) -> GuardDutyArchiveFindingsResponse:
        client = self._require_client()
        return await self._execute(client.archive_findings, request, GuardDutyArchiveFindingsResponse)

    async def create_custom_detection_rule_association(
        self,
        request: GuardDutyCreateCustomDetectionRuleAssociationRequest,
    ) -> GuardDutyCreateCustomDetectionRuleAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_detection_rule_association, request, GuardDutyCreateCustomDetectionRuleAssociationResponse)

    async def create_custom_detection_rule_org_configuration(
        self,
        request: GuardDutyCreateCustomDetectionRuleOrgConfigurationRequest,
    ) -> GuardDutyCreateCustomDetectionRuleOrgConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_detection_rule_org_configuration, request, GuardDutyCreateCustomDetectionRuleOrgConfigurationResponse)

    async def create_detector(
        self,
        request: GuardDutyCreateDetectorRequest,
    ) -> GuardDutyCreateDetectorResponse:
        client = self._require_client()
        return await self._execute(client.create_detector, request, GuardDutyCreateDetectorResponse)

    async def create_filter(
        self,
        request: GuardDutyCreateFilterRequest,
    ) -> GuardDutyCreateFilterResponse:
        client = self._require_client()
        return await self._execute(client.create_filter, request, GuardDutyCreateFilterResponse)

    async def create_ip_set(
        self,
        request: GuardDutyCreateIPSetRequest,
    ) -> GuardDutyCreateIPSetResponse:
        client = self._require_client()
        return await self._execute(client.create_ip_set, request, GuardDutyCreateIPSetResponse)

    async def create_investigation(
        self,
        request: GuardDutyCreateInvestigationRequest,
    ) -> GuardDutyCreateInvestigationResponse:
        client = self._require_client()
        return await self._execute(client.create_investigation, request, GuardDutyCreateInvestigationResponse)

    async def create_malware_protection_plan(
        self,
        request: GuardDutyCreateMalwareProtectionPlanRequest,
    ) -> GuardDutyCreateMalwareProtectionPlanResponse:
        client = self._require_client()
        return await self._execute(client.create_malware_protection_plan, request, GuardDutyCreateMalwareProtectionPlanResponse)

    async def create_members(
        self,
        request: GuardDutyCreateMembersRequest,
    ) -> GuardDutyCreateMembersResponse:
        client = self._require_client()
        return await self._execute(client.create_members, request, GuardDutyCreateMembersResponse)

    async def create_publishing_destination(
        self,
        request: GuardDutyCreatePublishingDestinationRequest,
    ) -> GuardDutyCreatePublishingDestinationResponse:
        client = self._require_client()
        return await self._execute(client.create_publishing_destination, request, GuardDutyCreatePublishingDestinationResponse)

    async def create_sample_findings(
        self,
        request: GuardDutyCreateSampleFindingsRequest,
    ) -> GuardDutyCreateSampleFindingsResponse:
        client = self._require_client()
        return await self._execute(client.create_sample_findings, request, GuardDutyCreateSampleFindingsResponse)

    async def create_threat_entity_set(
        self,
        request: GuardDutyCreateThreatEntitySetRequest,
    ) -> GuardDutyCreateThreatEntitySetResponse:
        client = self._require_client()
        return await self._execute(client.create_threat_entity_set, request, GuardDutyCreateThreatEntitySetResponse)

    async def create_threat_intel_set(
        self,
        request: GuardDutyCreateThreatIntelSetRequest,
    ) -> GuardDutyCreateThreatIntelSetResponse:
        client = self._require_client()
        return await self._execute(client.create_threat_intel_set, request, GuardDutyCreateThreatIntelSetResponse)

    async def create_trusted_entity_set(
        self,
        request: GuardDutyCreateTrustedEntitySetRequest,
    ) -> GuardDutyCreateTrustedEntitySetResponse:
        client = self._require_client()
        return await self._execute(client.create_trusted_entity_set, request, GuardDutyCreateTrustedEntitySetResponse)

    async def decline_invitations(
        self,
        request: GuardDutyDeclineInvitationsRequest,
    ) -> GuardDutyDeclineInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.decline_invitations, request, GuardDutyDeclineInvitationsResponse)

    async def delete_custom_detection_rule_association(
        self,
        request: GuardDutyDeleteCustomDetectionRuleAssociationRequest,
    ) -> GuardDutyDeleteCustomDetectionRuleAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_detection_rule_association, request, GuardDutyDeleteCustomDetectionRuleAssociationResponse)

    async def delete_custom_detection_rule_org_configuration(
        self,
        request: GuardDutyDeleteCustomDetectionRuleOrgConfigurationRequest,
    ) -> GuardDutyDeleteCustomDetectionRuleOrgConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_detection_rule_org_configuration, request, GuardDutyDeleteCustomDetectionRuleOrgConfigurationResponse)

    async def delete_detector(
        self,
        request: GuardDutyDeleteDetectorRequest,
    ) -> GuardDutyDeleteDetectorResponse:
        client = self._require_client()
        return await self._execute(client.delete_detector, request, GuardDutyDeleteDetectorResponse)

    async def delete_filter(
        self,
        request: GuardDutyDeleteFilterRequest,
    ) -> GuardDutyDeleteFilterResponse:
        client = self._require_client()
        return await self._execute(client.delete_filter, request, GuardDutyDeleteFilterResponse)

    async def delete_ip_set(
        self,
        request: GuardDutyDeleteIPSetRequest,
    ) -> GuardDutyDeleteIPSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_ip_set, request, GuardDutyDeleteIPSetResponse)

    async def delete_invitations(
        self,
        request: GuardDutyDeleteInvitationsRequest,
    ) -> GuardDutyDeleteInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.delete_invitations, request, GuardDutyDeleteInvitationsResponse)

    async def delete_malware_protection_plan(
        self,
        request: GuardDutyDeleteMalwareProtectionPlanRequest,
    ) -> GuardDutyDeleteMalwareProtectionPlanResponse:
        client = self._require_client()
        return await self._execute(client.delete_malware_protection_plan, request, GuardDutyDeleteMalwareProtectionPlanResponse)

    async def delete_members(
        self,
        request: GuardDutyDeleteMembersRequest,
    ) -> GuardDutyDeleteMembersResponse:
        client = self._require_client()
        return await self._execute(client.delete_members, request, GuardDutyDeleteMembersResponse)

    async def delete_publishing_destination(
        self,
        request: GuardDutyDeletePublishingDestinationRequest,
    ) -> GuardDutyDeletePublishingDestinationResponse:
        client = self._require_client()
        return await self._execute(client.delete_publishing_destination, request, GuardDutyDeletePublishingDestinationResponse)

    async def delete_threat_entity_set(
        self,
        request: GuardDutyDeleteThreatEntitySetRequest,
    ) -> GuardDutyDeleteThreatEntitySetResponse:
        client = self._require_client()
        return await self._execute(client.delete_threat_entity_set, request, GuardDutyDeleteThreatEntitySetResponse)

    async def delete_threat_intel_set(
        self,
        request: GuardDutyDeleteThreatIntelSetRequest,
    ) -> GuardDutyDeleteThreatIntelSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_threat_intel_set, request, GuardDutyDeleteThreatIntelSetResponse)

    async def delete_trusted_entity_set(
        self,
        request: GuardDutyDeleteTrustedEntitySetRequest,
    ) -> GuardDutyDeleteTrustedEntitySetResponse:
        client = self._require_client()
        return await self._execute(client.delete_trusted_entity_set, request, GuardDutyDeleteTrustedEntitySetResponse)

    async def describe_malware_scans(
        self,
        request: GuardDutyDescribeMalwareScansRequest,
    ) -> GuardDutyDescribeMalwareScansResponse:
        client = self._require_client()
        return await self._execute(client.describe_malware_scans, request, GuardDutyDescribeMalwareScansResponse)

    async def describe_malware_scans_paginated(
        self,
        request: GuardDutyDescribeMalwareScansRequest,
    ) -> list[GuardDutyDescribeMalwareScansResponse]:
        return await self._paginate('describe_malware_scans', request, GuardDutyDescribeMalwareScansResponse)

    async def describe_organization_configuration(
        self,
        request: GuardDutyDescribeOrganizationConfigurationRequest,
    ) -> GuardDutyDescribeOrganizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_organization_configuration, request, GuardDutyDescribeOrganizationConfigurationResponse)

    async def describe_publishing_destination(
        self,
        request: GuardDutyDescribePublishingDestinationRequest,
    ) -> GuardDutyDescribePublishingDestinationResponse:
        client = self._require_client()
        return await self._execute(client.describe_publishing_destination, request, GuardDutyDescribePublishingDestinationResponse)

    async def disable_organization_admin_account(
        self,
        request: GuardDutyDisableOrganizationAdminAccountRequest,
    ) -> GuardDutyDisableOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.disable_organization_admin_account, request, GuardDutyDisableOrganizationAdminAccountResponse)

    async def disassociate_from_administrator_account(
        self,
        request: GuardDutyDisassociateFromAdministratorAccountRequest,
    ) -> GuardDutyDisassociateFromAdministratorAccountResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_from_administrator_account, request, GuardDutyDisassociateFromAdministratorAccountResponse)

    async def disassociate_from_master_account(
        self,
        request: GuardDutyDisassociateFromMasterAccountRequest,
    ) -> GuardDutyDisassociateFromMasterAccountResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_from_master_account, request, GuardDutyDisassociateFromMasterAccountResponse)

    async def disassociate_members(
        self,
        request: GuardDutyDisassociateMembersRequest,
    ) -> GuardDutyDisassociateMembersResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_members, request, GuardDutyDisassociateMembersResponse)

    async def enable_organization_admin_account(
        self,
        request: GuardDutyEnableOrganizationAdminAccountRequest,
    ) -> GuardDutyEnableOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.enable_organization_admin_account, request, GuardDutyEnableOrganizationAdminAccountResponse)

    async def get_administrator_account(
        self,
        request: GuardDutyGetAdministratorAccountRequest,
    ) -> GuardDutyGetAdministratorAccountResponse:
        client = self._require_client()
        return await self._execute(client.get_administrator_account, request, GuardDutyGetAdministratorAccountResponse)

    async def get_coverage_statistics(
        self,
        request: GuardDutyGetCoverageStatisticsRequest,
    ) -> GuardDutyGetCoverageStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_coverage_statistics, request, GuardDutyGetCoverageStatisticsResponse)

    async def get_custom_detection_rule(
        self,
        request: GuardDutyGetCustomDetectionRuleRequest,
    ) -> GuardDutyGetCustomDetectionRuleResponse:
        client = self._require_client()
        return await self._execute(client.get_custom_detection_rule, request, GuardDutyGetCustomDetectionRuleResponse)

    async def get_custom_detection_rule_association(
        self,
        request: GuardDutyGetCustomDetectionRuleAssociationRequest,
    ) -> GuardDutyGetCustomDetectionRuleAssociationResponse:
        client = self._require_client()
        return await self._execute(client.get_custom_detection_rule_association, request, GuardDutyGetCustomDetectionRuleAssociationResponse)

    async def get_custom_detection_rule_org_configuration(
        self,
        request: GuardDutyGetCustomDetectionRuleOrgConfigurationRequest,
    ) -> GuardDutyGetCustomDetectionRuleOrgConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_custom_detection_rule_org_configuration, request, GuardDutyGetCustomDetectionRuleOrgConfigurationResponse)

    async def get_detector(
        self,
        request: GuardDutyGetDetectorRequest,
    ) -> GuardDutyGetDetectorResponse:
        client = self._require_client()
        return await self._execute(client.get_detector, request, GuardDutyGetDetectorResponse)

    async def get_filter(
        self,
        request: GuardDutyGetFilterRequest,
    ) -> GuardDutyGetFilterResponse:
        client = self._require_client()
        return await self._execute(client.get_filter, request, GuardDutyGetFilterResponse)

    async def get_findings(
        self,
        request: GuardDutyGetFindingsRequest,
    ) -> GuardDutyGetFindingsResponse:
        client = self._require_client()
        return await self._execute(client.get_findings, request, GuardDutyGetFindingsResponse)

    async def get_findings_statistics(
        self,
        request: GuardDutyGetFindingsStatisticsRequest,
    ) -> GuardDutyGetFindingsStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_findings_statistics, request, GuardDutyGetFindingsStatisticsResponse)

    async def get_ip_set(
        self,
        request: GuardDutyGetIPSetRequest,
    ) -> GuardDutyGetIPSetResponse:
        client = self._require_client()
        return await self._execute(client.get_ip_set, request, GuardDutyGetIPSetResponse)

    async def get_investigation(
        self,
        request: GuardDutyGetInvestigationRequest,
    ) -> GuardDutyGetInvestigationResponse:
        client = self._require_client()
        return await self._execute(client.get_investigation, request, GuardDutyGetInvestigationResponse)

    async def get_invitations_count(
        self,
        request: GuardDutyGetInvitationsCountRequest | None = None,
    ) -> GuardDutyGetInvitationsCountResponse:
        client = self._require_client()
        return await self._execute(client.get_invitations_count, request, GuardDutyGetInvitationsCountResponse)

    async def get_malware_protection_plan(
        self,
        request: GuardDutyGetMalwareProtectionPlanRequest,
    ) -> GuardDutyGetMalwareProtectionPlanResponse:
        client = self._require_client()
        return await self._execute(client.get_malware_protection_plan, request, GuardDutyGetMalwareProtectionPlanResponse)

    async def get_malware_scan(
        self,
        request: GuardDutyGetMalwareScanRequest,
    ) -> GuardDutyGetMalwareScanResponse:
        client = self._require_client()
        return await self._execute(client.get_malware_scan, request, GuardDutyGetMalwareScanResponse)

    async def get_malware_scan_settings(
        self,
        request: GuardDutyGetMalwareScanSettingsRequest,
    ) -> GuardDutyGetMalwareScanSettingsResponse:
        client = self._require_client()
        return await self._execute(client.get_malware_scan_settings, request, GuardDutyGetMalwareScanSettingsResponse)

    async def get_master_account(
        self,
        request: GuardDutyGetMasterAccountRequest,
    ) -> GuardDutyGetMasterAccountResponse:
        client = self._require_client()
        return await self._execute(client.get_master_account, request, GuardDutyGetMasterAccountResponse)

    async def get_member_detectors(
        self,
        request: GuardDutyGetMemberDetectorsRequest,
    ) -> GuardDutyGetMemberDetectorsResponse:
        client = self._require_client()
        return await self._execute(client.get_member_detectors, request, GuardDutyGetMemberDetectorsResponse)

    async def get_members(
        self,
        request: GuardDutyGetMembersRequest,
    ) -> GuardDutyGetMembersResponse:
        client = self._require_client()
        return await self._execute(client.get_members, request, GuardDutyGetMembersResponse)

    async def get_organization_statistics(
        self,
        request: GuardDutyGetOrganizationStatisticsRequest | None = None,
    ) -> GuardDutyGetOrganizationStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_organization_statistics, request, GuardDutyGetOrganizationStatisticsResponse)

    async def get_remaining_free_trial_days(
        self,
        request: GuardDutyGetRemainingFreeTrialDaysRequest,
    ) -> GuardDutyGetRemainingFreeTrialDaysResponse:
        client = self._require_client()
        return await self._execute(client.get_remaining_free_trial_days, request, GuardDutyGetRemainingFreeTrialDaysResponse)

    async def get_threat_entity_set(
        self,
        request: GuardDutyGetThreatEntitySetRequest,
    ) -> GuardDutyGetThreatEntitySetResponse:
        client = self._require_client()
        return await self._execute(client.get_threat_entity_set, request, GuardDutyGetThreatEntitySetResponse)

    async def get_threat_intel_set(
        self,
        request: GuardDutyGetThreatIntelSetRequest,
    ) -> GuardDutyGetThreatIntelSetResponse:
        client = self._require_client()
        return await self._execute(client.get_threat_intel_set, request, GuardDutyGetThreatIntelSetResponse)

    async def get_trusted_entity_set(
        self,
        request: GuardDutyGetTrustedEntitySetRequest,
    ) -> GuardDutyGetTrustedEntitySetResponse:
        client = self._require_client()
        return await self._execute(client.get_trusted_entity_set, request, GuardDutyGetTrustedEntitySetResponse)

    async def get_usage_statistics(
        self,
        request: GuardDutyGetUsageStatisticsRequest,
    ) -> GuardDutyGetUsageStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_usage_statistics, request, GuardDutyGetUsageStatisticsResponse)

    async def invite_members(
        self,
        request: GuardDutyInviteMembersRequest,
    ) -> GuardDutyInviteMembersResponse:
        client = self._require_client()
        return await self._execute(client.invite_members, request, GuardDutyInviteMembersResponse)

    async def list_coverage(
        self,
        request: GuardDutyListCoverageRequest,
    ) -> GuardDutyListCoverageResponse:
        client = self._require_client()
        return await self._execute(client.list_coverage, request, GuardDutyListCoverageResponse)

    async def list_coverage_paginated(
        self,
        request: GuardDutyListCoverageRequest,
    ) -> list[GuardDutyListCoverageResponse]:
        return await self._paginate('list_coverage', request, GuardDutyListCoverageResponse)

    async def list_custom_detection_rule_associations(
        self,
        request: GuardDutyListCustomDetectionRuleAssociationsRequest | None = None,
    ) -> GuardDutyListCustomDetectionRuleAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_custom_detection_rule_associations, request, GuardDutyListCustomDetectionRuleAssociationsResponse)

    async def list_custom_detection_rule_associations_paginated(
        self,
        request: GuardDutyListCustomDetectionRuleAssociationsRequest | None = None,
    ) -> list[GuardDutyListCustomDetectionRuleAssociationsResponse]:
        return await self._paginate('list_custom_detection_rule_associations', request, GuardDutyListCustomDetectionRuleAssociationsResponse)

    async def list_custom_detection_rule_org_configurations(
        self,
        request: GuardDutyListCustomDetectionRuleOrgConfigurationsRequest | None = None,
    ) -> GuardDutyListCustomDetectionRuleOrgConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_custom_detection_rule_org_configurations, request, GuardDutyListCustomDetectionRuleOrgConfigurationsResponse)

    async def list_custom_detection_rule_org_configurations_paginated(
        self,
        request: GuardDutyListCustomDetectionRuleOrgConfigurationsRequest | None = None,
    ) -> list[GuardDutyListCustomDetectionRuleOrgConfigurationsResponse]:
        return await self._paginate('list_custom_detection_rule_org_configurations', request, GuardDutyListCustomDetectionRuleOrgConfigurationsResponse)

    async def list_custom_detection_rules(
        self,
        request: GuardDutyListCustomDetectionRulesRequest | None = None,
    ) -> GuardDutyListCustomDetectionRulesResponse:
        client = self._require_client()
        return await self._execute(client.list_custom_detection_rules, request, GuardDutyListCustomDetectionRulesResponse)

    async def list_custom_detection_rules_paginated(
        self,
        request: GuardDutyListCustomDetectionRulesRequest | None = None,
    ) -> list[GuardDutyListCustomDetectionRulesResponse]:
        return await self._paginate('list_custom_detection_rules', request, GuardDutyListCustomDetectionRulesResponse)

    async def list_detectors(
        self,
        request: GuardDutyListDetectorsRequest | None = None,
    ) -> GuardDutyListDetectorsResponse:
        client = self._require_client()
        return await self._execute(client.list_detectors, request, GuardDutyListDetectorsResponse)

    async def list_detectors_paginated(
        self,
        request: GuardDutyListDetectorsRequest | None = None,
    ) -> list[GuardDutyListDetectorsResponse]:
        return await self._paginate('list_detectors', request, GuardDutyListDetectorsResponse)

    async def list_filters(
        self,
        request: GuardDutyListFiltersRequest,
    ) -> GuardDutyListFiltersResponse:
        client = self._require_client()
        return await self._execute(client.list_filters, request, GuardDutyListFiltersResponse)

    async def list_filters_paginated(
        self,
        request: GuardDutyListFiltersRequest,
    ) -> list[GuardDutyListFiltersResponse]:
        return await self._paginate('list_filters', request, GuardDutyListFiltersResponse)

    async def list_findings(
        self,
        request: GuardDutyListFindingsRequest,
    ) -> GuardDutyListFindingsResponse:
        client = self._require_client()
        return await self._execute(client.list_findings, request, GuardDutyListFindingsResponse)

    async def list_findings_paginated(
        self,
        request: GuardDutyListFindingsRequest,
    ) -> list[GuardDutyListFindingsResponse]:
        return await self._paginate('list_findings', request, GuardDutyListFindingsResponse)

    async def list_ip_sets(
        self,
        request: GuardDutyListIPSetsRequest,
    ) -> GuardDutyListIPSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_ip_sets, request, GuardDutyListIPSetsResponse)

    async def list_ip_sets_paginated(
        self,
        request: GuardDutyListIPSetsRequest,
    ) -> list[GuardDutyListIPSetsResponse]:
        return await self._paginate('list_ip_sets', request, GuardDutyListIPSetsResponse)

    async def list_investigation_records(
        self,
        request: GuardDutyListInvestigationRecordsRequest,
    ) -> GuardDutyListInvestigationRecordsResponse:
        client = self._require_client()
        return await self._execute(client.list_investigation_records, request, GuardDutyListInvestigationRecordsResponse)

    async def list_investigation_records_paginated(
        self,
        request: GuardDutyListInvestigationRecordsRequest,
    ) -> list[GuardDutyListInvestigationRecordsResponse]:
        return await self._paginate('list_investigation_records', request, GuardDutyListInvestigationRecordsResponse)

    async def list_investigations(
        self,
        request: GuardDutyListInvestigationsRequest,
    ) -> GuardDutyListInvestigationsResponse:
        client = self._require_client()
        return await self._execute(client.list_investigations, request, GuardDutyListInvestigationsResponse)

    async def list_investigations_paginated(
        self,
        request: GuardDutyListInvestigationsRequest,
    ) -> list[GuardDutyListInvestigationsResponse]:
        return await self._paginate('list_investigations', request, GuardDutyListInvestigationsResponse)

    async def list_invitations(
        self,
        request: GuardDutyListInvitationsRequest | None = None,
    ) -> GuardDutyListInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.list_invitations, request, GuardDutyListInvitationsResponse)

    async def list_invitations_paginated(
        self,
        request: GuardDutyListInvitationsRequest | None = None,
    ) -> list[GuardDutyListInvitationsResponse]:
        return await self._paginate('list_invitations', request, GuardDutyListInvitationsResponse)

    async def list_malware_protection_plans(
        self,
        request: GuardDutyListMalwareProtectionPlansRequest | None = None,
    ) -> GuardDutyListMalwareProtectionPlansResponse:
        client = self._require_client()
        return await self._execute(client.list_malware_protection_plans, request, GuardDutyListMalwareProtectionPlansResponse)

    async def list_malware_scans(
        self,
        request: GuardDutyListMalwareScansRequest | None = None,
    ) -> GuardDutyListMalwareScansResponse:
        client = self._require_client()
        return await self._execute(client.list_malware_scans, request, GuardDutyListMalwareScansResponse)

    async def list_malware_scans_paginated(
        self,
        request: GuardDutyListMalwareScansRequest | None = None,
    ) -> list[GuardDutyListMalwareScansResponse]:
        return await self._paginate('list_malware_scans', request, GuardDutyListMalwareScansResponse)

    async def list_members(
        self,
        request: GuardDutyListMembersRequest,
    ) -> GuardDutyListMembersResponse:
        client = self._require_client()
        return await self._execute(client.list_members, request, GuardDutyListMembersResponse)

    async def list_members_paginated(
        self,
        request: GuardDutyListMembersRequest,
    ) -> list[GuardDutyListMembersResponse]:
        return await self._paginate('list_members', request, GuardDutyListMembersResponse)

    async def list_organization_admin_accounts(
        self,
        request: GuardDutyListOrganizationAdminAccountsRequest | None = None,
    ) -> GuardDutyListOrganizationAdminAccountsResponse:
        client = self._require_client()
        return await self._execute(client.list_organization_admin_accounts, request, GuardDutyListOrganizationAdminAccountsResponse)

    async def list_organization_admin_accounts_paginated(
        self,
        request: GuardDutyListOrganizationAdminAccountsRequest | None = None,
    ) -> list[GuardDutyListOrganizationAdminAccountsResponse]:
        return await self._paginate('list_organization_admin_accounts', request, GuardDutyListOrganizationAdminAccountsResponse)

    async def list_publishing_destinations(
        self,
        request: GuardDutyListPublishingDestinationsRequest,
    ) -> GuardDutyListPublishingDestinationsResponse:
        client = self._require_client()
        return await self._execute(client.list_publishing_destinations, request, GuardDutyListPublishingDestinationsResponse)

    async def list_tags_for_resource(
        self,
        request: GuardDutyListTagsForResourceRequest,
    ) -> GuardDutyListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, GuardDutyListTagsForResourceResponse)

    async def list_threat_entity_sets(
        self,
        request: GuardDutyListThreatEntitySetsRequest,
    ) -> GuardDutyListThreatEntitySetsResponse:
        client = self._require_client()
        return await self._execute(client.list_threat_entity_sets, request, GuardDutyListThreatEntitySetsResponse)

    async def list_threat_entity_sets_paginated(
        self,
        request: GuardDutyListThreatEntitySetsRequest,
    ) -> list[GuardDutyListThreatEntitySetsResponse]:
        return await self._paginate('list_threat_entity_sets', request, GuardDutyListThreatEntitySetsResponse)

    async def list_threat_intel_sets(
        self,
        request: GuardDutyListThreatIntelSetsRequest,
    ) -> GuardDutyListThreatIntelSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_threat_intel_sets, request, GuardDutyListThreatIntelSetsResponse)

    async def list_threat_intel_sets_paginated(
        self,
        request: GuardDutyListThreatIntelSetsRequest,
    ) -> list[GuardDutyListThreatIntelSetsResponse]:
        return await self._paginate('list_threat_intel_sets', request, GuardDutyListThreatIntelSetsResponse)

    async def list_trusted_entity_sets(
        self,
        request: GuardDutyListTrustedEntitySetsRequest,
    ) -> GuardDutyListTrustedEntitySetsResponse:
        client = self._require_client()
        return await self._execute(client.list_trusted_entity_sets, request, GuardDutyListTrustedEntitySetsResponse)

    async def list_trusted_entity_sets_paginated(
        self,
        request: GuardDutyListTrustedEntitySetsRequest,
    ) -> list[GuardDutyListTrustedEntitySetsResponse]:
        return await self._paginate('list_trusted_entity_sets', request, GuardDutyListTrustedEntitySetsResponse)

    async def send_object_malware_scan(
        self,
        request: GuardDutySendObjectMalwareScanRequest | None = None,
    ) -> GuardDutySendObjectMalwareScanResponse:
        client = self._require_client()
        return await self._execute(client.send_object_malware_scan, request, GuardDutySendObjectMalwareScanResponse)

    async def start_malware_scan(
        self,
        request: GuardDutyStartMalwareScanRequest,
    ) -> GuardDutyStartMalwareScanResponse:
        client = self._require_client()
        return await self._execute(client.start_malware_scan, request, GuardDutyStartMalwareScanResponse)

    async def start_monitoring_members(
        self,
        request: GuardDutyStartMonitoringMembersRequest,
    ) -> GuardDutyStartMonitoringMembersResponse:
        client = self._require_client()
        return await self._execute(client.start_monitoring_members, request, GuardDutyStartMonitoringMembersResponse)

    async def stop_monitoring_members(
        self,
        request: GuardDutyStopMonitoringMembersRequest,
    ) -> GuardDutyStopMonitoringMembersResponse:
        client = self._require_client()
        return await self._execute(client.stop_monitoring_members, request, GuardDutyStopMonitoringMembersResponse)

    async def tag_resource(
        self,
        request: GuardDutyTagResourceRequest,
    ) -> GuardDutyTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, GuardDutyTagResourceResponse)

    async def unarchive_findings(
        self,
        request: GuardDutyUnarchiveFindingsRequest,
    ) -> GuardDutyUnarchiveFindingsResponse:
        client = self._require_client()
        return await self._execute(client.unarchive_findings, request, GuardDutyUnarchiveFindingsResponse)

    async def untag_resource(
        self,
        request: GuardDutyUntagResourceRequest,
    ) -> GuardDutyUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, GuardDutyUntagResourceResponse)

    async def update_custom_detection_rule_association(
        self,
        request: GuardDutyUpdateCustomDetectionRuleAssociationRequest,
    ) -> GuardDutyUpdateCustomDetectionRuleAssociationResponse:
        client = self._require_client()
        return await self._execute(client.update_custom_detection_rule_association, request, GuardDutyUpdateCustomDetectionRuleAssociationResponse)

    async def update_custom_detection_rule_org_configuration(
        self,
        request: GuardDutyUpdateCustomDetectionRuleOrgConfigurationRequest,
    ) -> GuardDutyUpdateCustomDetectionRuleOrgConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_custom_detection_rule_org_configuration, request, GuardDutyUpdateCustomDetectionRuleOrgConfigurationResponse)

    async def update_detector(
        self,
        request: GuardDutyUpdateDetectorRequest,
    ) -> GuardDutyUpdateDetectorResponse:
        client = self._require_client()
        return await self._execute(client.update_detector, request, GuardDutyUpdateDetectorResponse)

    async def update_filter(
        self,
        request: GuardDutyUpdateFilterRequest,
    ) -> GuardDutyUpdateFilterResponse:
        client = self._require_client()
        return await self._execute(client.update_filter, request, GuardDutyUpdateFilterResponse)

    async def update_findings_feedback(
        self,
        request: GuardDutyUpdateFindingsFeedbackRequest,
    ) -> GuardDutyUpdateFindingsFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.update_findings_feedback, request, GuardDutyUpdateFindingsFeedbackResponse)

    async def update_ip_set(
        self,
        request: GuardDutyUpdateIPSetRequest,
    ) -> GuardDutyUpdateIPSetResponse:
        client = self._require_client()
        return await self._execute(client.update_ip_set, request, GuardDutyUpdateIPSetResponse)

    async def update_malware_protection_plan(
        self,
        request: GuardDutyUpdateMalwareProtectionPlanRequest,
    ) -> GuardDutyUpdateMalwareProtectionPlanResponse:
        client = self._require_client()
        return await self._execute(client.update_malware_protection_plan, request, GuardDutyUpdateMalwareProtectionPlanResponse)

    async def update_malware_scan_settings(
        self,
        request: GuardDutyUpdateMalwareScanSettingsRequest,
    ) -> GuardDutyUpdateMalwareScanSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_malware_scan_settings, request, GuardDutyUpdateMalwareScanSettingsResponse)

    async def update_member_detectors(
        self,
        request: GuardDutyUpdateMemberDetectorsRequest,
    ) -> GuardDutyUpdateMemberDetectorsResponse:
        client = self._require_client()
        return await self._execute(client.update_member_detectors, request, GuardDutyUpdateMemberDetectorsResponse)

    async def update_organization_configuration(
        self,
        request: GuardDutyUpdateOrganizationConfigurationRequest,
    ) -> GuardDutyUpdateOrganizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_organization_configuration, request, GuardDutyUpdateOrganizationConfigurationResponse)

    async def update_publishing_destination(
        self,
        request: GuardDutyUpdatePublishingDestinationRequest,
    ) -> GuardDutyUpdatePublishingDestinationResponse:
        client = self._require_client()
        return await self._execute(client.update_publishing_destination, request, GuardDutyUpdatePublishingDestinationResponse)

    async def update_threat_entity_set(
        self,
        request: GuardDutyUpdateThreatEntitySetRequest,
    ) -> GuardDutyUpdateThreatEntitySetResponse:
        client = self._require_client()
        return await self._execute(client.update_threat_entity_set, request, GuardDutyUpdateThreatEntitySetResponse)

    async def update_threat_intel_set(
        self,
        request: GuardDutyUpdateThreatIntelSetRequest,
    ) -> GuardDutyUpdateThreatIntelSetResponse:
        client = self._require_client()
        return await self._execute(client.update_threat_intel_set, request, GuardDutyUpdateThreatIntelSetResponse)

    async def update_trusted_entity_set(
        self,
        request: GuardDutyUpdateTrustedEntitySetRequest,
    ) -> GuardDutyUpdateTrustedEntitySetResponse:
        client = self._require_client()
        return await self._execute(client.update_trusted_entity_set, request, GuardDutyUpdateTrustedEntitySetResponse)
