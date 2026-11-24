from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_data_quality_result_v2_item import GlueDataQualityResultV2Item


class GlueBatchGetDataQualityResultV2Response(BaseModel):
    Results: list[GlueDataQualityResultV2Item] | None = None
    ResultsNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
