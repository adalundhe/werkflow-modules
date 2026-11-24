from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_hours_of_operation import ConnectHoursOfOperation


class ConnectSearchHoursOfOperationsResponse(BaseModel):
    HoursOfOperations: list[ConnectHoursOfOperation] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
