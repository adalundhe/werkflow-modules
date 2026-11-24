from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_flywheel_summary import ComprehendFlywheelSummary


class ComprehendListFlywheelsResponse(BaseModel):
    FlywheelSummaryList: list[ComprehendFlywheelSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
