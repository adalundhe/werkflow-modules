from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubPutResourcePolicyRequest(BaseModel):
    Policy: StrictStr
    ResourceArn: StrictStr
