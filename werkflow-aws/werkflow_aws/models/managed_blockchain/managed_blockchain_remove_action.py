from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainRemoveAction(BaseModel):
    MemberId: StrictStr | None = None
