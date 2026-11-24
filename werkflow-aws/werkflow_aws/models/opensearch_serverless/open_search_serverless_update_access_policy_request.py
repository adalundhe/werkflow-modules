from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessUpdateAccessPolicyRequest(BaseModel):
    type: Literal['data']
    name: StrictStr
    policyVersion: StrictStr
    description: StrictStr | None = None
    policy: StrictStr | None = None
    clientToken: StrictStr | None = None
