from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListEvaluationFormVersionsRequest(BaseModel):
    InstanceId: StrictStr
    EvaluationFormId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
