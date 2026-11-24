from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SESListTenantResourcesRequest(BaseModel):
    TenantName: StrictStr
    Filter: dict[Literal['RESOURCE_TYPE'], StrictStr] | None = None
    PageSize: StrictInt | None = None
    NextToken: StrictStr | None = None
