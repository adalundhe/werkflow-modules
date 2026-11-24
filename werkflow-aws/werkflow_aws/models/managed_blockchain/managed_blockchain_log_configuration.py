from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ManagedBlockchainLogConfiguration(BaseModel):
    Enabled: StrictBool | None = None
