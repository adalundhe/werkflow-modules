from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_assessment_finding import MSKAssessmentFinding


class MSKListAssessmentFindingsResponse(BaseModel):
    Findings: list[MSKAssessmentFinding] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
