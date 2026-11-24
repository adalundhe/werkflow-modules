from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2GetLoggingConfigurationRequest(BaseModel):
    ResourceArn: StrictStr
    LogType: Literal['WAF_LOGS'] | None = None
    LogScope: Literal['CUSTOMER', 'SECURITY_LAKE', 'CLOUDWATCH_TELEMETRY_RULE_MANAGED'] | None = None
