from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_flywheel_iteration_properties import ComprehendFlywheelIterationProperties


class ComprehendListFlywheelIterationHistoryResponse(BaseModel):
    FlywheelIterationPropertiesList: list[ComprehendFlywheelIterationProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
