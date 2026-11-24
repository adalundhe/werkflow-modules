from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_data_quality_results_v2_description import GlueDataQualityResultsV2Description


class GlueListDataQualityResultsV2Response(BaseModel):
    Results: list[GlueDataQualityResultsV2Description] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
