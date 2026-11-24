from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncListTypesRequest(BaseModel):
    apiId: StrictStr
    format: Literal['SDL', 'JSON']
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
