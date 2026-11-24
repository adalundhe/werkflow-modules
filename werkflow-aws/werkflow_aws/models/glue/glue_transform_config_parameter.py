from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueTransformConfigParameter(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    ValidationRule: StrictStr | None = None
    ValidationMessage: StrictStr | None = None
    Value: list[StrictStr] | None = None
    ListType: StrictStr | None = None
    IsOptional: StrictBool | None = None
