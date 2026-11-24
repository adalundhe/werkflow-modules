from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectAssociatedCoreNetwork(BaseModel):
    id: StrictStr | None = None
    ownerAccount: StrictStr | None = None
    attachmentId: StrictStr | None = None
