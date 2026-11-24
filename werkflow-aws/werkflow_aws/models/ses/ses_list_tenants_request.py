from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SESListTenantsRequest(BaseModel):
    Filter: dict[Literal['TENANT_NAME_CONTAINS', 'SENDING_STATUS'], StrictStr] | None = None
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
