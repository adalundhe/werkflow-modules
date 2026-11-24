from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2CreateAPIKeyRequest(BaseModel):
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    TokenDomains: list[StrictStr]
