from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_analytics_data_association_result import ConnectAnalyticsDataAssociationResult
from .connect_error_result import ConnectErrorResult


class ConnectBatchAssociateAnalyticsDataSetResponse(BaseModel):
    Created: list[ConnectAnalyticsDataAssociationResult] | None = None
    Errors: list[ConnectErrorResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
