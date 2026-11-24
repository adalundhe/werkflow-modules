from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_data_quality_results_v2_filter_criteria import GlueDataQualityResultsV2FilterCriteria


class GlueListDataQualityResultsV2Request(BaseModel):
    Filter: GlueDataQualityResultsV2FilterCriteria | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
