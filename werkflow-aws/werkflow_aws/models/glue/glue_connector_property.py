from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueConnectorProperty(BaseModel):
    Name: StrictStr | None = None
    KeyOverride: StrictStr | None = None
    Required: StrictBool | None = None
    DefaultValue: StrictStr | None = None
    AllowedValues: list[StrictStr] | None = None
    PropertyLocation: StrictStr | None = None
    PropertyType: StrictStr | None = None
    Format: StrictStr | None = None
