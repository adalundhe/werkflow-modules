from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DisassociateSubnetCidrBlockRequest(BaseModel):
    AssociationId: StrictStr
