from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaDurableConfig(BaseModel):
    KMSKeyArn: StrictStr | None = None
    RetentionPeriodInDays: StrictInt | None = None
    ExecutionTimeout: StrictInt | None = None
