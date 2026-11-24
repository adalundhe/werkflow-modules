from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .access_analyzer_finding_source import AccessAnalyzerFindingSource


class AccessAnalyzerExternalAccessDetails(BaseModel):
    action: list[StrictStr] | None = None
    condition: dict[StrictStr, StrictStr] | None = None
    isPublic: StrictBool | None = None
    principal: dict[StrictStr, StrictStr] | None = None
    sources: list[AccessAnalyzerFindingSource] | None = None
    resourceControlPolicyRestriction: StrictStr | None = None
