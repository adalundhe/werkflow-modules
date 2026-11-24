from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessCreateLifecyclePolicyRequest(BaseModel):
    type: Literal['retention']
    name: StrictStr
    policy: StrictStr
    description: StrictStr | None = None
    clientToken: StrictStr | None = None
