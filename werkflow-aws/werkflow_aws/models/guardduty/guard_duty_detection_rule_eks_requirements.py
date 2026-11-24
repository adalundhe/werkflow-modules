from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDetectionRuleEksRequirements(BaseModel):
    MinAgentVersion: StrictStr | None = None
