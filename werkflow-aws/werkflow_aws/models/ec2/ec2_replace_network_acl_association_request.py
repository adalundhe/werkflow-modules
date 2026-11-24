from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ReplaceNetworkAclAssociationRequest(BaseModel):
    AssociationId: StrictStr
    NetworkAclId: StrictStr
    DryRun: StrictBool | None = None
