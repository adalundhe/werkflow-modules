from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateDBSecurityGroupRequest(BaseModel):
    DBSecurityGroupName: StrictStr
    DBSecurityGroupDescription: StrictStr
    Tags: list[RDSTagModel] | None = None
