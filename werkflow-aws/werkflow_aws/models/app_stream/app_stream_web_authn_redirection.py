from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppStreamWebAuthnRedirection(BaseModel):
    Enabled: StrictBool | None = None
    ProcessCompatibilityList: list[StrictStr] | None = None
