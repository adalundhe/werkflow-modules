from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessCreateAccessPolicyRequest(BaseModel):
    type: Literal['data']
    name: StrictStr
    policy: StrictStr
    description: StrictStr | None = None
    clientToken: StrictStr | None = None
