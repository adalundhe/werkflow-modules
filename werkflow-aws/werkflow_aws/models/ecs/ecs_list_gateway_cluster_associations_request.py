from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECSListGatewayClusterAssociationsRequest(BaseModel):
    gateway: StrictStr | None = None
    cluster: StrictStr | None = None
    status: list[Literal['ACTIVE', 'DISASSOCIATING', 'INACTIVE']] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
