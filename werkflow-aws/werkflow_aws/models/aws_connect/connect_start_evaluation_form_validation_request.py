from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectStartEvaluationFormValidationRequest(BaseModel):
    InstanceId: StrictStr
    EvaluationFormId: StrictStr
    EvaluationFormVersion: StrictInt
