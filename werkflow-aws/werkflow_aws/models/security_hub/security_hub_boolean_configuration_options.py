from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubBooleanConfigurationOptions(BaseModel):
    DefaultValue: StrictBool | None = None
