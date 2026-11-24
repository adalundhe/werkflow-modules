from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneEnvironmentConfigurationParameter(BaseModel):
    name: StrictStr | None = None
    value: StrictStr | None = None
    isEditable: StrictBool | None = None
