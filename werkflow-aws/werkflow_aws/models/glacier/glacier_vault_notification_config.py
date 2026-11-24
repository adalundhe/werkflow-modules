from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierVaultNotificationConfig(BaseModel):
    SNSTopic: StrictStr | None = None
    Events: list[StrictStr] | None = None
