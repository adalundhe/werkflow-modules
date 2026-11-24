from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LocationDescribeRouteCalculatorResponse(BaseModel):
    CalculatorName: StrictStr | None = None
    CalculatorArn: StrictStr | None = None
    PricingPlan: StrictStr | None = None
    Description: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    DataSource: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
