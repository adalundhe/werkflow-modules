from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteResourcePolicyRequest(BaseModel):
    policyName: StrictStr | None = None
    resourceArn: StrictStr | None = None
    expectedRevisionId: StrictStr | None = None
