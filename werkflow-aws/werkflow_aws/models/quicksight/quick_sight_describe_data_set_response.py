from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_data_set import QuickSightDataSet


class QuickSightDescribeDataSetResponse(BaseModel):
    DataSet: QuickSightDataSet | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
