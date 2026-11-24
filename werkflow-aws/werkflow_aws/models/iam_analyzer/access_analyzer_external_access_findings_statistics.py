from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .access_analyzer_resource_type_details import AccessAnalyzerResourceTypeDetails


class AccessAnalyzerExternalAccessFindingsStatistics(BaseModel):
    resourceTypeStatistics: dict[StrictStr, AccessAnalyzerResourceTypeDetails] | None = None
    totalActiveFindings: StrictInt | None = None
    totalArchivedFindings: StrictInt | None = None
    totalResolvedFindings: StrictInt | None = None
