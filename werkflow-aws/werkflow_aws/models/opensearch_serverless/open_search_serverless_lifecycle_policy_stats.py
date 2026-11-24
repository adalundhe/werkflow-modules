from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchServerlessLifecyclePolicyStats(BaseModel):
    RetentionPolicyCount: StrictInt | None = None
