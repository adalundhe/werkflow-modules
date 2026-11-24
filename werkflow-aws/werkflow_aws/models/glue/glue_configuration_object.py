from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueConfigurationObject(BaseModel):
    DefaultValue: StrictStr | None = None
    AllowedValues: list[StrictStr] | None = None
    MinValue: StrictStr | None = None
    MaxValue: StrictStr | None = None
