from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessLifecyclePolicyIdentifier(BaseModel):
    type: Literal['retention']
    name: StrictStr
