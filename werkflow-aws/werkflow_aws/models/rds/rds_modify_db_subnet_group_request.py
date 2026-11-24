from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSModifyDBSubnetGroupRequest(BaseModel):
    DBSubnetGroupName: StrictStr
    SubnetIds: list[StrictStr]
    DBSubnetGroupDescription: StrictStr | None = None
