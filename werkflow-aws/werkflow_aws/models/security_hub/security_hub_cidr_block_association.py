from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubCidrBlockAssociation(BaseModel):
    AssociationId: StrictStr | None = None
    CidrBlock: StrictStr | None = None
    CidrBlockState: StrictStr | None = None
