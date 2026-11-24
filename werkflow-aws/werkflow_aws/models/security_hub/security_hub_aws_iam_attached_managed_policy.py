from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsIamAttachedManagedPolicy(BaseModel):
    PolicyName: StrictStr | None = None
    PolicyArn: StrictStr | None = None
