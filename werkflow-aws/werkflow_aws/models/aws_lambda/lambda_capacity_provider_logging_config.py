from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaCapacityProviderLoggingConfig(BaseModel):
    SystemLogLevel: StrictStr | None = None
    LogGroup: StrictStr | None = None
