from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsIamGroupPolicy(BaseModel):
    PolicyName: StrictStr | None = None
