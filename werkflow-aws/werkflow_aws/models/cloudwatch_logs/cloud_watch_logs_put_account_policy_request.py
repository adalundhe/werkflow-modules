from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsPutAccountPolicyRequest(BaseModel):
    policyName: StrictStr
    policyDocument: StrictStr
    policyType: Literal['DATA_PROTECTION_POLICY', 'SUBSCRIPTION_FILTER_POLICY', 'FIELD_INDEX_POLICY', 'TRANSFORMER_POLICY', 'METRIC_EXTRACTION_POLICY', 'RETENTION_POLICY']
    scope: Literal['ALL'] | None = None
    selectionCriteria: StrictStr | None = None
    dryRun: StrictBool | None = None
