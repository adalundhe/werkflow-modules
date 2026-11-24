from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class SecurityHubDoubleConfigurationOptions(BaseModel):
    DefaultValue: StrictFloat | StrictInt | None = None
    Min: StrictFloat | StrictInt | None = None
    Max: StrictFloat | StrictInt | None = None
