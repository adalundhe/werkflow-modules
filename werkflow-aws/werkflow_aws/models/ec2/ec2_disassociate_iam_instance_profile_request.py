from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DisassociateIamInstanceProfileRequest(BaseModel):
    AssociationId: StrictStr
