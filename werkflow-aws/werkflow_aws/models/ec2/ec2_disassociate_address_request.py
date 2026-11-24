from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisassociateAddressRequest(BaseModel):
    AssociationId: StrictStr | None = None
    PublicIp: StrictStr | None = None
    DryRun: StrictBool | None = None
