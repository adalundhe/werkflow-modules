from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class HealthImagingListDatastoresRequest(BaseModel):
    datastoreStatus: Literal['CREATING', 'CREATE_FAILED', 'ACTIVE', 'DELETING', 'DELETED'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
