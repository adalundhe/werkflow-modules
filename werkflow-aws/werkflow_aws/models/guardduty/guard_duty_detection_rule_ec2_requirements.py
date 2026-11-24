from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDetectionRuleEc2Requirements(BaseModel):
    MinAgentVersion: StrictStr | None = None
