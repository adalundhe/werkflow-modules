from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineListRuleTypesRequest(BaseModel):
    ruleOwnerFilter: Literal['AWS'] | None = None
    regionFilter: StrictStr | None = None
