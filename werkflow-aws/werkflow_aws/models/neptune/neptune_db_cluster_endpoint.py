from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDBClusterEndpoint(BaseModel):
    DBClusterEndpointIdentifier: StrictStr | None = None
    DBClusterIdentifier: StrictStr | None = None
    DBClusterEndpointResourceIdentifier: StrictStr | None = None
    Endpoint: StrictStr | None = None
    Status: StrictStr | None = None
    EndpointType: StrictStr | None = None
    CustomEndpointType: StrictStr | None = None
    StaticMembers: list[StrictStr] | None = None
    ExcludedMembers: list[StrictStr] | None = None
    DBClusterEndpointArn: StrictStr | None = None
