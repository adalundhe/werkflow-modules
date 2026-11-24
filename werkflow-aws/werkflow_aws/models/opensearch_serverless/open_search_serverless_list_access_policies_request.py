from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchServerlessListAccessPoliciesRequest(BaseModel):
    type: Literal['data']
    resource: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
