from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_metric_data_error import SESMetricDataError
from .ses_metric_data_result import SESMetricDataResult


class SESBatchGetMetricDataResponse(BaseModel):
    Results: list[SESMetricDataResult] | None = None
    Errors: list[SESMetricDataError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
