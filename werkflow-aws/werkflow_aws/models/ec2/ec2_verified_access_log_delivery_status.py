from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VerifiedAccessLogDeliveryStatus(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
