from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_data_quality_ruleset_list_details import GlueDataQualityRulesetListDetails


class GlueListDataQualityRulesetsResponse(BaseModel):
    Rulesets: list[GlueDataQualityRulesetListDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
