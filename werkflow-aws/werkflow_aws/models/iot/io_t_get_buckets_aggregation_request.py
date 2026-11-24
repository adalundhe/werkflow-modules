from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_buckets_aggregation_type import IoTBucketsAggregationType


class IoTGetBucketsAggregationRequest(BaseModel):
    queryString: StrictStr
    aggregationField: StrictStr
    bucketsAggregationType: IoTBucketsAggregationType
    indexName: StrictStr | None = None
    queryVersion: StrictStr | None = None
