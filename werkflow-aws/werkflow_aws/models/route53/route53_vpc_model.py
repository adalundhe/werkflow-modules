from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53VPCModel(BaseModel):
    VPCRegion: StrictStr | None = None
    VPCId: StrictStr | None = None
