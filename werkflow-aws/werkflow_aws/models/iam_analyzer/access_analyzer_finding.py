from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .access_analyzer_finding_source import AccessAnalyzerFindingSource


class AccessAnalyzerFinding(BaseModel):
    id: StrictStr | None = None
    principal: dict[StrictStr, StrictStr] | None = None
    action: list[StrictStr] | None = None
    resource: StrictStr | None = None
    isPublic: StrictBool | None = None
    resourceType: StrictStr | None = None
    condition: dict[StrictStr, StrictStr] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    analyzedAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    resourceOwnerAccount: StrictStr | None = None
    error: StrictStr | None = None
    sources: list[AccessAnalyzerFindingSource] | None = None
    resourceControlPolicyRestriction: StrictStr | None = None
