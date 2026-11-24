from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsListStateMachinesRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
