from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_statistic_summary import GlueStatisticSummary


class GlueListDataQualityStatisticsResponse(BaseModel):
    Statistics: list[GlueStatisticSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
