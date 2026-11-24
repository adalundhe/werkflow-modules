from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MSKReplicatorFirehose(BaseModel):
    Enabled: StrictBool | None = None
    DeliveryStream: StrictStr | None = None
