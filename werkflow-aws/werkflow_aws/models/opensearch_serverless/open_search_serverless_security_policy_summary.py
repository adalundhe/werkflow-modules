from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchServerlessSecurityPolicySummary(BaseModel):
    type: StrictStr | None = None
    name: StrictStr | None = None
    policyVersion: StrictStr | None = None
    description: StrictStr | None = None
    createdDate: StrictInt | None = None
    lastModifiedDate: StrictInt | None = None
