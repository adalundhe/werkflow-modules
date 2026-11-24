from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IAMParameterDefinition(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    SubType: StrictStr | None = None
    Description: StrictStr | None = None
    IsRequired: StrictBool | None = None
    DefaultValue: StrictStr | None = None
    Immutable: StrictBool | None = None
