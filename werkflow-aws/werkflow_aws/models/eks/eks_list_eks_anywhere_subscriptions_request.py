from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EKSListEksAnywhereSubscriptionsRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    includeStatus: list[Literal['CREATING', 'ACTIVE', 'UPDATING', 'EXPIRING', 'EXPIRED', 'DELETING']] | None = None
