from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchGetMetricWidgetImageRequest(BaseModel):
    MetricWidget: StrictStr
    OutputFormat: StrictStr | None = None
