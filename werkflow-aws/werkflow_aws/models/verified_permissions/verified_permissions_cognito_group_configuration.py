from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsCognitoGroupConfiguration(BaseModel):
    groupEntityType: StrictStr
