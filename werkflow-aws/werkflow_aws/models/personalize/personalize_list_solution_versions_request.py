from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PersonalizeListSolutionVersionsRequest(BaseModel):
    solutionArn: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
