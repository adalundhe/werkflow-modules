from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDescribeAccountPoliciesRequest(BaseModel):
    policyType: Literal['DATA_PROTECTION_POLICY', 'SUBSCRIPTION_FILTER_POLICY', 'FIELD_INDEX_POLICY', 'TRANSFORMER_POLICY', 'METRIC_EXTRACTION_POLICY', 'RETENTION_POLICY']
    policyName: StrictStr | None = None
    accountIdentifiers: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
