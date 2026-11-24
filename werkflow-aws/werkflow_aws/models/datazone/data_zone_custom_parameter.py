from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneCustomParameter(BaseModel):
    keyName: StrictStr | None = None
    description: StrictStr | None = None
    fieldType: StrictStr | None = None
    defaultValue: StrictStr | None = None
    isEditable: StrictBool | None = None
    isOptional: StrictBool | None = None
    isUpdateSupported: StrictBool | None = None
