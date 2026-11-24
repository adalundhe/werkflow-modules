from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class SecurityHubClient(ABC):

    @abstractmethod
    def accept_administrator_invitation(
        self,
        *,
        AdministratorId: str,
        InvitationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_invitation(
        self,
        *,
        MasterId: str,
        InvitationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_automation_rules(
        self,
        *,
        AutomationRulesArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_disable_standards(
        self,
        *,
        StandardsSubscriptionArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_enable_standards(
        self,
        *,
        StandardsSubscriptionRequests: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_automation_rules(
        self,
        *,
        AutomationRulesArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_configuration_policy_associations(
        self,
        *,
        ConfigurationPolicyAssociationIdentifiers: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_security_controls(
        self,
        *,
        SecurityControlIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_standards_control_associations(
        self,
        *,
        StandardsControlAssociationIds: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_import_findings(
        self,
        *,
        Findings: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_update_automation_rules(
        self,
        *,
        UpdateAutomationRulesRequestItems: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_update_findings(
        self,
        *,
        FindingIdentifiers: list[dict[str, Any]],
        Note: dict[str, Any] | None = None,
        Severity: dict[str, Any] | None = None,
        VerificationState: str | None = None,
        Confidence: int | None = None,
        Criticality: int | None = None,
        Types: list[str] | None = None,
        UserDefinedFields: dict[str, str] | None = None,
        Workflow: dict[str, Any] | None = None,
        RelatedFindings: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_update_findings_v2(
        self,
        *,
        MetadataUids: list[str] | None = None,
        FindingIdentifiers: list[dict[str, Any]] | None = None,
        Comment: str | None = None,
        SeverityId: int | None = None,
        StatusId: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_update_standards_control_associations(
        self,
        *,
        StandardsControlAssociationUpdates: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_export_job_v2(
        self,
        *,
        ExportJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_action_target(
        self,
        *,
        Name: str,
        Description: str,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_aggregator_v2(
        self,
        *,
        RegionLinkingMode: str,
        LinkedRegions: list[str] | None = None,
        Tags: dict[str, str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_automation_rule(
        self,
        *,
        RuleOrder: int,
        RuleName: str,
        Description: str,
        Criteria: dict[str, Any],
        Actions: list[dict[str, Any]],
        Tags: dict[str, str] | None = None,
        RuleStatus: str | None = None,
        IsTerminal: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_automation_rule_v2(
        self,
        *,
        RuleName: str,
        Description: str,
        RuleOrder: float | int,
        Criteria: dict[str, Any],
        Actions: list[dict[str, Any]],
        RuleStatus: str | None = None,
        Tags: dict[str, str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_configuration_policy(
        self,
        *,
        Name: str,
        ConfigurationPolicy: dict[str, Any],
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connector(
        self,
        *,
        Name: str,
        Provider: dict[str, Any],
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connector_v2(
        self,
        *,
        Name: str,
        Provider: dict[str, Any],
        Description: str | None = None,
        KmsKeyArn: str | None = None,
        Tags: dict[str, str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_finding_aggregator(
        self,
        *,
        RegionLinkingMode: str,
        Regions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_insight(
        self,
        *,
        Name: str,
        Filters: dict[str, Any],
        GroupByAttribute: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_members(
        self,
        *,
        AccountDetails: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ticket_v2(
        self,
        *,
        ConnectorId: str,
        FindingMetadataUid: str,
        ClientToken: str | None = None,
        Mode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def decline_invitations(
        self,
        *,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_action_target(
        self,
        *,
        ActionTargetArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_aggregator_v2(
        self,
        *,
        AggregatorV2Arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_automation_rule_v2(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_configuration_policy(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connector(
        self,
        *,
        ConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connector_v2(
        self,
        *,
        ConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_finding_aggregator(
        self,
        *,
        FindingAggregatorArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_insight(
        self,
        *,
        InsightArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_invitations(
        self,
        *,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_members(
        self,
        *,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_action_targets(
        self,
        *,
        ActionTargetArns: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_hub(
        self,
        *,
        HubArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_products(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ProductArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_products_v2(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_security_hub_v2(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_standards(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Providers: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_standards_controls(
        self,
        *,
        StandardsSubscriptionArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_import_findings_for_product(
        self,
        *,
        ProductSubscriptionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_organization_admin_account(
        self,
        *,
        AdminAccountId: str,
        Feature: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_security_hub(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_security_hub_feature_v2(
        self,
        *,
        FeatureName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_security_hub_v2(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_from_administrator_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_from_master_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_members(
        self,
        *,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_import_findings_for_product(
        self,
        *,
        ProductArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_organization_admin_account(
        self,
        *,
        AdminAccountId: str,
        Feature: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_security_hub(
        self,
        *,
        Tags: dict[str, str] | None = None,
        EnableDefaultStandards: bool | None = None,
        ControlFindingGenerator: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_security_hub_feature_v2(
        self,
        *,
        FeatureName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_security_hub_v2(
        self,
        *,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_recommended_policy_v2(
        self,
        *,
        MetadataUid: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_administrator_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_aggregator_v2(
        self,
        *,
        AggregatorV2Arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_automation_rule_v2(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_configuration_policy(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_configuration_policy_association(
        self,
        *,
        Target: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connector(
        self,
        *,
        ConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connector_v2(
        self,
        *,
        ConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_enabled_standards(
        self,
        *,
        StandardsSubscriptionArns: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Providers: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_export_job_v2(
        self,
        *,
        ExportJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_finding_aggregator(
        self,
        *,
        FindingAggregatorArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_finding_history(
        self,
        *,
        FindingIdentifier: dict[str, Any],
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_finding_statistics_v2(
        self,
        *,
        GroupByRules: list[dict[str, Any]],
        Scopes: dict[str, Any] | None = None,
        SortOrder: str | None = None,
        MaxStatisticResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_findings(
        self,
        *,
        Filters: dict[str, Any] | None = None,
        SortCriteria: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_findings_trends_v2(
        self,
        *,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        Filters: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_findings_v2(
        self,
        *,
        Filters: dict[str, Any] | None = None,
        Scopes: dict[str, Any] | None = None,
        SortCriteria: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_insight_results(
        self,
        *,
        InsightArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_insights(
        self,
        *,
        InsightArns: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_invitations_count(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_master_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_members(
        self,
        *,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_recommended_policy_v2(
        self,
        *,
        MetadataUid: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_remediations_v2(
        self,
        *,
        TargetUid: str | None = None,
        MetadataUid: str | None = None,
        Filters: dict[str, Any] | None = None,
        ShowGuidance: bool | None = None,
        GuidanceFormat: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resources_statistics_v2(
        self,
        *,
        GroupByRules: list[dict[str, Any]],
        Scopes: dict[str, Any] | None = None,
        SortOrder: str | None = None,
        MaxStatisticResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resources_trends_v2(
        self,
        *,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        Filters: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resources_v2(
        self,
        *,
        Filters: dict[str, Any] | None = None,
        Scopes: dict[str, Any] | None = None,
        SortCriteria: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_security_control_definition(
        self,
        *,
        SecurityControlId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_software_resources_v2(
        self,
        *,
        PackageName: str,
        PackageType: str,
        PackageVersion: str | None = None,
        Filters: dict[str, Any] | None = None,
        Scopes: dict[str, Any] | None = None,
        SortCriteria: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_software_statistics_v2(
        self,
        *,
        GroupByRules: list[dict[str, Any]],
        Scopes: dict[str, Any] | None = None,
        SortOrder: str | None = None,
        MaxStatisticResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_software_v2(
        self,
        *,
        Filters: dict[str, Any] | None = None,
        Scopes: dict[str, Any] | None = None,
        SortCriteria: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invite_members(
        self,
        *,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_aggregators_v2(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_automation_rules(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_automation_rules_v2(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_configuration_policies(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_configuration_policy_associations(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connectors(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ProviderName: str | None = None,
        ConnectorStatus: str | None = None,
        EnablementStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connectors_v2(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ProviderName: str | None = None,
        ConnectorStatus: str | None = None,
        EnablementStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_enabled_products_for_import(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_export_jobs_v2(
        self,
        *,
        Status: str | None = None,
        DataType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_exposures_by_remediation_v2(
        self,
        *,
        TargetUid: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_finding_aggregators(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_free_trial_statuses_v2(
        self,
        *,
        AccountIds: list[str] | None = None,
        Statuses: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_invitations(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_members(
        self,
        *,
        OnlyAssociated: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_organization_admin_accounts(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Feature: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_control_definitions(
        self,
        *,
        StandardsArn: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Providers: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_standards_control_associations(
        self,
        *,
        SecurityControlId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_connector_v2(
        self,
        *,
        AuthCode: str,
        AuthState: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_configuration_policy_association(
        self,
        *,
        ConfigurationPolicyIdentifier: str,
        Target: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_configuration_policy_disassociation(
        self,
        *,
        ConfigurationPolicyIdentifier: str,
        Target: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_export_job_v2(
        self,
        *,
        Destination: dict[str, Any],
        OutputConfiguration: dict[str, Any],
        Name: str | None = None,
        Scopes: dict[str, Any] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_action_target(
        self,
        *,
        ActionTargetArn: str,
        Name: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_aggregator_v2(
        self,
        *,
        AggregatorV2Arn: str,
        RegionLinkingMode: str,
        LinkedRegions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_automation_rule_v2(
        self,
        *,
        Identifier: str,
        RuleStatus: str | None = None,
        RuleOrder: float | int | None = None,
        Description: str | None = None,
        RuleName: str | None = None,
        Criteria: dict[str, Any] | None = None,
        Actions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_configuration_policy(
        self,
        *,
        Identifier: str,
        Name: str | None = None,
        Description: str | None = None,
        UpdatedReason: str | None = None,
        ConfigurationPolicy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connector(
        self,
        *,
        ConnectorId: str,
        Description: str | None = None,
        Provider: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connector_v2(
        self,
        *,
        ConnectorId: str,
        Description: str | None = None,
        Provider: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_finding_aggregator(
        self,
        *,
        FindingAggregatorArn: str,
        RegionLinkingMode: str,
        Regions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_findings(
        self,
        *,
        Filters: dict[str, Any],
        Note: dict[str, Any] | None = None,
        RecordState: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_insight(
        self,
        *,
        InsightArn: str,
        Name: str | None = None,
        Filters: dict[str, Any] | None = None,
        GroupByAttribute: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_organization_configuration(
        self,
        *,
        AutoEnable: bool,
        AutoEnableStandards: str | None = None,
        OrganizationConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_security_control(
        self,
        *,
        SecurityControlId: str,
        Parameters: dict[str, dict[str, Any]],
        LastUpdateReason: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_security_hub_configuration(
        self,
        *,
        AutoEnableControls: bool | None = None,
        ControlFindingGenerator: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_standards_control(
        self,
        *,
        StandardsControlArn: str,
        ControlStatus: str | None = None,
        DisabledReason: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
