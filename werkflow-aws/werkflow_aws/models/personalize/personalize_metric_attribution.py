from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .personalize_metric_attribution_output import PersonalizeMetricAttributionOutput


class PersonalizeMetricAttribution(BaseModel):
    name: StrictStr | None = None
    metricAttributionArn: StrictStr | None = None
    datasetGroupArn: StrictStr | None = None
    metricsOutputConfig: PersonalizeMetricAttributionOutput | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    failureReason: StrictStr | None = None
