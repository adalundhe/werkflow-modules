from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubBooleanFilter(BaseModel):
    Value: StrictBool | None = None
