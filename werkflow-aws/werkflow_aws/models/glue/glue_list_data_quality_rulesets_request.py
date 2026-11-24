from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_data_quality_ruleset_filter_criteria import GlueDataQualityRulesetFilterCriteria


class GlueListDataQualityRulesetsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filter: GlueDataQualityRulesetFilterCriteria | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
