from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_metric_attribute import PersonalizeMetricAttribute


class PersonalizeListMetricAttributionMetricsResponse(BaseModel):
    metrics: list[PersonalizeMetricAttribute] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
