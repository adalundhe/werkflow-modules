from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectGlobalResiliencyMetadata(BaseModel):
    ActiveRegion: StrictStr | None = None
    OriginRegion: StrictStr | None = None
    TrafficDistributionGroupId: StrictStr | None = None
