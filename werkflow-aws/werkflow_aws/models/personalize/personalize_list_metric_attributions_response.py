from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_metric_attribution_summary import PersonalizeMetricAttributionSummary


class PersonalizeListMetricAttributionsResponse(BaseModel):
    metricAttributions: list[PersonalizeMetricAttributionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
