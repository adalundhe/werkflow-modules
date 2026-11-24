from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteContactEvaluationRequest(BaseModel):
    InstanceId: StrictStr
    EvaluationId: StrictStr
