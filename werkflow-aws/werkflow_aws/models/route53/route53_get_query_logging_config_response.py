from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_query_logging_config import Route53QueryLoggingConfig


class Route53GetQueryLoggingConfigResponse(BaseModel):
    QueryLoggingConfig: Route53QueryLoggingConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
