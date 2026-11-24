from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_aggregation_type import IoTAggregationType


class IoTDescribeFleetMetricResponse(BaseModel):
    metricName: StrictStr | None = None
    queryString: StrictStr | None = None
    aggregationType: IoTAggregationType | None = None
    period: StrictInt | None = None
    aggregationField: StrictStr | None = None
    description: StrictStr | None = None
    queryVersion: StrictStr | None = None
    indexName: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    unit: StrictStr | None = None
    version: StrictInt | None = None
    metricArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
