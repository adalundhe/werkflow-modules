from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsUpdateCognitoGroupConfiguration(BaseModel):
    groupEntityType: StrictStr
