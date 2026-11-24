from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class GuardDutyClient(ABC):

    @abstractmethod
    def accept_administrator_invitation(
        self,
        *,
        DetectorId: str,
        AdministratorId: str,
        InvitationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_invitation(
        self,
        *,
        DetectorId: str,
        MasterId: str,
        InvitationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def archive_findings(
        self,
        *,
        DetectorId: str,
        FindingIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_detection_rule_association(
        self,
        *,
        RuleId: str,
        Mode: str,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_detection_rule_org_configuration(
        self,
        *,
        RuleId: str,
        Mode: str,
        IncludeAccountIds: list[str] | None = None,
        ExcludeAccountIds: list[str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_detector(
        self,
        *,
        Enable: bool,
        ClientToken: str | None = None,
        FindingPublishingFrequency: str | None = None,
        DataSources: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        Features: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_filter(
        self,
        *,
        DetectorId: str,
        Name: str,
        FindingCriteria: dict[str, Any],
        Description: str | None = None,
        Action: str | None = None,
        Rank: int | None = None,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ip_set(
        self,
        *,
        DetectorId: str,
        Name: str,
        Format: str,
        Location: str,
        Activate: bool,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_investigation(
        self,
        *,
        DetectorId: str,
        TriggerPrompt: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_malware_protection_plan(
        self,
        *,
        Role: str,
        ProtectedResource: dict[str, Any],
        ClientToken: str | None = None,
        Actions: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_members(
        self,
        *,
        DetectorId: str,
        AccountDetails: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_publishing_destination(
        self,
        *,
        DetectorId: str,
        DestinationType: str,
        DestinationProperties: dict[str, Any],
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_sample_findings(
        self,
        *,
        DetectorId: str,
        FindingTypes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_threat_entity_set(
        self,
        *,
        DetectorId: str,
        Name: str,
        Format: str,
        Location: str,
        Activate: bool,
        ExpectedBucketOwner: str | None = None,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_threat_intel_set(
        self,
        *,
        DetectorId: str,
        Name: str,
        Format: str,
        Location: str,
        Activate: bool,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_trusted_entity_set(
        self,
        *,
        DetectorId: str,
        Name: str,
        Format: str,
        Location: str,
        Activate: bool,
        ExpectedBucketOwner: str | None = None,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
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
    def delete_custom_detection_rule_association(
        self,
        *,
        RuleId: str,
        AssociationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_detection_rule_org_configuration(
        self,
        *,
        RuleId: str,
        Mode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_detector(
        self,
        *,
        DetectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_filter(
        self,
        *,
        DetectorId: str,
        FilterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ip_set(
        self,
        *,
        DetectorId: str,
        IpSetId: str,
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
    def delete_malware_protection_plan(
        self,
        *,
        MalwareProtectionPlanId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_members(
        self,
        *,
        DetectorId: str,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_publishing_destination(
        self,
        *,
        DetectorId: str,
        DestinationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_threat_entity_set(
        self,
        *,
        DetectorId: str,
        ThreatEntitySetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_threat_intel_set(
        self,
        *,
        DetectorId: str,
        ThreatIntelSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_trusted_entity_set(
        self,
        *,
        DetectorId: str,
        TrustedEntitySetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_malware_scans(
        self,
        *,
        DetectorId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        FilterCriteria: dict[str, Any] | None = None,
        SortCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization_configuration(
        self,
        *,
        DetectorId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_publishing_destination(
        self,
        *,
        DetectorId: str,
        DestinationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_organization_admin_account(
        self,
        *,
        AdminAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_from_administrator_account(
        self,
        *,
        DetectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_from_master_account(
        self,
        *,
        DetectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_members(
        self,
        *,
        DetectorId: str,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_organization_admin_account(
        self,
        *,
        AdminAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_administrator_account(
        self,
        *,
        DetectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_coverage_statistics(
        self,
        *,
        DetectorId: str,
        StatisticsType: list[str],
        FilterCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_custom_detection_rule(
        self,
        *,
        RuleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_custom_detection_rule_association(
        self,
        *,
        RuleId: str,
        AssociationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_custom_detection_rule_org_configuration(
        self,
        *,
        RuleId: str,
        Mode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_detector(
        self,
        *,
        DetectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_filter(
        self,
        *,
        DetectorId: str,
        FilterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_findings(
        self,
        *,
        DetectorId: str,
        FindingIds: list[str],
        SortCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_findings_statistics(
        self,
        *,
        DetectorId: str,
        FindingStatisticTypes: list[str] | None = None,
        FindingCriteria: dict[str, Any] | None = None,
        GroupBy: str | None = None,
        OrderBy: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ip_set(
        self,
        *,
        DetectorId: str,
        IpSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_investigation(
        self,
        *,
        DetectorId: str,
        InvestigationId: str,
        SummaryFormat: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_invitations_count(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_malware_protection_plan(
        self,
        *,
        MalwareProtectionPlanId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_malware_scan(
        self,
        *,
        ScanId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_malware_scan_settings(
        self,
        *,
        DetectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_master_account(
        self,
        *,
        DetectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_member_detectors(
        self,
        *,
        DetectorId: str,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_members(
        self,
        *,
        DetectorId: str,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_organization_statistics(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_remaining_free_trial_days(
        self,
        *,
        DetectorId: str,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_threat_entity_set(
        self,
        *,
        DetectorId: str,
        ThreatEntitySetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_threat_intel_set(
        self,
        *,
        DetectorId: str,
        ThreatIntelSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trusted_entity_set(
        self,
        *,
        DetectorId: str,
        TrustedEntitySetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_usage_statistics(
        self,
        *,
        DetectorId: str,
        UsageStatisticType: str,
        UsageCriteria: dict[str, Any],
        Unit: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invite_members(
        self,
        *,
        DetectorId: str,
        AccountIds: list[str],
        DisableEmailNotification: bool | None = None,
        Message: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_coverage(
        self,
        *,
        DetectorId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        FilterCriteria: dict[str, Any] | None = None,
        SortCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_custom_detection_rule_associations(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        RuleId: str | None = None,
        Mode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_custom_detection_rule_org_configurations(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_custom_detection_rules(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_detectors(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_filters(
        self,
        *,
        DetectorId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_findings(
        self,
        *,
        DetectorId: str,
        FindingCriteria: dict[str, Any] | None = None,
        SortCriteria: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ip_sets(
        self,
        *,
        DetectorId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_investigation_records(
        self,
        *,
        DetectorId: str,
        InvestigationId: str,
        RecordTypes: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_investigations(
        self,
        *,
        DetectorId: str,
        FilterCriteria: dict[str, Any] | None = None,
        SortCriteria: dict[str, Any] | None = None,
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
    def list_malware_protection_plans(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_malware_scans(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        FilterCriteria: dict[str, Any] | None = None,
        SortCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_members(
        self,
        *,
        DetectorId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        OnlyAssociated: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_organization_admin_accounts(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_publishing_destinations(
        self,
        *,
        DetectorId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
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
    def list_threat_entity_sets(
        self,
        *,
        DetectorId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_threat_intel_sets(
        self,
        *,
        DetectorId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_trusted_entity_sets(
        self,
        *,
        DetectorId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_object_malware_scan(
        self,
        *,
        S3Object: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_malware_scan(
        self,
        *,
        ResourceArn: str,
        ClientToken: str | None = None,
        ScanConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_monitoring_members(
        self,
        *,
        DetectorId: str,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_monitoring_members(
        self,
        *,
        DetectorId: str,
        AccountIds: list[str],
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
    def unarchive_findings(
        self,
        *,
        DetectorId: str,
        FindingIds: list[str],
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
    def update_custom_detection_rule_association(
        self,
        *,
        RuleId: str,
        AssociationId: str,
        Mode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_custom_detection_rule_org_configuration(
        self,
        *,
        RuleId: str,
        Mode: str,
        IncludeAccountIds: list[str] | None = None,
        ExcludeAccountIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_detector(
        self,
        *,
        DetectorId: str,
        Enable: bool | None = None,
        FindingPublishingFrequency: str | None = None,
        DataSources: dict[str, Any] | None = None,
        Features: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_filter(
        self,
        *,
        DetectorId: str,
        FilterName: str,
        Description: str | None = None,
        Action: str | None = None,
        Rank: int | None = None,
        FindingCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_findings_feedback(
        self,
        *,
        DetectorId: str,
        FindingIds: list[str],
        Feedback: str,
        Comments: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_ip_set(
        self,
        *,
        DetectorId: str,
        IpSetId: str,
        Name: str | None = None,
        Location: str | None = None,
        Activate: bool | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_malware_protection_plan(
        self,
        *,
        MalwareProtectionPlanId: str,
        Role: str | None = None,
        Actions: dict[str, Any] | None = None,
        ProtectedResource: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_malware_scan_settings(
        self,
        *,
        DetectorId: str,
        ScanResourceCriteria: dict[str, Any] | None = None,
        EbsSnapshotPreservation: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_member_detectors(
        self,
        *,
        DetectorId: str,
        AccountIds: list[str],
        DataSources: dict[str, Any] | None = None,
        Features: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_organization_configuration(
        self,
        *,
        DetectorId: str,
        AutoEnable: bool | None = None,
        DataSources: dict[str, Any] | None = None,
        Features: list[dict[str, Any]] | None = None,
        AutoEnableOrganizationMembers: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_publishing_destination(
        self,
        *,
        DetectorId: str,
        DestinationId: str,
        DestinationProperties: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_threat_entity_set(
        self,
        *,
        DetectorId: str,
        ThreatEntitySetId: str,
        Name: str | None = None,
        Location: str | None = None,
        ExpectedBucketOwner: str | None = None,
        Activate: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_threat_intel_set(
        self,
        *,
        DetectorId: str,
        ThreatIntelSetId: str,
        Name: str | None = None,
        Location: str | None = None,
        Activate: bool | None = None,
        ExpectedBucketOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_trusted_entity_set(
        self,
        *,
        DetectorId: str,
        TrustedEntitySetId: str,
        Name: str | None = None,
        Location: str | None = None,
        ExpectedBucketOwner: str | None = None,
        Activate: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
