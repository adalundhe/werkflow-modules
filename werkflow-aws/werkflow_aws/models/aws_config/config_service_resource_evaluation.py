from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceResourceEvaluation(BaseModel):
    ResourceEvaluationId: StrictStr | None = None
    EvaluationMode: StrictStr | None = None
    EvaluationStartTimestamp: datetime.datetime | StrictStr | None = None
