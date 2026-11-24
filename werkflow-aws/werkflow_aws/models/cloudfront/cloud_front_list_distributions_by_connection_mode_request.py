from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontListDistributionsByConnectionModeRequest(BaseModel):
    ConnectionMode: Literal['direct', 'tenant-only']
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
