from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectDescribeEvaluationFormRequest(BaseModel):
    InstanceId: StrictStr
    EvaluationFormId: StrictStr
    EvaluationFormVersion: StrictInt | None = None
