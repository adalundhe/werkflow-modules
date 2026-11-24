from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_threat_intelligence_detail import GuardDutyThreatIntelligenceDetail


class GuardDutyEvidence(BaseModel):
    ThreatIntelligenceDetails: list[GuardDutyThreatIntelligenceDetail] | None = None
