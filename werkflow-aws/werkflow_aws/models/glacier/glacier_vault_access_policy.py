from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierVaultAccessPolicy(BaseModel):
    Policy: StrictStr | None = None
