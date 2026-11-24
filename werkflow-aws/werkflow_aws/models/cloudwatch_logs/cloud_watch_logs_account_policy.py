from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsAccountPolicy(BaseModel):
    policyName: StrictStr | None = None
    policyDocument: StrictStr | None = None
    lastUpdatedTime: StrictInt | None = None
    policyType: StrictStr | None = None
    scope: StrictStr | None = None
    selectionCriteria: StrictStr | None = None
    accountId: StrictStr | None = None
