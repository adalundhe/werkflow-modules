from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubEnumListConfigurationOptions(BaseModel):
    DefaultValue: list[StrictStr] | None = None
    MaxItems: StrictInt | None = None
    AllowedValues: list[StrictStr] | None = None
