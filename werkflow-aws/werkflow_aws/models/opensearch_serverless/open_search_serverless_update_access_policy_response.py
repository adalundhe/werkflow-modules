from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_access_policy_detail import OpenSearchServerlessAccessPolicyDetail


class OpenSearchServerlessUpdateAccessPolicyResponse(BaseModel):
    accessPolicyDetail: OpenSearchServerlessAccessPolicyDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
