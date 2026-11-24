from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_data_set_refresh_properties import QuickSightDataSetRefreshProperties


class QuickSightDescribeDataSetRefreshPropertiesResponse(BaseModel):
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    DataSetRefreshProperties: QuickSightDataSetRefreshProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
