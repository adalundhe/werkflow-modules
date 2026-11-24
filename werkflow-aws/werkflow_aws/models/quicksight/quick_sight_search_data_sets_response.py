from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_data_set_summary import QuickSightDataSetSummary


class QuickSightSearchDataSetsResponse(BaseModel):
    DataSetSummaries: list[QuickSightDataSetSummary] | None = None
    NextToken: StrictStr | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
