from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyIdentityIdFormatRequest(BaseModel):
    Resource: StrictStr
    UseLongIds: StrictBool
    PrincipalArn: StrictStr
