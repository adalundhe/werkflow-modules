from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_data_quality_result import GlueDataQualityResult


class GlueBatchGetDataQualityResultResponse(BaseModel):
    Results: list[GlueDataQualityResult] | None = None
    ResultsNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
