from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessDeleteLifecyclePolicyRequest(BaseModel):
    type: Literal['retention']
    name: StrictStr
    clientToken: StrictStr | None = None
