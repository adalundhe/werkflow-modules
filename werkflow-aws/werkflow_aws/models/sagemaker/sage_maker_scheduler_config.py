from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_priority_class import SageMakerPriorityClass


class SageMakerSchedulerConfig(BaseModel):
    PriorityClasses: list[SageMakerPriorityClass] | None = None
    FairShare: StrictStr | None = None
    IdleResourceSharing: StrictStr | None = None
