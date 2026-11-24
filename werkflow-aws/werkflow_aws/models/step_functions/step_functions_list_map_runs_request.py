from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsListMapRunsRequest(BaseModel):
    executionArn: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
