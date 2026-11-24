from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_phase import SageMakerPhase
from .sage_maker_stairs import SageMakerStairs


class SageMakerTrafficPattern(BaseModel):
    TrafficType: StrictStr | None = None
    Phases: list[SageMakerPhase] | None = None
    Stairs: SageMakerStairs | None = None
