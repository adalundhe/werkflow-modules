from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_lifecycle_policy_detail import OpenSearchServerlessLifecyclePolicyDetail
from .open_search_serverless_lifecycle_policy_error_detail import OpenSearchServerlessLifecyclePolicyErrorDetail


class OpenSearchServerlessBatchGetLifecyclePolicyResponse(BaseModel):
    lifecyclePolicyDetails: list[OpenSearchServerlessLifecyclePolicyDetail] | None = None
    lifecyclePolicyErrorDetails: list[OpenSearchServerlessLifecyclePolicyErrorDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
