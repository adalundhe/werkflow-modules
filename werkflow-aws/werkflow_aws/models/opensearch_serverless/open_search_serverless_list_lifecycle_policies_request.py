from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchServerlessListLifecyclePoliciesRequest(BaseModel):
    type: Literal['retention']
    resources: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
