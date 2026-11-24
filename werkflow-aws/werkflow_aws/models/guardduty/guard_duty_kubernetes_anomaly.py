from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyKubernetesAnomaly(BaseModel):
    UnusualBehavior: StrictStr | None = None
    BaselineContext: StrictStr | None = None
    AnomalyScore: StrictStr | None = None
    TrainingPeriod: StrictStr | None = None
