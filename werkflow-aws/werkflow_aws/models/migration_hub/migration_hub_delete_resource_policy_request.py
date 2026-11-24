from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubDeleteResourcePolicyRequest(BaseModel):
    Identifier: StrictStr
