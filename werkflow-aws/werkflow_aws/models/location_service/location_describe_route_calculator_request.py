from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDescribeRouteCalculatorRequest(BaseModel):
    CalculatorName: StrictStr
