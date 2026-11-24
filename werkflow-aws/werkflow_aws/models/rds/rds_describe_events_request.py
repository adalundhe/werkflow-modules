from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeEventsRequest(BaseModel):
    SourceIdentifier: StrictStr | None = None
    SourceType: Literal['db-instance', 'db-parameter-group', 'db-security-group', 'db-snapshot', 'db-cluster', 'db-cluster-snapshot', 'custom-engine-version', 'db-proxy', 'blue-green-deployment', 'db-shard-group', 'zero-etl'] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    EventCategories: list[StrictStr] | None = None
    Filters: list[RDSFilterModel] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
