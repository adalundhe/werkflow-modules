from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_security_policy_detail import OpenSearchServerlessSecurityPolicyDetail


class OpenSearchServerlessCreateSecurityPolicyResponse(BaseModel):
    securityPolicyDetail: OpenSearchServerlessSecurityPolicyDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
