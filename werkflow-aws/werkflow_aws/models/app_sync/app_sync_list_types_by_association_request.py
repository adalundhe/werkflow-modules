from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncListTypesByAssociationRequest(BaseModel):
    mergedApiIdentifier: StrictStr
    associationId: StrictStr
    format: Literal['SDL', 'JSON']
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
