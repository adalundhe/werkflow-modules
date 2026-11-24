from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AthenaIdentityCenterConfiguration(BaseModel):
    EnableIdentityCenter: StrictBool | None = None
    IdentityCenterInstanceArn: StrictStr | None = None
