from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_timestamp_filter import GlueTimestampFilter


class GlueListDataQualityStatisticsRequest(BaseModel):
    StatisticId: StrictStr | None = None
    ProfileId: StrictStr | None = None
    TimestampFilter: GlueTimestampFilter | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
