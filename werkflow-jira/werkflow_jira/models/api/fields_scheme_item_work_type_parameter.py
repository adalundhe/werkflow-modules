from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class FieldsSchemeItemWorkTypeParameter(BaseModel):
    description: StrictStr | None = None
    isRequired: StrictBool | None = None
    rendererType: StrictStr | None = None
    workTypeId: StrictInt | None = None
