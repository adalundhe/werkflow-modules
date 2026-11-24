from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectActivateEvaluationFormRequest(BaseModel):
    InstanceId: StrictStr
    EvaluationFormId: StrictStr
    EvaluationFormVersion: StrictInt
