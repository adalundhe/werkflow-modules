from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2ConnectionTrackingSpecification(BaseModel):
    TcpEstablishedTimeout: StrictInt | None = None
    UdpTimeout: StrictInt | None = None
    UdpStreamTimeout: StrictInt | None = None
