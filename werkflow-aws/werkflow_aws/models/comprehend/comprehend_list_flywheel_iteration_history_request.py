from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_flywheel_iteration_filter import ComprehendFlywheelIterationFilter


class ComprehendListFlywheelIterationHistoryRequest(BaseModel):
    FlywheelArn: StrictStr
    Filter: ComprehendFlywheelIterationFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
