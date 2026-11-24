from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2ListLoggingConfigurationsRequest(BaseModel):
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    NextMarker: StrictStr | None = None
    Limit: StrictInt | None = None
    LogScope: Literal['CUSTOMER', 'SECURITY_LAKE', 'CLOUDWATCH_TELEMETRY_RULE_MANAGED'] | None = None
