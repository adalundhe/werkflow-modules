from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateDBParameterGroupRequest(BaseModel):
    DBParameterGroupName: StrictStr
    DBParameterGroupFamily: StrictStr
    Description: StrictStr
    Tags: list[RDSTagModel] | None = None
