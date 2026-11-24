from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CloudWatchLogsMetricTransformation(BaseModel):
    metricName: StrictStr | None = None
    metricNamespace: StrictStr | None = None
    metricValue: StrictStr | None = None
    defaultValue: StrictFloat | StrictInt | None = None
    dimensions: dict[StrictStr, StrictStr] | None = None
    unit: StrictStr | None = None
