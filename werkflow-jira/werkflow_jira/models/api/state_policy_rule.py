from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StatePolicyRule(BaseModel):
    description: StrictStr | None = None
    domain: StrictStr | None = None
    properties: dict[StrictStr, Any] | None = None
    ruleId: StrictStr | None = None
    ruleTypeId: StrictStr | None = None
