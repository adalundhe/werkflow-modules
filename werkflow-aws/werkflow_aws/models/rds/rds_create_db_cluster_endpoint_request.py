from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateDBClusterEndpointRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    DBClusterEndpointIdentifier: StrictStr
    EndpointType: StrictStr
    StaticMembers: list[StrictStr] | None = None
    ExcludedMembers: list[StrictStr] | None = None
    Tags: list[RDSTagModel] | None = None
