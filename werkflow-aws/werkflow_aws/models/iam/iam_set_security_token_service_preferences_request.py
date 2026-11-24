from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class IAMSetSecurityTokenServicePreferencesRequest(BaseModel):
    GlobalEndpointTokenVersion: Literal['v1Token', 'v2Token']
