from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_analytics_data_association_result import ConnectAnalyticsDataAssociationResult


class ConnectListAnalyticsDataAssociationsResponse(BaseModel):
    Results: list[ConnectAnalyticsDataAssociationResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
