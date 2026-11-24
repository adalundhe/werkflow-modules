from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2ProvisionedBandwidth(BaseModel):
    ProvisionTime: datetime.datetime | StrictStr | None = None
    Provisioned: StrictStr | None = None
    RequestTime: datetime.datetime | StrictStr | None = None
    Requested: StrictStr | None = None
    Status: StrictStr | None = None
