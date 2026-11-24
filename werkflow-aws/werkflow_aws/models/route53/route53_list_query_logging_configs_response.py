from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_query_logging_config import Route53QueryLoggingConfig


class Route53ListQueryLoggingConfigsResponse(BaseModel):
    QueryLoggingConfigs: list[Route53QueryLoggingConfig] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
