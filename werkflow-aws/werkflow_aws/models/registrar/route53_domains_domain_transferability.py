from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsDomainTransferability(BaseModel):
    Transferable: StrictStr | None = None
