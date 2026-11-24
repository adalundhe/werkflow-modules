from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubIntegerListConfigurationOptions(BaseModel):
    DefaultValue: list[StrictInt] | None = None
    Min: StrictInt | None = None
    Max: StrictInt | None = None
    MaxItems: StrictInt | None = None
