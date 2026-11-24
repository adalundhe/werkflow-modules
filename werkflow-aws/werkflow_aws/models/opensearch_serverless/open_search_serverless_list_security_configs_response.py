from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_serverless_security_config_summary import OpenSearchServerlessSecurityConfigSummary


class OpenSearchServerlessListSecurityConfigsResponse(BaseModel):
    securityConfigSummaries: list[OpenSearchServerlessSecurityConfigSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
