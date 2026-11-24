from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DisassociateVpcCidrBlockRequest(BaseModel):
    AssociationId: StrictStr
