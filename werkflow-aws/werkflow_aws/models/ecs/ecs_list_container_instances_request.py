from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECSListContainerInstancesRequest(BaseModel):
    cluster: StrictStr | None = None
    filter: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    status: Literal['ACTIVE', 'DRAINING', 'REGISTERING', 'DEREGISTERING', 'REGISTRATION_FAILED'] | None = None
