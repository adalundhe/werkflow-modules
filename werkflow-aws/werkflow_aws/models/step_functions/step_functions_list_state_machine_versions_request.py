from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsListStateMachineVersionsRequest(BaseModel):
    stateMachineArn: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
