from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .personalize_metric_attribute import PersonalizeMetricAttribute
from .personalize_metric_attribution_output import PersonalizeMetricAttributionOutput


class PersonalizeCreateMetricAttributionRequest(BaseModel):
    name: StrictStr
    datasetGroupArn: StrictStr
    metrics: list[PersonalizeMetricAttribute]
    metricsOutputConfig: PersonalizeMetricAttributionOutput
