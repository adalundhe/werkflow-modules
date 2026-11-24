from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeUsageLimitsRequest(BaseModel):
    UsageLimitId: StrictStr | None = None
    ClusterIdentifier: StrictStr | None = None
    FeatureType: Literal['spectrum', 'concurrency-scaling', 'cross-region-datasharing', 'extra-compute-for-automatic-optimization'] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    TagKeys: list[StrictStr] | None = None
    TagValues: list[StrictStr] | None = None
