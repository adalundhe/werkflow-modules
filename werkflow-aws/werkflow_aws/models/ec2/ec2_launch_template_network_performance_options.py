from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2LaunchTemplateNetworkPerformanceOptions(BaseModel):
    BandwidthWeighting: StrictStr | None = None
