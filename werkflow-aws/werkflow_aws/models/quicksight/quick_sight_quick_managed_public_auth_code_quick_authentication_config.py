from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightQuickManagedPublicAuthCodeQuickAuthenticationConfig(BaseModel):
    RedirectUris: list[StrictStr] | None = None
    ClientId: StrictStr | None = None
