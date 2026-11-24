from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeDBRecommendationsRequest(BaseModel):
    LastUpdatedAfter: datetime.datetime | StrictStr | None = None
    LastUpdatedBefore: datetime.datetime | StrictStr | None = None
    Locale: StrictStr | None = None
    Filters: list[RDSFilterModel] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
