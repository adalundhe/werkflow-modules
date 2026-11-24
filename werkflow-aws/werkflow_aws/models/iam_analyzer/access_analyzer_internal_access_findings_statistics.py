from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .access_analyzer_internal_access_resource_type_details import AccessAnalyzerInternalAccessResourceTypeDetails


class AccessAnalyzerInternalAccessFindingsStatistics(BaseModel):
    resourceTypeStatistics: dict[StrictStr, AccessAnalyzerInternalAccessResourceTypeDetails] | None = None
    totalActiveFindings: StrictInt | None = None
    totalArchivedFindings: StrictInt | None = None
    totalResolvedFindings: StrictInt | None = None
