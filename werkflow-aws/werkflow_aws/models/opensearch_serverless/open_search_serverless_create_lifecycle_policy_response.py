from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_lifecycle_policy_detail import OpenSearchServerlessLifecyclePolicyDetail


class OpenSearchServerlessCreateLifecyclePolicyResponse(BaseModel):
    lifecyclePolicyDetail: OpenSearchServerlessLifecyclePolicyDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
