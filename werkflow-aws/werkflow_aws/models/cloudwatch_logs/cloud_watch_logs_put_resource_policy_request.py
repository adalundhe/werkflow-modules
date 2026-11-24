from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsPutResourcePolicyRequest(BaseModel):
    policyName: StrictStr | None = None
    policyDocument: StrictStr | None = None
    resourceArn: StrictStr | None = None
    expectedRevisionId: StrictStr | None = None
