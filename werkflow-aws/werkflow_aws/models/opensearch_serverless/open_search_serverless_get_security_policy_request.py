from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessGetSecurityPolicyRequest(BaseModel):
    type: Literal['encryption', 'network']
    name: StrictStr
