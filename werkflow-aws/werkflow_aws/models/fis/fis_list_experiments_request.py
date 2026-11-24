from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FISListExperimentsRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    experimentTemplateId: StrictStr | None = None
