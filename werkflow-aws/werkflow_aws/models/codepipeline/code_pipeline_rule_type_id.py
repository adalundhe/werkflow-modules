from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineRuleTypeId(BaseModel):
    category: StrictStr | None = None
    owner: StrictStr | None = None
    provider: StrictStr | None = None
    version: StrictStr | None = None
