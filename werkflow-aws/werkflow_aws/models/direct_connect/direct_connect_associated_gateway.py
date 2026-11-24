from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectAssociatedGateway(BaseModel):
    id: StrictStr | None = None
    type: StrictStr | None = None
    ownerAccount: StrictStr | None = None
    region: StrictStr | None = None
