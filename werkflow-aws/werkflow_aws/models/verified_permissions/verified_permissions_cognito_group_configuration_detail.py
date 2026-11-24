from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsCognitoGroupConfigurationDetail(BaseModel):
    groupEntityType: StrictStr | None = None
