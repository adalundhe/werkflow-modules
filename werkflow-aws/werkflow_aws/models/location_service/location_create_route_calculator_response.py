from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LocationCreateRouteCalculatorResponse(BaseModel):
    CalculatorName: StrictStr | None = None
    CalculatorArn: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
