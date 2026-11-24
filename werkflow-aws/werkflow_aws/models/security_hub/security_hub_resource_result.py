from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_criticality_source import SecurityHubCriticalitySource
from .security_hub_resource_config import SecurityHubResourceConfig
from .security_hub_resource_findings_summary import SecurityHubResourceFindingsSummary
from .security_hub_resource_info import SecurityHubResourceInfo
from .security_hub_resource_tag import SecurityHubResourceTag


class SecurityHubResourceResult(BaseModel):
    ResourceGuid: StrictStr | None = None
    ResourceId: StrictStr | None = None
    AccountId: StrictStr | None = None
    AccountName: StrictStr | None = None
    Region: StrictStr | None = None
    ResourceProvider: StrictStr | None = None
    ResourceOwnerAccountId: StrictStr | None = None
    ResourceOwnerOrgId: StrictStr | None = None
    ResourceCloudPartition: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
    ResourceCategory: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceName: StrictStr | None = None
    ResourceCreationTimeDt: StrictStr | None = None
    ResourceDetailCaptureTimeDt: StrictStr | None = None
    FindingsSummary: list[SecurityHubResourceFindingsSummary] | None = None
    ResourceTags: list[SecurityHubResourceTag] | None = None
    ResourceConfig: SecurityHubResourceConfig | None = None
    ResourceSubCategory: StrictStr | None = None
    DiscoveryType: StrictStr | None = None
    ResourceInfo: SecurityHubResourceInfo | None = None
    ResourceCriticality: StrictStr | None = None
    CriticalitySources: list[SecurityHubCriticalitySource] | None = None
