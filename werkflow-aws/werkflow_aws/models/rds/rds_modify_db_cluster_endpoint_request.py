from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSModifyDBClusterEndpointRequest(BaseModel):
    DBClusterEndpointIdentifier: StrictStr
    EndpointType: StrictStr | None = None
    StaticMembers: list[StrictStr] | None = None
    ExcludedMembers: list[StrictStr] | None = None
