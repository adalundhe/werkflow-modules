from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectListContactEvaluationsRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    NextToken: StrictStr | None = None
