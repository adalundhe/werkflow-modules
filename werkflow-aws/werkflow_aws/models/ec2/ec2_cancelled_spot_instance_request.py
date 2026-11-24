from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CancelledSpotInstanceRequest(BaseModel):
    SpotInstanceRequestId: StrictStr | None = None
    State: StrictStr | None = None
