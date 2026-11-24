from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchListApplicationsRequest(BaseModel):
    nextToken: StrictStr | None = None
    statuses: list[Literal['CREATING', 'UPDATING', 'DELETING', 'ACTIVE', 'FAILED']] | None = None
    maxResults: StrictInt | None = None
