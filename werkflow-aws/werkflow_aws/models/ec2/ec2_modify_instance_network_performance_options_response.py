from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2ModifyInstanceNetworkPerformanceOptionsResponse(BaseModel):
    InstanceId: StrictStr | None = None
    BandwidthWeighting: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
