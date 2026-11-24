from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchManagedRuleState(BaseModel):
    RuleName: StrictStr | None = None
    State: StrictStr | None = None
