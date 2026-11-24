from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_application_log_level import LambdaApplicationLogLevel
from .lambda_log_format import LambdaLogFormat
from .lambda_system_log_level import LambdaSystemLogLevel


class LambdaLoggingConfig(BaseModel):
    LogFormat: LambdaLogFormat | None = None
    ApplicationLogLevel: LambdaApplicationLogLevel | None = None
    SystemLogLevel: LambdaSystemLogLevel | None = None
    LogGroup: StrictStr | None = None
