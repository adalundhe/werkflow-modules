from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeContactEvaluationRequest(BaseModel):
    InstanceId: StrictStr
    EvaluationId: StrictStr
