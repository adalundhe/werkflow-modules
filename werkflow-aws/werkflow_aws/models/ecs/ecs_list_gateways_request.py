from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECSListGatewaysRequest(BaseModel):
    names: list[StrictStr] | None = None
    status: list[Literal['ACTIVE', 'UPDATE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'DELETED']] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
