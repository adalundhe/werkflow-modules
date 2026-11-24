from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .personalize_metric_attribute import PersonalizeMetricAttribute
from .personalize_metric_attribution_output import PersonalizeMetricAttributionOutput


class PersonalizeUpdateMetricAttributionRequest(BaseModel):
    addMetrics: list[PersonalizeMetricAttribute] | None = None
    removeMetrics: list[StrictStr] | None = None
    metricsOutputConfig: PersonalizeMetricAttributionOutput | None = None
    metricAttributionArn: StrictStr | None = None
