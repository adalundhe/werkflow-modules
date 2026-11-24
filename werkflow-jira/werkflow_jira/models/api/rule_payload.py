from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RulePayload(BaseModel):
    parameters: dict[StrictStr, StrictStr] | None = None
    ruleKey: StrictStr | None = None
