from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_finding_details import AccessAnalyzerFindingDetails


class AccessAnalyzerGetFindingV2Response(BaseModel):
    analyzedAt: datetime.datetime | StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    error: StrictStr | None = None
    id: StrictStr | None = None
    nextToken: StrictStr | None = None
    resource: StrictStr | None = None
    resourceType: StrictStr | None = None
    resourceOwnerAccount: StrictStr | None = None
    status: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    findingDetails: list[AccessAnalyzerFindingDetails] | None = None
    findingType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
