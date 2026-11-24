from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneCreateDBSubnetGroupRequest(BaseModel):
    DBSubnetGroupName: StrictStr
    DBSubnetGroupDescription: StrictStr
    SubnetIds: list[StrictStr]
    Tags: list[NeptuneTag] | None = None
