from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubEnumConfigurationOptions(BaseModel):
    DefaultValue: StrictStr | None = None
    AllowedValues: list[StrictStr] | None = None
