from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class MSKAssessmentSummary(BaseModel):
    ByCategory: dict[StrictStr, StrictInt] | None = None
    BySeverity: dict[StrictStr, StrictInt] | None = None
    FindingsCapped: StrictBool | None = None
    HasBlockingFindings: StrictBool | None = None
    TotalFindings: StrictInt | None = None
