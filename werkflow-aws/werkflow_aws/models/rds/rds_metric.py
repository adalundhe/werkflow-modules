from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_metric_query import RDSMetricQuery
from .rds_metric_reference import RDSMetricReference


class RDSMetric(BaseModel):
    Name: StrictStr | None = None
    References: list[RDSMetricReference] | None = None
    StatisticsDetails: StrictStr | None = None
    MetricQuery: RDSMetricQuery | None = None
