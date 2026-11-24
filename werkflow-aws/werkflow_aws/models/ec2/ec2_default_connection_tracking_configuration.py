from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2DefaultConnectionTrackingConfiguration(BaseModel):
    DefaultTcpEstablishedTimeout: StrictInt | None = None
    DefaultUdpTimeout: StrictInt | None = None
    DefaultUdpStreamTimeout: StrictInt | None = None
