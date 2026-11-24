from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessDeleteSecurityPolicyRequest(BaseModel):
    type: Literal['encryption', 'network']
    name: StrictStr
    clientToken: StrictStr | None = None
