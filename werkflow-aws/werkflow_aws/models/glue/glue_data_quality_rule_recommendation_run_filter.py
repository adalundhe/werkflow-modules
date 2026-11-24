from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_data_source import GlueDataSource


class GlueDataQualityRuleRecommendationRunFilter(BaseModel):
    DataSource: GlueDataSource
    StartedBefore: datetime.datetime | StrictStr | None = None
    StartedAfter: datetime.datetime | StrictStr | None = None
