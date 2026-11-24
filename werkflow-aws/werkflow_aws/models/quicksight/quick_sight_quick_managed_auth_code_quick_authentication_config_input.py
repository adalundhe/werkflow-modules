from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightQuickManagedAuthCodeQuickAuthenticationConfigInput(BaseModel):
    RedirectUris: list[StrictStr]
