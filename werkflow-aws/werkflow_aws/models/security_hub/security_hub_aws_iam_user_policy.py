from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsIamUserPolicy(BaseModel):
    PolicyName: StrictStr | None = None
