from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class StepFunctionsGetExecutionHistoryRequest(BaseModel):
    executionArn: StrictStr
    maxResults: StrictInt | None = None
    reverseOrder: StrictBool | None = None
    nextToken: StrictStr | None = None
    includeExecutionData: StrictBool | None = None
