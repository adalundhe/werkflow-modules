from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_analytics_data_sets_result import ConnectAnalyticsDataSetsResult


class ConnectListAnalyticsDataLakeDataSetsResponse(BaseModel):
    Results: list[ConnectAnalyticsDataSetsResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
