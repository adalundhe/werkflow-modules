from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2RulePriorityPair(BaseModel):
    RuleArn: StrictStr | None = None
    Priority: StrictInt | None = None
