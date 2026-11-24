from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_error_result import ConnectErrorResult


class ConnectBatchDisassociateAnalyticsDataSetResponse(BaseModel):
    Deleted: list[StrictStr] | None = None
    Errors: list[ConnectErrorResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
