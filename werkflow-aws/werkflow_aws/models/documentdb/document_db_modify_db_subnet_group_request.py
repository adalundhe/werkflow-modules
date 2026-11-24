from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBModifyDBSubnetGroupRequest(BaseModel):
    DBSubnetGroupName: StrictStr
    SubnetIds: list[StrictStr]
    DBSubnetGroupDescription: StrictStr | None = None
