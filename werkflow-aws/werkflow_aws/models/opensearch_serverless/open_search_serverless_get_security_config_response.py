from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_security_config_detail import OpenSearchServerlessSecurityConfigDetail


class OpenSearchServerlessGetSecurityConfigResponse(BaseModel):
    securityConfigDetail: OpenSearchServerlessSecurityConfigDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
