from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2EventInformation(BaseModel):
    EventDescription: StrictStr | None = None
    EventSubType: StrictStr | None = None
    InstanceId: StrictStr | None = None
