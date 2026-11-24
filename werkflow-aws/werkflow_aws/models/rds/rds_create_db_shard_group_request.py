from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateDBShardGroupRequest(BaseModel):
    DBShardGroupIdentifier: StrictStr
    DBClusterIdentifier: StrictStr
    MaxACU: StrictFloat | StrictInt
    ComputeRedundancy: StrictInt | None = None
    MinACU: StrictFloat | StrictInt | None = None
    PubliclyAccessible: StrictBool | None = None
    Tags: list[RDSTagModel] | None = None
