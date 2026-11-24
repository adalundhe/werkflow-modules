from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .detective_investigation_detail import DetectiveInvestigationDetail


class DetectiveListInvestigationsResponse(BaseModel):
    InvestigationDetails: list[DetectiveInvestigationDetail] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
