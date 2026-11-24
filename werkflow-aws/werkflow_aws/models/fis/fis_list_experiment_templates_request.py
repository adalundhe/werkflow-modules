from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FISListExperimentTemplatesRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
