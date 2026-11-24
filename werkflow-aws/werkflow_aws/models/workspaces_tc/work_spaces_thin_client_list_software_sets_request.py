from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesThinClientListSoftwareSetsRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
