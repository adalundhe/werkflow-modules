from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr
    DBParameterGroupFamily: StrictStr
    Description: StrictStr
    Tags: list[RDSTagModel] | None = None
