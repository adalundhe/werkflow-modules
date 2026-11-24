from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierVaultLockPolicy(BaseModel):
    Policy: StrictStr | None = None
