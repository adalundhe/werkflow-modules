from werkflow_aws.models.security_hub import (
    SecurityHubAcceptAdministratorInvitationRequest,
    SecurityHubAcceptAdministratorInvitationResponse,
    SecurityHubAcceptInvitationRequest,
    SecurityHubAcceptInvitationResponse,
    SecurityHubBatchDeleteAutomationRulesRequest,
    SecurityHubBatchDeleteAutomationRulesResponse,
    SecurityHubBatchDisableStandardsRequest,
    SecurityHubBatchDisableStandardsResponse,
    SecurityHubBatchEnableStandardsRequest,
    SecurityHubBatchEnableStandardsResponse,
    SecurityHubBatchGetAutomationRulesRequest,
    SecurityHubBatchGetAutomationRulesResponse,
    SecurityHubBatchGetConfigurationPolicyAssociationsRequest,
    SecurityHubBatchGetConfigurationPolicyAssociationsResponse,
    SecurityHubBatchGetSecurityControlsRequest,
    SecurityHubBatchGetSecurityControlsResponse,
    SecurityHubBatchGetStandardsControlAssociationsRequest,
    SecurityHubBatchGetStandardsControlAssociationsResponse,
    SecurityHubBatchImportFindingsRequest,
    SecurityHubBatchImportFindingsResponse,
    SecurityHubBatchUpdateAutomationRulesRequest,
    SecurityHubBatchUpdateAutomationRulesResponse,
    SecurityHubBatchUpdateFindingsRequest,
    SecurityHubBatchUpdateFindingsResponse,
    SecurityHubBatchUpdateFindingsV2Request,
    SecurityHubBatchUpdateFindingsV2Response,
    SecurityHubBatchUpdateStandardsControlAssociationsRequest,
    SecurityHubBatchUpdateStandardsControlAssociationsResponse,
    SecurityHubCancelExportJobV2Request,
    SecurityHubCancelExportJobV2Response,
    SecurityHubCreateActionTargetRequest,
    SecurityHubCreateActionTargetResponse,
    SecurityHubCreateAggregatorV2Request,
    SecurityHubCreateAggregatorV2Response,
    SecurityHubCreateAutomationRuleRequest,
    SecurityHubCreateAutomationRuleResponse,
    SecurityHubCreateAutomationRuleV2Request,
    SecurityHubCreateAutomationRuleV2Response,
    SecurityHubCreateConfigurationPolicyRequest,
    SecurityHubCreateConfigurationPolicyResponse,
    SecurityHubCreateConnectorRequest,
    SecurityHubCreateConnectorResponse,
    SecurityHubCreateConnectorV2Request,
    SecurityHubCreateConnectorV2Response,
    SecurityHubCreateFindingAggregatorRequest,
    SecurityHubCreateFindingAggregatorResponse,
    SecurityHubCreateInsightRequest,
    SecurityHubCreateInsightResponse,
    SecurityHubCreateMembersRequest,
    SecurityHubCreateMembersResponse,
    SecurityHubCreateTicketV2Request,
    SecurityHubCreateTicketV2Response,
    SecurityHubDeclineInvitationsRequest,
    SecurityHubDeclineInvitationsResponse,
    SecurityHubDeleteActionTargetRequest,
    SecurityHubDeleteActionTargetResponse,
    SecurityHubDeleteAggregatorV2Request,
    SecurityHubDeleteAggregatorV2Response,
    SecurityHubDeleteAutomationRuleV2Request,
    SecurityHubDeleteAutomationRuleV2Response,
    SecurityHubDeleteConfigurationPolicyRequest,
    SecurityHubDeleteConfigurationPolicyResponse,
    SecurityHubDeleteConnectorRequest,
    SecurityHubDeleteConnectorResponse,
    SecurityHubDeleteConnectorV2Request,
    SecurityHubDeleteConnectorV2Response,
    SecurityHubDeleteFindingAggregatorRequest,
    SecurityHubDeleteFindingAggregatorResponse,
    SecurityHubDeleteInsightRequest,
    SecurityHubDeleteInsightResponse,
    SecurityHubDeleteInvitationsRequest,
    SecurityHubDeleteInvitationsResponse,
    SecurityHubDeleteMembersRequest,
    SecurityHubDeleteMembersResponse,
    SecurityHubDescribeActionTargetsRequest,
    SecurityHubDescribeActionTargetsResponse,
    SecurityHubDescribeHubRequest,
    SecurityHubDescribeHubResponse,
    SecurityHubDescribeOrganizationConfigurationRequest,
    SecurityHubDescribeOrganizationConfigurationResponse,
    SecurityHubDescribeProductsRequest,
    SecurityHubDescribeProductsResponse,
    SecurityHubDescribeProductsV2Request,
    SecurityHubDescribeProductsV2Response,
    SecurityHubDescribeSecurityHubV2Request,
    SecurityHubDescribeSecurityHubV2Response,
    SecurityHubDescribeStandardsControlsRequest,
    SecurityHubDescribeStandardsControlsResponse,
    SecurityHubDescribeStandardsRequest,
    SecurityHubDescribeStandardsResponse,
    SecurityHubDisableImportFindingsForProductRequest,
    SecurityHubDisableImportFindingsForProductResponse,
    SecurityHubDisableOrganizationAdminAccountRequest,
    SecurityHubDisableOrganizationAdminAccountResponse,
    SecurityHubDisableSecurityHubFeatureV2Request,
    SecurityHubDisableSecurityHubFeatureV2Response,
    SecurityHubDisableSecurityHubRequest,
    SecurityHubDisableSecurityHubResponse,
    SecurityHubDisableSecurityHubV2Request,
    SecurityHubDisableSecurityHubV2Response,
    SecurityHubDisassociateFromAdministratorAccountRequest,
    SecurityHubDisassociateFromAdministratorAccountResponse,
    SecurityHubDisassociateFromMasterAccountRequest,
    SecurityHubDisassociateFromMasterAccountResponse,
    SecurityHubDisassociateMembersRequest,
    SecurityHubDisassociateMembersResponse,
    SecurityHubEnableImportFindingsForProductRequest,
    SecurityHubEnableImportFindingsForProductResponse,
    SecurityHubEnableOrganizationAdminAccountRequest,
    SecurityHubEnableOrganizationAdminAccountResponse,
    SecurityHubEnableSecurityHubFeatureV2Request,
    SecurityHubEnableSecurityHubFeatureV2Response,
    SecurityHubEnableSecurityHubRequest,
    SecurityHubEnableSecurityHubResponse,
    SecurityHubEnableSecurityHubV2Request,
    SecurityHubEnableSecurityHubV2Response,
    SecurityHubGenerateRecommendedPolicyV2Request,
    SecurityHubGenerateRecommendedPolicyV2Response,
    SecurityHubGetAdministratorAccountRequest,
    SecurityHubGetAdministratorAccountResponse,
    SecurityHubGetAggregatorV2Request,
    SecurityHubGetAggregatorV2Response,
    SecurityHubGetAutomationRuleV2Request,
    SecurityHubGetAutomationRuleV2Response,
    SecurityHubGetConfigurationPolicyAssociationRequest,
    SecurityHubGetConfigurationPolicyAssociationResponse,
    SecurityHubGetConfigurationPolicyRequest,
    SecurityHubGetConfigurationPolicyResponse,
    SecurityHubGetConnectorRequest,
    SecurityHubGetConnectorResponse,
    SecurityHubGetConnectorV2Request,
    SecurityHubGetConnectorV2Response,
    SecurityHubGetEnabledStandardsRequest,
    SecurityHubGetEnabledStandardsResponse,
    SecurityHubGetExportJobV2Request,
    SecurityHubGetExportJobV2Response,
    SecurityHubGetFindingAggregatorRequest,
    SecurityHubGetFindingAggregatorResponse,
    SecurityHubGetFindingHistoryRequest,
    SecurityHubGetFindingHistoryResponse,
    SecurityHubGetFindingStatisticsV2Request,
    SecurityHubGetFindingStatisticsV2Response,
    SecurityHubGetFindingsRequest,
    SecurityHubGetFindingsResponse,
    SecurityHubGetFindingsTrendsV2Request,
    SecurityHubGetFindingsTrendsV2Response,
    SecurityHubGetFindingsV2Request,
    SecurityHubGetFindingsV2Response,
    SecurityHubGetInsightResultsRequest,
    SecurityHubGetInsightResultsResponse,
    SecurityHubGetInsightsRequest,
    SecurityHubGetInsightsResponse,
    SecurityHubGetInvitationsCountRequest,
    SecurityHubGetInvitationsCountResponse,
    SecurityHubGetMasterAccountRequest,
    SecurityHubGetMasterAccountResponse,
    SecurityHubGetMembersRequest,
    SecurityHubGetMembersResponse,
    SecurityHubGetRecommendedPolicyV2Request,
    SecurityHubGetRecommendedPolicyV2Response,
    SecurityHubGetRemediationsV2Request,
    SecurityHubGetRemediationsV2Response,
    SecurityHubGetResourcesStatisticsV2Request,
    SecurityHubGetResourcesStatisticsV2Response,
    SecurityHubGetResourcesTrendsV2Request,
    SecurityHubGetResourcesTrendsV2Response,
    SecurityHubGetResourcesV2Request,
    SecurityHubGetResourcesV2Response,
    SecurityHubGetSecurityControlDefinitionRequest,
    SecurityHubGetSecurityControlDefinitionResponse,
    SecurityHubGetSoftwareResourcesV2Request,
    SecurityHubGetSoftwareResourcesV2Response,
    SecurityHubGetSoftwareStatisticsV2Request,
    SecurityHubGetSoftwareStatisticsV2Response,
    SecurityHubGetSoftwareV2Request,
    SecurityHubGetSoftwareV2Response,
    SecurityHubInviteMembersRequest,
    SecurityHubInviteMembersResponse,
    SecurityHubListAggregatorsV2Request,
    SecurityHubListAggregatorsV2Response,
    SecurityHubListAutomationRulesRequest,
    SecurityHubListAutomationRulesResponse,
    SecurityHubListAutomationRulesV2Request,
    SecurityHubListAutomationRulesV2Response,
    SecurityHubListConfigurationPoliciesRequest,
    SecurityHubListConfigurationPoliciesResponse,
    SecurityHubListConfigurationPolicyAssociationsRequest,
    SecurityHubListConfigurationPolicyAssociationsResponse,
    SecurityHubListConnectorsRequest,
    SecurityHubListConnectorsResponse,
    SecurityHubListConnectorsV2Request,
    SecurityHubListConnectorsV2Response,
    SecurityHubListEnabledProductsForImportRequest,
    SecurityHubListEnabledProductsForImportResponse,
    SecurityHubListExportJobsV2Request,
    SecurityHubListExportJobsV2Response,
    SecurityHubListExposuresByRemediationV2Request,
    SecurityHubListExposuresByRemediationV2Response,
    SecurityHubListFindingAggregatorsRequest,
    SecurityHubListFindingAggregatorsResponse,
    SecurityHubListFreeTrialStatusesV2Request,
    SecurityHubListFreeTrialStatusesV2Response,
    SecurityHubListInvitationsRequest,
    SecurityHubListInvitationsResponse,
    SecurityHubListMembersRequest,
    SecurityHubListMembersResponse,
    SecurityHubListOrganizationAdminAccountsRequest,
    SecurityHubListOrganizationAdminAccountsResponse,
    SecurityHubListSecurityControlDefinitionsRequest,
    SecurityHubListSecurityControlDefinitionsResponse,
    SecurityHubListStandardsControlAssociationsRequest,
    SecurityHubListStandardsControlAssociationsResponse,
    SecurityHubListTagsForResourceRequest,
    SecurityHubListTagsForResourceResponse,
    SecurityHubRegisterConnectorV2Request,
    SecurityHubRegisterConnectorV2Response,
    SecurityHubStartConfigurationPolicyAssociationRequest,
    SecurityHubStartConfigurationPolicyAssociationResponse,
    SecurityHubStartConfigurationPolicyDisassociationRequest,
    SecurityHubStartConfigurationPolicyDisassociationResponse,
    SecurityHubStartExportJobV2Request,
    SecurityHubStartExportJobV2Response,
    SecurityHubTagResourceRequest,
    SecurityHubTagResourceResponse,
    SecurityHubUntagResourceRequest,
    SecurityHubUntagResourceResponse,
    SecurityHubUpdateActionTargetRequest,
    SecurityHubUpdateActionTargetResponse,
    SecurityHubUpdateAggregatorV2Request,
    SecurityHubUpdateAggregatorV2Response,
    SecurityHubUpdateAutomationRuleV2Request,
    SecurityHubUpdateAutomationRuleV2Response,
    SecurityHubUpdateConfigurationPolicyRequest,
    SecurityHubUpdateConfigurationPolicyResponse,
    SecurityHubUpdateConnectorRequest,
    SecurityHubUpdateConnectorResponse,
    SecurityHubUpdateConnectorV2Request,
    SecurityHubUpdateConnectorV2Response,
    SecurityHubUpdateFindingAggregatorRequest,
    SecurityHubUpdateFindingAggregatorResponse,
    SecurityHubUpdateFindingsRequest,
    SecurityHubUpdateFindingsResponse,
    SecurityHubUpdateInsightRequest,
    SecurityHubUpdateInsightResponse,
    SecurityHubUpdateOrganizationConfigurationRequest,
    SecurityHubUpdateOrganizationConfigurationResponse,
    SecurityHubUpdateSecurityControlRequest,
    SecurityHubUpdateSecurityControlResponse,
    SecurityHubUpdateSecurityHubConfigurationRequest,
    SecurityHubUpdateSecurityHubConfigurationResponse,
    SecurityHubUpdateStandardsControlRequest,
    SecurityHubUpdateStandardsControlResponse,
)
from werkflow_aws.types.security_hub_client import SecurityHubClient
from .base import AWSBaseService


