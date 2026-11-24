from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateDBSubnetGroupRequest(BaseModel):
    DBSubnetGroupName: StrictStr
    DBSubnetGroupDescription: StrictStr
    SubnetIds: list[StrictStr]
    Tags: list[RDSTagModel] | None = None
