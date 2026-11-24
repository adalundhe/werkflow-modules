from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceRetentionConfiguration(BaseModel):
    Name: StrictStr | None = None
    RetentionPeriodInDays: StrictInt | None = None
