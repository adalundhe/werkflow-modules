from __future__ import annotations
from pydantic import BaseModel
from .macie_block_public_access import MacieBlockPublicAccess


class MacieAccountLevelPermissions(BaseModel):
    blockPublicAccess: MacieBlockPublicAccess | None = None
