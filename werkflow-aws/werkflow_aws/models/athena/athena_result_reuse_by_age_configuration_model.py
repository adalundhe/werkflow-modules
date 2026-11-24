from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class AthenaResultReuseByAgeConfigurationModel(BaseModel):
    Enabled: StrictBool | None = None
    MaxAgeInMinutes: StrictInt | None = None
