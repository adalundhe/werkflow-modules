from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubIntegerConfigurationOptions(BaseModel):
    DefaultValue: StrictInt | None = None
    Min: StrictInt | None = None
    Max: StrictInt | None = None
