from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectDeleteEvaluationFormRequest(BaseModel):
    InstanceId: StrictStr
    EvaluationFormId: StrictStr
    EvaluationFormVersion: StrictInt | None = None
