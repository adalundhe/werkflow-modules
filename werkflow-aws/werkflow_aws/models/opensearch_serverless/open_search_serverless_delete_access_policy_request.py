from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessDeleteAccessPolicyRequest(BaseModel):
    type: Literal['data']
    name: StrictStr
    clientToken: StrictStr | None = None
