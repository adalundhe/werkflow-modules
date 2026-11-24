from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEvaluationFormTargetConfiguration(BaseModel):
    ContactInteractionType: StrictStr | None = None
