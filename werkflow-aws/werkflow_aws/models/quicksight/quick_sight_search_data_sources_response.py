from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_data_source_summary import QuickSightDataSourceSummary


class QuickSightSearchDataSourcesResponse(BaseModel):
    DataSourceSummaries: list[QuickSightDataSourceSummary] | None = None
    NextToken: StrictStr | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
