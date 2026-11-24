from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessLifecyclePolicyResourceIdentifier(BaseModel):
    type: Literal['retention']
    resource: StrictStr
