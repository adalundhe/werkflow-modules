from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsIamRolePolicy(BaseModel):
    PolicyName: StrictStr | None = None
