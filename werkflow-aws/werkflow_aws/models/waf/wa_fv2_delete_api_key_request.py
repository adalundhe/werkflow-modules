from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2DeleteAPIKeyRequest(BaseModel):
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    APIKey: StrictStr
