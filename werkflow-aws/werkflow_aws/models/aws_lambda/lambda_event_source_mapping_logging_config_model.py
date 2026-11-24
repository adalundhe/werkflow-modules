from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaEventSourceMappingLoggingConfigModel(BaseModel):
    SystemLogLevel: StrictStr | None = None
