from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDetectionRuleEcsFargateRequirements(BaseModel):
    MinAgentVersion: StrictStr | None = None
