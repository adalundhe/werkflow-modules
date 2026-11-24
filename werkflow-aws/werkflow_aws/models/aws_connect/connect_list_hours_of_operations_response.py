from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_hours_of_operation_summary import ConnectHoursOfOperationSummary


class ConnectListHoursOfOperationsResponse(BaseModel):
    HoursOfOperationSummaryList: list[ConnectHoursOfOperationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
