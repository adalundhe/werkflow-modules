from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .detective_indicator import DetectiveIndicator


class DetectiveListIndicatorsResponse(BaseModel):
    GraphArn: StrictStr | None = None
    InvestigationId: StrictStr | None = None
    NextToken: StrictStr | None = None
    Indicators: list[DetectiveIndicator] | None = None
    ResponseMetadata: dict[str, Any] | None = None
