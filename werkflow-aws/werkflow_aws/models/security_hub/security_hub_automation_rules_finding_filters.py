from __future__ import annotations
from pydantic import BaseModel
from .security_hub_date_filter import SecurityHubDateFilter
from .security_hub_map_filter import SecurityHubMapFilter
from .security_hub_number_filter import SecurityHubNumberFilter
from .security_hub_string_filter import SecurityHubStringFilter


class SecurityHubAutomationRulesFindingFilters(BaseModel):
    ProductArn: list[SecurityHubStringFilter] | None = None
    AwsAccountId: list[SecurityHubStringFilter] | None = None
    Id: list[SecurityHubStringFilter] | None = None
    GeneratorId: list[SecurityHubStringFilter] | None = None
    Type: list[SecurityHubStringFilter] | None = None
    FirstObservedAt: list[SecurityHubDateFilter] | None = None
    LastObservedAt: list[SecurityHubDateFilter] | None = None
    CreatedAt: list[SecurityHubDateFilter] | None = None
    UpdatedAt: list[SecurityHubDateFilter] | None = None
    Confidence: list[SecurityHubNumberFilter] | None = None
    Criticality: list[SecurityHubNumberFilter] | None = None
    Title: list[SecurityHubStringFilter] | None = None
    Description: list[SecurityHubStringFilter] | None = None
    SourceUrl: list[SecurityHubStringFilter] | None = None
    ProductName: list[SecurityHubStringFilter] | None = None
    CompanyName: list[SecurityHubStringFilter] | None = None
    SeverityLabel: list[SecurityHubStringFilter] | None = None
    ResourceType: list[SecurityHubStringFilter] | None = None
    ResourceId: list[SecurityHubStringFilter] | None = None
    ResourcePartition: list[SecurityHubStringFilter] | None = None
    ResourceRegion: list[SecurityHubStringFilter] | None = None
    ResourceTags: list[SecurityHubMapFilter] | None = None
    ResourceDetailsOther: list[SecurityHubMapFilter] | None = None
    ComplianceStatus: list[SecurityHubStringFilter] | None = None
    ComplianceSecurityControlId: list[SecurityHubStringFilter] | None = None
    ComplianceAssociatedStandardsId: list[SecurityHubStringFilter] | None = None
    VerificationState: list[SecurityHubStringFilter] | None = None
    WorkflowStatus: list[SecurityHubStringFilter] | None = None
    RecordState: list[SecurityHubStringFilter] | None = None
    RelatedFindingsProductArn: list[SecurityHubStringFilter] | None = None
    RelatedFindingsId: list[SecurityHubStringFilter] | None = None
    NoteText: list[SecurityHubStringFilter] | None = None
    NoteUpdatedAt: list[SecurityHubDateFilter] | None = None
    NoteUpdatedBy: list[SecurityHubStringFilter] | None = None
    UserDefinedFields: list[SecurityHubMapFilter] | None = None
    ResourceApplicationArn: list[SecurityHubStringFilter] | None = None
    ResourceApplicationName: list[SecurityHubStringFilter] | None = None
    AwsAccountName: list[SecurityHubStringFilter] | None = None
    ResourceProvider: list[SecurityHubStringFilter] | None = None
    ResourceOwnerAccountId: list[SecurityHubStringFilter] | None = None
    ResourceOwnerOrgId: list[SecurityHubStringFilter] | None = None
