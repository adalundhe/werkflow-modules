from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTDescribeCustomMetricResponse(BaseModel):
    metricName: StrictStr | None = None
    metricArn: StrictStr | None = None
    metricType: StrictStr | None = None
    displayName: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
