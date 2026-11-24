from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_data_quality_result_filter_criteria import GlueDataQualityResultFilterCriteria


class GlueListDataQualityResultsRequest(BaseModel):
    Filter: GlueDataQualityResultFilterCriteria | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
