from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_data_quality_result_description import GlueDataQualityResultDescription


class GlueListDataQualityResultsResponse(BaseModel):
    Results: list[GlueDataQualityResultDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
