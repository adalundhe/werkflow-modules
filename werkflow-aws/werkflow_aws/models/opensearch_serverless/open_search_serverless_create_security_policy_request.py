from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessCreateSecurityPolicyRequest(BaseModel):
    type: Literal['encryption', 'network']
    name: StrictStr
    policy: StrictStr
    description: StrictStr | None = None
    clientToken: StrictStr | None = None
