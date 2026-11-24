from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_query_logging_config import Route53QueryLoggingConfig


class Route53CreateQueryLoggingConfigResponse(BaseModel):
    QueryLoggingConfig: Route53QueryLoggingConfig | None = None
    Location: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
