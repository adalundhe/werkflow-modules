from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_manager_supportability_score import EC2CapacityManagerSupportabilityScore


class EC2GetCapacityManagerSupportabilityScoresResponse(BaseModel):
    AggregateScore: StrictStr | None = None
    CapacityManagerSupportabilityScores: list[EC2CapacityManagerSupportabilityScore] | None = None
    ResponseMetadata: dict[str, Any] | None = None
