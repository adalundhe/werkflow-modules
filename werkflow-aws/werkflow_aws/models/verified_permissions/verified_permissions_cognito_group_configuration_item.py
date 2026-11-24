from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsCognitoGroupConfigurationItem(BaseModel):
    groupEntityType: StrictStr | None = None
