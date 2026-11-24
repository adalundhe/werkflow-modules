from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_data_quality_target_table import GlueDataQualityTargetTable


class GlueCreateDataQualityRulesetRequest(BaseModel):
    Name: StrictStr
    Ruleset: StrictStr
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    TargetTable: GlueDataQualityTargetTable | None = None
    DataQualitySecurityConfiguration: StrictStr | None = None
    ClientToken: StrictStr | None = None
