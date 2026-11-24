from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchServerlessEffectiveLifecyclePolicyDetail(BaseModel):
    type: StrictStr | None = None
    resource: StrictStr | None = None
    policyName: StrictStr | None = None
    resourceType: StrictStr | None = None
    retentionPeriod: StrictStr | None = None
    noMinRetentionPeriod: StrictBool | None = None
