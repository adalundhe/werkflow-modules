from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSOptionSetting(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
    DefaultValue: StrictStr | None = None
    Description: StrictStr | None = None
    ApplyType: StrictStr | None = None
    DataType: StrictStr | None = None
    AllowedValues: StrictStr | None = None
    IsModifiable: StrictBool | None = None
    IsCollection: StrictBool | None = None
