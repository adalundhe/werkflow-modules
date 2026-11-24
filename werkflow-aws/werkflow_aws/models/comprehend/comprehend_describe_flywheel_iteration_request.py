from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeFlywheelIterationRequest(BaseModel):
    FlywheelArn: StrictStr
    FlywheelIterationId: StrictStr
