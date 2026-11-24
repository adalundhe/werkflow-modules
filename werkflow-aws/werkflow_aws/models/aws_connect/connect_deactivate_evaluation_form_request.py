from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectDeactivateEvaluationFormRequest(BaseModel):
    InstanceId: StrictStr
    EvaluationFormId: StrictStr
    EvaluationFormVersion: StrictInt
