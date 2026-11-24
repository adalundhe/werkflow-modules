from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECSListGatewayRoutesRequest(BaseModel):
    gateway: StrictStr | None = None
    cluster: StrictStr | None = None
    service: StrictStr | None = None
    serviceContainerPortName: StrictStr | None = None
    status: list[Literal['ACTIVE', 'CREATE_IN_PROGRESS', 'CREATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_FAILED']] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
