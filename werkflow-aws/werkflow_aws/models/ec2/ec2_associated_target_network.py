from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AssociatedTargetNetwork(BaseModel):
    NetworkId: StrictStr | None = None
    NetworkType: StrictStr | None = None
