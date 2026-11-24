from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsResourcePolicy(BaseModel):
    policyName: StrictStr | None = None
    policyDocument: StrictStr | None = None
    lastUpdatedTime: StrictInt | None = None
    policyScope: StrictStr | None = None
    resourceArn: StrictStr | None = None
    revisionId: StrictStr | None = None
