from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsListActivitiesRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
