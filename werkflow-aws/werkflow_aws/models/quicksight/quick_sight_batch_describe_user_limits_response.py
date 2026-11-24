from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .quick_sight_batch_describe_user_limits_error import QuickSightBatchDescribeUserLimitsError
from .quick_sight_user_limits import QuickSightUserLimits


class QuickSightBatchDescribeUserLimitsResponse(BaseModel):
    userLimits: list[QuickSightUserLimits] | None = None
    errors: list[QuickSightBatchDescribeUserLimitsError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
