from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisassociateRouteTableRequest(BaseModel):
    AssociationId: StrictStr
    DryRun: StrictBool | None = None
