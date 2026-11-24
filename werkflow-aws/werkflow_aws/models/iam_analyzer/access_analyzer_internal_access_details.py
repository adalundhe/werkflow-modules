from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_finding_source import AccessAnalyzerFindingSource


class AccessAnalyzerInternalAccessDetails(BaseModel):
    action: list[StrictStr] | None = None
    condition: dict[StrictStr, StrictStr] | None = None
    principal: dict[StrictStr, StrictStr] | None = None
    principalOwnerAccount: StrictStr | None = None
    accessType: StrictStr | None = None
    principalType: StrictStr | None = None
    sources: list[AccessAnalyzerFindingSource] | None = None
    resourceControlPolicyRestriction: StrictStr | None = None
    serviceControlPolicyRestriction: StrictStr | None = None
