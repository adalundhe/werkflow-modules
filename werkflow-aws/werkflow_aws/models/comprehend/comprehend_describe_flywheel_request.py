from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeFlywheelRequest(BaseModel):
    FlywheelArn: StrictStr
