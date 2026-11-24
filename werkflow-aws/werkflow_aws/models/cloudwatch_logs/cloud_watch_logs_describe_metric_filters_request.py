from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeMetricFiltersRequest(BaseModel):
    logGroupName: StrictStr | None = None
    filterNamePrefix: StrictStr | None = None
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
    metricName: StrictStr | None = None
    metricNamespace: StrictStr | None = None