class AWSSecurityHub(AWSBaseService[SecurityHubClient]):
    service_name = 'security-hub'
    boto3_service_name = 'securityhub'

    def __init__(self) -> None:
        super().__init__(service_name='security-hub', boto3_service_name='securityhub')

    async def accept_administrator_invitation(
        self,
        request: SecurityHubAcceptAdministratorInvitationRequest,
    ) -> SecurityHubAcceptAdministratorInvitationResponse:
        client = self._require_client()
        return await self._execute(client.accept_administrator_invitation, request, SecurityHubAcceptAdministratorInvitationResponse)

    async def accept_invitation(
        self,
        request: SecurityHubAcceptInvitationRequest,
    ) -> SecurityHubAcceptInvitationResponse:
        client = self._require_client()
        return await self._execute(client.accept_invitation, request, SecurityHubAcceptInvitationResponse)

    async def batch_delete_automation_rules(
        self,
        request: SecurityHubBatchDeleteAutomationRulesRequest,
    ) -> SecurityHubBatchDeleteAutomationRulesResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_automation_rules, request, SecurityHubBatchDeleteAutomationRulesResponse)

    async def batch_disable_standards(
        self,
        request: SecurityHubBatchDisableStandardsRequest,
    ) -> SecurityHubBatchDisableStandardsResponse:
        client = self._require_client()
        return await self._execute(client.batch_disable_standards, request, SecurityHubBatchDisableStandardsResponse)

    async def batch_enable_standards(
        self,
        request: SecurityHubBatchEnableStandardsRequest,
    ) -> SecurityHubBatchEnableStandardsResponse:
        client = self._require_client()
        return await self._execute(client.batch_enable_standards, request, SecurityHubBatchEnableStandardsResponse)

    async def batch_get_automation_rules(
        self,
        request: SecurityHubBatchGetAutomationRulesRequest,
    ) -> SecurityHubBatchGetAutomationRulesResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_automation_rules, request, SecurityHubBatchGetAutomationRulesResponse)

    async def batch_get_configuration_policy_associations(
        self,
        request: SecurityHubBatchGetConfigurationPolicyAssociationsRequest,
    ) -> SecurityHubBatchGetConfigurationPolicyAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_configuration_policy_associations, request, SecurityHubBatchGetConfigurationPolicyAssociationsResponse)

    async def batch_get_security_controls(
        self,
        request: SecurityHubBatchGetSecurityControlsRequest,
    ) -> SecurityHubBatchGetSecurityControlsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_security_controls, request, SecurityHubBatchGetSecurityControlsResponse)

    async def batch_get_standards_control_associations(
        self,
        request: SecurityHubBatchGetStandardsControlAssociationsRequest,
    ) -> SecurityHubBatchGetStandardsControlAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_standards_control_associations, request, SecurityHubBatchGetStandardsControlAssociationsResponse)

    async def batch_import_findings(
        self,
        request: SecurityHubBatchImportFindingsRequest,
    ) -> SecurityHubBatchImportFindingsResponse:
        client = self._require_client()
        return await self._execute(client.batch_import_findings, request, SecurityHubBatchImportFindingsResponse)

    async def batch_update_automation_rules(
        self,
        request: SecurityHubBatchUpdateAutomationRulesRequest,
    ) -> SecurityHubBatchUpdateAutomationRulesResponse:
        client = self._require_client()
        return await self._execute(client.batch_update_automation_rules, request, SecurityHubBatchUpdateAutomationRulesResponse)

    async def batch_update_findings(
        self,
        request: SecurityHubBatchUpdateFindingsRequest,
    ) -> SecurityHubBatchUpdateFindingsResponse:
        client = self._require_client()
        return await self._execute(client.batch_update_findings, request, SecurityHubBatchUpdateFindingsResponse)

    async def batch_update_findings_v2(
        self,
        request: SecurityHubBatchUpdateFindingsV2Request | None = None,
    ) -> SecurityHubBatchUpdateFindingsV2Response:
        client = self._require_client()
        return await self._execute(client.batch_update_findings_v2, request, SecurityHubBatchUpdateFindingsV2Response)

    async def batch_update_standards_control_associations(
        self,
        request: SecurityHubBatchUpdateStandardsControlAssociationsRequest,
    ) -> SecurityHubBatchUpdateStandardsControlAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.batch_update_standards_control_associations, request, SecurityHubBatchUpdateStandardsControlAssociationsResponse)

    async def cancel_export_job_v2(
        self,
        request: SecurityHubCancelExportJobV2Request,
    ) -> SecurityHubCancelExportJobV2Response:
        client = self._require_client()
        return await self._execute(client.cancel_export_job_v2, request, SecurityHubCancelExportJobV2Response)

    async def create_action_target(
        self,
        request: SecurityHubCreateActionTargetRequest,
    ) -> SecurityHubCreateActionTargetResponse:
        client = self._require_client()
        return await self._execute(client.create_action_target, request, SecurityHubCreateActionTargetResponse)

    async def create_aggregator_v2(
        self,
        request: SecurityHubCreateAggregatorV2Request,
    ) -> SecurityHubCreateAggregatorV2Response:
        client = self._require_client()
        return await self._execute(client.create_aggregator_v2, request, SecurityHubCreateAggregatorV2Response)

    async def create_automation_rule(
        self,
        request: SecurityHubCreateAutomationRuleRequest,
    ) -> SecurityHubCreateAutomationRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_automation_rule, request, SecurityHubCreateAutomationRuleResponse)

    async def create_automation_rule_v2(
        self,
        request: SecurityHubCreateAutomationRuleV2Request,
    ) -> SecurityHubCreateAutomationRuleV2Response:
        client = self._require_client()
        return await self._execute(client.create_automation_rule_v2, request, SecurityHubCreateAutomationRuleV2Response)

    async def create_configuration_policy(
        self,
        request: SecurityHubCreateConfigurationPolicyRequest,
    ) -> SecurityHubCreateConfigurationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_configuration_policy, request, SecurityHubCreateConfigurationPolicyResponse)

    async def create_connector(
        self,
        request: SecurityHubCreateConnectorRequest,
    ) -> SecurityHubCreateConnectorResponse:
        client = self._require_client()
        return await self._execute(client.create_connector, request, SecurityHubCreateConnectorResponse)

    async def create_connector_v2(
        self,
        request: SecurityHubCreateConnectorV2Request,
    ) -> SecurityHubCreateConnectorV2Response:
        client = self._require_client()
        return await self._execute(client.create_connector_v2, request, SecurityHubCreateConnectorV2Response)

    async def create_finding_aggregator(
        self,
        request: SecurityHubCreateFindingAggregatorRequest,
    ) -> SecurityHubCreateFindingAggregatorResponse:
        client = self._require_client()
        return await self._execute(client.create_finding_aggregator, request, SecurityHubCreateFindingAggregatorResponse)

    async def create_insight(
        self,
        request: SecurityHubCreateInsightRequest,
    ) -> SecurityHubCreateInsightResponse:
        client = self._require_client()
        return await self._execute(client.create_insight, request, SecurityHubCreateInsightResponse)

    async def create_members(
        self,
        request: SecurityHubCreateMembersRequest,
    ) -> SecurityHubCreateMembersResponse:
        client = self._require_client()
        return await self._execute(client.create_members, request, SecurityHubCreateMembersResponse)

    async def create_ticket_v2(
        self,
        request: SecurityHubCreateTicketV2Request,
    ) -> SecurityHubCreateTicketV2Response:
        client = self._require_client()
        return await self._execute(client.create_ticket_v2, request, SecurityHubCreateTicketV2Response)

    async def decline_invitations(
        self,
        request: SecurityHubDeclineInvitationsRequest,
    ) -> SecurityHubDeclineInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.decline_invitations, request, SecurityHubDeclineInvitationsResponse)

    async def delete_action_target(
        self,
        request: SecurityHubDeleteActionTargetRequest,
    ) -> SecurityHubDeleteActionTargetResponse:
        client = self._require_client()
        return await self._execute(client.delete_action_target, request, SecurityHubDeleteActionTargetResponse)

    async def delete_aggregator_v2(
        self,
        request: SecurityHubDeleteAggregatorV2Request,
    ) -> SecurityHubDeleteAggregatorV2Response:
        client = self._require_client()
        return await self._execute(client.delete_aggregator_v2, request, SecurityHubDeleteAggregatorV2Response)

    async def delete_automation_rule_v2(
        self,
        request: SecurityHubDeleteAutomationRuleV2Request,
    ) -> SecurityHubDeleteAutomationRuleV2Response:
        client = self._require_client()
        return await self._execute(client.delete_automation_rule_v2, request, SecurityHubDeleteAutomationRuleV2Response)

    async def delete_configuration_policy(
        self,
        request: SecurityHubDeleteConfigurationPolicyRequest,
    ) -> SecurityHubDeleteConfigurationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_configuration_policy, request, SecurityHubDeleteConfigurationPolicyResponse)

    async def delete_connector(
        self,
        request: SecurityHubDeleteConnectorRequest,
    ) -> SecurityHubDeleteConnectorResponse:
        client = self._require_client()
        return await self._execute(client.delete_connector, request, SecurityHubDeleteConnectorResponse)

    async def delete_connector_v2(
        self,
        request: SecurityHubDeleteConnectorV2Request,
    ) -> SecurityHubDeleteConnectorV2Response:
        client = self._require_client()
        return await self._execute(client.delete_connector_v2, request, SecurityHubDeleteConnectorV2Response)

    async def delete_finding_aggregator(
        self,
        request: SecurityHubDeleteFindingAggregatorRequest,
    ) -> SecurityHubDeleteFindingAggregatorResponse:
        client = self._require_client()
        return await self._execute(client.delete_finding_aggregator, request, SecurityHubDeleteFindingAggregatorResponse)

    async def delete_insight(
        self,
        request: SecurityHubDeleteInsightRequest,
    ) -> SecurityHubDeleteInsightResponse:
        client = self._require_client()
        return await self._execute(client.delete_insight, request, SecurityHubDeleteInsightResponse)

    async def delete_invitations(
        self,
        request: SecurityHubDeleteInvitationsRequest,
    ) -> SecurityHubDeleteInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.delete_invitations, request, SecurityHubDeleteInvitationsResponse)

    async def delete_members(
        self,
        request: SecurityHubDeleteMembersRequest,
    ) -> SecurityHubDeleteMembersResponse:
        client = self._require_client()
        return await self._execute(client.delete_members, request, SecurityHubDeleteMembersResponse)

    async def describe_action_targets(
        self,
        request: SecurityHubDescribeActionTargetsRequest | None = None,
    ) -> SecurityHubDescribeActionTargetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_action_targets, request, SecurityHubDescribeActionTargetsResponse)

    async def describe_action_targets_paginated(
        self,
        request: SecurityHubDescribeActionTargetsRequest | None = None,
    ) -> list[SecurityHubDescribeActionTargetsResponse]:
        return await self._paginate('describe_action_targets', request, SecurityHubDescribeActionTargetsResponse)

    async def describe_hub(
        self,
        request: SecurityHubDescribeHubRequest | None = None,
    ) -> SecurityHubDescribeHubResponse:
        client = self._require_client()
        return await self._execute(client.describe_hub, request, SecurityHubDescribeHubResponse)

    async def describe_organization_configuration(
        self,
        request: SecurityHubDescribeOrganizationConfigurationRequest | None = None,
    ) -> SecurityHubDescribeOrganizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_organization_configuration, request, SecurityHubDescribeOrganizationConfigurationResponse)

    async def describe_products(
        self,
        request: SecurityHubDescribeProductsRequest | None = None,
    ) -> SecurityHubDescribeProductsResponse:
        client = self._require_client()
        return await self._execute(client.describe_products, request, SecurityHubDescribeProductsResponse)

    async def describe_products_paginated(
        self,
        request: SecurityHubDescribeProductsRequest | None = None,
    ) -> list[SecurityHubDescribeProductsResponse]:
        return await self._paginate('describe_products', request, SecurityHubDescribeProductsResponse)

    async def describe_products_v2(
        self,
        request: SecurityHubDescribeProductsV2Request | None = None,
    ) -> SecurityHubDescribeProductsV2Response:
        client = self._require_client()
        return await self._execute(client.describe_products_v2, request, SecurityHubDescribeProductsV2Response)

    async def describe_products_v2_paginated(
        self,
        request: SecurityHubDescribeProductsV2Request | None = None,
    ) -> list[SecurityHubDescribeProductsV2Response]:
        return await self._paginate('describe_products_v2', request, SecurityHubDescribeProductsV2Response)

    async def describe_security_hub_v2(
        self,
        request: SecurityHubDescribeSecurityHubV2Request | None = None,
    ) -> SecurityHubDescribeSecurityHubV2Response:
        client = self._require_client()
        return await self._execute(client.describe_security_hub_v2, request, SecurityHubDescribeSecurityHubV2Response)

    async def describe_standards(
        self,
        request: SecurityHubDescribeStandardsRequest | None = None,
    ) -> SecurityHubDescribeStandardsResponse:
        client = self._require_client()
        return await self._execute(client.describe_standards, request, SecurityHubDescribeStandardsResponse)

    async def describe_standards_paginated(
        self,
        request: SecurityHubDescribeStandardsRequest | None = None,
    ) -> list[SecurityHubDescribeStandardsResponse]:
        return await self._paginate('describe_standards', request, SecurityHubDescribeStandardsResponse)

    async def describe_standards_controls(
        self,
        request: SecurityHubDescribeStandardsControlsRequest,
    ) -> SecurityHubDescribeStandardsControlsResponse:
        client = self._require_client()
        return await self._execute(client.describe_standards_controls, request, SecurityHubDescribeStandardsControlsResponse)

    async def describe_standards_controls_paginated(
        self,
        request: SecurityHubDescribeStandardsControlsRequest,
    ) -> list[SecurityHubDescribeStandardsControlsResponse]:
        return await self._paginate('describe_standards_controls', request, SecurityHubDescribeStandardsControlsResponse)

    async def disable_import_findings_for_product(
        self,
        request: SecurityHubDisableImportFindingsForProductRequest,
    ) -> SecurityHubDisableImportFindingsForProductResponse:
        client = self._require_client()
        return await self._execute(client.disable_import_findings_for_product, request, SecurityHubDisableImportFindingsForProductResponse)

    async def disable_organization_admin_account(
        self,
        request: SecurityHubDisableOrganizationAdminAccountRequest,
    ) -> SecurityHubDisableOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.disable_organization_admin_account, request, SecurityHubDisableOrganizationAdminAccountResponse)

    async def disable_security_hub(
        self,
        request: SecurityHubDisableSecurityHubRequest | None = None,
    ) -> SecurityHubDisableSecurityHubResponse:
        client = self._require_client()
        return await self._execute(client.disable_security_hub, request, SecurityHubDisableSecurityHubResponse)

    async def disable_security_hub_feature_v2(
        self,
        request: SecurityHubDisableSecurityHubFeatureV2Request,
    ) -> SecurityHubDisableSecurityHubFeatureV2Response:
        client = self._require_client()
        return await self._execute(client.disable_security_hub_feature_v2, request, SecurityHubDisableSecurityHubFeatureV2Response)

    async def disable_security_hub_v2(
        self,
        request: SecurityHubDisableSecurityHubV2Request | None = None,
    ) -> SecurityHubDisableSecurityHubV2Response:
        client = self._require_client()
        return await self._execute(client.disable_security_hub_v2, request, SecurityHubDisableSecurityHubV2Response)

    async def disassociate_from_administrator_account(
        self,
        request: SecurityHubDisassociateFromAdministratorAccountRequest | None = None,
    ) -> SecurityHubDisassociateFromAdministratorAccountResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_from_administrator_account, request, SecurityHubDisassociateFromAdministratorAccountResponse)

    async def disassociate_from_master_account(
        self,
        request: SecurityHubDisassociateFromMasterAccountRequest | None = None,
    ) -> SecurityHubDisassociateFromMasterAccountResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_from_master_account, request, SecurityHubDisassociateFromMasterAccountResponse)

    async def disassociate_members(
        self,
        request: SecurityHubDisassociateMembersRequest,
    ) -> SecurityHubDisassociateMembersResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_members, request, SecurityHubDisassociateMembersResponse)

    async def enable_import_findings_for_product(
        self,
        request: SecurityHubEnableImportFindingsForProductRequest,
    ) -> SecurityHubEnableImportFindingsForProductResponse:
        client = self._require_client()
        return await self._execute(client.enable_import_findings_for_product, request, SecurityHubEnableImportFindingsForProductResponse)

    async def enable_organization_admin_account(
        self,
        request: SecurityHubEnableOrganizationAdminAccountRequest,
    ) -> SecurityHubEnableOrganizationAdminAccountResponse:
        client = self._require_client()
        return await self._execute(client.enable_organization_admin_account, request, SecurityHubEnableOrganizationAdminAccountResponse)

    async def enable_security_hub(
        self,
        request: SecurityHubEnableSecurityHubRequest | None = None,
    ) -> SecurityHubEnableSecurityHubResponse:
        client = self._require_client()
        return await self._execute(client.enable_security_hub, request, SecurityHubEnableSecurityHubResponse)

    async def enable_security_hub_feature_v2(
        self,
        request: SecurityHubEnableSecurityHubFeatureV2Request,
    ) -> SecurityHubEnableSecurityHubFeatureV2Response:
        client = self._require_client()
        return await self._execute(client.enable_security_hub_feature_v2, request, SecurityHubEnableSecurityHubFeatureV2Response)

    async def enable_security_hub_v2(
        self,
        request: SecurityHubEnableSecurityHubV2Request | None = None,
    ) -> SecurityHubEnableSecurityHubV2Response:
        client = self._require_client()
        return await self._execute(client.enable_security_hub_v2, request, SecurityHubEnableSecurityHubV2Response)

    async def generate_recommended_policy_v2(
        self,
        request: SecurityHubGenerateRecommendedPolicyV2Request,
    ) -> SecurityHubGenerateRecommendedPolicyV2Response:
        client = self._require_client()
        return await self._execute(client.generate_recommended_policy_v2, request, SecurityHubGenerateRecommendedPolicyV2Response)

    async def get_administrator_account(
        self,
        request: SecurityHubGetAdministratorAccountRequest | None = None,
    ) -> SecurityHubGetAdministratorAccountResponse:
        client = self._require_client()
        return await self._execute(client.get_administrator_account, request, SecurityHubGetAdministratorAccountResponse)

    async def get_aggregator_v2(
        self,
        request: SecurityHubGetAggregatorV2Request,
    ) -> SecurityHubGetAggregatorV2Response:
        client = self._require_client()
        return await self._execute(client.get_aggregator_v2, request, SecurityHubGetAggregatorV2Response)

    async def get_automation_rule_v2(
        self,
        request: SecurityHubGetAutomationRuleV2Request,
    ) -> SecurityHubGetAutomationRuleV2Response:
        client = self._require_client()
        return await self._execute(client.get_automation_rule_v2, request, SecurityHubGetAutomationRuleV2Response)

    async def get_configuration_policy(
        self,
        request: SecurityHubGetConfigurationPolicyRequest,
    ) -> SecurityHubGetConfigurationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_configuration_policy, request, SecurityHubGetConfigurationPolicyResponse)

    async def get_configuration_policy_association(
        self,
        request: SecurityHubGetConfigurationPolicyAssociationRequest,
    ) -> SecurityHubGetConfigurationPolicyAssociationResponse:
        client = self._require_client()
        return await self._execute(client.get_configuration_policy_association, request, SecurityHubGetConfigurationPolicyAssociationResponse)

    async def get_connector(
        self,
        request: SecurityHubGetConnectorRequest,
    ) -> SecurityHubGetConnectorResponse:
        client = self._require_client()
        return await self._execute(client.get_connector, request, SecurityHubGetConnectorResponse)

    async def get_connector_v2(
        self,
        request: SecurityHubGetConnectorV2Request,
    ) -> SecurityHubGetConnectorV2Response:
        client = self._require_client()
        return await self._execute(client.get_connector_v2, request, SecurityHubGetConnectorV2Response)

    async def get_enabled_standards(
        self,
        request: SecurityHubGetEnabledStandardsRequest | None = None,
    ) -> SecurityHubGetEnabledStandardsResponse:
        client = self._require_client()
        return await self._execute(client.get_enabled_standards, request, SecurityHubGetEnabledStandardsResponse)

    async def get_enabled_standards_paginated(
        self,
        request: SecurityHubGetEnabledStandardsRequest | None = None,
    ) -> list[SecurityHubGetEnabledStandardsResponse]:
        return await self._paginate('get_enabled_standards', request, SecurityHubGetEnabledStandardsResponse)

    async def get_export_job_v2(
        self,
        request: SecurityHubGetExportJobV2Request,
    ) -> SecurityHubGetExportJobV2Response:
        client = self._require_client()
        return await self._execute(client.get_export_job_v2, request, SecurityHubGetExportJobV2Response)

    async def get_finding_aggregator(
        self,
        request: SecurityHubGetFindingAggregatorRequest,
    ) -> SecurityHubGetFindingAggregatorResponse:
        client = self._require_client()
        return await self._execute(client.get_finding_aggregator, request, SecurityHubGetFindingAggregatorResponse)

    async def get_finding_history(
        self,
        request: SecurityHubGetFindingHistoryRequest,
    ) -> SecurityHubGetFindingHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_finding_history, request, SecurityHubGetFindingHistoryResponse)

    async def get_finding_history_paginated(
        self,
        request: SecurityHubGetFindingHistoryRequest,
    ) -> list[SecurityHubGetFindingHistoryResponse]:
        return await self._paginate('get_finding_history', request, SecurityHubGetFindingHistoryResponse)

    async def get_finding_statistics_v2(
        self,
        request: SecurityHubGetFindingStatisticsV2Request,
    ) -> SecurityHubGetFindingStatisticsV2Response:
        client = self._require_client()
        return await self._execute(client.get_finding_statistics_v2, request, SecurityHubGetFindingStatisticsV2Response)

    async def get_findings(
        self,
        request: SecurityHubGetFindingsRequest | None = None,
    ) -> SecurityHubGetFindingsResponse:
        client = self._require_client()
        return await self._execute(client.get_findings, request, SecurityHubGetFindingsResponse)

    async def get_findings_paginated(
        self,
        request: SecurityHubGetFindingsRequest | None = None,
    ) -> list[SecurityHubGetFindingsResponse]:
        return await self._paginate('get_findings', request, SecurityHubGetFindingsResponse)

    async def get_findings_trends_v2(
        self,
        request: SecurityHubGetFindingsTrendsV2Request,
    ) -> SecurityHubGetFindingsTrendsV2Response:
        client = self._require_client()
        return await self._execute(client.get_findings_trends_v2, request, SecurityHubGetFindingsTrendsV2Response)

    async def get_findings_trends_v2_paginated(
        self,
        request: SecurityHubGetFindingsTrendsV2Request,
    ) -> list[SecurityHubGetFindingsTrendsV2Response]:
        return await self._paginate('get_findings_trends_v2', request, SecurityHubGetFindingsTrendsV2Response)

    async def get_findings_v2(
        self,
        request: SecurityHubGetFindingsV2Request | None = None,
    ) -> SecurityHubGetFindingsV2Response:
        client = self._require_client()
        return await self._execute(client.get_findings_v2, request, SecurityHubGetFindingsV2Response)

    async def get_findings_v2_paginated(
        self,
        request: SecurityHubGetFindingsV2Request | None = None,
    ) -> list[SecurityHubGetFindingsV2Response]:
        return await self._paginate('get_findings_v2', request, SecurityHubGetFindingsV2Response)

    async def get_insight_results(
        self,
        request: SecurityHubGetInsightResultsRequest,
    ) -> SecurityHubGetInsightResultsResponse:
        client = self._require_client()
        return await self._execute(client.get_insight_results, request, SecurityHubGetInsightResultsResponse)

    async def get_insights(
        self,
        request: SecurityHubGetInsightsRequest | None = None,
    ) -> SecurityHubGetInsightsResponse:
        client = self._require_client()
        return await self._execute(client.get_insights, request, SecurityHubGetInsightsResponse)

    async def get_insights_paginated(
        self,
        request: SecurityHubGetInsightsRequest | None = None,
    ) -> list[SecurityHubGetInsightsResponse]:
        return await self._paginate('get_insights', request, SecurityHubGetInsightsResponse)

    async def get_invitations_count(
        self,
        request: SecurityHubGetInvitationsCountRequest | None = None,
    ) -> SecurityHubGetInvitationsCountResponse:
        client = self._require_client()
        return await self._execute(client.get_invitations_count, request, SecurityHubGetInvitationsCountResponse)

    async def get_master_account(
        self,
        request: SecurityHubGetMasterAccountRequest | None = None,
    ) -> SecurityHubGetMasterAccountResponse:
        client = self._require_client()
        return await self._execute(client.get_master_account, request, SecurityHubGetMasterAccountResponse)

    async def get_members(
        self,
        request: SecurityHubGetMembersRequest,
    ) -> SecurityHubGetMembersResponse:
        client = self._require_client()
        return await self._execute(client.get_members, request, SecurityHubGetMembersResponse)

    async def get_recommended_policy_v2(
        self,
        request: SecurityHubGetRecommendedPolicyV2Request,
    ) -> SecurityHubGetRecommendedPolicyV2Response:
        client = self._require_client()
        return await self._execute(client.get_recommended_policy_v2, request, SecurityHubGetRecommendedPolicyV2Response)

    async def get_recommended_policy_v2_paginated(
        self,
        request: SecurityHubGetRecommendedPolicyV2Request,
    ) -> list[SecurityHubGetRecommendedPolicyV2Response]:
        return await self._paginate('get_recommended_policy_v2', request, SecurityHubGetRecommendedPolicyV2Response)

    async def get_remediations_v2(
        self,
        request: SecurityHubGetRemediationsV2Request | None = None,
    ) -> SecurityHubGetRemediationsV2Response:
        client = self._require_client()
        return await self._execute(client.get_remediations_v2, request, SecurityHubGetRemediationsV2Response)

    async def get_remediations_v2_paginated(
        self,
        request: SecurityHubGetRemediationsV2Request | None = None,
    ) -> list[SecurityHubGetRemediationsV2Response]:
        return await self._paginate('get_remediations_v2', request, SecurityHubGetRemediationsV2Response)

    async def get_resources_statistics_v2(
        self,
        request: SecurityHubGetResourcesStatisticsV2Request,
    ) -> SecurityHubGetResourcesStatisticsV2Response:
        client = self._require_client()
        return await self._execute(client.get_resources_statistics_v2, request, SecurityHubGetResourcesStatisticsV2Response)

    async def get_resources_trends_v2(
        self,
        request: SecurityHubGetResourcesTrendsV2Request,
    ) -> SecurityHubGetResourcesTrendsV2Response:
        client = self._require_client()
        return await self._execute(client.get_resources_trends_v2, request, SecurityHubGetResourcesTrendsV2Response)

    async def get_resources_trends_v2_paginated(
        self,
        request: SecurityHubGetResourcesTrendsV2Request,
    ) -> list[SecurityHubGetResourcesTrendsV2Response]:
        return await self._paginate('get_resources_trends_v2', request, SecurityHubGetResourcesTrendsV2Response)

    async def get_resources_v2(
        self,
        request: SecurityHubGetResourcesV2Request | None = None,
    ) -> SecurityHubGetResourcesV2Response:
        client = self._require_client()
        return await self._execute(client.get_resources_v2, request, SecurityHubGetResourcesV2Response)

    async def get_resources_v2_paginated(
        self,
        request: SecurityHubGetResourcesV2Request | None = None,
    ) -> list[SecurityHubGetResourcesV2Response]:
        return await self._paginate('get_resources_v2', request, SecurityHubGetResourcesV2Response)

    async def get_security_control_definition(
        self,
        request: SecurityHubGetSecurityControlDefinitionRequest,
    ) -> SecurityHubGetSecurityControlDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.get_security_control_definition, request, SecurityHubGetSecurityControlDefinitionResponse)

    async def get_software_resources_v2(
        self,
        request: SecurityHubGetSoftwareResourcesV2Request,
    ) -> SecurityHubGetSoftwareResourcesV2Response:
        client = self._require_client()
        return await self._execute(client.get_software_resources_v2, request, SecurityHubGetSoftwareResourcesV2Response)

    async def get_software_resources_v2_paginated(
        self,
        request: SecurityHubGetSoftwareResourcesV2Request,
    ) -> list[SecurityHubGetSoftwareResourcesV2Response]:
        return await self._paginate('get_software_resources_v2', request, SecurityHubGetSoftwareResourcesV2Response)

    async def get_software_statistics_v2(
        self,
        request: SecurityHubGetSoftwareStatisticsV2Request,
    ) -> SecurityHubGetSoftwareStatisticsV2Response:
        client = self._require_client()
        return await self._execute(client.get_software_statistics_v2, request, SecurityHubGetSoftwareStatisticsV2Response)

    async def get_software_v2(
        self,
        request: SecurityHubGetSoftwareV2Request | None = None,
    ) -> SecurityHubGetSoftwareV2Response:
        client = self._require_client()
        return await self._execute(client.get_software_v2, request, SecurityHubGetSoftwareV2Response)

    async def get_software_v2_paginated(
        self,
        request: SecurityHubGetSoftwareV2Request | None = None,
    ) -> list[SecurityHubGetSoftwareV2Response]:
        return await self._paginate('get_software_v2', request, SecurityHubGetSoftwareV2Response)

    async def invite_members(
        self,
        request: SecurityHubInviteMembersRequest,
    ) -> SecurityHubInviteMembersResponse:
        client = self._require_client()
        return await self._execute(client.invite_members, request, SecurityHubInviteMembersResponse)

    async def list_aggregators_v2(
        self,
        request: SecurityHubListAggregatorsV2Request | None = None,
    ) -> SecurityHubListAggregatorsV2Response:
        client = self._require_client()
        return await self._execute(client.list_aggregators_v2, request, SecurityHubListAggregatorsV2Response)

    async def list_aggregators_v2_paginated(
        self,
        request: SecurityHubListAggregatorsV2Request | None = None,
    ) -> list[SecurityHubListAggregatorsV2Response]:
        return await self._paginate('list_aggregators_v2', request, SecurityHubListAggregatorsV2Response)

    async def list_automation_rules(
        self,
        request: SecurityHubListAutomationRulesRequest | None = None,
    ) -> SecurityHubListAutomationRulesResponse:
        client = self._require_client()
        return await self._execute(client.list_automation_rules, request, SecurityHubListAutomationRulesResponse)

    async def list_automation_rules_v2(
        self,
        request: SecurityHubListAutomationRulesV2Request | None = None,
    ) -> SecurityHubListAutomationRulesV2Response:
        client = self._require_client()
        return await self._execute(client.list_automation_rules_v2, request, SecurityHubListAutomationRulesV2Response)

    async def list_configuration_policies(
        self,
        request: SecurityHubListConfigurationPoliciesRequest | None = None,
    ) -> SecurityHubListConfigurationPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_configuration_policies, request, SecurityHubListConfigurationPoliciesResponse)

    async def list_configuration_policies_paginated(
        self,
        request: SecurityHubListConfigurationPoliciesRequest | None = None,
    ) -> list[SecurityHubListConfigurationPoliciesResponse]:
        return await self._paginate('list_configuration_policies', request, SecurityHubListConfigurationPoliciesResponse)

    async def list_configuration_policy_associations(
        self,
        request: SecurityHubListConfigurationPolicyAssociationsRequest | None = None,
    ) -> SecurityHubListConfigurationPolicyAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_configuration_policy_associations, request, SecurityHubListConfigurationPolicyAssociationsResponse)

    async def list_configuration_policy_associations_paginated(
        self,
        request: SecurityHubListConfigurationPolicyAssociationsRequest | None = None,
    ) -> list[SecurityHubListConfigurationPolicyAssociationsResponse]:
        return await self._paginate('list_configuration_policy_associations', request, SecurityHubListConfigurationPolicyAssociationsResponse)

    async def list_connectors(
        self,
        request: SecurityHubListConnectorsRequest | None = None,
    ) -> SecurityHubListConnectorsResponse:
        client = self._require_client()
        return await self._execute(client.list_connectors, request, SecurityHubListConnectorsResponse)

    async def list_connectors_v2(
        self,
        request: SecurityHubListConnectorsV2Request | None = None,
    ) -> SecurityHubListConnectorsV2Response:
        client = self._require_client()
        return await self._execute(client.list_connectors_v2, request, SecurityHubListConnectorsV2Response)

    async def list_enabled_products_for_import(
        self,
        request: SecurityHubListEnabledProductsForImportRequest | None = None,
    ) -> SecurityHubListEnabledProductsForImportResponse:
        client = self._require_client()
        return await self._execute(client.list_enabled_products_for_import, request, SecurityHubListEnabledProductsForImportResponse)

    async def list_enabled_products_for_import_paginated(
        self,
        request: SecurityHubListEnabledProductsForImportRequest | None = None,
    ) -> list[SecurityHubListEnabledProductsForImportResponse]:
        return await self._paginate('list_enabled_products_for_import', request, SecurityHubListEnabledProductsForImportResponse)

    async def list_export_jobs_v2(
        self,
        request: SecurityHubListExportJobsV2Request | None = None,
    ) -> SecurityHubListExportJobsV2Response:
        client = self._require_client()
        return await self._execute(client.list_export_jobs_v2, request, SecurityHubListExportJobsV2Response)

    async def list_export_jobs_v2_paginated(
        self,
        request: SecurityHubListExportJobsV2Request | None = None,
    ) -> list[SecurityHubListExportJobsV2Response]:
        return await self._paginate('list_export_jobs_v2', request, SecurityHubListExportJobsV2Response)

    async def list_exposures_by_remediation_v2(
        self,
        request: SecurityHubListExposuresByRemediationV2Request,
    ) -> SecurityHubListExposuresByRemediationV2Response:
        client = self._require_client()
        return await self._execute(client.list_exposures_by_remediation_v2, request, SecurityHubListExposuresByRemediationV2Response)

    async def list_exposures_by_remediation_v2_paginated(
        self,
        request: SecurityHubListExposuresByRemediationV2Request,
    ) -> list[SecurityHubListExposuresByRemediationV2Response]:
        return await self._paginate('list_exposures_by_remediation_v2', request, SecurityHubListExposuresByRemediationV2Response)

    async def list_finding_aggregators(
        self,
        request: SecurityHubListFindingAggregatorsRequest | None = None,
    ) -> SecurityHubListFindingAggregatorsResponse:
        client = self._require_client()
        return await self._execute(client.list_finding_aggregators, request, SecurityHubListFindingAggregatorsResponse)

    async def list_finding_aggregators_paginated(
        self,
        request: SecurityHubListFindingAggregatorsRequest | None = None,
    ) -> list[SecurityHubListFindingAggregatorsResponse]:
        return await self._paginate('list_finding_aggregators', request, SecurityHubListFindingAggregatorsResponse)

    async def list_free_trial_statuses_v2(
        self,
        request: SecurityHubListFreeTrialStatusesV2Request | None = None,
    ) -> SecurityHubListFreeTrialStatusesV2Response:
        client = self._require_client()
        return await self._execute(client.list_free_trial_statuses_v2, request, SecurityHubListFreeTrialStatusesV2Response)

    async def list_free_trial_statuses_v2_paginated(
        self,
        request: SecurityHubListFreeTrialStatusesV2Request | None = None,
    ) -> list[SecurityHubListFreeTrialStatusesV2Response]:
        return await self._paginate('list_free_trial_statuses_v2', request, SecurityHubListFreeTrialStatusesV2Response)

    async def list_invitations(
        self,
        request: SecurityHubListInvitationsRequest | None = None,
    ) -> SecurityHubListInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.list_invitations, request, SecurityHubListInvitationsResponse)

    async def list_invitations_paginated(
        self,
        request: SecurityHubListInvitationsRequest | None = None,
    ) -> list[SecurityHubListInvitationsResponse]:
        return await self._paginate('list_invitations', request, SecurityHubListInvitationsResponse)

    async def list_members(
        self,
        request: SecurityHubListMembersRequest | None = None,
    ) -> SecurityHubListMembersResponse:
        client = self._require_client()
        return await self._execute(client.list_members, request, SecurityHubListMembersResponse)

    async def list_members_paginated(
        self,
        request: SecurityHubListMembersRequest | None = None,
    ) -> list[SecurityHubListMembersResponse]:
        return await self._paginate('list_members', request, SecurityHubListMembersResponse)

    async def list_organization_admin_accounts(
        self,
        request: SecurityHubListOrganizationAdminAccountsRequest | None = None,
    ) -> SecurityHubListOrganizationAdminAccountsResponse:
        client = self._require_client()
        return await self._execute(client.list_organization_admin_accounts, request, SecurityHubListOrganizationAdminAccountsResponse)

    async def list_organization_admin_accounts_paginated(
        self,
        request: SecurityHubListOrganizationAdminAccountsRequest | None = None,
    ) -> list[SecurityHubListOrganizationAdminAccountsResponse]:
        return await self._paginate('list_organization_admin_accounts', request, SecurityHubListOrganizationAdminAccountsResponse)

    async def list_security_control_definitions(
        self,
        request: SecurityHubListSecurityControlDefinitionsRequest | None = None,
    ) -> SecurityHubListSecurityControlDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.list_security_control_definitions, request, SecurityHubListSecurityControlDefinitionsResponse)

    async def list_security_control_definitions_paginated(
        self,
        request: SecurityHubListSecurityControlDefinitionsRequest | None = None,
    ) -> list[SecurityHubListSecurityControlDefinitionsResponse]:
        return await self._paginate('list_security_control_definitions', request, SecurityHubListSecurityControlDefinitionsResponse)

    async def list_standards_control_associations(
        self,
        request: SecurityHubListStandardsControlAssociationsRequest,
    ) -> SecurityHubListStandardsControlAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_standards_control_associations, request, SecurityHubListStandardsControlAssociationsResponse)

    async def list_standards_control_associations_paginated(
        self,
        request: SecurityHubListStandardsControlAssociationsRequest,
    ) -> list[SecurityHubListStandardsControlAssociationsResponse]:
        return await self._paginate('list_standards_control_associations', request, SecurityHubListStandardsControlAssociationsResponse)

    async def list_tags_for_resource(
        self,
        request: SecurityHubListTagsForResourceRequest,
    ) -> SecurityHubListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, SecurityHubListTagsForResourceResponse)

    async def register_connector_v2(
        self,
        request: SecurityHubRegisterConnectorV2Request,
    ) -> SecurityHubRegisterConnectorV2Response:
        client = self._require_client()
        return await self._execute(client.register_connector_v2, request, SecurityHubRegisterConnectorV2Response)

    async def start_configuration_policy_association(
        self,
        request: SecurityHubStartConfigurationPolicyAssociationRequest,
    ) -> SecurityHubStartConfigurationPolicyAssociationResponse:
        client = self._require_client()
        return await self._execute(client.start_configuration_policy_association, request, SecurityHubStartConfigurationPolicyAssociationResponse)

    async def start_configuration_policy_disassociation(
        self,
        request: SecurityHubStartConfigurationPolicyDisassociationRequest,
    ) -> SecurityHubStartConfigurationPolicyDisassociationResponse:
        client = self._require_client()
        return await self._execute(client.start_configuration_policy_disassociation, request, SecurityHubStartConfigurationPolicyDisassociationResponse)

    async def start_export_job_v2(
        self,
        request: SecurityHubStartExportJobV2Request,
    ) -> SecurityHubStartExportJobV2Response:
        client = self._require_client()
        return await self._execute(client.start_export_job_v2, request, SecurityHubStartExportJobV2Response)

    async def tag_resource(
        self,
        request: SecurityHubTagResourceRequest,
    ) -> SecurityHubTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, SecurityHubTagResourceResponse)

    async def untag_resource(
        self,
        request: SecurityHubUntagResourceRequest,
    ) -> SecurityHubUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, SecurityHubUntagResourceResponse)

    async def update_action_target(
        self,
        request: SecurityHubUpdateActionTargetRequest,
    ) -> SecurityHubUpdateActionTargetResponse:
        client = self._require_client()
        return await self._execute(client.update_action_target, request, SecurityHubUpdateActionTargetResponse)

    async def update_aggregator_v2(
        self,
        request: SecurityHubUpdateAggregatorV2Request,
    ) -> SecurityHubUpdateAggregatorV2Response:
        client = self._require_client()
        return await self._execute(client.update_aggregator_v2, request, SecurityHubUpdateAggregatorV2Response)

    async def update_automation_rule_v2(
        self,
        request: SecurityHubUpdateAutomationRuleV2Request,
    ) -> SecurityHubUpdateAutomationRuleV2Response:
        client = self._require_client()
        return await self._execute(client.update_automation_rule_v2, request, SecurityHubUpdateAutomationRuleV2Response)

    async def update_configuration_policy(
        self,
        request: SecurityHubUpdateConfigurationPolicyRequest,
    ) -> SecurityHubUpdateConfigurationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_configuration_policy, request, SecurityHubUpdateConfigurationPolicyResponse)

    async def update_connector(
        self,
        request: SecurityHubUpdateConnectorRequest,
    ) -> SecurityHubUpdateConnectorResponse:
        client = self._require_client()
        return await self._execute(client.update_connector, request, SecurityHubUpdateConnectorResponse)

    async def update_connector_v2(
        self,
        request: SecurityHubUpdateConnectorV2Request,
    ) -> SecurityHubUpdateConnectorV2Response:
        client = self._require_client()
        return await self._execute(client.update_connector_v2, request, SecurityHubUpdateConnectorV2Response)

    async def update_finding_aggregator(
        self,
        request: SecurityHubUpdateFindingAggregatorRequest,
    ) -> SecurityHubUpdateFindingAggregatorResponse:
        client = self._require_client()
        return await self._execute(client.update_finding_aggregator, request, SecurityHubUpdateFindingAggregatorResponse)

    async def update_findings(
        self,
        request: SecurityHubUpdateFindingsRequest,
    ) -> SecurityHubUpdateFindingsResponse:
        client = self._require_client()
        return await self._execute(client.update_findings, request, SecurityHubUpdateFindingsResponse)

    async def update_insight(
        self,
        request: SecurityHubUpdateInsightRequest,
    ) -> SecurityHubUpdateInsightResponse:
        client = self._require_client()
        return await self._execute(client.update_insight, request, SecurityHubUpdateInsightResponse)

    async def update_organization_configuration(
        self,
        request: SecurityHubUpdateOrganizationConfigurationRequest,
    ) -> SecurityHubUpdateOrganizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_organization_configuration, request, SecurityHubUpdateOrganizationConfigurationResponse)

    async def update_security_control(
        self,
        request: SecurityHubUpdateSecurityControlRequest,
    ) -> SecurityHubUpdateSecurityControlResponse:
        client = self._require_client()
        return await self._execute(client.update_security_control, request, SecurityHubUpdateSecurityControlResponse)

    async def update_security_hub_configuration(
        self,
        request: SecurityHubUpdateSecurityHubConfigurationRequest | None = None,
    ) -> SecurityHubUpdateSecurityHubConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_security_hub_configuration, request, SecurityHubUpdateSecurityHubConfigurationResponse)

    async def update_standards_control(
        self,
        request: SecurityHubUpdateStandardsControlRequest,
    ) -> SecurityHubUpdateStandardsControlResponse:
        client = self._require_client()
        return await self._execute(client.update_standards_control, request, SecurityHubUpdateStandardsControlResponse)
