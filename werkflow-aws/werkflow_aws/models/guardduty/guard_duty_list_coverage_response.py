from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_coverage_resource import GuardDutyCoverageResource


class GuardDutyListCoverageResponse(BaseModel):
    Resources: list[GuardDutyCoverageResource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
