from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2HostProperties(BaseModel):
    Cores: StrictInt | None = None
    InstanceType: StrictStr | None = None
    InstanceFamily: StrictStr | None = None
    Sockets: StrictInt | None = None
    TotalVCpus: StrictInt | None = None
