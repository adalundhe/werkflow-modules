from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_metric_attribution import PersonalizeMetricAttribution


class PersonalizeDescribeMetricAttributionResponse(BaseModel):
    metricAttribution: PersonalizeMetricAttribution | None = None
    ResponseMetadata: dict[str, Any] | None = None
