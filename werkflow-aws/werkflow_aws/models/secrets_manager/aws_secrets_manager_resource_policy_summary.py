from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerResourcePolicySummary(BaseModel):
    PolicyName: StrictStr | None = None
