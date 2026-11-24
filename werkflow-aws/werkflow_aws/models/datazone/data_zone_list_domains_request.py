from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListDomainsRequest(BaseModel):
    status: Literal['CREATING', 'AVAILABLE', 'CREATION_FAILED', 'DELETING', 'DELETED', 'DELETION_FAILED'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
