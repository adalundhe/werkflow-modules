from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_data_quality_evaluation_config_list_details import GlueDataQualityEvaluationConfigListDetails


class GlueListDataQualityEvaluationConfigsResponse(BaseModel):
    DataQualityEvaluationConfigs: list[GlueDataQualityEvaluationConfigListDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
