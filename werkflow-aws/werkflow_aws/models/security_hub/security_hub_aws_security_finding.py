from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_action import SecurityHubAction
from .security_hub_compliance import SecurityHubCompliance
from .security_hub_detection import SecurityHubDetection
from .security_hub_finding_provider_fields import SecurityHubFindingProviderFields
from .security_hub_generator_details import SecurityHubGeneratorDetails
from .security_hub_malware import SecurityHubMalware
from .security_hub_network import SecurityHubNetwork
from .security_hub_network_path_component import SecurityHubNetworkPathComponent
from .security_hub_note import SecurityHubNote
from .security_hub_patch_summary import SecurityHubPatchSummary
from .security_hub_process_details import SecurityHubProcessDetails
from .security_hub_related_finding import SecurityHubRelatedFinding
from .security_hub_remediation import SecurityHubRemediation
from .security_hub_resource import SecurityHubResource
from .security_hub_severity import SecurityHubSeverity
from .security_hub_threat import SecurityHubThreat
from .security_hub_threat_intel_indicator import SecurityHubThreatIntelIndicator
from .security_hub_vulnerability import SecurityHubVulnerability
from .security_hub_workflow import SecurityHubWorkflow


class SecurityHubAwsSecurityFinding(BaseModel):
    SchemaVersion: StrictStr | None = None
    Id: StrictStr | None = None
    ProductArn: StrictStr | None = None
    ProductName: StrictStr | None = None
    CompanyName: StrictStr | None = None
    Region: StrictStr | None = None
    GeneratorId: StrictStr | None = None
    AwsAccountId: StrictStr | None = None
    Types: list[StrictStr] | None = None
    FirstObservedAt: StrictStr | None = None
    LastObservedAt: StrictStr | None = None
    CreatedAt: StrictStr | None = None
    UpdatedAt: StrictStr | None = None
    Severity: SecurityHubSeverity | None = None
    Confidence: StrictInt | None = None
    Criticality: StrictInt | None = None
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    Remediation: SecurityHubRemediation | None = None
    SourceUrl: StrictStr | None = None
    ProductFields: dict[StrictStr, StrictStr] | None = None
    UserDefinedFields: dict[StrictStr, StrictStr] | None = None
    Malware: list[SecurityHubMalware] | None = None
    Network: SecurityHubNetwork | None = None
    NetworkPath: list[SecurityHubNetworkPathComponent] | None = None
    Process: SecurityHubProcessDetails | None = None
    Threats: list[SecurityHubThreat] | None = None
    ThreatIntelIndicators: list[SecurityHubThreatIntelIndicator] | None = None
    Resources: list[SecurityHubResource] | None = None
    Compliance: SecurityHubCompliance | None = None
    VerificationState: StrictStr | None = None
    WorkflowState: StrictStr | None = None
    Workflow: SecurityHubWorkflow | None = None
    RecordState: StrictStr | None = None
    RelatedFindings: list[SecurityHubRelatedFinding] | None = None
    Note: SecurityHubNote | None = None
    Vulnerabilities: list[SecurityHubVulnerability] | None = None
    PatchSummary: SecurityHubPatchSummary | None = None
    Action: SecurityHubAction | None = None
    FindingProviderFields: SecurityHubFindingProviderFields | None = None
    Sample: StrictBool | None = None
    GeneratorDetails: SecurityHubGeneratorDetails | None = None
    ProcessedAt: StrictStr | None = None
    AwsAccountName: StrictStr | None = None
    Detection: SecurityHubDetection | None = None
