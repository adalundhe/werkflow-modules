from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateUsageLimitRequest(BaseModel):
    ClusterIdentifier: StrictStr
    FeatureType: Literal['spectrum', 'concurrency-scaling', 'cross-region-datasharing', 'extra-compute-for-automatic-optimization']
    LimitType: Literal['time', 'data-scanned']
    Amount: StrictInt
    Period: Literal['daily', 'weekly', 'monthly'] | None = None
    BreachAction: Literal['log', 'emit-metric', 'disable'] | None = None
    Tags: list[RedshiftTag] | None = None
