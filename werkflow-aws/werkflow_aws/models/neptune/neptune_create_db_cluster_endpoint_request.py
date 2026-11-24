from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneCreateDBClusterEndpointRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    DBClusterEndpointIdentifier: StrictStr
    EndpointType: StrictStr
    StaticMembers: list[StrictStr] | None = None
    ExcludedMembers: list[StrictStr] | None = None
    Tags: list[NeptuneTag] | None = None
