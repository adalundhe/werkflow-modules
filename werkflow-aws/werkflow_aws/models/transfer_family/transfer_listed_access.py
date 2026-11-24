from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferListedAccess(BaseModel):
    HomeDirectory: StrictStr | None = None
    HomeDirectoryType: StrictStr | None = None
    Role: StrictStr | None = None
    ExternalId: StrictStr | None = None
