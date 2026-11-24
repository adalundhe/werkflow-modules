from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_allowed_value import GlueAllowedValue


class GlueProperty(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Required: StrictBool | None = None
    DefaultValue: StrictStr | None = None
    PropertyTypes: list[StrictStr] | None = None
    AllowedValues: list[GlueAllowedValue] | None = None
    DataOperationScopes: list[StrictStr] | None = None
    KeyOverride: StrictStr | None = None
    PropertyLocation: StrictStr | None = None
