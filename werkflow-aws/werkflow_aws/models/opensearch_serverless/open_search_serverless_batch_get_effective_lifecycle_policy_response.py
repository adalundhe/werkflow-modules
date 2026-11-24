from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_effective_lifecycle_policy_detail import OpenSearchServerlessEffectiveLifecyclePolicyDetail
from .open_search_serverless_effective_lifecycle_policy_error_detail import OpenSearchServerlessEffectiveLifecyclePolicyErrorDetail


class OpenSearchServerlessBatchGetEffectiveLifecyclePolicyResponse(BaseModel):
    effectiveLifecyclePolicyDetails: list[OpenSearchServerlessEffectiveLifecyclePolicyDetail] | None = None
    effectiveLifecyclePolicyErrorDetails: list[OpenSearchServerlessEffectiveLifecyclePolicyErrorDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
