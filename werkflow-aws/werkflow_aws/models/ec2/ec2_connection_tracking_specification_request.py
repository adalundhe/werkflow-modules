from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2ConnectionTrackingSpecificationRequest(BaseModel):
    TcpEstablishedTimeout: StrictInt | None = None
    UdpStreamTimeout: StrictInt | None = None
    UdpTimeout: StrictInt | None = None
