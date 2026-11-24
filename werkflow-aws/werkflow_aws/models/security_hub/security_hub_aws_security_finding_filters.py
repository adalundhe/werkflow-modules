from __future__ import annotations
from pydantic import BaseModel
from .security_hub_boolean_filter import SecurityHubBooleanFilter
from .security_hub_date_filter import SecurityHubDateFilter
from .security_hub_ip_filter import SecurityHubIpFilter
from .security_hub_keyword_filter import SecurityHubKeywordFilter
from .security_hub_map_filter import SecurityHubMapFilter
from .security_hub_number_filter import SecurityHubNumberFilter
from .security_hub_string_filter import SecurityHubStringFilter


class SecurityHubAwsSecurityFindingFilters(BaseModel):
    ProductArn: list[SecurityHubStringFilter] | None = None
    AwsAccountId: list[SecurityHubStringFilter] | None = None
    Id: list[SecurityHubStringFilter] | None = None
    GeneratorId: list[SecurityHubStringFilter] | None = None
    Region: list[SecurityHubStringFilter] | None = None
    Type: list[SecurityHubStringFilter] | None = None
    FirstObservedAt: list[SecurityHubDateFilter] | None = None
    LastObservedAt: list[SecurityHubDateFilter] | None = None
    CreatedAt: list[SecurityHubDateFilter] | None = None
    UpdatedAt: list[SecurityHubDateFilter] | None = None
    SeverityProduct: list[SecurityHubNumberFilter] | None = None
    SeverityNormalized: list[SecurityHubNumberFilter] | None = None
    SeverityLabel: list[SecurityHubStringFilter] | None = None
    Confidence: list[SecurityHubNumberFilter] | None = None
    Criticality: list[SecurityHubNumberFilter] | None = None
    Title: list[SecurityHubStringFilter] | None = None
    Description: list[SecurityHubStringFilter] | None = None
    RecommendationText: list[SecurityHubStringFilter] | None = None
    SourceUrl: list[SecurityHubStringFilter] | None = None
    ProductFields: list[SecurityHubMapFilter] | None = None
    ProductName: list[SecurityHubStringFilter] | None = None
    CompanyName: list[SecurityHubStringFilter] | None = None
    UserDefinedFields: list[SecurityHubMapFilter] | None = None
    MalwareName: list[SecurityHubStringFilter] | None = None
    MalwareType: list[SecurityHubStringFilter] | None = None
    MalwarePath: list[SecurityHubStringFilter] | None = None
    MalwareState: list[SecurityHubStringFilter] | None = None
    NetworkDirection: list[SecurityHubStringFilter] | None = None
    NetworkProtocol: list[SecurityHubStringFilter] | None = None
    NetworkSourceIpV4: list[SecurityHubIpFilter] | None = None
    NetworkSourceIpV6: list[SecurityHubIpFilter] | None = None
    NetworkSourcePort: list[SecurityHubNumberFilter] | None = None
    NetworkSourceDomain: list[SecurityHubStringFilter] | None = None
    NetworkSourceMac: list[SecurityHubStringFilter] | None = None
    NetworkDestinationIpV4: list[SecurityHubIpFilter] | None = None
    NetworkDestinationIpV6: list[SecurityHubIpFilter] | None = None
    NetworkDestinationPort: list[SecurityHubNumberFilter] | None = None
    NetworkDestinationDomain: list[SecurityHubStringFilter] | None = None
    ProcessName: list[SecurityHubStringFilter] | None = None
    ProcessPath: list[SecurityHubStringFilter] | None = None
    ProcessPid: list[SecurityHubNumberFilter] | None = None
    ProcessParentPid: list[SecurityHubNumberFilter] | None = None
    ProcessLaunchedAt: list[SecurityHubDateFilter] | None = None
    ProcessTerminatedAt: list[SecurityHubDateFilter] | None = None
    ThreatIntelIndicatorType: list[SecurityHubStringFilter] | None = None
    ThreatIntelIndicatorValue: list[SecurityHubStringFilter] | None = None
    ThreatIntelIndicatorCategory: list[SecurityHubStringFilter] | None = None
    ThreatIntelIndicatorLastObservedAt: list[SecurityHubDateFilter] | None = None
    ThreatIntelIndicatorSource: list[SecurityHubStringFilter] | None = None
    ThreatIntelIndicatorSourceUrl: list[SecurityHubStringFilter] | None = None
    ResourceType: list[SecurityHubStringFilter] | None = None
    ResourceId: list[SecurityHubStringFilter] | None = None
    ResourcePartition: list[SecurityHubStringFilter] | None = None
    ResourceRegion: list[SecurityHubStringFilter] | None = None
    ResourceTags: list[SecurityHubMapFilter] | None = None
    ResourceAwsEc2InstanceType: list[SecurityHubStringFilter] | None = None
    ResourceAwsEc2InstanceImageId: list[SecurityHubStringFilter] | None = None
    ResourceAwsEc2InstanceIpV4Addresses: list[SecurityHubIpFilter] | None = None
    ResourceAwsEc2InstanceIpV6Addresses: list[SecurityHubIpFilter] | None = None
    ResourceAwsEc2InstanceKeyName: list[SecurityHubStringFilter] | None = None
    ResourceAwsEc2InstanceIamInstanceProfileArn: list[SecurityHubStringFilter] | None = None
    ResourceAwsEc2InstanceVpcId: list[SecurityHubStringFilter] | None = None
    ResourceAwsEc2InstanceSubnetId: list[SecurityHubStringFilter] | None = None
    ResourceAwsEc2InstanceLaunchedAt: list[SecurityHubDateFilter] | None = None
    ResourceAwsS3BucketOwnerId: list[SecurityHubStringFilter] | None = None
    ResourceAwsS3BucketOwnerName: list[SecurityHubStringFilter] | None = None
    ResourceAwsIamAccessKeyUserName: list[SecurityHubStringFilter] | None = None
    ResourceAwsIamAccessKeyPrincipalName: list[SecurityHubStringFilter] | None = None
    ResourceAwsIamAccessKeyStatus: list[SecurityHubStringFilter] | None = None
    ResourceAwsIamAccessKeyCreatedAt: list[SecurityHubDateFilter] | None = None
    ResourceAwsIamUserUserName: list[SecurityHubStringFilter] | None = None
    ResourceContainerName: list[SecurityHubStringFilter] | None = None
    ResourceContainerImageId: list[SecurityHubStringFilter] | None = None
    ResourceContainerImageName: list[SecurityHubStringFilter] | None = None
    ResourceContainerLaunchedAt: list[SecurityHubDateFilter] | None = None
    ResourceDetailsOther: list[SecurityHubMapFilter] | None = None
    ComplianceStatus: list[SecurityHubStringFilter] | None = None
    VerificationState: list[SecurityHubStringFilter] | None = None
    WorkflowState: list[SecurityHubStringFilter] | None = None
    WorkflowStatus: list[SecurityHubStringFilter] | None = None
    RecordState: list[SecurityHubStringFilter] | None = None
    RelatedFindingsProductArn: list[SecurityHubStringFilter] | None = None
    RelatedFindingsId: list[SecurityHubStringFilter] | None = None
    NoteText: list[SecurityHubStringFilter] | None = None
    NoteUpdatedAt: list[SecurityHubDateFilter] | None = None
    NoteUpdatedBy: list[SecurityHubStringFilter] | None = None
    Keyword: list[SecurityHubKeywordFilter] | None = None
    FindingProviderFieldsConfidence: list[SecurityHubNumberFilter] | None = None
    FindingProviderFieldsCriticality: list[SecurityHubNumberFilter] | None = None
    FindingProviderFieldsRelatedFindingsId: list[SecurityHubStringFilter] | None = None
    FindingProviderFieldsRelatedFindingsProductArn: list[SecurityHubStringFilter] | None = None
    FindingProviderFieldsSeverityLabel: list[SecurityHubStringFilter] | None = None
    FindingProviderFieldsSeverityOriginal: list[SecurityHubStringFilter] | None = None
    FindingProviderFieldsTypes: list[SecurityHubStringFilter] | None = None
    Sample: list[SecurityHubBooleanFilter] | None = None
    ComplianceSecurityControlId: list[SecurityHubStringFilter] | None = None
    ComplianceAssociatedStandardsId: list[SecurityHubStringFilter] | None = None
    VulnerabilitiesExploitAvailable: list[SecurityHubStringFilter] | None = None
    VulnerabilitiesFixAvailable: list[SecurityHubStringFilter] | None = None
    ComplianceSecurityControlParametersName: list[SecurityHubStringFilter] | None = None
    ComplianceSecurityControlParametersValue: list[SecurityHubStringFilter] | None = None
    AwsAccountName: list[SecurityHubStringFilter] | None = None
    ResourceApplicationName: list[SecurityHubStringFilter] | None = None
    ResourceApplicationArn: list[SecurityHubStringFilter] | None = None
    ResourceOwnerAccountId: list[SecurityHubStringFilter] | None = None
    ResourceOwnerOrgId: list[SecurityHubStringFilter] | None = None
    ResourceProvider: list[SecurityHubStringFilter] | None = None
